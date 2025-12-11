from flask import Flask, render_template, request
import jinja2

from invoice import load_stock, item_list

STOCK_FILENAME = "stock.txt"
app = Flask(__name__, template_folder="templates")


@app.route("/")
def index():
    env = jinja2.Environment(loader=jinja2.FileSystemLoader("."))
    temp = env.get_template("templates/index.j2")
    temp_list = ["Item 1", "Item 2", "Item 3"]
    page = temp.render(data=temp_list)
    return page


@app.route("/list_stock")
def list_stock():
    env = jinja2.Environment(loader=jinja2.FileSystemLoader("."))
    temp = env.get_template("templates/list_stock.j2")
    temp_list = load_stock(STOCK_FILENAME)
    page = temp.render(data=temp_list)
    return page


def get_stock(file):
    with open(file, "r") as f:
        stock = f.read
    return stock


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
