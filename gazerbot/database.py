import sqlite3
import os

class LyricDatabase:
    def __init__(self, name="gazerbot.db"):
        appdata = os.path.expandvars(r'%APPDATA%\Gazerbot')
        self.path = f'{appdata}\cache'
        self.db_name = name
        # create folder to store cache in app data
        if not os.path.exists(self.path):
            os.mkdir(appdata)
            os.mkdir(self.path)

    def connect(self):
        if not os.path.exists(f'{self.path}\\{self.db_name}'):
            self.conn = sqlite3.connect(f'{self.path}\\{self.db_name}')
            self.cursor = self.conn.cursor()
            self.cursor.execute("CREATE TABLE tracks(artist TEXT, title TEXT, content TEXT, error TEXT)")
        else:
            self.conn = sqlite3.connect(f'{self.path}\\{self.db_name}')
            self.cursor = self.conn.cursor()
        return self

    def close(self):
        #Exception handling here
        self.conn.close()

    def get_track(self, artist, title):
        rows = self.cursor.execute(f'SELECT content, error FROM tracks WHERE artist="{artist}" and title="{title}"').fetchall()
        return {"content": rows[0][0], "error": rows[0][1]} if rows else None

    def get_all_tracks(self):
        rows = self.cursor.execute(f'SELECT * FROM tracks').fetchall()
        return rows

    def insert_track(self, artist, title, content):
        content = content.replace("\"", "'")
        return self.cursor.execute(f'INSERT INTO tracks VALUES("{artist}", "{title}", "{content}", NULL)')

    def insert_track_error(self, artist, title, error):
        return self.cursor.execute(f'INSERT INTO tracks VALUES("{artist}", "{title}", NULL, "{error}")')


class LyricDatabaseContext:
    def __init__(self, name="gazerbot.db"):
        self.db = LyricDatabase(name)

    def __enter__(self):
        self.db.connect()
        return self.db

    def __exit__(self, type, value, traceback):
        #Exception handling here
        self.db.close()