import React, { useEffect, useState } from 'react';
import axios from 'axios';

function ProductList() {
  const [productos, setProductos] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/productos')
      .then(response => setProductos(response.data))
      .catch(error => console.error('Error al obtener productos:', error));
  }, []);

  return (
    <div>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>ID</th>
            <th>Nombre</th>
            <th>Cantidad</th>
            <th>Precio</th>
          </tr>
        </thead>
        <tbody>
          {productos.map((producto) => (
            <tr key={producto.id}>
              <td>{producto.id}</td>
              <td>{producto.nombre}</td>
              <td>{producto.cantidad}</td>
              <td>${producto.precio}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default ProductList;
