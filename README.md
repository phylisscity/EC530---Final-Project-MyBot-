
# 🤖 MyBot World

**MyBot World** is a playful, browser-based ecosystem where users can create, control, and communicate with autonomous bots on an interactive grid. Built with a modular architecture and designed to support both independent bot actions and collaborative goals, the platform blends educational backend logic with an engaging cartoon-style frontend.

---

## 🌐 Live Features (Backend Completed)
The Python-Flask backend is fully functional and exposes a robust REST API that supports:

### 🛠️ Core Bot Functionality
- `POST /create`: Create a bot with a unique name and emoji
- `POST /shutdown/<bot_id>`: Shut down a specific bot
- `POST /recharge/<bot_id>`: Recharge a bot's energy
- `POST /move/<bot_id>` + `/move_random/<bot_id>`: Move a bot manually or randomly

### 💌 Messaging System
- `POST /send_message/<sender_id>/<receiver_id>`: Bots send messages to each other
- `GET /inbox/<bot_id>`: Fetch inbox for a bot
- `GET /outbox/<bot_id>`: Fetch outbox for a bot
- `GET /status/<bot_id>`: Get a bot's position, energy, and logs

### 🌱 Grid and Goal Logic
- `POST /resize_grid`: Change the grid dynamically
- `POST /create_shared_goal`: Define a shared location-based target
- Bots gain rewards when reaching goals
- Logs and energy costs are tracked

---

## 🖼️ Frontend Plans (In Progress)
The React.js + Tailwind frontend is being fully redesigned to resemble a cozy desktop-style grid world. The layout is inspired by idle pet games and productivity apps.

### 🎨 Visual Features (Ongoing)
- Soft green "garden" background as base
- Bots represented by emoji or custom character avatars
- No harsh grid borders — characters float in ambient grid cells
- Control panel includes:
  - Create Bot (➕)
  - Recharge All (🔋)
  - Delete All (🗑️)
  - Message Hub ✉️ (Gmail-style side drawer)
- Floating bubbles, icons, and goal objects
- Clicking a bot opens a mini-popup to:
  - Recharge/delete that specific bot
  - View its inbox/outbox
  - Set/update mood/status emoji

### 📂 Project Folder Structure
```
MyBot/
│   └── bot_manager.py   # Bot logic and state
├── API/                 # Flask backend with routes and manager
│   └── routes.py        # All REST API endpoints
├── world/               # Grid and position logic
│   └── grid.py
Frontend/
├── frontend/
│   ├── src/components/  # React components (Grid, Bot, BotUIHub, etc.)
│   ├── pages/           # App.jsx layout
│   ├── index.css        # Global styling
│   └── main.jsx         # App entry point
```

---

## 🖼️ Interface Preview

![MyBot World UI](./public/goalfrontend.png)

---

## ⚙️ Setup Instructions

### 🐍 Backend (Flask)
```bash
cd MyBot
pip install -r requirements.txt
flask run
```

### ⚛️ Frontend (Vite + React)
```bash
cd Frontend/frontend
npm install
npm run dev
```

---

## 💡 Future Goals
- Multiplayer/real-time updates
- Save/load grid state from database
- Bot AI/mood detection via OpenAI
- Stats dashboard: energy trends, message volume
- Pet-style evolution or traits per bot

---
