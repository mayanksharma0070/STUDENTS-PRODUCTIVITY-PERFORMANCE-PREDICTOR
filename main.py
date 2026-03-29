import pandas as pd
import numpy as np
from model import train_model, predict
from utils import show_menu, show_help, performance_label

DATA_FILE = "data.csv"

theta = None  # model

def load_data():
    return pd.read_csv(DATA_FILE)
    
# a function define for adding new data of student
def add_data():
    try:
        hours = float(input("Enter study hours: "))
        attendance = float(input("Enter attendance (%): "))
        sleep = float(input("Enter sleep hours: "))
        marks = float(input("Enter actual marks: "))

        new_data = pd.DataFrame([[hours, attendance, sleep, marks]],
                                columns=["hours", "attendance", "sleep", "marks"])

        with open(DATA_FILE, 'a', newline='') as f:
            new_data.to_csv(f, header=False, index=False)

        print("✅ Data added successfully!")

    except:
        print("❌ Invalid input!")

# a function is define for training ai model to work as expected
def train():
    global theta
    data = load_data()

    X = data[['hours', 'attendance', 'sleep']].values
    y = data['marks'].values

    theta = train_model(X, y)
    print("✅ Model trained successfully!")

# function define for prediction of marks of student based on data
def predict_marks():
    global theta

    if theta is None:
        print("❌ Train the model first!")
        return

    try:
        hours = float(input("Study hours: "))
        attendance = float(input("Attendance (%): "))
        sleep = float(input("Sleep hours: "))

        input_data = np.array([hours, attendance, sleep])
        result = predict(theta, input_data)

        print(f"\n📊 Predicted Marks: {round(result, 2)}")
        print("Performance:", performance_label(result))

    except:
        print("❌ Invalid input!")

# function define for viewing data on the basis of model is predicting marks
def view_data():
    data = load_data()
    print("\nDataset:\n", data)

# main function which directs all the other functions
def main():
    while True:
        show_menu()
        choice = input("Enter choice: ")

        if choice == '1':
            add_data()
        elif choice == '2':
            train()
        elif choice == '3':
            predict_marks()
        elif choice == '4':
            view_data()
        elif choice == '5':
            show_help()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()
