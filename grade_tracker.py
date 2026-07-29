"""
Student Grade Tracker
Student: Sydney Manning
GitHub Username: sydmann4

This application allows students to track assignments,
calculate weighted grades, and monitor their progress.
"""

DATA_FILE = "data/assignments.csv"

def add_assignment(
        assignments,
        assignment_name,
        category,
        points_earned,
        points_possible,
        status
):
    """Create an assignment dictionary and add it to the list."""

    assignment = {
        "id": len(assignments) + 1,
        "assignment_name": assignment_name,
        "category": category,
        "points_earned": points_earned,
        "points_possible": points_possible,
        "status": status
    }
    assignments.append(assignment)
    return assignment


def view_assignments(assignments):
    """ Display all assignments."""

    print("\n===== Assignment List =====")

    for assignment in assignments:
        print(f"ID: {assignment['id']}")
        print(f"Assignment: {assignment['assignment_name']}")
        print(f"Category: {assignment['category']}")
        print(f"Points Earned: {assignment['points_earned']}")
        print(f"Points Possible: {assignment['points_possible']}")
        print(f"Status: {assignment['status']}")
        print("_" * 30)
    return assignments
def save_assignments(file_name, assignments):
    """Save assignments to a CSV file."""

    try:
        with open(file_name, "w") as file:
            file.write(
                "id,assignment_name,category,"
                "points_earned,points_possible,status\n"
            )

            for assignment in assignments:
                row = (
                    f"{assignment['id']},"
                    f"{assignment['assignment_name']},"
                    f"{assignment['category']},"
                    f"{assignment['points_earned']},"
                    f"{assignment['points_possible']},"
                    f"{assignment['status']}\n"
                )

                file.write(row)

        return True

    except FileNotFoundError:
        print("Error: Could not save the file.")
        return False

def main():

    assignments = []

    add_assignment(
        assignments,
        "Quiz 1",
        "Quizzes",
        18,
        20,
        "Graded"
    )

    view_assignments(assignments)
    save_assignments(DATA_FILE,assignments)


if __name__ == "__main__":
    main()
