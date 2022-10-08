from re import I
from flask import Flask, render_template, request
from website import *

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
