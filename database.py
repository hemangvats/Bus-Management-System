import mysql.connector
from tkinter import messagebox

class DatabaseHandler:
    def __init__(self, host="localhost", user="root", password="Home@1234", database="vbb_bus_booking"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.conn.cursor(buffered=True)
            return True
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
            return False

    def close(self):
        if self.conn:
            self.conn.close()

    def execute_query(self, query, params=None):
        try:
            if not self.conn or not self.conn.is_connected():
                self.connect()
            self.cursor.execute(query, params or ())
            self.conn.commit()
            return True
        except mysql.connector.Error as err:
            messagebox.showerror("Query Error", f"Error: {err}")
            return False

    def fetch_all(self, query, params=None):
        try:
            if not self.conn or not self.conn.is_connected():
                self.connect()
            self.cursor.execute(query, params or ())
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            messagebox.showerror("Fetch Error", f"Error: {err}")
            return []

    def fetch_one(self, query, params=None):
        try:
            if not self.conn or not self.conn.is_connected():
                self.connect()
            self.cursor.execute(query, params or ())
            return self.cursor.fetchone()
        except mysql.connector.Error as err:
            messagebox.showerror("Fetch Error", f"Error: {err}")
            return None

# Initial Setup Script
def setup_database(host="localhost", user="root", password="Home@1234"):
    try:
        conn = mysql.connector.connect(host=host, user=user, password=password)
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS vbb_bus_booking")
        cursor.execute("USE vbb_bus_booking")

        # Create Tables
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                firstname VARCHAR(100),
                lastname VARCHAR(100),
                email VARCHAR(100),
                username VARCHAR(100) UNIQUE,
                password VARCHAR(100)
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS locations (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) UNIQUE,
                price INT
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS bus_types (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) UNIQUE,
                price INT
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS bookings (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(100),
                location VARCHAR(100),
                bus_type VARCHAR(100),
                num_passengers INT,
                total_fare INT,
                booking_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        conn.commit()
        conn.close()
        return True
    except mysql.connector.Error as err:
        print(f"Setup Error: {err}")
        return False
