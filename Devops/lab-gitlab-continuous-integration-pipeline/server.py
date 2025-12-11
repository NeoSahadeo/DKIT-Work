# flask app to display simple page

from flask import Flask, render_template
import app1

app = Flask(__name__)

@app.route('/')
def list_stock():
    stock_data = app1.loadStock('stock.txt')
    return render_template('stock.html.j2', data=stock_data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
            
