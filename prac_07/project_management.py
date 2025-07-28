
"""
Estimated time: 40min
Actual time: 2 hours 30 min

"""

import datetime
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
            file_name = input("Enter the name you will like to load:")
            file_name = file_name + ".txt"
            temp_projects = load_from_file(file_name)
            if temp_projects is not None:
                projects = temp_projects
                print(f"{len(projects)} projects loaded")
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
            date_choice = input("Show projects after date (d/m/yyyy): ")  # e.g., "30/9/2022"
            date = datetime.datetime.strptime(date_choice, "%d/%m/%Y").date()
            for project in projects:
                project_date = datetime.datetime.strptime(project.start_date, "%d/%m/%Y").date()
                if date < project_date:
                    print(project)
        elif choice == "A":
            projects.append(add_new_project())
        elif choice == "U":
            for i, project in enumerate(projects):
                print(f"{i} {project}")
            project_choice = int(input("Project choice: "))
            if project_choice != "":
                try:
                    print(projects[project_choice])
                    new_percentage = int(input("New percentage: "))
                    new_priority = int(input("New priority: "))
                    projects[project_choice].completion_percentage = new_percentage
                    projects[project_choice].priority = new_priority
                except IndexError:
                    print("Invalid choice")
        else:
            print("Invalid input")
        choice = input(MENU).upper()


def add_new_project():
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date(dd/mm/yy): ")
    priority = input("Priority: ")
    cost = input("Cost estimate: ")
    percent_complete = input("Percent complete: ")
    new_project = Project(name, start_date, priority, cost, percent_complete)
    return new_project


def save_to_file(file_name, projects):
    """Saves projects to a file."""
    with open(file_name, "w") as projects_file:
        projects_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            projects_file.write(
                f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t"
                f"{project.completion_percentage}\n")


def load_from_file(file_name):
    """Load projects from specified file."""
    projects = []
    try:
        with open(file_name, "r") as file:
            file.readline()  # To step over the title in the textfile
            for line in file:
                line = line.strip()
                parts = line.split("\t")
                project = Project(parts[0], parts[1], parts[2], parts[3], parts[4])
                projects.append(project)
        return projects
    except FileNotFoundError:
        print("File does not exist")


main()
