# 🎯 Head Movement Classification with CNN, ViT, and CvT  

## 📖 Description  
This project focuses on classifying head movements using three computer vision models:  
✅ **Convolutional Neural Network (CNN)**  
✅ **Vision Transformer (ViT)**  
✅ **Convolutional Vision Transformer (CvT)**  

The system is trained to recognize four head positions:  
1️⃣ **Neutral (Front-facing)**  
2️⃣ **Looking Down**  
3️⃣ **Tilting Left**  
4️⃣ **Tilting Right**  

## 📊 Dataset Overview  
📌 **Total images:** `3,727`  
📌 **Number of classes:** `4`  

**🔹 Training Set (70%)**  
- Neutral: `707` images  
- Looking Down: `568` images  
- Tilting Left: `602` images  
- Tilting Right: `725` images  

**🔹 Validation Set (20%)**  
- Neutral: `202` images  
- Looking Down: `162` images  
- Tilting Left: `174` images  
- Tilting Right: `208` images  

**🔹 Testing Set (10%)**  
- Neutral: `102` images  
- Looking Down: `82` images  
- Tilting Left: `87` images  
- Tilting Right: `104` images  

## 🏗️ Model Architecture  
📌 **CNN (Convolutional Neural Network)**  
✔️ Extracts spatial features using convolutional layers.  

📌 **ViT (Vision Transformer)**  
✔️ Uses self-attention mechanisms to analyze image patches.  

📌 **CvT (Convolutional Vision Transformer)**  
✔️ Combines CNN's local feature extraction with Transformer's global attention.  

## 🏆 Experiment Results  
| Model  | Accuracy |
|--------|----------|
| 🧩 **CNN** | 📊 `96.53%` |
| 🧩 **ViT** | 📊 `98.76%` |
| 🧩 **CvT** | 📊 `95.20%` |

## 🖥️ System Requirements  
**🔹 Hardware:**  
- ⚡ GPU: `NVIDIA RTX 3090`  
- 💾 RAM: `32GB`  
- 🔥 Processor: `Intel Core i9 12th Gen`  

**🔹 Software:**  
- 🐍 Python 3.x  
- 🏗 TensorFlow / PyTorch  
- 📂 Jupyter Notebook  

## 🤝 Contributors
👤 Alexius Andrianno Alfa R. - Universitas Brawijaya  
👤 Alif Akbar Grafidi - Universitas Brawijaya  
📌 Supervisor: Prof. Dr. Eng. Fitri Utaminingrum, S.T., M.T.
