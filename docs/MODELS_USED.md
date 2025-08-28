# Models Used

## 🎯 Primary Model
- **LightGBM Classifier**
  - Chosen for efficiency and high accuracy.
  - Works well with tabular features extracted from packet data.

## 🛠️ Alternative Models Tried
- Random Forest (scikit-learn)
- XGBoost
- Torch-based LSTM
- Torch-based 1D-CNN

## 📊 Model Selection
After experimentation, LightGBM gave the best tradeoff between:
- Accuracy
- Training time
- Inference speed
