from flask import Flask, render_template, request, redirect, url_for, session
from data import *

app = Flask(__name__)
app.secret_key = '123'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['name']
        session['user'] = user
        return redirect(url_for('user',))
    else:
        if 'user' in session:
            return redirect(url_for('user',))
        return render_template('login.html')

@app.route('/user')
def user():
    if 'user' in session:
        user = session['user']
        return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/menu')
def basemenu():
    return render_template('basemenu.html')

@app.route('/menu/<meals_type>')
def menu(meals_type):
    return render_template('menu.html',meals_type=meals_type,meals=meals,alacarte=alacarte,combomeals=combomeals,drinks=drinks)

@app.route('/menu/<meals_type>/<alacarte_type>/<int:alacarteid>')
def alacartemeals(meals_type,alacarte_type,alacarteid):
    #debatable for deletion---
    for meal in meals:
        if meal == 'alacarte':
            alacarte
    #------------------------
    alacarteid = alacarteid
    for keys, values in alacarte.items():
        for value in values:
            value = value
    return render_template('alacartemeals.html',meals=meals,meals_type=meals_type,alacarte=alacarte,alacarte_type=alacarte_type,price=price)

@app.route('/order')
def baseorder():
    return render_template('order.html')

@app.route('/instprocessing/', methods=['POST'])
def instprocessing():
    finalize = False
    for cartdatas in cartdata:
        cartdatas=cartdatas

    cartdata_data = {
        'alacarte_type' : request.form['alkeys'],
        'flavor' : request.form['value.flavor'],
    }
    cartprice_data = {
        'price': request.form['value.price'],
        'amount' : request.form['value.amount'],
    }
    if finalize == False:
        cartdata[cartdatas].append(cartdata_data)
        cartdata[cartdatas].append(cartprice_data)

    return redirect(url_for('cart'),)


@app.route('/cart')
def cart():
    return render_template('cart.html', instance=instance, cartdata=cartdata, alacarte=alacarte)


# Kiosk route to work on later
""" 
@app.route('order/<kiosk>')
def order(kiosk):
    return render_template('kiosk.html')
"""

@app.route('/animals/<pet_type>')
def animals(pet_type):
    return render_template('animals.html',pet_type=pet_type, pets=read_pets_by_type(pet_type))

@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
    pet = read_pets_by_id(pet_id)
    return render_template('pet_profile.html',pet=pet)

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/processing', methods=['post'])
def processing():
    pet_type = request.form['pet_type']
    pet_name = request.form['pet_name']
    pet_breed = request.form['pet_breed']
    pet_url = request.form['pet_url']
    pet_age = request.form['pet_age']
    pet_desc = request.form['pet_desc']

    pet_data= {'name' : pet_name,
               'age' : pet_age,
               'breed': pet_breed,
               'url' : pet_url,
               'description' : pet_desc,
               'type': pet_type}
    insert_pet(pet_data)
    return redirect(url_for('animals', pet_type=pet_type))

@app.route('/modify/pet_type/<int:pet_id>', methods=['POST'])
def modify(pet_id):
    pet = read_pets_by_id(pet_id)
    if request.form['action'] == 'Edit':
        return render_template('edit.html', pet=pet)
    elif request.form['action'] == 'Delete':
        delete_pet(pet_id)
        return redirect(url_for('animals', pet_type=pet['type']))

@app.route('/update/pet_type/<int:pet_id>', methods=['POST'])
def update(pet_id):
    pet_name = request.form['pet_name']
    pet_age = request.form['pet_age']
    pet_desc = request.form['pet_desc']
    pet_breed = request.form['pet_breed']
    pet_url = request.form['pet_url']
    pet_type = request.form['pet_type']

    pet_data = {
        'name': pet_name,
        'description': pet_desc,
        'age': pet_age,
        'breed': pet_breed,
        'url': pet_url,
        'type': pet_type,
        'id': pet_id
    }
    update_pet(pet_data)
    return redirect(url_for('pet', pet_id=pet['id']))
    pass


if __name__ == '__main__':
    app.run(debug=True)