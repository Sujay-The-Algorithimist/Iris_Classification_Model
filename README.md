# 🌸 Iris Classification Project

This is a machine learning project that classifies the species of Iris flowers based on four features: **sepal length**, **sepal width**, **petal length**, and **petal width**. It uses a supervised learning algorithm to predict whether a given flower belongs to the *Setosa*, *Versicolor*, or *Virginica* species.

---

## 📁 Project Structure

├── app.py # Flask web app for model deployment
├── savedmodel.pkl # Trained ML model saved using pickle
├── templates/
│ └── index.html # Frontend UI for input & prediction
├── Iris.csv # Dataset used for training
├── requirements.txt # List of required Python libraries
└── README.md # This file


---

## 📊 Dataset

- Dataset: [Iris Dataset](https://archive.ics.uci.edu/ml/datasets/iris)
- Features:
  - Sepal Length (cm)
  - Sepal Width (cm)
  - Petal Length (cm)
  - Petal Width (cm)
- Target: Species (Setosa, Versicolor, Virginica)

---

## 🔧 Technologies Used

- Python
- Flask
- Pandas
- Scikit-learn
- Matplotlib & Seaborn (for visualization)
- HTML (for UI)
- Gunicorn (for production server)

---

## 🚀 How to Run the Project

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/iris-classification.git
   cd iris-classification
Create a virtual environment (recommended):

bash
Copy
Edit
python -m venv myenv
myenv\Scripts\activate  # Windows
# or
source myenv/bin/activate  # macOS/Linux
