#nav sidebar active
active = 'active'

import sqlite3

db_path = 'pb.db'

def connect_db(path):
    conn = sqlite3.connect(path)
    #converts tuples to dictionary
    conn.row_factory = sqlite3.Row
    return (conn, conn.cursor())

def insert_user_into_user(session):
    conn, cur = connect_db(db_path)
    query = 'INSERT INTO user (username) VALUES (?)'
    values = (session['user'],)
    cur.execute(query, values)
    conn.commit()
    conn.close()

def read_user_by_id(user_id):
    conn, cur = connect_db(db_path)
    query = 'SELECT * FROM user WHERE user_id=?'
    results = cur.execute(query, (user_id,)).fetchone()
    conn.close()
    return results

def delete_user_from_user(username):
    conn, cur = connect_db(db_path)
    query = 'DELETE FROM user WHERE username=?'
    cur.execute(query, (username,))
    conn.commit()
    conn.close()

def select_dict_user():
    conn, cur = connect_db(db_path)
    query = 'SELECT * FROM user'
    results = cur.execute(query,).fetchall()
    return results

def select_dict_meals():
    conn, cur = connect_db(db_path)
    query = 'SELECT * FROM meals'
    results = cur.execute(query,).fetchall()
    return results

def read_meals_by_type(meals_type):
    conn, cur = connect_db(db_path)
    query = 'SELECT * FROM meals WHERE meals_type=?'
    results = cur.execute(query, (meals_type,)).fetchone()
    conn.close()
    return results

def select_dict_alacarte_type():
    conn, cur = connect_db(db_path)
    query = 'SELECT * FROM alacarte'
    results = cur.execute(query,).fetchall()
    return results

def read_alacarte_by_id(alacarte_id):
    conn, cur = connect_db(db_path)
    query = 'SELECT * FROM alacarte WHERE alacarte_id=?'
    results = cur.execute(query, (alacarte_id,)).fetchone()
    conn.close()
    return results

def select_dict_flavors():
    conn, cur = connect_db(db_path)
    query = 'SELECT * FROM flavors'
    results = cur.execute(query, ()).fetchall()
    conn.close()
    return results

def select_dict_sauces():
    conn, cur = connect_db(db_path)
    query = 'SELECT * FROM sauces'
    results = cur.execute(query, ()).fetchall()
    conn.close()
    return results

def select_dict_cart():
    conn, cur = connect_db(db_path)
    query = 'SELECT * FROM cart'
    results = cur.execute(query, ()).fetchall()
    conn.close()
    return results

def read_cart_by_id(cart_id):
    conn, cur = connect_db(db_path)
    query = 'SELECT * FROM cart WHERE cart_id=?'
    results = cur.execute(query, (cart_id,)).fetchone()
    conn.close()
    return results

def insert_alacarte_into_cart(cart_data):
    conn, cur = connect_db(db_path)
    query = 'INSERT INTO cart (user_id, user, meals_type, alacarte_type, ' \
            'amount, price, flavors_type, sauces_type, total_amount) ' \
            'VALUES (?,?,?,?,?,?,?,?,?)'
    values = (
              cart_data['user_id'],
              cart_data['user'],
              cart_data['meals_type'],
              cart_data['alacarte_type'],
              cart_data['amount'],
              cart_data['price'],
              cart_data['flavors_type'],
              cart_data['sauces_type'],
              cart_data['total_amount'],
    )
    cur.execute(query, values)
    conn.commit()
    conn.close()

def delete_cart_from_cart(cart_id):
    conn, cur = connect_db(db_path)
    query = 'DELETE FROM cart WHERE cart_id=?'
    cur.execute(query, (cart_id,))
    conn.commit()
    conn.close()

def update_cart(cart_data):
    conn, cur = connect_db(db_path)
    query ='UPDATE cart SET amount=?, flavors_type=?, sauces_type=?, total_amount=? WHERE cart_id=?'
    values = (
            cart_data['amount'],
            cart_data['flavors_type'],
            cart_data['sauces_type'],
            cart_data['total_amount'],
            cart_data['cart_id'],
    )
    cur.execute(query,values)
    conn.commit()
    conn.close()

def insert_final_into_finalcart(finalcart_data):
    conn, cur = connect_db(db_path)
    query = 'INSERT INTO finalcart (finalcart_id, order_type, order_location, cart_id, user_id, user, ' \
            'total_price, payment_amount, change, payment_method) ' \
            'VALUES (?,?,?,?,?,?,?,?,?,?)'
    values = (
            finalcart_data['finalcart_id'],
            finalcart_data['order_type'],
            finalcart_data['order_location'],
            finalcart_data['cart_id'],
            finalcart_data['user_id'],
            finalcart_data['user'],
            finalcart_data['total_price'],
            finalcart_data['payment_amount'],
            finalcart_data['change'],
            finalcart_data['payment_method'],
    )
    cur.execute(query, values)
    conn.commit()
    conn.close()


def read_finalcart_by_id(finalcart_id):
    conn, cur = connect_db(db_path)
    query = 'SELECT * FROM finalcart WHERE finalcart_id=?'
    results = cur.execute(query, (finalcart_id,)).fetchone()
    conn.close()
    return results

def select_dict_finalcart():
    conn, cur = connect_db(db_path)
    query = 'SELECT * FROM finalcart'
    results = cur.execute(query, ()).fetchall()
    conn.close()
    return results
