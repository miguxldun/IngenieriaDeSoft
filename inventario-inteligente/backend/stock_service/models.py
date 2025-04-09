from sqlalchemy import Column, Integer, String, DECIMAL
from database import Base

class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)
    cantidad = Column(Integer, nullable=False)
    precio = Column(DECIMAL(10, 2), nullable=False, default=0.00)
