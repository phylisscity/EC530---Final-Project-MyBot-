// Main App component to display all bots
import React from 'react';
import BotCard from './components/BotCard';

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
      <h1 className="text-7xl font-bold text-gray-800 mb-10">
        MyBot World 🌱🤖
      </h1>

      {/* Bots grid */}
      <div className="flex flex-wrap justify-center gap-4">
        {bots.map((bot, index) => (
          
          <BotCard
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
