import sqlite3


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
        owners = []
        for row in rows:
            owner = {
                'id': row[0],
                'username': row[1],
                'password': row[2]
            }
            owners.append(owner)
        return owners

    @staticmethod
    def get_owner(owner_id):
        connection = sqlite3.connect('site.db')
        cursor = connection.cursor()

        query = 'SELECT * FROM owners WHERE id=?'
        cursor.execute(query, (owner_id,))

        row = cursor.fetchone()
        columns = ('id', 'username', 'password')
        if row:
            return dict(zip(columns, row))

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
        hosts = []
        for row in rows:
            host = {
                'id': row[0],
                'username': row[1],
                'password': row[2]
            }
            hosts.append(host)
        return hosts

    @staticmethod
    def get_host(host_id):
        connection = sqlite3.connect('site.db')
        cursor = connection.cursor()

        query = 'SELECT * FROM hosts WHERE id=?'
        cursor.execute(query, (host_id,))

        row = cursor.fetchone()
        columns = ('id', 'username', 'password')
        if row:
            return dict(zip(columns, row))
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
