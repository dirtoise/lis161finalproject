from flask import Flask, render_template, request, redirect, url_for
from data import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

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