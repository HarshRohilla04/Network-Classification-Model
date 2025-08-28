# Implementation Details

## 1️⃣ Data Preprocessing
- Loaded raw CSV traffic files.
- Extracted features:
  - Length
  - info_len
  - digits_in_info
  - delta_time
  - src_port
  - dst_port
- Cleaned missing values, normalized features.

## 2️⃣ Model Training
- Default: LightGBM Classifier.
- Configurable via `configs/default.yaml`.
- Metrics tracked: Accuracy, F1-macro, Precision, Recall.

## 3️⃣ Model Serving
- Exported trained model as `.pkl`.
- Wrapped with FastAPI to provide prediction endpoint.

## 4️⃣ Frontend
- React.js application.
- Connects to API endpoint.
- Displays classification results and statistics.


