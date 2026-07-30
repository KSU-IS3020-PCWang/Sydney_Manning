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
    """Read assignment records from a CSV file and return a list."""

    assignments = []

    try:
        with open(file_name, "r") as file:
            file.readline()

            for line in file:
                data = line.strip().split(",")

                if len(data) == 6:
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
        print(
            "No existing assignment file found. "
            "Starting with an empty list."
        )

    return assignments

def find_assignment(assignments, assignment_id):
    """Find an assignment by ID."""

    for assignment in assignments:
        if assignment["id"] == assignment_id:
            return assignment

    return None

def modify_assignment(
        assignments,
        assignment_id,
        assignment_name,
        category,
        points_earned,
        points_possible,
        status
):
    """Replace the information in an existing assignment."""
    assignment = find_assignment(assignments, assignment_id)
    if assignment is None:
        return False

    assignment["assignment_name"] = assignment_name
    assignment["category"] = category
    assignment["points_earned"] = points_earned
    assignment["points_possible"] = points_possible
    assignment["status"] = status
    return True

def delete_assignment(assignments, assignment_id):
    """ Delete an assignment by ID."""

    assignment = find_assignment(assignments, assignment_id)

    if assignment is None:
        return False
    assignments.remove(assignment)
    return True


def get_assignments_by_category(assignments, category):
    """Return all assignments in the selected category"""
    category_assignments = []
    for assignment in assignments:
        if assignment["category"].lower() == category.lower():
            category_assignments.append(assignment)
    return category_assignments


def main():
    """Run the Grade Tracker menu."""

    assignments = load_assignments(DATA_FILE)
    running = True
    while running:
        print("\n===== STUDENT GRADE TRACKER =====")
        print("1. Add Assignment")
        print("2. View Assignments")
        print("3. Modify Assignment")
        print("4. Delete Assignment")
        print("5. View Assignments by Category")
        print("6. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            assignment_name = input("Assignment name: ").strip()
            category = input("Category: ").strip()
            points_earned = int(input("Points earned: "))
            points_possible = int(input("Points possible: "))
            status = input("Status: ").strip()

            add_assignment(
                assignments,
                assignment_name,
                category,
                points_earned,
                points_possible,
                status
            )

            save_assignments(DATA_FILE, assignments)
            print("Assignment added.")

        elif choice == "2":
            view_assignments(assignments)


        elif choice == "3":

            view_assignments(assignments)

            assignment_id = int(
                input("Enter assignment ID to modify: ")
            )

            assignment_name = input("New assignment name: "
            ).strip()

            class_name = input("Enter class name: "
            ).strip()

            points_earned = int(
                input("New points earned: ")
            )

            points_possible = int(
                input("New points possible: ")
            )

            status = input( "New status: "
            ).strip()

            modified = modify_assignment(
                assignments,
                assignment_id,
                assignment_name,
                class_name,
                points_earned,
                points_possible,
                status,
            )

            if modified:
                save_assignments(DATA_FILE, assignments)
                print("Assignment modified.")
            else:
                print("Assignment ID not found.")

        elif choice == "5":

            category = input("Enter category: ").strip()

            category_assignments = get_assignments_by_category(
                assignments,
                category,
            )
            view_assignments(category_assignments)


        elif choice == "4":

            view_assignments(assignments)

            assignment_id = int( input("Enter assignment ID to delete: ")
         )

            deleted = delete_assignment(
                assignments,
                assignment_id
            )

            if deleted:

                save_assignments(DATA_FILE, assignments)

                print("Assignment deleted.")

            else:

                print("Assignment not found.")

        elif choice == "5":
            category = input("Enter category: ").strip()

            category_assignments = get_assignments_by_category(
                assignments,
                category,
            )
            view_assignments(category_assignments)

        elif choice == "6":
            save_assignments(DATA_FILE, assignments)
            print("Goodbye!")
            running = False

        else:
            print("Please choose a number from 1 to 6."
                  )

if __name__ == "__main__":
    main()
