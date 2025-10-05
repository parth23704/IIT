# ---------------------------------------------------------
# Name: Parth Bhavsar
# Student ID: u3311230
# Subject: IIT
# Assignment: [2nd - Python Fundamentals] Case Study 2 - Smart Classroom Monitor
# Date: 17/09/2025
# ---------------------------------------------------------

room = {"projector": False, "topic": "", "capacity": 5}
attendance = set()
temperatures = []

def toggle_projector():
    room["projector"] = not room["projector"]
    print("Projector is now", "ON" if room["projector"] else "OFF")

def set_topic():
    topic = input("Enter topic: ")
    room["topic"] = topic
    print(f"Topic set to {topic}")

def add_student():
    student = input("Enter student name: ")
    attendance.add(student)
    print(f"{student} added. Total students: {len(attendance)}/{room['capacity']}")
    if len(attendance) > room["capacity"]:
        print("ROOM FULL!")

def remove_student():
    student = input("Enter student name: ")
    if student in attendance:
        attendance.remove(student)
        print(f"{student} removed. Total students: {len(attendance)}/{room['capacity']}")
    else:
        print("Student not found.")

def add_temperature():
    try:
        temp = float(input("Enter temperature: "))
        temperatures.append(temp)
        print(f"Temperature recorded: {temp}°C")
        if temp < 16 or temp > 28:
            print("⚠ Temperature out of safe range!")
    except ValueError:
        print("Invalid input.")

def show_statistics():
    if not temperatures:
        print("No temperatures recorded.")
        return
    minimum = min(temperatures)
    maximum = max(temperatures)
    average = sum(temperatures) / len(temperatures)
    print(f"Temperatures: Min = {minimum}°C, Max = {maximum}°C, Avg = {average:.1f}°C")

def show_report():
    print("--- Classroom Report ---")
    print(f"Topic: {room['topic'] if room['topic'] else 'Not set'}")
    print(f"Projector: {'ON' if room['projector'] else 'OFF'}")
    print(f"Attendance: {len(attendance)}/{room['capacity']}")
    if temperatures:
        minimum = min(temperatures)
        maximum = max(temperatures)
        average = sum(temperatures) / len(temperatures)
        print(f"Temperatures: Min = {minimum}°C, Max = {maximum}°C, Avg = {average:.1f}°C")
    else:
        print("No temperatures recorded.")

while True:
    print("\n1. Toggle projector\n2. Set topic\n3. Add student\n4. Remove student\n5. Add temperature\n6. Show statistics\n7. Show report\n8. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        toggle_projector()
    elif choice == "2":
        set_topic()
    elif choice == "3":
        add_student()
    elif choice == "4":
        remove_student()
    elif choice == "5":
        add_temperature()
    elif choice == "6":
        show_statistics()
    elif choice == "7":
        show_report()
    elif choice == "8":
        print("Exiting program.")
        break
    else:
        print("Invalid choice.")
