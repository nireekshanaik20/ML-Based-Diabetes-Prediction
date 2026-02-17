import tkinter as tk
from tkinter import messagebox, font as tkfont
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import svm

def train_model():
    
    try:
        diabetes_dataset = pd.read_csv('diabetes.csv')

        # Separating data and labels
        X = diabetes_dataset.drop(columns='Outcome', axis=1)
        Y = diabetes_dataset['Outcome']

        # Data Standardization
        scaler = StandardScaler()
        scaler.fit(X.values)  # Use .values to avoid feature name warnings
        standardized_data = scaler.transform(X.values)
        X = standardized_data

        # Train Test Split
        X_train, _, Y_train, _ = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

        # Training the SVM classifier
        classifier = svm.SVC(kernel='linear')
        classifier.fit(X_train, Y_train)

        return classifier, scaler

    except FileNotFoundError:
        # Show an error message if the CSV is not found and exit
        messagebox.showerror("Error", "diabetes.csv not found!\nMake sure the dataset file is in the same directory.")
        return None, None


def make_prediction(classifier, scaler, entries, result_label):
    
    try:
        # Collect input data from Tkinter entry widgets
        input_data = [float(entry.get()) for entry in entries]

        # Changing input data to a numpy array and reshaping
        input_data_as_numpy_array = np.asarray(input_data)
        input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

        # Standardize the input data using the trained scaler
        std_data = scaler.transform(input_data_reshaped)

        # Make a prediction
        prediction = classifier.predict(std_data)

        # Display the result
        if prediction[0] == 0:
            result_text = "✓ Result: Not Diabetic"
            result_color = "#10b981"  # Green
            bg_color = "#d1fae5"  # Light green background
        else:
            result_text = "⚠ Result: Diabetic"
            result_color = "#ef4444"  # Red
            bg_color = "#fee2e2"  # Light red background
            
        result_label.config(text=result_text, fg=result_color, bg=bg_color, font=("Helvetica", 16, "bold"))

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers in all fields.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")



def open_prediction_form(classifier, scaler, previous_window):
    # Destroy the welcome window
    previous_window.destroy()

    # Create the main window with gradient-like background
    root = tk.Tk()
    root.title("Diabetes Prediction System")
    root.geometry("700x850")  # INCREASED HEIGHT
    root.configure(bg="#0f172a")  # Dark blue-gray background

    # Create gradient effect with canvas
    canvas = tk.Canvas(root, width=700, height=850, bg="#0f172a", highlightthickness=0)
    canvas.place(x=0, y=0)
    
    # Create gradient rectangles
    for i in range(60):
        color_val = int(15 + i * 1.5)
        color = f"#{color_val:02x}{color_val + 10:02x}{color_val + 30:02x}"
        canvas.create_rectangle(0, i * 15, 700, (i + 1) * 15, fill=color, outline="")

    # Create a card-style main frame - INCREASED HEIGHT
    main_frame = tk.Frame(root, bg="white", bd=0)
    main_frame.place(relx=0.5, rely=0.5, anchor="center", width=620, height=780)
    
    # Add shadow effect with multiple frames
    shadow_frame = tk.Frame(root, bg="#1e293b")
    shadow_frame.place(relx=0.5, rely=0.502, anchor="center", width=625, height=785)
    shadow_frame.lower()

    # Header section with gradient-like effect
    header_frame = tk.Frame(main_frame, bg="#6366f1", height=90)
    header_frame.pack(fill="x", padx=0, pady=0)
    header_frame.pack_propagate(False)

    # Title with icon
    title_label = tk.Label(
        header_frame, 
        text="🏥 Diabetes Prediction System", 
        font=("Segoe UI", 22, "bold"), 
        bg="#6366f1", 
        fg="white"
    )
    title_label.pack(pady=20)

    # Content frame
    content_frame = tk.Frame(main_frame, bg="white")
    content_frame.pack(fill="both", expand=True, padx=35, pady=20)

    # Subtitle
    subtitle_label = tk.Label(
        content_frame, 
        text="Enter Patient Information", 
        font=("Segoe UI", 13, "bold"), 
        bg="white", 
        fg="#334155"
    )
    subtitle_label.pack(pady=(0, 15))

    # Labels for the input fields
    feature_labels = [
        ("Pregnancies", "Number of times pregnant"),
        ("Glucose", "Plasma glucose concentration"),
        ("Blood Pressure", "Diastolic blood pressure (mm Hg)"),
        ("Skin Thickness", "Triceps skin fold thickness (mm)"),
        ("Insulin", "2-Hour serum insulin (mu U/ml)"),
        ("BMI", "Body mass index (weight/height²)"),
        ("Diabetes Pedigree", "Diabetes pedigree function"),
        ("Age", "Age in years")
    ]

    # Create entry widgets for each feature - REDUCED SPACING
    entries = []
    for i, (label_text, tooltip) in enumerate(feature_labels):
        # Container for each input
        input_container = tk.Frame(content_frame, bg="white")
        input_container.pack(fill="x", pady=4)  # Reduced from 6 to 4
        
        # Label
        label = tk.Label(
            input_container, 
            text=label_text, 
            font=("Segoe UI", 10, "bold"), 
            bg="white", 
            fg="#475569",
            anchor="w",
            width=18
        )
        label.pack(side="left", padx=(0, 10))
        
        # Entry with modern styling
        entry = tk.Entry(
            input_container, 
            width=28, 
            font=("Segoe UI", 10), 
            bd=2, 
            relief="solid",
            highlightthickness=2,
            highlightbackground="#e2e8f0",
            highlightcolor="#6366f1"
        )
        entry.pack(side="right", ipady=5)
        entries.append(entry)

    # Prediction button with modern styling
    button_frame = tk.Frame(content_frame, bg="white")
    button_frame.pack(pady=(20, 12))
    
    predict_button = tk.Button(
        button_frame,
        text="🔍 Analyze & Predict",
        font=("Segoe UI", 13, "bold"),
        bg="#6366f1",
        fg="white",
        activebackground="#4f46e5",
        activeforeground="white",
        cursor="hand2",
        padx=45,
        pady=12,
        bd=0,
        relief="flat",
        command=lambda: make_prediction(classifier, scaler, entries, result_label)
    )
    predict_button.pack()
    
    # Hover effect simulation
    def on_enter(e):
        predict_button['bg'] = '#4f46e5'
    
    def on_leave(e):
        predict_button['bg'] = '#6366f1'
    
    predict_button.bind("<Enter>", on_enter)
    predict_button.bind("<Leave>", on_leave)

    # Result label with card styling
    result_frame = tk.Frame(content_frame, bg="#f8fafc", bd=1, relief="solid", highlightbackground="#e2e8f0", highlightthickness=1)
    result_frame.pack(fill="x", pady=(8, 0), ipady=8)
    
    result_label = tk.Label(
        result_frame, 
        text="⏳ Ready for prediction...", 
        font=("Segoe UI", 13, "italic"), 
        bg="#f8fafc", 
        fg="#64748b"
    )
    result_label.pack(pady=5)

    # Footer
    footer_label = tk.Label(
        main_frame,
        text="Powered by Machine Learning (SVM) • Accuracy: ~77%",
        font=("Segoe UI", 9),
        bg="white",
        fg="#94a3b8"
    )
    footer_label.pack(side="bottom", pady=8)

    # Start the GUI event loop
    root.mainloop()


def show_welcome_screen():
    classifier, scaler = train_model()
    if not classifier or not scaler:
        return

    welcome_window = tk.Tk()
    welcome_window.title("Welcome - Diabetes Prediction")
    welcome_window.geometry("700x550")
    welcome_window.configure(bg="#0f172a")

    # Create gradient background
    canvas = tk.Canvas(welcome_window, width=700, height=550, bg="#0f172a", highlightthickness=0)
    canvas.place(x=0, y=0)
    
    for i in range(55):
        color_val = int(15 + i * 1.5)
        color = f"#{color_val:02x}{color_val + 10:02x}{color_val + 30:02x}"
        canvas.create_rectangle(0, i * 10, 700, (i + 1) * 10, fill=color, outline="")

    # Content Frame with card design - INCREASED HEIGHT
    content_frame = tk.Frame(welcome_window, bg="white", bd=0)
    content_frame.place(relx=0.5, rely=0.5, anchor="center", width=550, height=450)
    
    # Shadow effect
    shadow_frame = tk.Frame(welcome_window, bg="#1e293b")
    shadow_frame.place(relx=0.5, rely=0.502, anchor="center", width=555, height=455)
    shadow_frame.lower()

    # Icon/Logo area
    icon_label = tk.Label(
        content_frame,
        text="🏥",
        font=("Segoe UI", 72),
        bg="white"
    )
    icon_label.pack(pady=(35, 10))

    # Welcome title
    welcome_label = tk.Label(
        content_frame, 
        text="Diabetes Prediction System", 
        font=("Segoe UI", 26, "bold"), 
        bg="white", 
        fg="#1e293b"
    )
    welcome_label.pack(pady=(0, 12))

    # Description
    desc_label = tk.Label(
        content_frame, 
        text="AI-Powered Health Diagnostics\n\nUsing Support Vector Machine (SVM) to predict\ndiabetes risk based on diagnostic measurements", 
        font=("Segoe UI", 12), 
        bg="white", 
        fg="#64748b",
        justify="center"
    )
    desc_label.pack(pady=(0, 30))

    # Get Started button - MADE MORE PROMINENT
    next_button = tk.Button(
        content_frame,
        text="Get Started →",
        font=("Segoe UI", 15, "bold"),
        bg="#6366f1",
        fg="white",
        activebackground="#4f46e5",
        activeforeground="white",
        cursor="hand2",
        padx=60,
        pady=16,
        bd=0,
        relief="flat",
        command=lambda: open_prediction_form(classifier, scaler, welcome_window)
    )
    next_button.pack(pady=(0, 20))
    
    # Hover effect
    def on_enter(e):
        next_button['bg'] = '#4f46e5'
    
    def on_leave(e):
        next_button['bg'] = '#6366f1'
    
    next_button.bind("<Enter>", on_enter)
    next_button.bind("<Leave>", on_leave)

    welcome_window.mainloop()

# --- SCRIPT ENTRY POINT ---
if __name__ == "__main__":
    show_welcome_screen()
