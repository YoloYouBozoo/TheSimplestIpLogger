import requests
import socket

# Replace WEBHOOK_URL with the URL of your Discord webhook
WEBHOOK_URL = "WEBHOOK_HERE"

def send_message(message):
    data = {"content": message}
    requests.post(WEBHOOK_URL, json=data)

# Get the machine's public IP address
public_ip = requests.get("https://api.ipify.org").text

# Send the IP address to the Discord webhook
send_message(f"The machine's public IP address is: {public_ip}")