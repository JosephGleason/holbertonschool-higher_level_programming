#!/usr/bin/python3

from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    products = []
    error = None

    if source == "json":
        try:
            with open("products.json") as f:
                data = json.load(f)
                products = data
        except Exception:
            error = "Error reading JSON file."

    elif source == "csv":
        try:
            with open("products.csv") as f:
                reader = csv.DictReader(f)
                products = [row for row in reader]
        except Exception:
            error = "Error reading CSV file."

    else:
        error = "Wrong source"

    return render_template("product_display.html", products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
