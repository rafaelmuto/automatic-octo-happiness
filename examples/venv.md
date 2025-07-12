### VENV

`venv` is a standard Python module used to create isolated, lightweight virtual environments.

### What is a Virtual Environment?

A virtual environment is a self-contained directory that houses a specific version of the Python interpreter and its own set of installed packages. When you activate a virtual environment, your shell is configured to use the Python interpreter and packages from that environment, rather than the system-wide Python installation.

### Why Use `venv`?

1.  **Dependency Isolation:** Prevents package conflicts between projects that require different versions of the same library.
2.  **Clean Global Environment:** Keeps your system's global Python installation free of project-specific packages.
3.  **Reproducibility:** Allows you to create a `requirements.txt` file (`pip freeze > requirements.txt`) that lists all project dependencies. Others can then easily replicate the environment (`pip install -r requirements.txt`).

### How `venv` Works: The Workflow

1.  **Creation:**
    Create a new environment (e.g., named `my-project-env`).
    ```bash
    python3 -m venv my-project-env
    ```

2.  **Activation:**
    Activate the environment to start using it.
    *   **Linux/macOS:**
        ```bash
        source my-project-env/bin/activate
        ```
    *   **Windows:**
        ```bash
        my-project-env\Scripts\activate
        ```
    Your shell prompt will typically change to show the name of the active environment.

3.  **Usage:**
    While active, `python` and `pip` commands are local to the environment. Installed packages are stored within the environment's directory.

4.  **Deactivation:**
    Return to the global Python context.
    ```bash
    deactivate
    ```

5. Save dependencies to file
    ```bash
    pip freeze > requirements.txt
    ```
6. Install dependencies from file
    ```bash
    pip install -r requirements.txt
    ```