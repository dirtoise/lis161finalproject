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
    query = 'INSERT INTO cart (user_id, user, meals_type, alacarte_type, amount, price, flavors_type, sauces_type) VALUES (?,?,?,?,?,?,?,?)'
    values = (
              cart_data['user_id'],
              cart_data['user'],
              cart_data['meals_type'],
              cart_data['alacarte_type'],
              cart_data['amount'],
              cart_data['price'],
              cart_data['flavors_type'],
              cart_data['sauces_type']
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
    query ='UPDATE cart SET amount=?, flavors_type=?, sauces_type=? WHERE cart_id=?'
    values = (
            cart_data['amount'],
            cart_data['flavors_type'],
            cart_data['sauces_type'],
            cart_data['cart_id']
    )
    cur.execute(query,values)
    conn.commit()
    conn.close()
