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
