from flask import Flask, render_template, request

app = Flask(__name__)

# Sample menu items
menu_items = [
    {'id': 1, 'name': 'Chocolate Cake', 'price': 20.00},
    {'id': 2, 'name': 'Vanilla Cupcake', 'price': 3.00},
    {'id': 3, 'name': 'Apple Pie', 'price': 15.00},
    {'id': 4, 'name': 'Croissant', 'price': 2.50},
]

@app.route('/')
def home():
    return render_template('menu.html', items=menu_items)

@app.route('/checkout', methods=['POST'])
def checkout():
    selected_items = request.form.getlist('item')
    total_price = sum(item['price'] for item in menu_items if str(item['id']) in selected_items)
    return render_template('checkout.html', total=total_price)

if __name__ == '__main__':
    app.run(debug=True)