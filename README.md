# 🏥 ML-Based Diabetes Prediction System

A powerful Machine Learning application aimed at predicting the likelihood of diabetes in patients based on diagnostic measurements. This system utilizes a Support Vector Machine (SVM) classifier to analyze health parameters and provide instant, accurate predictions.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-SVM-orange)
![GUI](https://img.shields.io/badge/GUI-Tkinter-green)

## 📋 Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [Dataset](#-dataset)
- [Technologies Used](#-technologies-used)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)
- [License](#-license)

## 📖 Overview

The **Diabetes Prediction System** is designed to assist medical professionals and individuals in assessing the risk of diabetes. By inputting standard health metrics, the application uses a trained Machine Learning model to classify the patient as "Diabetic" or "Not Diabetic". The user-friendly Graphical User Interface (GUI) makes it accessible to users with no technical background.

## ✨ Features

*   **Accurate Predictions:** Uses a Support Vector Machine (SVM) algorithm with a linear kernel for reliable classification.
*   **User-Friendly GUI:** Built with Python's Tkinter, featuring a modern, clean interface with card-style layouts and gradient backgrounds.
*   **Real-time Analysis:** Instantly processes input data and standardizes it for the model.
*   **Visual Feedback:** Clear color-coded results (Green for Negative, Red for Positive) with actionable status messages.
*   **Data Validation:** Basic input validation to ensure correct data entry.

## 📊 Dataset

The model is trained on the **Pima Indians Diabetes Database** (or a similar structured dataset). The dataset should be a CSV file named `diabetes.csv` located in the project root.

**Required Columns:**
1.  **Pregnancies:** Number of times pregnant
2.  **Glucose:** Plasma glucose concentration a 2 hours in an oral glucose tolerance test
3.  **BloodPressure:** Diastolic blood pressure (mm Hg)
4.  **SkinThickness:** Triceps skin fold thickness (mm)
5.  **Insulin:** 2-Hour serum insulin (mu U/ml)
6.  **BMI:** Body mass index (weight in kg / (height in m)^2)
7.  **DiabetesPedigreeFunction:** Diabetes pedigree function
8.  **Age:** Age in years
9.  **Outcome:** Class variable (0 or 1) - used for training

## 🛠 Technologies Used

*   **Programming Language:** Python 3
*   **GUI Framework:** Tkinter (Standard Python GUI library)
*   **Data Manipulation:** Pandas, NumPy
*   **Machine Learning:** Scikit-Learn (sklearn) - SVC (Support Vector Classifier), StandardScaler

## 🚀 Installation

Follow these steps to set up the project locally:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/nireekshanaik20/ML-Based-Diabetes-Prediction.git
    cd ML-Based-Diabetes-Prediction
    ```

2.  **Install dependencies:**
    Ensure you have Python installed. Then run:
    ```bash
    pip install -r requirements.txt
    ```
    *Note: `tkinter` is usually included with Python. If not, you may need to install it separately (e.g., `sudo apt-get install python3-tk` on Linux).*

3.  **Prepare the Dataset:**
    Ensure the `diabetes.csv` file is present in the main project directory.

## 💻 Usage

1.  **Run the application:**
    ```bash
    python tkinterdiabeties.py
    ```

2.  **Navigate the Interface:**
    *   Click **"Get Started"** on the welcome screen.
    *   Enter the patient's health metrics in the input fields.
    *   Click **"Analyze & Predict"**.
    *   View the result displayed at the bottom of the card.

## 📂 Project Structure

```
ML-Based-Diabetes-Prediction/
├── diabetes.csv            # Dataset file (Required)
├── tkinterdiabeties.py     # Main application script
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements or bug fixes, please feel free to:
1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/YourFeature`).
3.  Commit your changes (`git commit -m 'Add some feature'`).
4.  Push to the branch (`git push origin feature/YourFeature`).
5.  Open a Pull Request.

## 📜 License

This project is open-source and available under the information in the repository. Provide appropriate credit when using or modifying this code.
