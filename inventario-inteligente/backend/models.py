class ProductoModel:
    def __init__(self, mysql):
        self.mysql = mysql

    def obtener_todos(self):
        conn = self.mysql.connection
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        cursor.close()
        return productos

    def agregar(self, nombre, cantidad, precio):
        conn = self.mysql.connection
        cursor = conn.cursor()

        sql = "INSERT INTO productos (nombre, cantidad, precio) VALUES (%s, %s, %s)"
        valores = (nombre, cantidad, precio)

        cursor.execute(sql, valores)
        conn.commit()

        cursor.close()

    def actualizar(self, id, nombre, cantidad, precio):
        conn = self.mysql.connection
        cursor = conn.cursor()

        sql = "UPDATE productos SET nombre=%s, cantidad=%s, precio=%s WHERE id=%s"
        valores = (nombre, cantidad, precio, id)

        cursor.execute(sql, valores)
        conn.commit()
        cursor.close()

    def eliminar(self, id):
        conn = self.mysql.connection
        cursor = conn.cursor()

        sql = "DELETE FROM productos WHERE id=%s"
        cursor.execute(sql, (id,))
        conn.commit()
        cursor.close()
