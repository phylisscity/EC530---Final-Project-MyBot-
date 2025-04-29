//Main application layout for MyBot World 🌱🤖
import React, { useState } from 'react'; // updated. Need useState for sidebar control
import Grid from './components/Grid'; // Grid layout
import Bot from './components/Bot';   // Bot component
import Sidebar from './components/Sidebar';  //sidebar for menu
import BotControlPanel from './components/ControlPanel'; // ✅ Floating action panel


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

      {/* Hamburger Menu Button */}
      {!isMenuOpen && (
      <button 
        onClick={() => setIsMenuOpen(true)} 
        className="fixed top-6 left-6 text-4xl z-50 bg-white/70 p-3 rounded-full shadow-md hover:bg-white transition hover:scale-110 active:scale-90 duration-200 ease-in-out"
        >
        ☰
      </button>
    )}



      {/* Sidebar component (slide-in menu) */}
      <Sidebar isOpen={isMenuOpen} onClose={() => setIsMenuOpen(false)} />


      {/* Main title */}
      <h1 className="text-4xl font-bold text-gray-800 mb-10">
        MyBot World 🌱🤖
      </h1>


      {/* World grid (background cells) */}
      {/* Custom golden grid frame with corner brackets */}
      <div className="relative bracket-frame p-[10px] bg-gradient-to-br from-pink-200 via-purple-400 to-yellow-500 border-[12px] border-yellow-400 rounded-[36px] shadow-[0_8px_30px_rgba(0,0,0,0.2)] mt-6">


        {/* Inner grid area with soft background and blur */}
        <div className="bg-gradient-to-br from-[#edefec] to-[#f7f1d4] rounded-[30px] p-5 shadow-inner backdrop-blur-sm">
          <Grid />
        </div>

      </div>



      {/* Bots (floating below for now - will move inside the grid later) */}
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




      {/* Floating Control Panel for Bot Actions */}
      <BotControlPanel 
        onCreateBot={() => console.log("Create Bot Clicked!")}
        onMoveRandom={() => console.log("Move Random Clicked!")}
        onRecharge={() => console.log("Recharge Clicked!")}
        onMessage={() => console.log("Message Clicked!")}
      />






















    </div>
  );
}


export default App;
