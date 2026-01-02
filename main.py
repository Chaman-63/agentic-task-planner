def plan_task(goal):
    steps = [
        "Understand the goal",
        "Break the goal into smaller tasks",
        "Execute each task step by step",
        "Review the result"
    ]
    return steps


if __name__ == "__main__":
    user_goal = input("Enter your goal: ")
    plan = plan_task(user_goal)

    print("\nGenerated Plan:")
    for i, step in enumerate(plan, start=1):
        print(f"{i}. {step}")
