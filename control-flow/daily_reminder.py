task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"{task} is a high priority task that requires immediate action today!")
        elif time_bound == "no":
            print(f"{task} is a high priority task, get to it when you can.")
        else:
            print(f"You have not entered a proper time for: {task}.")
    case "medium":
        if time_bound == "yes":
            print(f"{task} is a medium priority task that requires an action today!")
        elif time_bound == "no":
            print(f"{task} is a medium priority task, get to it when you can.")
        else: 
            print(f"You have not entered a proper time for: {task}.")
    case "low":
        if time_bound == "yes":
            print(f"{task} is low priority task that requires an action!")
        elif time_bound == "no":
            print(f"{task} is low priority task, get to it when you can.")
        else:
            print(f"You have not entered a proper time for: {task}.")
    case _:
        print("Invalid priority")
