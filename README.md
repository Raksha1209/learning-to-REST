create a virtual environment----

# python -m venv .venv

activate it

# .venv\Scripts\Activate.ps1

to be 100% sure we're using the right one

# python -m pip install requests

# python -m pip install flask

# python -m pip install flask-sqlalchemy

to save them requirements.txt---

# pip freeze > requrements.txt

# python -m pip install requests

to tell Flask which python file has our app--->

# $env:FLASK_APP = "application.py"(powershell cmd)

Puts Flask into development mode(auto reload, debugging features, bad code warnings) instead of production.

# $env:FLASK_ENV = "development"

to run

# flask run
