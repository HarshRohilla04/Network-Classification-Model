# Project Overview

## 🎯 Problem Statement
Applications are affected differently under varying traffic conditions, channel states, and coverage scenarios.  
By classifying traffic of each User Equipment (UE) into categories like:
- Video Streaming
- Audio Calls
- Video Calls
- Gaming
- Video Uploads
- Browsing
- Texting

…the network can serve a differentiated and curated **Quality of Service (QoS)**.

---

## 💡 Our Solution
We built a **network traffic classification system** that:
1. Extracts features from packet data.
2. Trains a machine learning model (LightGBM).
3. Exposes the model through an **API** for real-time predictions.
4. Provides a **frontend dashboard** to visualize results.

---

## 🏗️ System Components
- **Training module**: Prepares and trains ML models.
- **Inference API**: Serves predictions via REST API.
- **Frontend**: User-friendly interface for visualization.

---

## 📊 Key Features
- Accurate classification into application categories.
- Configurable training/evaluation via YAML configs.
- Modular codebase for extensibility.
