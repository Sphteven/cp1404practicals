"""
Estimated time: 40min
Actual time:

"""

from project import Project


def main():
    """Run through the menu until user decides to quit."""
    MENU = "- (L)oad projects \n" \
           "- (S)ave projects \n" \
           "- (D)isplay projects  \n" \
           "- (F)ilter projects by date\n" \
           "- (A)dd new project  \n" \
           "- (U)pdate project \n" \
           "- (Q)uit\n"
    FILENAME = "projects.txt"

    projects = load_from_file(FILENAME)
    print("Welcome to Pythonic Project Management")
    print(f"{len(projects)} projects loaded")
    choice = input(MENU).upper()
    while choice != "Q":
        if choice == "L":
            print("yes")
        elif choice == "S":
            file_name = input("Enter a file name you would like to save to: ")
            while file_name == "":
                print("Your filename can't be empty")
                file_name = input("Enter a file name you would like to save to: ")
            file_name = file_name + ".txt"  # to make sure file is saved as a textfile
            save_to_file(file_name, projects)
        elif choice == "D":
            print("Incomplete projects: ")
            for project in projects:
                if project.is_complete() is False:
                    print(project)
            print("Completed projects: ")
            for project in projects:
                if project.is_complete() is True:
                    print(project)
        elif choice == "F":
            print("yest")
        elif choice == "A":
            print("Let's add a new project")
            name = input("Name: ")
            start_date = input("Start date(dd/mm/yy): ")
            priority = input("Priority: ")
            cost = input("Cost estimate: ")
            percent_complete = input("Percent complete: ")
            projects.append(Project(name, start_date, priority, cost, percent_complete))
        elif choice == "U":
            print("yest")
        else:
            print("Invalid input")
        choice = input(MENU).upper()


def save_to_file(file_name, projects):
    with open(file_name, "w") as projects_file:
        projects_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            projects_file.write(
                f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")


def load_from_file(file_name):
    projects = []
    with open(file_name, "r") as file:
        file.readline()  # To step over the title in the textfile
        for line in file:
            line = line.strip()
            parts = line.split("\t")
            project = Project(parts[0], parts[1], parts[2], parts[3], parts[4])
            projects.append(project)
    return projects


main()
