#!/usr/bin/env python3
import json
import subprocess
import platform
from datetime import datetime

# Define your devices here
servers_department = [
    {"ip": "8.8.8.8", "hostname": "dep-server-1", "owner": "Lab-A", "room": "R101", "rack": "Rack-1"},
    {"ip": "1.2.3.4", "hostname": "dep-server-2", "owner": "Lab-B", "room": "R102", "rack": "Rack-2"},
]

servers_projects = [
    {"ip": "192.168.2.10", "hostname": "proj-server-1", "owner": "lab-a", "room": "R201", "rack": "Rack-3"},
]

printers = [
    {"ip": "8.8.8.8", "hostname": "printer-1", "location": "Lab-3"},
    {"ip": "8.8.8.8", "hostname": "printer-2", "location": "Lab-4"},
]

cameras = [
    {"ip": "192.168.4.10", "location": "Entrance"},
    {"ip": "192.168.4.11", "location": "Hallway"},
]

def ping(host):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    try:
        result = subprocess.run(["ping", param, "1", host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.returncode == 0
    except Exception:
        return False

def check_devices(devices, type="server"):
    checked = []
    for d in devices:
        status = ping(d["ip"])
        d_copy = d.copy()
        d_copy["status"] = status
        checked.append(d_copy)
    return checked

def generate_status():
    status = {
        "last_updated": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        "servers": {
            "department": check_devices(servers_department),
            "projects": check_devices(servers_projects)
        },
        "printers": check_devices(printers),
        "cameras": check_devices(cameras)
    }
    with open("status.json", "w") as f:
        json.dump(status, f, indent=4)

if __name__ == "__main__":
    generate_status()
    print("status.json generated successfully.")

