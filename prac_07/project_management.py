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
           "- (Q)uit"
    FILENAME = "projects.txt"

    print("Welcome to Pythonic Project Management")

    projects = load_from_file(FILENAME)



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
