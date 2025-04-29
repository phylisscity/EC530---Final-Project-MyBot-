//Main application layout for MyBot World
import React from 'react';
import Grid from './components/Grid';   
import Bot from './components/Bot';     


function App() {

  // Temporary list of bots (mock data for now)
  const bots = [
    { botName: 'Bot #1', energy: 8, balance: 12, emoji: '🤖' },
    { botName: 'Bot #2', energy: 5, balance: 7, emoji: '🛸' },
    { botName: 'Bot #3', energy: 10, balance: 15, emoji: '🐝' },
  ];

  return (
    <div className="min-h-screen p-8 flex flex-col items-center">
      
      {/* Main heading */}
      <h1 className="text-4xl font-bold text-gray-800 mb-10">
        MyBot World 🌱🤖
      </h1>

      {/* World grid */}
      <Grid />

      {/* Bots shown below for now (later will move them INTO the grid) */}
      <div className="flex flex-wrap justify-center gap-4 mt-10">
        {bots.map((bot, index) => (
          <Bot
            key={index}
            botName={bot.botName}
            energy={bot.energy}
            balance={bot.balance}
            emoji={bot.emoji}
          />
        ))}
      </div>

    </div>
  );
}

export default App;
