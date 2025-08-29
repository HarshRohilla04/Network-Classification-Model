🚀 Network Traffic Classification Model

A machine learning project to classify user application traffic in multi-UE (User Equipment) connected scenarios.
The model analyzes traffic patterns and predicts the application category (e.g., Video Streaming, Audio Calls, Gaming, Browsing) with high accuracy.
This project was initially developed during a hackathon (Team KODE CRACKHEADS) and is now maintained by Harsh Rohilla for portfolio and research purposes.

🔍 Problem Statement

In real-world networks, applications behave differently under varying:

1)Traffic conditions

2)Channel states

3)Coverage scenarios

If user traffic can be categorized into broader groups (e.g., video, audio, gaming, browsing), networks can deliver optimized Quality of Service (QoS).

👉 Goal: Develop an AI model that analyzes traffic patterns and predicts the application category with high accuracy.

🛠️ Models Used

-Primary Model: LightGBM Classifier

Best tradeoff between accuracy, training time, and inference speed.

-Other Models Experimented:

1)Random Forest (scikit-learn)

2)XGBoost

3)Torch-based LSTM

4)Torch-based 1D-CNN

⚙️ Tech Stack

Languages: Python

Libraries: scikit-learn, LightGBM, XGBoost, PyTorch, Pandas, NumPy

Environment: Jupyter Notebook / Google Colab

📊 Results

LightGBM outperformed other models in both accuracy and efficiency.

Successfully classified network traffic into application-level categories with high accuracy.

🎥 Demo

Watch on YouTube [https://www.youtube.com/watch?v=fX2eX5cJ-eg]

👨‍💻 Contributors

Harsh Rohilla (Maintainer)

Karan, Shivaansh Kaushik, Gauri Chopra (Hackathon teammates)
