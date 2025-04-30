
//Displays the main world grid where bots will live
import React from 'react';

function Grid() {

  // Set the grid size
  const rows = 10;
  const cols = 10;


  
  // Sample bot positions (you can update later)
  const bots = [
    { position: { x: 2, y: 3 }, emoji: '🤖' },
    { position: { x: 5, y: 7 }, emoji: '🐝' }
  ];


  // Build an array representing each cell
  const cells = [];
  for (let row = 0; row < rows; row++) {
    for (let col = 0; col < cols; col++) {


      // Check if a bot is here
      const botHere = bots.find(
        (bot) => bot.position.x === col && bot.position.y === row
      );

      cells.push(

        <div
        key={`${row}-${col}`}
        className="border border-blue-400 bg-white/20 w-16 h-16 flex items-center justify-center rounded-md 
                    hover:shadow-lg hover:scale-110 transition-all duration-200 ease-in-out"
        >
        {/* Bot will be inserted here later */}
          {botHere ? botHere.emoji : ''}
        </div>

      );
    }
  }


  return (
    <div className="grid-container">
      {/*  actual grid */}
      <div className="grid grid-cols-10 gap-1">{cells}</div>

      {/* Mini map overlay */}
      <MiniMap bots={bots} />
    </div>
  );
}





// MiniMap is a small floating grid that shows bot positions in real-time
function MiniMap({ bots, gridSize = 12 }) {
  const map = [];

  for (let row = 0; row < gridSize; row++) {
    const rowElements = [];

    for (let col = 0; col < gridSize; col++) {
      
      // Check if any bot is at this (col, row) coordinate
      const botHere = bots.find(
        (bot) => bot.position.x === col && bot.position.y === row
      );

      
      // Add a mini cell with either the bot emoji or blank
      rowElements.push(
        <div className="mini-cell" key={`${row}-${col}`}>
          {botHere ? botHere.emoji || '🤖' : ''}
        </div>
      );
    }

    // After filling a row, add it to the overall grid
    map.push(
      <div className="mini-row" key={`row-${row}`}>
        {rowElements}
      </div>
    );
  }

  return (
    <div className="mini-map-container">
      <p className="mini-title">Mini Map</p>
      <div className="mini-grid">{map}</div>
    </div>
  );
}

export default Grid;