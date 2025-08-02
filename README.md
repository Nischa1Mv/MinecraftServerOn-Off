# Minecraft Server Control Panel

A simple web application built with Flask that allows you to control (start/stop) a Minecraft server hosted on a DigitalOcean droplet.

## Features

- Web-based control panel
- Real-time server status monitoring
- Start/Stop server functionality
- Loading indicators for server state transitions
- Environment-based configuration

## Prerequisites

- Python 3.x
- DigitalOcean account
- DigitalOcean API token
- Droplet ID of your Minecraft server

## Setup

1. Clone this repository
2. Create a virtual environment:
   ```
   python -m venv venv
   ```
3. Activate the virtual environment:
   - Windows:
     ```
     .\venv\Scripts\activate
     ```
   - Linux/Mac:
     ```
     source venv/bin/activate
     ```
4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
5. Create a `.env` file based on `.env.example`:
   ```
   DIGITALOCEAN_TOKEN = your_digitalocean_api_token
   DROPLET_ID = your_droplet_id
   ```

## Running the Application

1. Make sure your virtual environment is activated
2. Run the Flask application:
   ```
   python app.py
   ```
3. Open your web browser and navigate to `http://localhost:5000`

## Usage

- Click "Start Server" to power on your Minecraft server
- Click "Stop Server" to power off your Minecraft server
- The status indicator shows the current state of your server:
  - "active": Server is running
  - "off": Server is stopped
  - "starting": Server is in the process of starting
  - "stopping": Server is in the process of stopping
  - "unknown": Unable to fetch server status

## Security Notes

- Keep your `.env` file secure and never commit it to version control
- Your DigitalOcean API token has full access to your account, so keep it private
- Consider implementing user authentication if deploying publicly

## License

This project is open source and available under the MIT License.