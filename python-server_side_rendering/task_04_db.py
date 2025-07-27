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

    elif source == "sql":
        import sqlite3
        try:
            conn = sqlite3.connect("products.db")
            cursor = conn.cursor()

            if product_id:
                cursor.execute("SELECT id, name, category, price FROM Products WHERE id=?", (product_id,))
                row = cursor.fetchone()
                if row:
                    products.append({
                        "id": row[0],
                        "name": row[1],
                        "category": row[2],
                        "price": row[3]
                    })
                else:
                    error = "Product not found"
            else:
                cursor.execute("SELECT id, name, category, price FROM Products")
                rows = cursor.fetchall()
                for row in rows:
                    products.append({
                        "id": row[0],
                        "name": row[1],
                        "category": row[2],
                        "price": row[3]
                    })

            conn.close()
        except Exception:
            error = "Error reading SQLite database"

    else:
        error = "Wrong source"

    #filter by product_id
    if product_id and not error:
        filtered = []
        for p in products:
            pid = p.get("id")
            if str(pid) == str(product_id):
                filtered.append(p)

        if filtered:
            products = filtered
        else:
            products = []
            error = "Product not found"
            
    return render_template("product_display.html", products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
