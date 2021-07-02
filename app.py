from flask import Flask, render_template, request, redirect, url_for, session
from data import *

app = Flask(__name__)
app.secret_key = '123'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    cart = select_dict_cart()

    if request.method == 'POST':
        user = request.form['name']
        session['user'] = user
        session_data = {
            'user' :request.form['name'],
        }
        if any(cart) == True:
            for ids in cart:
                ids['cart_id']
                cart_id = ids['cart_id']
                delete_cart_from_cart(cart_id)
            insert_user_into_user(session_data)
        else:
            insert_user_into_user(session_data)
        return redirect(url_for('user'))
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
    loginuser = select_dict_user()
    cart = select_dict_cart()
    # deletes username in user database on logout #
    for users in loginuser:
        if users['username'] == session['user']:
            users['user_id']
            username = session['user']
            delete_user_from_user(username)

    # deletes cart in database and username in session on logout #
    if any(cart) == True:
        for ids in cart:
            ids['cart_id']
            cart_id = ids['cart_id']
            delete_cart_from_cart(cart_id)
        session.pop('user', None)
    else:
        session.pop('user', None)

    return redirect(url_for('login'))

@app.route('/menu')
def basemenu():
    return render_template('basemenu.html')

@app.route('/menu/<meals_type>/')
def menu(meals_type):
    meals = read_meals_by_type(meals_type,)
    alacartedict = select_dict_alacarte_type()
    return render_template('menu.html',meals_type=meals_type,meals=meals,alacartedict=alacartedict)

@app.route('/menu/<meals_type>/<int:alacarte_id>')
def alacartes(meals_type, alacarte_id):
    alacarteid = read_alacarte_by_id(alacarte_id)
    meals = read_meals_by_type(meals_type)
    flavordict = select_dict_flavors()
    saucedict = select_dict_sauces()
    userdict = select_dict_user()

    for users in userdict:
        if any(session) == False:
                users['username']
                username = users['username']
                user_id = users['user_id']
        else:
            if any(session) == True:
                if users['username'] == session['user']:
                    users['username']
                    username = users['username']
                    user_id = users['user_id']

    return render_template('alacartemeals.html',alacarte_id=alacarte_id, alacarteid=alacarteid,flavordict=flavordict,saucedict=saucedict,meals=meals,userdict=userdict,meals_type=meals_type,username=username,user_id=user_id)

@app.route('/order')
def baseorder():
    return render_template('order.html')

@app.route('/mealprocessing/', methods=['POST'])
def mealprocessing():

    totalamount = int(request.form['alacarte_amount']) * int(request.form['alacarte_price'])

    cart_data = {
        'user_id': request.form['user_id'],
        'user' : request.form['username'],
        'meals_type' : request.form['meals_type'],
        'alacarte_type' : request.form['alacarte_type'],
        'amount': int(request.form['alacarte_amount']),
        'price': int(request.form['alacarte_price']),
        'flavors_type' : request.form['alacarte_flavor'],
        'sauces_type' : request.form['alacarte_sauce'],
        'total_amount': int(totalamount),
    }

    insert_alacarte_into_cart(cart_data)

    return redirect(url_for('cart'))

@app.route('/cart/',)
def cart():
    usercart = select_dict_cart()
    loginuser = select_dict_user()

    totalprice = 0
    for userdata in usercart:
        totalprice += int(userdata['total_amount'])

    cartchecker = any(usercart)

    return render_template('cart.html', loginuser=loginuser, usercart=usercart, cartchecker=cartchecker, totalprice=totalprice)

@app.route('/cart/delete/<int:cart_id>', methods=['POST'])
def delete(cart_id):
    usercart = select_dict_cart()

    if request.form['action'] == 'DELETE':
        delete_cart_from_cart(cart_id)
        return redirect(url_for('cart', cart_id=cart_id, usercart=usercart))

@app.route('/cart/edit', methods=['post'])
def edit():
    usercart = select_dict_cart()

    alacarte_flavor = request.form['alacarte_flavor']
    alacarte_sauce = request.form['alacarte_sauce']
    alacarte_amount = request.form['alacarte_amount']
    cart_id = request.form['cart_id']
    price = request.form['price']

    totalamount = int(request.form['alacarte_amount']) * int(request.form['price'])

    cart_data = {
        'amount': alacarte_amount,
        'flavors_type' : alacarte_flavor,
        'sauces_type' : alacarte_sauce,
        'cart_id': cart_id,
        'price' : price,
        'total_amount' : totalamount,
    }
    update_cart(cart_data)

    return redirect(url_for('cart', cart_id=cart_id))



@app.route('/cart/<int:user_id>/<users>/checkout/',)
def checkout(user_id,users):
    loginuser = select_dict_user()

    if any(session) == False:
        for users in loginuser:
            users = users['username']
    else:
        if any(session) == True:
            for users in loginuser:
                users['username'] == session['user']
                users = users['username']
    return render_template('checkout.html', users=users,user_id=user_id)


# Kiosk route to work on later
""" 
@app.route('order/<kiosk>')
def order(kiosk):
    return render_template('kiosk.html')
"""

if __name__ == '__main__':
    app.run(debug=True)