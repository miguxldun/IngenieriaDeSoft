import React, { useState } from 'react';
import axios from 'axios';

function ProductForm() {
  const [nombre, setNombre] = useState('');
  const [cantidad, setCantidad] = useState('');
  const [precio, setPrecio] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();

    const datos = {
      nombre,
      cantidad: parseInt(cantidad, 10),  // Convertir a número entero
      precio: parseFloat(precio)         // Convertir a decimal
    };

    console.log("📌 Datos enviados desde React:", datos);  // 👀 Debug

    axios.post('http://127.0.0.1:5000/productos', datos)
      .then(() => {
        setNombre('');
        setCantidad('');
        setPrecio('');
        window.location.reload();  
      })
      .catch(error => console.error('❌ Error al agregar producto:', error));
  };

  return (
    <form onSubmit={handleSubmit} className="mb-3">
      <div className="form-group">
        <label>Nombre</label>
        <input type="text" className="form-control" value={nombre} onChange={e => setNombre(e.target.value)} required />
      </div>
      <div className="form-group">
        <label>Cantidad</label>
        <input type="number" className="form-control" value={cantidad} onChange={e => setCantidad(e.target.value)} required />
      </div>
      <div className="form-group">
        <label>Precio</label>
        <input type="number" step="0.01" className="form-control" value={precio} onChange={e => setPrecio(e.target.value)} required />
      </div>
      <button type="submit" className="btn btn-primary mt-2">Agregar Producto</button>
    </form>
  );
}

export default ProductForm;
