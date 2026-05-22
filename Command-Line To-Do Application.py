# Command-Line To-Do Application

tasks = []


# Function to add a task
def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print("✅ Task added successfully!\n")


# Function to view all tasks
def view_tasks():
    if len(tasks) == 0:
        print("📌 No tasks available.\n")
    else:
        print("\n📋 Your To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print()


# Main menu function
def main():
    while True:
        print("===== TO-DO APPLICATION =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            print("👋 Exiting To-Do Application.")
            break

        else:
            print("❌ Invalid choice! Please try again.\n")


# Run the program
main()