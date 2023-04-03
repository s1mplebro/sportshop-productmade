from data import *
from cart import *
from products import *

def init_controllers(connection, db_cursor):
    userController = UserController(connection, db_cursor)
    productController = ProductController(connection, db_cursor)
    cartController = CartController(connection, db_cursor)

    return userController, productController, cartController
