from flask import Flask, render_template, request, redirect, url_for, session
import requests
import os
from dotenv import load_dotenv
import socket

load_dotenv()  # Load environment variables from .env file if it exists

app = Flask(__name__)
app.secret_key = os.urandom(24)

DIGITALOCEAN_TOKEN = os.getenv("DIGITALOCEAN_TOKEN")
DROPLET_ID = os.getenv("DROPLET_ID")
DROPLET_IP = os.getenv("DROPLET_IP")
APP_PORT = int(os.getenv("APP_PORT"))
HEADERS = {
    "Authorization": f"Bearer {DIGITALOCEAN_TOKEN}",
    "Content-Type": "application/json"
}

def fetch_status():
    try:
        r = requests.get(
            f"https://api.digitalocean.com/v2/droplets/{DROPLET_ID}",
            headers=HEADERS
        )
        return r.json()["droplet"]["status"]
    except:
        return "unknown"
    
def is_server_responsive(ip, port, timeout=2):
    try:
        with socket.create_connection((ip, port), timeout=timeout):
            return True
    except:
        return False

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        action = request.form.get("action")
        current_status = fetch_status()

        if action == "power_on" and current_status != "active":
            session['status'] = "starting"
            requests.post(
                f"https://api.digitalocean.com/v2/droplets/{DROPLET_ID}/actions",
                headers=HEADERS,
                json={"type": "power_on"}
            )

        elif action == "power_off" and current_status != "off":
            session['status'] = "stopping"
            requests.post(
                f"https://api.digitalocean.com/v2/droplets/{DROPLET_ID}/actions",
                headers=HEADERS,
                json={"type": "power_off"}
            )

        return redirect(url_for("index"))

  # Determine what status to show
    live_status = fetch_status()
    session_status = session.get('status')

    if session_status == "starting":
        if live_status == "active":
            if is_server_responsive(DROPLET_IP, APP_PORT):
                session.pop('status')
                status = "active"
            else:
                status = "starting"
        else:
            status = "starting"

    elif session_status == "stopping":
        if live_status == "off":
            session.pop('status')
            status = "off"
        else:
            status = "stopping"
    else:
        status = live_status

    return render_template("index.html", status=status, DROPLET_IP=DROPLET_IP, APP_PORT=APP_PORT)


if __name__ == "__main__":
    app.run(debug=True)