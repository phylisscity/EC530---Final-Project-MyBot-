// Represents a single bot with emoji and stats
import React from 'react';


function Bot({ botName, emoji, energy, balance }) {

  return (

    // Outer container with relative positioning for floating bubble
    <div className="relative flex flex-col items-center m-4">


      {/* Floating stat bubble above bot */}
      <div className="absolute -top-8 bg-white/70 text-green-900 rounded-full px-4 py-2 text-sm shadow-lg whitespace-nowrap">
       
        {/* Show energy and balance side by side */}
        ⚡ {energy} | 💰 {balance}
      </div>

      {/* Bot emoji (big and centered) */}
      <div className="text-7xl mb-2">
        {emoji}
      </div>

      {/* Bot name below emoji */}
      <h2 className="text-base font-semibold text-gray-800 mt-1">
        {botName}
      </h2>

    </div>
  );
}

export default Bot;
