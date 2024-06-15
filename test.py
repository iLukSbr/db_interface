import tkinter as tk
from tkinter import messagebox
import pymysql
import psycopg2

class DatabaseGUI:
    def __init__(self, root):
        self.root = root
        self.root.title('Database GUI')
        
        # MySQL Connection
        tk.Label(root, text='MySQL').grid(row=0, column=0)
        tk.Label(root, text='Host:').grid(row=1, column=0)
        self.mysql_host = tk.Entry(root)
        self.mysql_host.grid(row=1, column=1)
        
        tk.Label(root, text='User:').grid(row=2, column=0)
        self.mysql_user = tk.Entry(root)
        self.mysql_user.grid(row=2, column=1)
        
        tk.Label(root, text='Password:').grid(row=3, column=0)
        self.mysql_password = tk.Entry(root, show='*')
        self.mysql_password.grid(row=3, column=1)
        
        tk.Label(root, text='Database:').grid(row=4, column=0)
        self.mysql_db = tk.Entry(root)
        self.mysql_db.grid(row=4, column=1)
        
        tk.Button(root, text='Connect to MySQL', command=self.connect_mysql).grid(row=5, column=0, columnspan=2)
        
        # PostgreSQL Connection
        tk.Label(root, text='PostgreSQL').grid(row=6, column=0)
        tk.Label(root, text='Host:').grid(row=7, column=0)
        self.postgresql_host = tk.Entry(root)
        self.postgresql_host.grid(row=7, column=1)
        
        tk.Label(root, text='User:').grid(row=8, column=0)
        self.postgresql_user = tk.Entry(root)
        self.postgresql_user.grid(row=8, column=1)
        
        tk.Label(root, text='Password:').grid(row=9, column=0)
        self.postgresql_password = tk.Entry(root, show='*')
        self.postgresql_password.grid(row=9, column=1)
        
        tk.Label(root, text='Database:').grid(row=10, column=0)
        self.postgresql_db = tk.Entry(root)
        self.postgresql_db.grid(row=10, column=1)
        
        tk.Button(root, text='Connect to PostgreSQL', command=self.connect_postgresql).grid(row=11, column=0, columnspan=2)
    
    def connect_mysql(self):
        try:
            pymysql.connect(
                host=self.mysql_host.get(),
                user=self.mysql_user.get(),
                password=self.mysql_password.get(),
                db=self.mysql_db.get()
            )
            messagebox.showinfo('Success', 'Connected to MySQL database successfully!')
        except Exception as e:
            messagebox.showerror('Error', str(e))
    
    def connect_postgresql(self):
        try:
            psycopg2.connect(
                host=self.postgresql_host.get(),
                user=self.postgresql_user.get(),
                password=self.postgresql_password.get(),
                dbname=self.postgresql_db.get()
            )
            messagebox.showinfo('Success', 'Connected to PostgreSQL database successfully!')
        except Exception as e:
            messagebox.showerror('Error', str(e))

if __name__ == '__main__':
    root = tk.Tk()
    gui = DatabaseGUI(root)
    root.mainloop()
