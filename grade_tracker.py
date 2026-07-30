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

def load_assignments(file_name):
    """Load assignments from a CSV file."""

    assignments = []

    try:
        with open(file_name, "r") as file:
            file.readline()

            for line in file:
                data = line.strip().split(",")

                assignment = {
                    "id": int(data[0]),
                    "assignment_name": data[1],
                    "category": data[2],
                    "points_earned": int(data[3]),
                    "points_possible": int(data[4]),
                    "status": data[5]
                }

                assignments.append(assignment)

    except FileNotFoundError:
        print("No existing assignment file found.")

    return assignments

def find_assignment(assignments, assignment_id):
    """Find an assignment by ID"""
    for assignment in assignments:
        if assignment["id"] == assignment_id:
           return assignment
    return None

def main():

    assignments = load_assignments(DATA_FILE)
    if len(assignments) == 0:
        add_assignment(
            assignments,
        "Quiz 1",
        "Quizzes",
        18,
        20,
        "Graded"
    )
    modified = modify_assignment(
        assignments,
        1,
        "Quiz 1 update",
        "Quizzes",
        19,
        20,
        "Graded"
    )

    if modified:
        save_assignments(DATA_FILE, assignments)
        print("\nAssignment updated")
        view_assignments(assignments)
    else:
        print("\nAssignment could not be found")

    found_assignment = find_assignment(assignments,1)

    if found_assignment is not None:
        print("\nAssignment found:")
        print(found_assignment)
    else:
        print("\nAssignment not found")

def modify_assignment(
        assignments,
         assignment_id,
        assignment_name,
        category,
        points_earned,
        points_possible,
        status
):
    """Modify an existing assignment."""
    assignment = find_assignment(assignments, assignment_id)

    if assignment is None:
        return False

    assignment ["assignment_name"]= assignment_name
    assignment["category"] = category
    assignment["points_earned"] = points_earned
    assignment["points_possible"] = points_possible
    assignment["status"] = status

    return True



if __name__ == "__main__":
    main()
