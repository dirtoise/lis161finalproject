
combomeals = {}
alacarte = {
    'pancit canton' : [
                                        {
                                        'flavor': 'classic',
                                        'url':'',
                                        'amnt':'',
                                        },
                                        {
                                            'flavor': 'calamansi',
                                            'url': '',
                                            'amnt':'',

                                        },
                                        {
                                        'flavor': 'chili-mansi',
                                        'url': '',
                                        'amnt':'',
                                        },
                                        {
                                            'flavor': 'sweetspicy',
                                            'url': '',
                                            'amnt':'',
                                        },
                                        {
                                            'flavor': 'hotchili',
                                            'url': '',
                                            'amnt':'',
                                        },
                    ],
    'kwek-kwek' : [
                                {
                                    'sauce': 'plain',
                                    'url': '',
                                    'amnt':'',
                                },
                                {
                                    'sauce': 'sweet',
                                    'url': '',
                                    'amnt':'',
                                },
                                {
                                    'sauce': 'sweetspicy',
                                    'url': '',
                                    'amnt':'',
                                },
                                {
                                    'sauce': 'vinegarsauce',
                                    'url': '',
                                    'amnt':'',
                                },
                                {
                                    'sauce': 'sweetvinegarsauce',
                                    'url': '',
                                    'amnt':'',
                                }
                    ],
    'kikiam' : [
                                {
                                    'sauce': 'plain',
                                    'url': '',
                                    'amnt':'',
                                },
                                {
                                    'sauce': 'sweet',
                                    'url': '',
                                    'amnt':'',
                                },
                                {
                                    'sauce': 'sweetspicy',
                                    'url': '',
                                    'amnt':'',
                                },
                                {
                                    'sauce': 'vinegarsauce',
                                    'url': '',
                                    'amnt':'',
                                },
                                {
                                    'sauce': 'sweetvinegarsauce',
                                    'url': '',
                                    'amnt':'',
                                }
                                                                         ],
    'fishball' : [
                                {
                                    'sauce': 'plain',
                                    'url': '',
                                    'amnt': '',
                                },
                                {
                                'sauce': 'sweet',
                                'url': '',
                                'amnt':'',
                                },
                                {
                                'sauce': 'sweetspicy',
                                'url': '',
                                'amnt':'',
                                },
                                {
                                'sauce': 'vinegarsauce',
                                'url': '',
                                'amnt':'',
                                },
                                {
                                'sauce': 'sweetvinegarsauce',
                                'url': '',
                                'amnt':'',
                                }
],
    'squidball' :  [
                                {
                                'sauce': 'plain',
                                'url': '',
                                'amnt':'',
                                },
                                {
                                'sauce': 'sweet',
                                'url': '',
                                'amnt':'',
                                },
                                {
                                'sauce': 'sweetspicy',
                                'url': '',
                                'amnt':'',
                                },
                                {
                                'sauce': 'vinegarsauce',
                                'url': '',
                                'amnt':'',
                                },
                                {
                                'sauce': 'sweetvinegarsauce',
                                'url': '',
                                'amnt':'',
                                }
                    ],
    'chickenball' : [
                                    {
                                    'sauce': 'plain',
                                    'url': '',
                                    'amnt':'',
                                    },
                                    {
                                    'sauce': 'sweet',
                                    'url': '',
                                    'amnt':'',
                                    },
                                    {
                                    'sauce': 'sweetspicy',
                                    'url': '',
                                    'amnt':'',
                                    },
                                    {
                                    'sauce': 'vinegarsauce',
                                    'url': '',
                                    'amnt':'',
                                    },
                                    {
                                    'sauce': 'sweetvinegarsauce',
                                    'url': '',
                                    'amnt':'',
                                    }
                                    ],
         }
drinks = {}
meals = {
    'combomeals' : combomeals,
    'alacarte' : alacarte,
    'drinks' : drinks
}

for i in meals:
   if i == 'alacarte':
        for x in alacarte:
            print(x)
   elif i == 'combomeals':
        for x in combomeals:
            print(x)
   else:
        for x in drinks:
            print(x)


pets = {
    'dogs': [
        {
            'name': 'Spot',
            'age': 2,
            #'breed': 'Dalmatian',
            'description': 'Spot is an energetic puppy who seeks fun and adventure!',
            'url': 'https://content.codecademy.com/programs/flask/introduction-to-flask/dog-spot.jpeg'
        },
        {
            'name': 'Shadow',
            'age': 4,
            'breed': 'Border Collie',
            'description': 'Eager and curious, Shadow enjoys company and can always be found tagging along at your heels!',
            'url': 'https://content.codecademy.com/programs/flask/introduction-to-flask/dog-shadow.jpeg'
        }
    ],
    'cats': [
        {
            'name': 'Snowflake',
            'age': 1,
            'breed': 'Tabby',
            'description': 'Snowflake is a playful kitten who loves roaming the house and exploring.',
            'url': 'https://content.codecademy.com/programs/flask/introduction-to-flask/cat-snowflake.jpeg'
        }
    ],
    'rabbits': [
        {
            'name': 'Easter',
            'age': 4,
            'breed': 'Mini Rex',
            'description': 'Easter is a sweet, gentle rabbit who likes spending most of the day sleeping.',
            'url': 'https://content.codecademy.com/programs/flask/introduction-to-flask/rabbit-easter.jpeg'
        }
    ]
}


import sqlite3

db_path = 'pa.db'

def connect_db(path):
    conn = sqlite3.connect(path)
    #converts tuples to dictionary
    conn.row_factory = sqlite3.Row
    return (conn, conn.cursor())

def read_pets_by_type(pet_type):
    conn, cur = connect_db(db_path)
    query = 'SELECT * FROM pets WHERE type=?'
    results = cur.execute(query, (pet_type,)).fetchall()
    conn.close()
    return results

def read_pets_by_id(pet_id):
    conn, cur = connect_db(db_path)
    query = 'SELECT * FROM pets WHERE id=?'
    results = cur.execute(query, (pet_id,)).fetchone()
    conn.close()
    return results

def insert_pet(pet_data):
    conn, cur = connect_db(db_path)
    query = 'INSERT INTO pets (name, age, description, breed, url, type) VALUES (?, ?, ?, ?, ?, ?)'
    values = (pet_data['name'],
              pet_data['age'],
              pet_data['description'],
              pet_data['breed'],
              pet_data['url'],
              pet_data['type'],)
    cur.execute(query, values)
    conn.commit()
    conn.close()

def delete_pet(pet_id):
    conn, cur = connect_db(db_path)
    query = 'DELETE FROM pets WHERE id=?'
    cur.execute(query, (pet_id,))
    conn.commit()
    conn.close()

def update_pet(pet_data):
    conn, cur = connect_db(db_path)
    query = 'UPDATE pets SET name=?, age=?, description=?, breed=?, url=?, type=? WHERE id=?'
    values = (pet_data['name'],
              pet_data['age'],
              pet_data['description'],
              pet_data['breed'],
              pet_data['url'],
              pet_data['type'],
              pet_data['id'],
              )
    cur.execute(query, values)
    conn.commit()
    conn.close()
