
// A simple BotCard component to display each bot's information
import React from 'react';


function BotCard({ botName, energy, balance, emoji }) {

  return (
    <div className="bg-white/60 backdrop-blur-lg rounded-xl shadow-md p-4 m-2 flex flex-col items-center w-40">
      {/* Bot emoji */}
      <div className="text-5xl mb-2">
        {emoji}
      </div>

      {/* Bot's name */}
      <h2 className="text-lg font-bold mb-1">{botName}</h2>

      {/* Bot's energy and balance */}
      <p className="text-sm">⚡ {energy} | 💰 {balance}</p>

      {/* Move button (we will add functionality later) */}
      <button className="mt-3 bg-green-400 hover:bg-green-500 text-white font-bold py-1 px-3 rounded">
        Move
      </button>
    </div>
  );
  
}

export default BotCard;
