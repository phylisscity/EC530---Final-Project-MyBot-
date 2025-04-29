//Main application layout for MyBot World 🌱🤖
import React from 'react';
import Grid from './components/Grid'; // Grid layout
import Bot from './components/Bot';   // Bot component


function App() {
  // List of bots (fake data for now - will connect to backend later)

  const bots = [
    { botName: 'Bot #1', energy: 8, balance: 12, emoji: '🤖' },
    { botName: 'Bot #2', energy: 5, balance: 7, emoji: '🛸' },
    { botName: 'Bot #3', energy: 10, balance: 15, emoji: '🐝' },
  ];

  return (
    <div className="min-h-screen p-8 flex flex-col items-center">
      
      {/* Main title */}
      <h1 className="text-4xl font-bold text-gray-800 mb-10">
        MyBot World 🌱🤖
      </h1>

      {/* World grid (background cells) */}
      <Grid />


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

    </div>
  );
}

export default App;
