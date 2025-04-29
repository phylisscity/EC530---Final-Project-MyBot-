// Sidebar.jsx - Hidden slide-in menu for controls
import React from 'react';


function Sidebar({ isOpen, onClose }) {
  return (

    <div className={`fixed top-0 left-0 h-full w-65 bg-white/80 shadow-2xl p-6 z-50 transform ${isOpen ? "translate-x-0" : "-translate-x-full"} transition-transform duration-300 ease-in-out rounded-tr-3xl rounded-br-3xl`}>
      
      {/* Close button */}
      <button onClick={onClose} className="text-2xl mb-8 hover:text-red-500 transition">
        ❌
      </button>


      {/* Menu Items */}
      <ul className="space-y-8 text-green-800 font-semibold text-lg">
        <li className="hover:text-purple-500 cursor-pointer">➕ Add Bot</li>
        <li className="hover:text-purple-500 cursor-pointer">🎯 Move Bots</li>
        <li className="hover:text-purple-500 cursor-pointer">⚙️ Settings</li>
      </ul>

    </div>
  );
}

export default Sidebar;
