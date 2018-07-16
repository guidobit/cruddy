# Getting started

1. Clone the project
2. Go into the project directory
3. From the terminal, init a virtualenv
`virtualenv -p python3.6 env` (This will create a virtual env with python3.6 included)
4. Run `pip install -r requirements.txt` to install dependencies.

If you need to edit or run the project, run the following command to activate the virtual env again:
`source env/bin/activate`

## Updating dependencies

Before you use newer packages:

1. Run tests
2. Make sure the `requirements.txt` is updated

Tips:

* `pipreqs .` generates requirements based of project files
* `pip freeze` shows current installed packages in your virtualenv


## Prerequisites

* Make sure `python3.6-dev` is installed with your OS package manager.
