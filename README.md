# Device & Server Monitoring Dashboard

A lightweight monitoring dashboard to track the status of servers, printers, and cameras in real time.  
This project uses Python to generate device statuses and a web dashboard for visualization.

---

## Project Structure

```
code/
├── server.py         # Python script to generate status.json
├── server.html       # Frontend dashboard to display devices
├── status.json       # Auto-generated status file (do not edit)
├── css/              # Local Bootstrap CSS
│   └── bootstrap.min.css
├── js/               # Local Bootstrap JS
│   └── bootstrap.bundle.min.js
└── README.md
```

---

## Features

- Displays Department and Project servers, Printers, and Cameras in an accordion layout.  
- Shows Up/Down status for each device.  
- Live updating every 10 seconds using `status.json`.  
- Search functionality across all categories (IP, hostname, owner, room, location).  
- Highlights matching search results in yellow.  
- Badges show Up Count / Total Count for each category.  
- Fully local frontend using Bootstrap (CSS & JS).  

---

## Requirements

- Python 3.x  
- Web browser to open `server.html`  

Optional for local deployment:

- Flask or other Python web server if you want to serve HTML dynamically.

---

## Setup & Usage

1. **Clone the repository**

```bash
git clone https://github.com/toshuiit/monitoring.git
cd monitoring
```

2. **Run the Python script to generate `status.json`**

```bash
python3 server.py
```

`status.json` will be generated in the same folder every few minutes.  

3. **Open the dashboard**

Open `server.html` in a browser to see the status of devices.  
Use the search box to filter devices and highlight results.

---

## Python Script (`server.py`)

- Generates `status.json` with device information and their status (Up/Down).  
- Can be extended to fetch real-time statuses via ping or API calls.

---

## HTML Dashboard (`server.html`)

- Uses Bootstrap accordion to organize device categories.  
- Dynamically renders all devices using JavaScript.  
- Highlights search matches and updates category badges in real-time.

---

## Contributing

- Add new devices by modifying `server.py` to include the new entries.  
- For new features or bug fixes, create a GitHub issue or pull request.

