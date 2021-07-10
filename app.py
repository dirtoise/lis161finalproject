from flask import Flask, render_template, request, redirect, url_for, session,jsonify
from data import *

app = Flask(__name__)
app.secret_key = '123'

@app.route('/test')
def test():
    flavordict = select_dict_flavors()

    return render_template('test.html',flavordict=flavordict)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',)
def login():
    return render_template('login.html',)

@app.route('/loginprocessing', methods=['POST', 'GET'])
def loginprocessing():
    usercart = select_dict_cart()
    loginuser = select_dict_user()

    for users in loginuser:
        if request.form['name'] in users['username']:
            if request.form['name'] == users['username'] and request.form['password'] == users['password']:
                user = request.form['name']
                session['user'] = user
                if user in users:
                    users['user_id']
                    user_id = users['user_id']
                    if any(usercart) == True:
                        for ids in usercart:

                            user_data = {
                                'user_id': user_id,
                                'user': user,
                                'cart_id': ids['cart_id'],
                            }

                            update_user_in_cart(user_data)
                        return redirect(url_for('user'))
                    else:
                        return redirect(url_for('user'))
            else:
                return redirect(url_for('login', ))
    else:
        return redirect(url_for('register', ))


@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/registerprocessing', methods=['POST'])
def registerprocessing():
    loginuser = select_dict_user()
    usercart = select_dict_cart()

    login_data = {
        'user' : request.form['name'],
        'password' : request.form['password'],
    }
    if request.form['password'] == request.form['confirmpassword']:
        if 'user' not in loginuser:
            user = request.form['name']
            session['user'] = user
            if any(usercart) == True:
                for ids in usercart:
                    ids['cart_id']
                    cart_id = ids['cart_id']
                user_data = {
                    'user' : request.form['name'],
                    'user_id' : ids['user_id'],
                    'cart_id' : cart_id,
                }
                insert_user_into_user(login_data)
                update_user_in_cart(user_data)
            elif any(cart) == False:
                insert_user_into_user(login_data)
            return redirect(url_for('user'))
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('register'))

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
    session.pop('user', None)

    return redirect(url_for('login'))

@app.route('/profile')
def profile():
    loginuser = select_dict_user()
    finalcart = select_dict_finalcart()
    for users in loginuser:
        if users['username'] == session['user']:
            users['username']
            username = users['username']
            user_id = users['user_id']
            for finalusers in finalcart:
                if finalusers['user'] == username:
                    finalusers['user_id']
                    finalusers = finalusers['user_id']
    return render_template('profile.html',loginuser=loginuser,username=username,user_id=user_id,finalcart=finalcart,finalusers=finalusers,)

@app.route('/menu')
def basemenu():
    return render_template('basemenu.html')

@app.route('/menu/<meals_type>/')
def menu(meals_type):
    meals = read_meals_by_type(meals_type,)
    alacartesdict = select_dict_alacarte_type()
    drinksdict = select_dict_drinks_type()
    return render_template('menu.html',meals_type=meals_type,meals=meals,alacartesdict=alacartesdict,drinksdict=drinksdict)

@app.route('/menu/drinks/<int:drinks_id>/<drinks_type>/')
def drinks(drinks_id,drinks_type):
    drinksid = read_drinks_by_id(drinks_id)
    meals = select_dict_meals()
    loginuser = select_dict_user()

    for users in loginuser:
        if 'user' not in session:
            if 'guest' in users['username']:
                username = users['username']
                user_id = users['user_id']
        elif 'user' in session:
            if users['username'] == session['user']:
                users['username']
                username = users['username']
                user_id = users['user_id']

    return render_template('drinks.html',drinks_id=drinks_id,drinks_type=drinks_type, drinksid=drinksid,
                           meals=meals,loginuser=loginuser,username=username,user_id=user_id)

@app.route('/menu/alacarte/<int:alacarte_id>/<alacarte_type>/')
def alacartes(alacarte_id, alacarte_type):
    alacarteid = read_alacarte_by_id(alacarte_id)
    meals = select_dict_meals()
    flavordict = select_dict_flavors()
    saucedict = select_dict_sauces()
    loginuser = select_dict_user()

    for users in loginuser:
        if 'user' not in session:
            if 'guest' in users['username']:
                username = users['username']
                user_id = users['user_id']
        elif 'user' in session:
            if users['username'] == session['user']:
                users['username']
                username = users['username']
                user_id = users['user_id']

    return render_template('alacartemeals.html',alacarte_id=alacarte_id, alacarteid=alacarteid,
                           alacarte_type=alacarte_type,flavordict=flavordict,saucedict=saucedict,
                           meals=meals,loginuser=loginuser,username=username,user_id=user_id)

@app.route('/order')
def baseorder():
    return render_template('order.html')

@app.route('/mealprocessing/', methods=['POST'])
def mealprocessing():

    totalamount = int(request.form['amount']) * int(request.form['price'])

    cart_data = {
        'user_id': request.form['user_id'],
        'user' : request.form['username'],
        'meals_type' : request.form['meals_type'],
        'alacarte_type' : request.form['alacarte_type'],
        'drinks_type' : request.form['drinks_type'],
        'amount': int(request.form['amount']),
        'price': int(request.form['price']),
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

    for users in loginuser:
        if 'user' not in session:
            if 'guest' in users['username']:
                username = users['username']
                user_id = users['user_id']
        elif 'user' in session:
            if users['username'] == session['user']:
                users['username']
                username = users['username']
                user_id = users['user_id']


    cartchecker = any(usercart)

    return render_template('cart.html', loginuser=loginuser, usercart=usercart, cartchecker=cartchecker, totalprice=totalprice,username=username,user_id=user_id)

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


@app.route('/cart/<int:user_id>/<users>/checkout/', methods=['post'])
def checkout(user_id,users):
    loginuser = select_dict_user()
    usercart = select_dict_cart()
    totalprice = 0
    for userdata in usercart:
        totalprice += int(userdata['total_amount'])

    if any(session) == False:
        for users in loginuser:
            users = users['username']
    else:
        if any(session) == True:
            for users in loginuser:
                users['username'] == session['user']
                users = users['username']

    return render_template('checkout.html', users=users,user_id=user_id,usercart=usercart,totalprice=totalprice)


@app.route('/finalizeprocessing', methods=['POST'])
def finalizeprocessing():
    usercart = select_dict_cart()
    finalcart = select_dict_finalcart()
    change = 0
    if int(request.form['payment_amount']) >= int(request.form['totalprice']):
        change = int(request.form['payment_amount']) - int(request.form['totalprice'])
    else:
        return redirect(url_for('checkout', users=users,user_id=user_id,usercart=usercart,totalprice=totalprice))

    if any(finalcart) == False:
        finalcart_id = 0
        finalcart_id += 1
    else:
        for data in finalcart:
            finalcart_id = data['finalcart_id']
            finalcart_id += 1

    for userdata in usercart:
        finalcart_data = {
            'finalcart_id' : int(finalcart_id),
            'order_type' : request.form['order_type'],
            'order_location' : request.form['order_location'],
            'cart_id' : userdata['cart_id'],
            'user_id' : userdata['user_id'],
            'user' : userdata['user'],
            'total_price' : int(request.form['totalprice']),
            'payment_amount' : int(request.form['payment_amount']),
            'change' : int(change),
            'payment_method' : request.form['payment_method']
        }
        insert_final_into_finalcart(finalcart_data)

    return redirect(url_for('finalize', user_id=request.form['user_id'], users=request.form['username'], finalcart_id=finalcart_id))

@app.route('/cart/<int:user_id>/<users>/<int:finalcart_id>/finalize')
def finalize(user_id,users,finalcart_id):
    loginuser = select_dict_user()
    finalcartid = read_finalcart_by_id(finalcart_id)
    finalcart = select_dict_finalcart()
    usercart = select_dict_cart()

    if 'user' not in session:
        for users in loginuser:
            users = users['username']
    else:
        if 'user' in session:
            for users in loginuser:
                users['username'] == session['user']
                users = users['username']

    return render_template('final.html', user_id=user_id, users=users, finalcart_id=finalcart_id,
                           finalcartid=finalcartid, finalcart=finalcart, usercart=usercart)

# Kiosk route to work on later
""" 
@app.route('order/<kiosk>')
def order(kiosk):
    return render_template('kiosk.html')
"""

if __name__ == '__main__':
    app.run(debug=True)