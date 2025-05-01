
import React, { useEffect, useState } from 'react';


// ==========================================================
// 🌸 Floating Icons Section (Ambient Emoji Background)
// ==========================================================

//ambient emojis
const emojis = ['✨', '🌿', '☁️', '🌸'];



// Example dummy log (temporary; will replace with real bot selection & data)
const dummyLog = [
  "Moved right to (4,2).",
  "Recharged at station.",
  "Captured shared goal at (7,5)! +5 coins",
  "Message sent to Bot #3.",
  "Moved down to (3,2)."
];


// Main BotUIHub component
function BotUIHub({ 
  isOpen, 
  onClose, 
  onCreateBot, 
  onMoveRandom, 
  onRecharge, 
  onMessage 
}) {

  // State: all floating icons on screen
  const [icons, setIcons] = useState([]);



  //modal open state + selected log
  const [showLogModal, setShowLogModal] = useState(false);
  const [logEntries, setLogEntries] = useState(dummyLog); // replace with bot.log later





  // Toast notifications
  const [toasts, setToasts] = useState([]);

  // Add a new toast to the stack
  const addToast = (message) => {
    const id = Math.random().toString(36).substring(2, 9);
    const newToast = { id, message };
    setToasts((prev) => [...prev, newToast]);

    // Auto-remove after 6 seconds
    setTimeout(() => {
      setToasts((prev) => prev.filter((t) => t.id !== id));
    }, 6000);
  };





  useEffect(() => {
    // Add a new floating icon every 1 second
    const interval = setInterval(() => {
      const id = Math.random().toString(36).substring(2, 9);  // Random ID
      const left = Math.floor(Math.random() * 100);           // Random horizontal position
      const emoji = emojis[Math.floor(Math.random() * emojis.length)];

      // Add the emoji to the screen
      setIcons(prev => [...prev, { id, left, emoji }]);

      // Remove it after 10 seconds
      setTimeout(() => {
        setIcons(prev => prev.filter(icon => icon.id !== id));
      }, 10000);
    }, 1000); // 1 icon per second

    return () => clearInterval(interval); // Cleanup
  }, []);






  return (
    <>
      {/* ==========================================================
          ✨ Floating Emoji Background
      ========================================================== */}
      <div className="pointer-events-none fixed top-0 left-0 w-full h-full z-0 overflow-hidden">
        {icons.map(({ id, left, emoji }) => (
          <div
            key={id}
            className="absolute text-4xl opacity-90 animate-drift"
            style={{ left: `${left}%` }}
          >
            {emoji}
          </div>
        ))}
      </div>





      {/* ==========================================================
          📋 Sidebar Panel (Left Side) — Help / Settings
      ========================================================== */}
      <div className={`
        fixed top-0 left-0 h-full w-72 bg-white/80 shadow-2xl p-6 z-50 transform
        ${isOpen ? "translate-x-0" : "-translate-x-full"}
        transition-transform duration-300 ease-in-out rounded-tr-3xl rounded-br-3xl
      `}>
        <button onClick={onClose} className="text-2xl mb-8 hover:text-red-500 transition">
          ❌
        </button>
        <ul className="space-y-8 text-green-800 font-semibold text-lg">
          <li className="hover:text-purple-500 cursor-pointer">📖 Help Guide</li>
          <li className="hover:text-purple-500 cursor-pointer">⚙️ Settings</li>
          <li className="hover:text-purple-500 cursor-pointer">📡 About</li>
        </ul>
      </div>







      {/* ==========================================================
          🕹️ Floating Control Panel (Right Side) — Bot Actions
      ========================================================== */}
      <div className="fixed bottom-[35%] right-10 bg-white/70 backdrop-blur-md p-6 rounded-3xl shadow-2xl flex flex-col space-y-6 z-50 animate-fade-in-bounce">


        {/* ➕ Create Bot */}
        <div className="relative group flex flex-col items-center">
          <button
            onClick={() => {
              onCreateBot();
              addToast("🤖 New bot created!");
            }}
            className="bg-green-300 hover:bg-green-400 p-6 rounded-full shadow-md transition-all duration-200 ease-in-out text-3xl hover:scale-110 active:scale-95"
          >
            ➕
          </button>
          <span className="absolute bottom-full mb-2 text-s bg-green-700 text-white px-4 py-1 min-w-[100px] text-center rounded-full opacity-0 group-hover:opacity-100 transition duration-200 transform group-hover:-translate-y-1 shadow-md">
            Create Bot
          </span>
        </div>


        {/* 🛸 Move Bot */}
        <div className="relative group flex flex-col items-center">
          <button
            onClick={() => {
              onMoveRandom();
              addToast("🛸 Bot moved randomly!");
            }}
            className="bg-blue-300 hover:bg-blue-400 p-6 rounded-full shadow-md transition-all duration-200 ease-in-out text-3xl hover:scale-110 active:scale-95"
          >
            🛸
          </button>
          <span className="absolute bottom-full mb-2 text-s bg-blue-700 text-white px-4 py-1 min-w-[100px] text-center rounded-full opacity-0 group-hover:opacity-100 transition duration-200 transform group-hover:-translate-y-1 shadow-md">
            Random Move
          </span>
        </div>


        {/* 🔋 Recharge */}
        <div className="relative group flex flex-col items-center">
          <button
            onClick={() => {
              onRecharge();
              addToast("🔋 Bot recharged!");
            }}
            className="bg-yellow-300 hover:bg-yellow-400 p-6 rounded-full shadow-md transition-all duration-200 ease-in-out text-3xl hover:scale-110 active:scale-95"
          >
            🔋
          </button>
          <span className="absolute bottom-full mb-2 text-s bg-yellow-600 text-black px-4 py-1 min-w-[100px] text-center rounded-full opacity-0 group-hover:opacity-100 transition duration-200 transform group-hover:-translate-y-1 shadow-md">
            Recharge
          </span>
        </div>


        {/* ✉️ Message Bot */}
        <div className="relative group flex flex-col items-center">
          <button
            onClick={() => {
              onMessage();
              addToast("✉️ Message sent!");
            }}
            className="bg-pink-300 hover:bg-pink-400 p-6 rounded-full shadow-md transition-all duration-200 ease-in-out text-3xl hover:scale-110 active:scale-95"
          >
            ✉️
          </button>
          <span className="absolute bottom-full mb-2 text-s bg-pink-600 text-white px-4 py-1 min-w-[100px] text-center rounded-full opacity-0 group-hover:opacity-100 transition duration-200 transform group-hover:-translate-y-1 shadow-md">
            Message
          </span>
        </div>





        
        {/* 🧾 View Log Button */}
        <div className="relative group flex flex-col items-center">
          <button
            onClick={() => setShowLogModal(true)}
            className="bg-purple-300 hover:bg-purple-400 p-6 rounded-full shadow-md transition-all text-3xl hover:scale-110 active:scale-95"
          >
            🧾
          </button>
          <span className="absolute bottom-full mb-2 text-s bg-purple-700 text-white px-4 py-1 min-w-[100px] text-center rounded-full opacity-0 group-hover:opacity-100 transition group-hover:-translate-y-1 shadow-md">
            View Log
          </span>
        </div>

      </div>

    



      {/* ==========================================================
          📜 Bot Log Modal
      ========================================================== */}
      {showLogModal && (
        <div className="fixed inset-0 bg-black bg-opacity-50 z-50 flex items-center justify-center">
          <div className="bg-white p-8 rounded-2xl shadow-2xl w-[400px] max-w-[90%] text-gray-800 relative animate-fade-in-fast">
            <button
              onClick={() => setShowLogModal(false)}
              className="absolute top-3 right-4 text-xl font-bold hover:text-red-500 transition"
            >
              ❌
            </button>
            <h2 className="text-xl font-semibold mb-4 text-center">🧾 Bot Activity Log</h2>
            <ul className="space-y-2 max-h-60 overflow-y-auto">
              {logEntries.map((entry, index) => (
                <li key={index} className="bg-gray-100 rounded-md px-4 py-2 text-sm shadow-sm">
                  {entry}
                </li>
              ))}
            </ul>
          </div>
        </div>
      )}






      {/* ==========================================================
          🔔 Toast Overlay
      ========================================================== */}
      <div className="fixed bottom-6 left-6 z-50 flex flex-col space-y-3 pointer-events-none">
        {toasts.map((toast) => (
          <div
            key={toast.id}
            className="bg-white/90 text-gray-800 px-4 py-2 rounded-lg shadow-lg backdrop-blur-md animate-fade-in-fast w-[260px] text-sm font-medium border-l-4 border-purple-400"
          >
            {toast.message}
          </div>
        ))}
      </div>





      





      
    </>
  );
}

export default BotUIHub;