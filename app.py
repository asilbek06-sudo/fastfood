from flask import Flask, render_template, request

app = Flask(__name__)

# Список блюд в коде (не JSON)
menu_items = [
    {"name": "Чизбургер", "price": 250},
    {"name": "Пицца Пепперони", "price": 450},
    {"name": "Кола 0.5 л", "price": 100}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html', items=menu_items)

@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        item = request.form['item']
        return render_template('success.html', name=name, item=item)
    return render_template('order.html', items=menu_items)

if __name__ == '__main__':
    app.run(debug=True)
