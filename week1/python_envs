# What is a Python virtual environment ("venv")?

| Global Install                                  | Virtual Environment                        |
|-------------------------------------------------|---------------------------------------------|
| Affects entire system                           | Isolated to a project                       |
| Can cause **version conflicts** between projects| Allows per-project dependencies             |
| Risk of breaking other tools                    | Safe sandbox for experimentation            |
| Hard to reproduce on other systems              | Easy to share via `requirements.txt`        |
| Needs admin rights on some systems              | No admin rights needed                      |

Basically, creating a Python env gives you a clean, isolated workspace where you can install specific packages and versions without interfering with other projects or your system Python—like setting up a custom sandbox for each project.

# How do I set up a venv?

On any machine, follow these steps:

1. **Create Project Folder**
   ```bash
   mkdir my_project
   cd my_project
2. **Create Virtual Environment**
   ```bash
   python -m venv venv
3. **Activate Environment**
   - Mac/Linux
   ```bash
   source venv/bin/activate
   ```

   - Windows
   ```bash
   venv\Scripts\activate
4. **Install Required Packages**
   ```bash
   pip install numpy pandas jupyterlab
5. **Save Installed Packages**
   ```bash
   pip freeze > requirements.txt
6. **Deactivate the Environment**
   ```bash
   deactivate
7. **Reactive Later**
   ```bash
   source venv/bin/activate  # or venv\Scripts\activate on Windows
8. **(Optional) Recreate Env from requirements.txt**
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
