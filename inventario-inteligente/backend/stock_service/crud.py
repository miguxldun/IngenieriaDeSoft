from sqlalchemy.orm import Session
from models import Producto

def get_productos(db: Session):
    return db.query(Producto).all()

def get_producto(db: Session, producto_id: int):
    return db.query(Producto).filter(Producto.id == producto_id).first()

def create_producto(db: Session, producto_data):
    nuevo = Producto(**producto_data.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def update_producto(db: Session, producto_id: int, data):
    producto = get_producto(db, producto_id)
    if producto:
        producto.nombre = data.nombre
        producto.cantidad = data.cantidad
        producto.precio = data.precio
        db.commit()
        db.refresh(producto)
        return producto
    return None

def delete_producto(db: Session, producto_id: int):
    producto = get_producto(db, producto_id)
    if producto:
        db.delete(producto)
        db.commit()
        return True
    return False
