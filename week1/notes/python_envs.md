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
    ```

2. **Create Virtual Environment**
    ```bash
    python3 -m venv venv
    ```

3. **Activate Environment**
    - **Mac/Linux**
        ```bash
        source venv/bin/activate
        ```
    - **Windows**
        ```bash
        venv\Scripts\activate
        ```

4. **Install Required Packages**
    ```bash
    pip install numpy pandas jupyterlab
    ```

5. **Save Installed Packages**
    ```bash
    pip freeze > requirements.txt
    ```

6. **Deactivate the Environment**
    ```bash
    deactivate
    ```

7. **Reactivate Later**
    ```bash
    source venv/bin/activate  # or venv\Scripts\activate on Windows
    ```

8. **(Optional) Recreate Env from `requirements.txt`**
    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

# Common Errors and Fixes

### ❌ Error: `python: command not found`
**Cause:** Python isn't installed or not in your system's PATH.  
**Fix:**  
- Make sure Python is installed: [https://www.python.org/downloads/](https://www.python.org/downloads/)
- On macOS/Linux, run `python3` instead.
- On Windows, ensure "Add Python to PATH" was checked during installation.

---

### ❌ Error: `No module named venv`
**Cause:** Your Python installation doesn’t include the `venv` module.  
**Fix:**  

# What is `requirements.txt`?

`requirements.txt` is a plain text file that lists all the Python packages (and their versions) installed in your current environment.

## What is the purpose of `requirements.txt`?

### 1. Reproducibility
It allows others (or you on another machine) to recreate the exact same environment by running:

```bash
pip install -r requirements.txt
```

### 2. Collaboration
When you share code (e.g., on GitHub), your teammates or users know exactly what dependencies are needed. This avoids the "it works on my machine" problem.

### 3. Version Pinning

You can pin versions to avoid future breaking changes. Example:

```bash
numpy==1.26.4
pandas==2.2.2
jupyterlab==4.1.8
```

### 4. Project Best Practice

In any serious Python project, having a `requirements.txt` is standard — it's like a project manifest.

### 5. How It's Created

While you're inside a virtual environment, just run:

`pip freeze > requirements.txt`
