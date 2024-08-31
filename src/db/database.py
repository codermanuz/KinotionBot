import psycopg2
from psycopg2 import sql

class MovieDatabase:
    def __init__(self, dbname, user, password, host='localhost', port='5432'):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None
        self.cursor = None
        self.connect()
        
#----------------- DB CONTROL -----------------#
    def connect(self):
        """Ma'lumotlar bazasiga ulanishni amalga oshiradi."""
        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cursor = self.connection.cursor()
            print("Ma'lumotlar bazasiga muvaffaqiyatli ulanish")
        except Exception as e:
            print(f"Ulanishda xatolik: {e}")

    def disconnect(self):
        """Ma'lumotlar bazasidan uzilish."""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Ma'lumotlar bazasidan muvaffaqiyatli uzilish")
        
#----------------- USER CONTROL -----------------#
    def create_user_table(self):
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    user_id BIGINT UNIQUE NOT NULL,
                    first_name VARCHAR(255),
                    last_name VARCHAR(255),
                    banned BOOLEAN DEFAULT FALSE
                )
            """)
            self.connection.commit()
            print("Foydalanuvchilar jadvali muvaffaqiyatli yaratildi")
        except Exception as e:
            print(f"Jadval yaratishda xatolik: {e}")
            self.connection.rollback()

    def add_user(self, user_id, first_name, last_name, banned=False):
        try:
            self.cursor.execute("""
                INSERT INTO users (user_id, first_name, last_name, banned)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (user_id) DO UPDATE SET
                    first_name = EXCLUDED.first_name,
                    last_name = EXCLUDED.last_name,
                    banned = EXCLUDED.banned
            """, (user_id, first_name, last_name, banned))
            self.connection.commit()
            print("Foydalanuvchi muvaffaqiyatli qo'shildi yoki yangilandi")
        except Exception as e:
            print(f"Foydalanuvchi qo'shishda xatolik: {e}")
            self.connection.rollback()
    def get_user(self, user_id):
        """Foydalanuvchi ma'lumotlarini olish."""
        try:
            self.cursor.execute("""
                SELECT * FROM users WHERE user_id = %s
            """, (user_id,))
            user = self.cursor.fetchone()
            return user
        except Exception as e:
            print(f"Foydalanuvchi ma'lumotlarini olishda xatolik: {e}")
            return None
            
#----------------- MOVIE CONTROL -----------------#
    def add_movie(self, title, code, description):
        """Yangi kino qo'shadi."""
        try:
            self.cursor.execute("""
                INSERT INTO movies (title, code, description)
                VALUES (%s, %s, %s)
            """, (title, code, description))
            self.connection.commit()
            print("Kino muvaffaqiyatli qo'shildi")
        except Exception as e:
            print(f"Kino qo'shishda xatolik: {e}")
            self.connection.rollback()

    def remove_movie(self, code):
        """Kino kodiga asoslanib kinosni o'chiradi."""
        try:
            self.cursor.execute("""
                DELETE FROM movies
                WHERE code = %s
            """, (code,))
            self.connection.commit()
            print("Kino muvaffaqiyatli o'chirildi")
        except Exception as e:
            print(f"Kino o'chirishda xatolik: {e}")
            self.connection.rollback()

    def fetch_all_movies(self):
        """Barcha kinolarni olish."""
        try:
            self.cursor.execute("SELECT * FROM movies;")
            rows = self.cursor.fetchall()
            return rows
        except Exception as e:
            print(f"Kinolarni olishda xatolik: {e}")
            return []

    def create_table(self):
        """Jadval yaratadi."""
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS movies (
                    id SERIAL PRIMARY KEY,
                    title VARCHAR(255) NOT NULL,
                    code VARCHAR(50) UNIQUE NOT NULL,
                    description TEXT
                )
            """)
            self.connection.commit()
            print("Jadval muvaffaqiyatli yaratildi")
        except Exception as e:
            print(f"Jadval yaratishda xatolik: {e}")
            self.connection.rollback()

db = MovieDatabase(dbname="kinobase", user="postgres", password="kinobase")