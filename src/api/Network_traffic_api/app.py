import pandas as pd
import numpy as np
import re
import joblib
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# ----------------------------
# 1. GLOBAL CONSTANTS
# ----------------------------
FLAGS = ['SYN', 'ACK', 'PSH', 'RST', 'FIN', 'URG', 'ECE', 'CWR']
KEYWORDS = ['http', 'tls', 'quic', 'dns', 'get', 'post', 'rtp', 'rtcp', 'rtsp',
            'ssl', 'video', 'audio', 'application data']

# ----------------------------
# 2. INITIALIZE APP & LOAD MODELS
# ----------------------------
app = FastAPI(title="Network Traffic Classifier API", version="1.0")

model = joblib.load("Models/lightgbm_packet_model.pkl")
ohe = joblib.load("Models/ohe_protocol.pkl")
print("✅ Model and encoder loaded successfully.")


# ----------------------------
# 3. DEFINE INPUT MODELS
# ----------------------------
class Packet(BaseModel):
    Time: float
    Source: str
    Destination: str
    Protocol: str
    Length: int
    Info: str

class PacketList(BaseModel):
    packets: List[Packet]


# ----------------------------
# 4. FEATURE ENGINEERING
# ----------------------------
def create_features(df: pd.DataFrame) -> pd.DataFrame:
    df['Info'] = df['Info'].astype(str)

    port_pattern = re.compile(r'(\d{1,5})\s*>\s*(\d{1,5})')

    df['info_len'] = df['Info'].apply(len)
    df['digits_in_info'] = df['Info'].apply(lambda s: sum(ch.isdigit() for ch in s))

    ports = df['Info'].apply(lambda s: port_pattern.search(s))
    df['src_port'] = ports.apply(lambda m: int(m.group(1)) if m else np.nan)
    df['dst_port'] = ports.apply(lambda m: int(m.group(2)) if m else np.nan)

    for f in FLAGS:
        df['flag_' + f] = df['Info'].apply(lambda s: 1 if f in s else 0)

    for k in KEYWORDS:
        df['has_' + k.replace(' ', '_')] = df['Info'].str.lower().str.contains(k).fillna(False).astype(int)

    df = df.sort_values('Time').reset_index(drop=True)
    df['delta_time'] = df['Time'].diff().fillna(0.0)

    return df


# ----------------------------
# 5. PREDICTION ENDPOINT
# ----------------------------
@app.post("/predict")
def predict_traffic(data: PacketList):
    input_df = pd.DataFrame([p.dict() for p in data.packets])
    features_df = create_features(input_df)

    candidate_features = [
        'Length', 'info_len', 'digits_in_info', 'delta_time',
        'src_port', 'dst_port'
    ] + [f'flag_{f}' for f in FLAGS] + ['has_' + k.replace(' ', '_') for k in KEYWORDS] + ['Protocol']

    X_df = features_df[[c for c in candidate_features if c in features_df.columns]].copy()

    X_df['src_port'] = X_df['src_port'].fillna(-1).astype(int)
    X_df['dst_port'] = X_df['dst_port'].fillna(-1).astype(int)
    if 'Length' in X_df:
        X_df['Length'] = X_df['Length'].fillna(X_df['Length'].median())

    num_cols = [c for c in X_df.columns if c != 'Protocol']
    X_num = X_df[num_cols].astype(float).fillna(0.0).reset_index(drop=True)

    X_cat = X_df[['Protocol']].fillna('missing').astype(str)
    P_sparse = ohe.transform(X_cat)
    try:
        P_cols = list(ohe.get_feature_names_out(['Protocol']))
    except AttributeError:
        P_cols = list(ohe.get_feature_names(['Protocol']))
    P_df = pd.DataFrame(P_sparse.toarray(), columns=P_cols).reset_index(drop=True)

    X_pre = pd.concat([X_num, P_df], axis=1)
    X_pre.columns = [re.sub(r'[^0-9a-zA-Z_]', '_', str(c)) for c in X_pre.columns]

    predictions = model.predict(X_pre)

    input_df['predicted_label'] = predictions
    return {"predictions": input_df.to_dict(orient="records")}


# ----------------------------
# 6. ROOT ENDPOINT
# ----------------------------
@app.get("/")
def read_root():
    return {"message": "Welcome to the Network Traffic Classifier API. Go to /docs for details."}
