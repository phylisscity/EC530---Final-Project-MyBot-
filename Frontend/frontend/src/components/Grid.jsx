
//Displays the main world grid where bots will live
import React from 'react';

function Grid() {

  // Set the grid size
  const rows = 10;
  const cols = 10;


  // Build an array representing each cell
  const cells = [];
  for (let row = 0; row < rows; row++) {
    for (let col = 0; col < cols; col++) {

      cells.push(

        <div
          key={`${row}-${col}`} // Unique key for each cell
          className="border border-blue-800 bg-white/20 w-16 h-16 flex items-center justify-center"
          >
          {/* Empty for now — bots will be placed here later */}
        </div>
      );
    }
  }

  return (
    // Grid container with 10 columns
    <div className="grid grid-cols-10 gap-1">
      {cells}
    </div>
  );
}

export default Grid;
