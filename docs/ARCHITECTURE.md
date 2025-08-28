# System Architecture

Our solution follows a modular, three-tier architecture:

## 1️⃣ Data Layer
- Input: CSV datasets derived from packet captures.
- Features used:
  - Length
  - info_len
  - digits_in_info
  - delta_time
  - src_port
  - dst_port
- Preprocessing: Cleaning, normalization, and feature extraction.

## 2️⃣ Model Layer
- Base model: **LightGBM** classifier.
- Configurable: Supports other models (Random Forest, LSTM, 1D-CNN).
- Training scripts handle validation, metrics, and checkpoint saving.

## 3️⃣ Application Layer
- **API**: FastAPI server exposing REST endpoints for prediction.
- **Frontend**: React-based web app for visualization and user interaction.

---

## 🖼️ Diagram
[ Raw Traffic Data ] → [ Preprocessing ] → [ ML Model Training ]
→ [ Trained Model ] → [ API Service ] → [ Frontend UI ]