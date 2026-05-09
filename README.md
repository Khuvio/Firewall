## What is This Project?

This is a **web-based firewall management tool** built specifically for Kali Linux. Instead of typing long iptables commands in the terminal every time, you can manage your entire firewall through a **beautiful graphical interface** in your browser — while still controlling the real iptables firewall underneath.
## How it Works

```
You click a button in Browser
           │
           ▼
    Flask Backend (app.py)
           │
           ▼
    iptables command runs
           │
           ▼
  Real Firewall gets updated
```

> Everything you do in the UI — adding rules, blocking ports, enabling firewall — all happens on the **real iptables firewall** on your Kali machine!


## Technologies Used

| Technology | Role | Why |
|---|---|---|
| **Python** | Backend language | Easy and powerful |
| **Flask** | Web framework | Lightweight and simple |
| **iptables** | Actual firewall | Built into Linux |
| **HTML/CSS** | Frontend UI | Runs in browser |
| **JavaScript** | UI logic | Makes it interactive |
| **subprocess** | Runs Linux commands | Connects Python to iptables |


## What You Can Do With It

| Feature | Description |
|---|---|
| ➕ Add Rules | Block or allow any port or IP address |
| ❌ Delete Rules | Remove rules you no longer need |
| 🔄 Toggle Firewall | Turn entire firewall ON or OFF |
| 🔍 View Rules | See all active iptables rules in real time |
| 🚫 Flush All | Wipe all rules and start fresh |
| 📊 Live Status | See policy and rule count updated every 5 seconds |


## Real Life Use Cases

| Situation | How This Tool Helps |
|---|---|
| Someone trying to hack your SSH | Block their IP instantly from UI |
| Running a web server | Open port 80 and 443 easily |
| Securing a database | Block port 3306 from outside |
| Learning cybersecurity | See how firewall rules work visually |
| Practicing ethical hacking | Test your own machine security |


## Project Structure Explained

```
firewall-project/
│
├── app.py  ← The Brain 🧠
│            Receives requests from UI
│            Runs iptables commands
│            Sends results back to browser
│
├── templates/
│   └── index.html  ← The Face 🎨
│                    What you see in browser
│                    Buttons, tables, toggles
│                    Talks to app.py via API
│
├── static/  ← Future use
│             CSS and JS files go here
│
└── README.md  ← Instructions 📖
               How to install and run

## API Endpoints (How UI talks to Backend)

| Action | Method | Endpoint | What Happens |
|---|---|---|---|
| View rules | GET | `/api/rules` | Reads iptables and returns rules |
| Add rule | POST | `/api/rules` | Runs iptables -A command |
| Delete rule | DELETE | `/api/rules/INPUT/1` | Runs iptables -D command |
| Enable firewall | POST | `/api/enable` | Sets policy to DROP |
| Disable firewall | POST | `/api/disable` | Sets policy to ACCEPT |
| Flush rules | POST | `/api/flush` | Runs iptables -F |
| Get status | GET | `/api/status` | Returns policy and rule count |

---

## Security Features

| Feature | Description |
|---|---|
| 🔒 localhost only | Runs on 127.0.0.1 — not exposed to internet |
| 🔑 sudo required | Only admin can run it |
| 🛡️ Real iptables | Not a simulation — controls actual firewall |
| ⚡ Instant updates | Rules apply immediately — no restart needed |

## Perfect For

| Who | Why |
|---|---|
| **MCA Students** | Great portfolio project showing Python + Linux + Security skills |
| **Beginners** | Learn firewall concepts visually |
| **Ethical Hackers** | Quickly configure protection during pentesting |
| **Developers** | Manage ports easily without memorizing commands |

---

## What Makes it Special 🌟

Most firewall tools are either:
- Too complex (requires deep Linux knowledge)
- Not real (just simulations)

This project is:
- ✅ **Simple** — runs with one command
- ✅ **Real** — controls actual iptables
- ✅ **Visual** — no need to memorize commands
- ✅ **Educational** — great for learning and resume
- ✅ **Lightweight** — no heavy dependencies

# Kali Linux Firewall Manager

A Flask-based firewall management UI for Kali Linux using iptables.

## Project Structure
```
firewall-project/
├── app.py              ← Flask backend
├── templates/
│   └── index.html      ← Firewall UI
└── static/             ← CSS/JS (future use)
```

## Setup Instructions

### Step 1 — Install Requirements
```bash
sudo apt install python3-pip -y
sudo pip3 install flask flask-cors --break-system-packages
```

### Step 2 — Run the Project
```bash
cd ~/firewall-project
sudo python3 app.py
```

### Step 3 — Open in Browser
```
http://127.0.0.1:5000
```

### Step 4 — Stop the Server
```
Ctrl + C
```

## Features
- View real iptables rules
- Add new firewall rules (INPUT/OUTPUT/FORWARD)
- Delete rules
- Enable/Disable firewall
- Flush all rules
- Live status updates every 5 seconds

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | /api/rules | Get all rules |
| POST   | /api/rules | Add a rule |
| DELETE | /api/rules/<chain>/<num> | Delete a rule |
| POST   | /api/enable | Enable firewall |
| POST   | /api/disable | Disable firewall |
| POST   | /api/flush | Flush all rules |
| GET    | /api/status | Get firewall status |

## Important Notes
- Always run with sudo (iptables needs root)
- Keep server on 127.0.0.1 only (never expose to internet)
- Allow port 22 before enabling firewall to avoid lockout
