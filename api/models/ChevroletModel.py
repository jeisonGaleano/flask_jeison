from api.database.db import get_connection
from .entities.Chevrolet import Chevrolet
from .entities.Login import Login


class ChevroletModel():
    
    @classmethod
    def login_chevrolet(self, user, contrasena):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT usuario, contrasena, tipo_usuario FROM login WHERE usuario = %s and contrasena = %s ", (user, contrasena,))
                row = cursor.fetchone()

                userget = None
                if row != None:
                    userget = Login(row[0], row[1], row[2])
                    userget = userget.to_JSON()

            connection.close()
            return userget
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def create_user(self, login):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""
                               INSERT INTO public.login
                                (usuario, contrasena, tipo_usuario)
                                VALUES(%s, %s, %s)""", (login.usuario, login.contrasena, login.tipo_usuario))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)