from flask import Flask
from src import *

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
