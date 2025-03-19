from flask import Blueprint, request, jsonify
from models import ProductoModel
from extensions import mysql  # Importamos MySQL desde extensions.py

productos_bp = Blueprint('productos', __name__)
producto_model = ProductoModel(mysql)  # Pasamos la instancia de MySQL

@productos_bp.route('/productos', methods=['GET'])
def obtener_productos():
    productos = producto_model.obtener_todos()
    return jsonify(productos)

@productos_bp.route('/productos', methods=['POST'])
def agregar_producto():
    datos = request.json
    print("📌 Datos recibidos en /productos [POST]:", datos)  # Debug

    nombre = datos.get('nombre')
    cantidad = int(datos.get('cantidad', 0))  # Convertir a número entero
    precio = float(datos.get('precio', 0))    # Convertir a decimal

    print(f"🛠️ Insertando: Nombre={nombre}, Cantidad={cantidad}, Precio={precio}")  # Debug

    producto_model.agregar(nombre, cantidad, precio)
    return jsonify({'mensaje': 'Producto agregado'}), 201

@productos_bp.route('/productos/<int:id>', methods=['PUT'])
def actualizar_producto(id):
    datos = request.json
    nombre = datos.get('nombre')
    cantidad = int(datos.get('cantidad', 0))
    precio = float(datos.get('precio', 0))

    producto_model.actualizar(id, nombre, cantidad, precio)
    return jsonify({'mensaje': 'Producto actualizado'})

@productos_bp.route('/productos/<int:id>', methods=['DELETE'])
def eliminar_producto(id):
    producto_model.eliminar(id)
    return jsonify({'mensaje': 'Producto eliminado'})
