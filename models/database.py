import sqlite3

'''
    create_owner(username, password)
    get_owners()
    get_owner(owner_id)
    delete_owner(owner_id)

    create_host(username, password)
    get_hosts()
    get_host(host_id)
    delete_host(host_id)
'''


class Database:

    @staticmethod
    def create_owner(username, password):
        connection = sqlite3.connect('site.db')
        cursor = connection.cursor()

        query = 'INSERT INTO owners VALUES (NULL, ?, ?)'
        cursor.execute(query, (username, password))

        connection.commit()
        connection.close()

    @staticmethod
    def get_owners():
        connection = sqlite3.connect('site.db')
        cursor = connection.cursor()

        query = 'SELECT * FROM owners'
        cursor.execute(query)

        rows = cursor.fetchall()
        return [dict(zip(('id', 'username', 'password'), row)) for row in rows]

    @staticmethod
    def get_owner(owner_id):
        connection = sqlite3.connect('site.db')
        cursor = connection.cursor()

        query = 'SELECT * FROM owners WHERE id=?'
        cursor.execute(query, (owner_id,))

        row = cursor.fetchone()
        if row:
            return dict(zip(('id', 'username', 'password'), row))

    @staticmethod
    def create_host(username, password):
        connection = sqlite3.connect('site.db')
        cursor = connection.cursor()

        query = 'INSERT INTO hosts VALUES (NULL, ?, ?)'
        cursor.execute(query, (username, password))

        connection.commit()
        connection.close()

    @staticmethod
    def get_hosts():
        connection = sqlite3.connect('site.db')
        cursor = connection.cursor()

        query = 'SELECT * FROM hosts'
        cursor.execute(query)

        rows = cursor.fetchall()
        return [dict(zip(('id', 'username', 'password'), row)) for row in rows]

    @staticmethod
    def get_host(host_id):
        connection = sqlite3.connect('site.db')
        cursor = connection.cursor()

        query = 'SELECT * FROM hosts WHERE id=?'
        cursor.execute(query, (host_id,))

        row = cursor.fetchone()
        if row:
            return dict(zip(('id', 'username', 'password'), row))
        connection.close()

    @staticmethod
    def delete_owner(owner_id):
        connection = sqlite3.connect('site.db')
        cursor = connection.cursor()

        query = 'DELETE FROM owners WHERE id=?'
        cursor.execute(query, (owner_id,))

        connection.commit()
        connection.close()

    @staticmethod
    def delete_host(host_id):
        connection = sqlite3.connect('site.db')
        cursor = connection.cursor()

        query = 'DELETE FROM hosts WHERE id=?'
        cursor.execute(query, (host_id,))

        connection.commit()
        connection.close()
