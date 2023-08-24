# halls-of-residence-flat-finder
A Flask web application that can be used to help new students find their Halls of Residence flatmates.

[![wakatime](https://wakatime.com/badge/user/55c30436-1509-4eb9-9f18-fa9b7c6060c4/project/afe5ed57-25dd-41e5-95f5-cd3eddc95aab.svg)](https://wakatime.com/badge/user/55c30436-1509-4eb9-9f18-fa9b7c6060c4/project/afe5ed57-25dd-41e5-95f5-cd3eddc95aab)

---

## Contents

---

# Software Installation Guide

This guide will walk you through the steps to set up and run the "Halls Flatmate Finder" project on your local machine.

## Prerequisites
Before you begin, ensure that you have the following installed on your system:
- Python (version 3.6 or later) *(3.10.8 recommended)*
- Git

## Step 1: Clone the Repository

1. Open your terminal or command prompt.

2. Navigate to the directory where you want to store the project.

3. Run the following command to clone the repository:
```bash
git clone https://github.com/corey-richardson/halls-of-residence-flat-finder.git
```

## Step 2: Install Required Packages

1. Navigate to the project directory:
```bash
cd halls-of-residence-flat-finder
```

2. Create a virtual environment (recommended but optional):
```bash
python -m venv venv
```

3. Activate the virtual environment:
- Windows
```bash
venv\Scripts\activate
```
- Linux, maxOS, GitHub Codespace
```bash
source venv/bin/activate
```

4. Install required packages from `requirements.txt` using pip:
```bash
pip install -r requirements.txt
```
> To update requirements, run `pip freeze > requirements.txt`.

5. Run the `pytest` command below.
```bash
pytest -v --no-header | tee tests/results.txt
```
> The `pytest` tests will run, and you will see the test output in the terminal as well as in the `results.txt` file in the `test/` directory.

## Step 3: Run the Flask Application

1. In the project directory, you'll find a file named app.py. This is the main Flask application file.

2. Run the application using the following command:
```bash
flask run
```
> By default, the application should start on [127.0.0.1:5000/](http://127.0.0.1:5000/) in your web browser.

3. Open your web browser and navigate to [127.0.0.1:5000/](http://127.0.0.1:5000/). You should see the "Halls Flatmate Finder" application running.

## Step 4: Stopping the Application

1. To stop the Flask application, go back to the terminal where the application is running and press <kbd>Ctrl</kbd>+<kbd>C</kbd>.

2. If you used a virtual environment, you can deactivate it by running:
```bash
deactivate
```

You've successfully installed and run the "Halls Flatmate Finder" project on your local machine.
