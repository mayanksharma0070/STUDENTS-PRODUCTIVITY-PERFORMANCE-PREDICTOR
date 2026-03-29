# utils is designed to perform simpler tasks and help main file and code to perform as expected
def show_menu():
    print("\n====== Student AI CLI ======")
    print("1. Add Student Data")
    print("2. Train Model")
    print("3. Predict Performance")
    print("4. View Data")
    print("5. Help")
    print("6. Exit")

def show_help():
    print("\nCommands:")
    print("1 → Add new student data")
    print("2 → Train ML model")
    print("3 → Predict marks")
    print("4 → View dataset")
    print("5 → Show help")
    print("6 → Exit")

def performance_label(marks):
    if marks >= 80:
        return "Excellent"
    elif marks >= 70:
        return "Average"
    else:
        return "Needs Improvement"
    
