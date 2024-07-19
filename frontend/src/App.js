import React, { useState } from "react";
import axios from "axios";
import ItemList from "./components/ItemList";
import ItemForm from "./components/ItemForm"; // Corrected import

const App = () => {
  const [currentItem, setCurrentItem] = useState(null);
  const [refresh, setRefresh] = useState(false);
  const [error, setError] = useState(null); // State to manage error messages

  const handleEdit = (item) => {
    setCurrentItem(item);
  };

  const handleDelete = async (id) => {
    try {
      await axios.delete(`http://localhost:8000/api/items/${id}/`);
      setRefresh(!refresh);
    } catch (error) {
      console.error('Error deleting item:', error);
      setError('There was an error deleting the item.');
    }
  };

  const handleSuccess = () => {
    setCurrentItem(null);
    setRefresh(!refresh);
  };

  return (
    <div className="App">
      <ItemForm item={currentItem} onSuccess={handleSuccess} />
      <ItemList key={refresh ? 'refreshed' : 'initial'} onEdit={handleEdit} onDelete={handleDelete} />
      {error && <p>Error: {error}</p>} {/* Display error message if error state is set */}
    </div>
  );
};

export default App;
