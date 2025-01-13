# Contributing to PyWar

Thank you for taking interest in contributing to **PyWar**!

This guide will walk you through the steps needed to begin contributing to the project.

## License

By contributing to this project, you acknowledge and agree that your contributions will be licensed under the terms of the [MIT License](./LICENSE).

## How to get started

1. The first step depends on wether you're my pair programming partner:
    - If you are my pair programming partner:
        - Clone this repository to your local machine.
    - If you're not:
        - [Fork](https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-a-project#about-forking) this repository (if you've never forked a repository before, have a look at this [great guide](https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-a-project#about-forking) that explains how it works).
        - Clone your fork to your local machine.
1. Run:
    ```
    cd pywar
    ```

1. Set up Python virtual environment and install dependencies. I'll present to you two possible ways to complete this step. Choose whichever one you feel the most comfortable with:
    - The first way is to use [uv](https://github.com/astral-sh/uv) Python package and project manager.
    - Alternatively, you can use [venv](https://docs.python.org/3/library/venv.html) and [pip](https://pip.pypa.io/en/stable/), the default tools that come with Python.

- ### `uv` method:

    - Install [uv](https://docs.astral.sh/uv/getting-started/installation/).
    - Create a virtual environment and install the dependencies:
        ```
        uv sync
        ```
    - To test your setup, run the test suite followed by the application:
    ```
    uv run pytest && uv run pywar
    ```

- ### `venv` and `pip` method:

    - Create a virtual environment:
        ```sh
        python -m venv .venv
        ```
    - Activate the created virtual environment:
        ```sh
        # On Linux and macOS.
        source .venv/bin/activate
        ```

        ```powershell
        # On Windows.
        .venv/Scripts/activate
        ```
    - Install the dependencies:
        ```
        pip install -e .[dev]
        ```

    5. To test your setup, run the test suite followed by the application:
        ```
        pytest && pywar
        ```
6. If you are my pair programming partner, you can stop reading here and I'll see you in our session👋! If you're not my pair programming partner, read on!

7. Set a remote named `upstream`:
    ```sh
    git remote add upstream git@github.com:dainmik/pywar.git
    ```

    or (if you're using HTTPS)

    ```sh
    git remote add upstream https://github.com/dainmik/pywar.git
    ```
8. You're all set!👍

### Workflow tips

Before starting to work on a feature:

- Ensure your fork's `main` branch is up-to-date with the original `pywar` repository:

    ```sh
    git checkout main

    # Assuming you have set a remote named `upstream` pointing to the original `pywar` repository.
    git pull --rebase upstream main
    ```

- Create a feature branch in your fork and commit the changes to it (this way, you will have a clean main branch that you can branch-off of to work on another feature in case you get stuck on your current one, or if you have any issues with merging your PR):

    ```sh
    # A nice way to name the branch is, for example: `feature/12-optional-description`, with 12 being the issue number or id, and an optional description to find the branch easier if you have a couple. 
    git switch -c feature/<issue_id><-optional-description>
    ```

## Pull request

After completing your feature implementation, please submit a pull request (PR) to the `main` branch of this repository.

## Pull request requirements

**PyWar** follows the **Test-Driven Development (TDD)** approach. When contributing:

1. Write tests before writing the implementation code.
2. Ensure that the tests cover the intended functionality.
3. Run all tests to confirm they pass before submitting a PR.

Please make sure your PR contains both your feature and the relevant tests.