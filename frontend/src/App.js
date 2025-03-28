import React, { useState } from "react";
import axios from "axios";

function App() {
  const [joke, setJoke] = useState(null);
  const [loading, setLoading] = useState(false);
  const API_URL = "http://localhost:8000/api/v1/joke"; // Altere conforme necessário

  const fetchJoke = async () => {
    setLoading(true);
    try {
      const response = await axios.get(API_URL);
      setJoke(response.data);
    } catch (error) {
      console.error("Erro ao buscar piada:", error);
      setJoke({ error: "Falha ao obter piada. Tente novamente!" });
    }
    setLoading(false);
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100 p-4">
      <h1 className="text-3xl font-bold text-gray-800 mb-4">😂 Gerador de Piadas</h1>
      <p className="text-gray-600 mb-4">Consumindo API FastAPI em /api/v1/joke</p>

      <button
        onClick={fetchJoke}
        className="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded-lg transition duration-200"
        disabled={loading}
      >
        {loading ? "Carregando..." : "Me conte uma piada! 😆"}
      </button>

      {joke && (
        <div className="mt-6 p-4 bg-white shadow-lg rounded-lg w-full max-w-lg">
          {joke.setup ? (
            <>
              <p className="text-lg font-semibold text-gray-700">{joke.setup}</p>
              <p className="text-gray-600 mt-2">{joke.delivery}</p>
            </>
          ) : (
            <p className="text-lg text-gray-700">{joke.joke}</p>
          )}
          <p className="text-sm text-gray-500 mt-2">Categoria: {joke.category}</p>
        </div>
      )}

      <footer className="mt-10 text-sm text-gray-500">
        © {new Date().getFullYear()} • Feito por Denilson, Edson, Jonathan, Hugo e Vilton.
      </footer>
    </div>
  );
}

export default App;
