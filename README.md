🚀 Network Traffic Classification Model

A machine learning project to classify user application traffic in multi-UE (User Equipment) connected scenarios. The model analyzes traffic patterns and predicts the application category (e.g., Video Streaming, Audio Calls, Gaming, Browsing) with high accuracy.
This work was developed during a hackathon as part of Team KODE CRACKHEADS and later maintained by Harsh Rohilla for portfolio/research purposes.

🔍 Problem Statement

In real-world networks, applications are affected differently under varying traffic conditions, channel states, and coverage scenarios. Differentiating user traffic into broader categories (e.g., video, audio, gaming, browsing) enables networks to serve optimized QoS (Quality of Service).
The goal: Develop an AI model to analyze traffic patterns and predict the application category with high accuracy.

🛠️ Models Used
🎯 Primary Model: LightGBM Classifier (best tradeoff of accuracy, training time, and inference speed).
🧪 Other Models Experimented:

1)Random Forest (scikit-learn)

2)XGBoost

3)Torch-based LSTM

4)Torch-based 1D-CNN

⚙️ Tech Stack
Languages: Python

Libraries: scikit-learn, LightGBM, XGBoost, PyTorch, Pandas, NumPy

Environment: Jupyter Notebook / Google Colab

📊 Results
LightGBM outperformed other models in terms of accuracy and efficiency.

Successfully classified network traffic into application-level categories with high accuracy.

🎥 Demo

Watch on YouTube

👨‍💻 Contributors

Harsh Rohilla (Maintainer)
Karan, Shivaansh Kaushik, Gauri Chopra (Hackathon teammates)
