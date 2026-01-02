from agent.planner import create_plan


def main():
    goal = input("Enter your goal: ")
    steps, reasoning = create_plan(goal)

    print("\nAgent Reasoning:")
    for r in reasoning:
        print(f"- {r}")

    print("\nGenerated Plan:")
    for i, step in enumerate(steps, start=1):
        print(f"{i}. {step}")


if __name__ == "__main__":
    main()
