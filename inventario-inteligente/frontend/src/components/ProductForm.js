import React, { useState } from 'react';
import axios from 'axios';

function ProductForm({ onProductAdded }) {
  const [nombre, setNombre] = useState('');
  const [cantidad, setCantidad] = useState('');
  const [precio, setPrecio] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    setIsSubmitting(true);
    setError(null);
    setSuccess(false);

    const datos = {
      nombre,
      cantidad: parseInt(cantidad, 10),
      precio: parseFloat(precio)
    };

    axios.post('http://127.0.0.1:5000/productos', datos)
      .then(() => {
        setNombre('');
        setCantidad('');
        setPrecio('');
        setSuccess(true);
        if (onProductAdded) onProductAdded();
      })
      .catch(error => {
        console.error('Error al agregar producto:', error);
        setError('Error al agregar producto');
      })
      .finally(() => {
        setIsSubmitting(false);
      });
  };

  return (
    <form onSubmit={handleSubmit} className="mb-3">
      <div className="form-group">
        <label>Nombre</label>
        <input 
          type="text" 
          className="form-control" 
          value={nombre} 
          onChange={e => setNombre(e.target.value)} 
          required 
        />
      </div>
      <div className="form-group">
        <label>Cantidad</label>
        <input 
          type="number" 
          className="form-control" 
          value={cantidad} 
          onChange={e => setCantidad(e.target.value)} 
          required 
          min="0"
        />
      </div>
      <div className="form-group">
        <label>Precio</label>
        <input 
          type="number" 
          step="0.01" 
          className="form-control" 
          value={precio} 
          onChange={e => setPrecio(e.target.value)} 
          required 
          min="0"
        />
      </div>
      <button 
        type="submit" 
        className="btn btn-primary mt-2"
        disabled={isSubmitting}
      >
        {isSubmitting ? 'Agregando...' : 'Agregar Producto'}
      </button>
      
      {error && <div className="alert alert-danger mt-2">{error}</div>}
      {success && <div className="alert alert-success mt-2">Producto agregado correctamente!</div>}
    </form>
  );
}

export default ProductForm;