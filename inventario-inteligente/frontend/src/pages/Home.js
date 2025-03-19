import React from 'react';
import ProductList from '../components/ProductList';
import ProductForm from '../components/ProductForm';

function Home() {
  return (
    <div>
      <h2>Gestión de Inventario</h2>
      <ProductForm />
      <ProductList />
    </div>
  );
}

export default Home;
