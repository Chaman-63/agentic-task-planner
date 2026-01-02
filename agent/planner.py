from agent.planner import create_plan


def main():
    goal = input("Enter your goal: ")
    plan = create_plan(goal)

    print("\nGenerated Plan:")
    for i, step in enumerate(plan, start=1):
        print(f"{i}. {step}")


if __name__ == "__main__":
    main()
