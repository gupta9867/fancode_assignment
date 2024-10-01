City FanCode Todo Automation
Overview
This project automates the validation that all users belonging to the city FanCode have completed more than 50% of their todo tasks. The automation checks each user's task completion status and ensures their completed task percentage is greater than 50%.

Scenario
Given: A user has todo tasks.
And: The user belongs to the city FanCode.
Then: The user's completed task percentage should be greater than 50%.
Requirements
Before running the project, ensure you have installed all necessary dependencies.

Installation
Clone the repository:
git clone https://github.com/yourusername/city-fancode-todo-automation.git

Navigate to the project directory:
cd city-fancode-todo-automation

Install the required dependencies:
pip install -r requirements.txt

Running the Automation
The main file to execute the automation is test_runner.py.
To run the automation:
python test_runner.py
This will execute the test scenario and verify that all users from the city FanCode have completed more than 50% of their todos.

Notes
Ensure the requirements.txt file is up to date with all necessary dependencies.
The script assumes users and their todos are correctly structured and available in the required format (e.g., database, file, API, etc.).
