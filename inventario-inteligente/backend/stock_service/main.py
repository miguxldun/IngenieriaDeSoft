from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List
from sqlalchemy.orm import Session

from database import SessionLocal
import crud
from models import Producto

app = FastAPI()

# Schemas con Pydantic
class ProductoSchema(BaseModel):
    nombre: str
    cantidad: int
    precio: float

    class Config:
        orm_mode = True

class ProductoSchemaOut(ProductoSchema):
    id: int

# Dependencia para la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoints

@app.get("/productos", response_model=List[ProductoSchemaOut])
def listar_productos(db: Session = Depends(get_db)):
    return crud.get_items(db)

@app.get("/productos/{producto_id}", response_model=ProductoSchemaOut)
def obtener_producto(producto_id: int, db: Session = Depends(get_db)):
    producto = crud.get_item(db, producto_id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@app.post("/productos", response_model=ProductoSchemaOut)
def crear_producto(producto: ProductoSchema, db: Session = Depends(get_db)):
    return crud.add_item(db, producto)

@app.put("/productos/{producto_id}", response_model=ProductoSchemaOut)
def actualizar_producto(producto_id: int, producto: ProductoSchema, db: Session = Depends(get_db)):
    actualizado = crud.update_item(db, producto_id, producto)
    if not actualizado:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return actualizado

@app.delete("/productos/{producto_id}")
def eliminar_producto(producto_id: int, db: Session = Depends(get_db)):
    eliminado = crud.delete_item(db, producto_id)
    if eliminado:
        return {"mensaje": "Producto eliminado"}
    raise HTTPException(status_code=404, detail="Producto no encontrado")
