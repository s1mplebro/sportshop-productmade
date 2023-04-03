import sqlite3 

class  CartController:
	def __init__(self, connection, db_cursor):
		self.connection = connection
		self.cursor = db_cursor

	def create_base_cart(self):
		self.cursor.execute("""CREATE TABLE IF NOT EXISTS cart(
			user_id integer,
			product_id integer
			)""")

	def add_cart(self,user_id,product_id):
		self.cursor.execute("""INSERT INTO cart (user_id, product_id) VALUES(?,?)""",[user_id,product_id])
		return self.connection.commit()

	def get_cart(self,idi):
		self.cursor.execute(f"SELECT * FROM cart WHERE user_id = {idi}")
		data =  self.cursor.fetchall()
		return data

	def del_final(self,idi):
		self.cursor.execute(f"DELETE FROM cart WHERE user_id={idi}")
		return  self.connection.commit()
		