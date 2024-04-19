import React from 'react';
import './tailwind.css'; // Importujeme Tailwind CSS

function HelloWorld() {
  return (
    <div className="bg-blue-500 p-4 rounded-lg">
      <h1 className="text-white text-3xl font-bold">Hello, World!</h1>
    </div>
  );
}

function App() {
  return (
    <div>
      <h1 className="text-4xl font-bold">My React App</h1>
      <HelloWorld />
    </div>
  );
}

export default App;
