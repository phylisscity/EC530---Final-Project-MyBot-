// Main application layout for MyBot World
import React, { useState } from 'react'; // updated. Need useState for sidebar control
import Grid from './components/Grid'; // Grid layout
import Bot from './components/Bot';   // Bot component
import Sidebar from './components/Sidebar';  // Sidebar for menu
import BotControlPanel from './components/ControlPanel'; // Floating action panel


function App() {

  // Menu open/close control
  const [isMenuOpen, setIsMenuOpen] = useState(false);


  // List of bots (fake data for now - will connect to backend later)
  const bots = [
    { botName: 'Bot #1', energy: 8, balance: 12, emoji: '🤖' },
    { botName: 'Bot #2', energy: 5, balance: 7, emoji: '🛸' },
    { botName: 'Bot #3', energy: 10, balance: 15, emoji: '🐝' },
  ];

  return (
    <div className="min-h-screen p-8 flex flex-col items-center">

            
      {/* ===== Top Navbar ===== */}
      <div className="w-full relative bg-white/70 backdrop-blur-md rounded-3xl p-4 shadow-md mb-8 animate-fade-in-bounce flex items-center justify-between">

        {/* Hamburger - Left Side */}
        {!isMenuOpen && (
          <button 
            onClick={() => setIsMenuOpen(true)} 
            className="text-4xl z-50 bg-white/70 p-3 rounded-full shadow-md hover:bg-white transition hover:scale-110 active:scale-90 duration-200 ease-in-out"
          >
            ☰
          </button>
        )}

        {/* Center Title - Always Centered */}
        <div className="absolute left-1/2 transform -translate-x-1/2">
          <h1 className="text-3xl font-bold text-gray-800">
            MyBot World 🌱🤖
          </h1>
        </div>

        {/* Right-side Stats */}
        <div className="flex items-center space-x-6 ml-auto">

          {/* Bot Count */}
          <div className="flex flex-col items-center hover:scale-110 transition">
            <span className="text-lg font-semibold">Bots</span>
            <span className="text-xl font-bold">3</span> {/* Replace later */}
          </div>

          {/* Coin Count */}
          <div className="flex flex-col items-center hover:scale-110 transition">
            <span className="text-lg font-semibold">Coins</span>
            <span className="text-xl font-bold">15</span> {/* Replace later */}
          </div>

          {/* Mood */}
          <div className="flex flex-col items-center hover:scale-110 transition">
            <span className="text-lg font-semibold">Mood</span>
            <span className="text-xl">🌤️</span> {/* Replace with mood state */}
          </div>

        </div>
      </div>
      {/* ===== End Top Navbar ===== */}




      {/* ===== Sidebar Slide-in Menu ===== */}
      <Sidebar isOpen={isMenuOpen} onClose={() => setIsMenuOpen(false)} />
      {/* ===== End Sidebar ===== */}


  
      {/* ===== World Grid ===== */}
      <div className="relative bracket-frame p-[10px] bg-gradient-to-br from-pink-200 via-purple-400 to-yellow-500 border-[12px] border-yellow-400 rounded-[36px] shadow-[0_8px_30px_rgba(0,0,0,0.2)] mt-6">

        {/* Inner Grid Area */}
        <div className="bg-gradient-to-br from-[#edefec] to-[#f7f1d4] rounded-[30px] p-5 shadow-inner backdrop-blur-sm">
          <Grid />
        </div>

      </div>
      {/* ===== End World Grid ===== */}




      {/* ===== Bots Floating Below ===== */}
      <div className="flex flex-wrap justify-center gap-6 mt-12">
        {bots.map((bot, index) => (
          <Bot
            key={index}
            botName={bot.botName}
            emoji={bot.emoji}
            energy={bot.energy}
            balance={bot.balance}
          />
        ))}
      </div>
      {/* ===== End Bots Floating ===== */}




      {/* ===== Floating Bot Control Panel ===== */}
      <BotControlPanel 
        onCreateBot={() => console.log("Create Bot Clicked!")}
        onMoveRandom={() => console.log("Move Random Clicked!")}
        onRecharge={() => console.log("Recharge Clicked!")}
        onMessage={() => console.log("Message Clicked!")}
      />
      {/* ===== End Control Panel ===== */}








    </div>
  );
}

export default App;
