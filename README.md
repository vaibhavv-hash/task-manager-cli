# Task Manager CLI

A simple command-line task manager built using Python.
It allows users to add, view, complete, and delete tasks.
Tasks are stored in a JSON file so they remain available after restarting the application.

## Features

- Add new tasks
- View all tasks
- Mark tasks as completed
- Delete tasks
- Save tasks using JSON file storage

## Requirements

- Python 3.x

## How to Run

1. Clone this repository.

   ```bash
   git clone https://github.com/vaibhavv-hash/task-manager-cli.git
   ```

2. Open the project folder.
3. Run the following command:

   ```bash
   python main.py
   ```

## Data Storage

The application uses a JSON file (`tasks.json`) to store task information.

Each task contains:
- Task name
- Completion status

The application loads previously saved tasks when it starts and saves changes to the JSON file.

## Sample Output

```text
===== TASK MANAGER =====
1. Add Task
2. View Tasks
3. Mark Task as Completed
4. Delete Task
5. Exit
```