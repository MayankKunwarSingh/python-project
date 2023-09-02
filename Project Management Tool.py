import json

# Initialize an empty project list
projects = []

def save_projects():
    with open("projects.json", "w") as file:
        json.dump(projects, file)

def load_projects():
    try:
        with open("projects.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def create_project(name, description):
    project = {"name": name, "description": description, "tasks": []}
    projects.append(project)
    save_projects()

def create_task(project_index, title, description, deadline):
    task = {"title": title, "description": description, "deadline": deadline}
    projects[project_index]["tasks"].append(task)
    save_projects()

def list_projects():
    for i, project in enumerate(projects):
        print(f"{i + 1}. {project['name']} - {project['description']}")

# Load existing projects
projects = load_projects()

while True:
    print("\nProject Management Tool")
    print("1. Create Project")
    print("2. List Projects")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter project name: ")
        description = input("Enter project description: ")
        create_project(name, description)
        print("Project created!")

    elif choice == "2":
        list_projects()

    elif choice == "3":
        break