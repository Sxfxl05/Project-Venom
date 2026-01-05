import os, json, time, requests
from datetime import datetime, timedelta

# --- CONFIGURATION (Sanitized) ---
# Replace placeholders with your actual credentials for local use
TOKEN = "YOUR_BOT_TOKEN_HERE"
CHAT_ID = "YOUR_CHAT_ID_HERE"
LOG_FILE = "/var/tmp/opencanary.log"

# Tracking for Daily Health Check
last_heartbeat = datetime.now()

def get_location(ip):
    try:
        # High-integrity IP lookup for attribution
        response = requests.get(f"http://ip-api.com/json/{ip}", timeout=5).json()
        if response.get("status") == "success":
            return f"{response.get('city')}, {response.get('country')}"
        return "Unknown Location"
    except:
        return "Lookup Failed"

def send_alert(message):
    try:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        requests.post(url, json={"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}, timeout=10)
    except Exception as e:
        print(f"Notification Error: {e}")

print("🚀 Venom Multi-Port Stinger Active...")

with open(LOG_FILE, "r") as f:
    f.seek(0, os.SEEK_END)
    while True:
        # --- DAILY HEARTBEAT LOGIC ---
        if datetime.now() > last_heartbeat + timedelta(days=1):
            send_alert("🏠 **System Health Check**: Project Venom is still standing guard.")
            last_heartbeat = datetime.now()

        line = f.readline()
        if not line:
            time.sleep(1)
            continue
        try:
            data = json.loads(line)
            logtype = data.get("logtype")
            logdata = data.get("logdata", {})
            
            # Monitoring Logtypes: 3001 (HTTP), 2000 (FTP), 4002 (SSH)
            if logtype in [3001, 2000, 4002]:
                user = logdata.get("USERNAME") or logdata.get("USER") or "Unknown"
                pwd = logdata.get("PASSWORD") or logdata.get("PASS") or "Unknown"
                src_ip = data.get("src_host", "Unknown")
                dst_port = data.get("dst_port", "Unknown")
                location = get_location(src_ip)
                
                protocol = "HTTP" if logtype == 3001 else "FTP" if logtype == 2000 else "SSH"
                
                alert = (
                    f"🚨 **VENOM ALERT: {protocol} STRIKE**\n\n"
                    f"👤 **User:** `{user}`\n"
                    f"🔑 **Pass:** `{pwd}`\n"
                    f"🌐 **IP:** `{src_ip}`\n"
                    f"📍 **Loc:** *{location}*\n"
                    f"🔌 **Port:** `{dst_port}`"
                )
                send_alert(alert)
        except:
            continue