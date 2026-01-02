# 👶 Baby Safety Monitoring System (YOLOv9)

![YOLOv9](https://img.shields.io/badge/Model-YOLOv9-blue)
![Python](https://img.shields.io/badge/Language-Python-green)
![Computer Vision](https://img.shields.io/badge/Field-Computer%20Vision-purple)
![Roboflow](https://img.shields.io/badge/Dataset-Roboflow-orange)

## 📋 Overview

**Baby Safety Monitoring System** is a Computer Vision project designed to enhance child safety by real-time monitoring of baby positions and behaviors. 

Developed during my internship at **Telkom Indonesia**, this project utilizes the **YOLOv9 (You Only Look Once)** object detection architecture to identify specific states of a baby in a crib. The primary goal is to provide an early warning system for parents or guardians when potentially dangerous situations occur (e.g., a baby climbing out of the crib).

## 🎯 Key Capabilities

The model is trained to detect and classify the following specific classes:

* **🛌 Sleeping:** Detects when the baby is safely sleeping.
* **🧍 Standing:** Detects when the baby is standing up in the crib.
* **⚠️ Near Bed Edge/Climbing:** Detects if the baby is dangerously close to the edge or attempting to climb out (High Risk).
* **👶 Sitting:** Detects when the baby is sitting up.

## 🛠️ Tech Stack

* **Core Algorithm:** YOLOv9 (State-of-the-art Object Detection)
* **Language:** Python
* **Training Environment:** Google Colab (GPU)
* **Dataset Management:** Roboflow (Annotation & Augmentation)
* **Deployment/Demo:** Streamlit (Optional Web Interface)
* **IDE:** Visual Studio Code

## 📊 Dataset & Training

1.  **Data Collection:** Images were collected representing various baby poses and lighting conditions (Day/Night mode).
2.  **Annotation:** Data was manually annotated using **Roboflow**, ensuring precise bounding boxes for each class.
3.  **Augmentation:** Applied preprocessing techniques (grayscale, blur, rotation) to improve model robustness against camera noise.
4.  **Training:** The YOLOv9 model was trained on [Number] epochs with custom hyperparameters to balance Precision and Recall.

## 🚀 How to Run

### 1. Clone the Repository
```bash
git clone [https://github.com/VarelAntoni/machine_learning_project.git](https://github.com/VarelAntoni/machine_learning_project.git)
cd machine_learning_project/baby_object_detection
