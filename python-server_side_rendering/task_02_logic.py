from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    # items.json faylını oxumaq üçün
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
            # JSON-dan "items" siyahısını götürürük. 
            # Əgər yoxdursa, boş siyahı qaytarırıq.
            items_list = data.get('items', [])
    except FileNotFoundError:
        # Əgər fayl tapılmazsa, boş siyahı kimi davranırıq
        items_list = []
    except json.JSONDecodeError:
        # Əgər JSON faylı xətalıdırsa
        items_list = []

    # Şablona 'items' dəyişənini göndəririk
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
