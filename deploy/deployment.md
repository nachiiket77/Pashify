# Pashify Production VPS Deployment Guide

This guide provides step-by-step instructions for deploying **Pashify** on a 24/7 **Ubuntu Linux VPS** behind an **Nginx Reverse Proxy**, with **Let's Encrypt HTTPS SSL** and **Cloudflare CDN protection**.

---

## 🏗️ Architecture Overview

```text
[ User / Web Browser ]
          │
          ▼
    [ Cloudflare ] (DNS, SSL/TLS Proxy, DDoS Protection)
          │
          ▼
   [ Nginx Server ] (Port 80/443, SSL Termination, WebSockets)
          │
          ▼ (Reverse Proxy to 127.0.0.1:8501)
 [ Pashify Systemd ] (Streamlit Engine running on Port 8501)
```

---

## 📋 Prerequisites

- Ubuntu 22.04 or 24.04 LTS VPS (1 GB RAM minimum, 2 GB recommended)
- A registered Domain Name (e.g. `YOUR_DOMAIN.com`) pointing to your VPS IP address
- SSH root/sudo access to the server

---

## 🚀 Step 1: System Update & Dependencies Installation

Connect to your VPS via SSH and update package repositories:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3 python3-pip python3-venv nginx certbot python3-certbot-nginx git curl
```

---

## 👤 Step 2: Create Non-Root System User

For security compliance, Pashify should run under a dedicated non-root user:

```bash
sudo useradd -m -s /bin/bash pashify
sudo mkdir -p /var/www/pashify
sudo chown -R pashify:pashify /var/www/pashify
```

---

## 📥 Step 3: Clone Repository & Virtual Environment Setup

Switch to the `pashify` user and deploy the codebase:

```bash
sudo su - pashify
cd /var/www/pashify
git clone https://github.com/nachiiket77/Pashify.git .

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Create .env from template
cp .env.example .env
exit
```

---

## ⚙️ Step 4: Configure Systemd Daemon Service

Create the systemd service file to keep Pashify running 24/7 automatically:

```bash
sudo cp /var/www/pashify/deploy/pashify.service /etc/systemd/system/pashify.service
sudo systemctl daemon-reload
sudo systemctl enable pashify
sudo systemctl start pashify
```

Verify service status:

```bash
sudo systemctl status pashify
```

---

## 🌐 Step 5: Configure Nginx Reverse Proxy

Copy the Nginx configuration to `sites-available`:

```bash
sudo cp /var/www/pashify/deploy/nginx.conf /etc/nginx/sites-available/pashify
```

Open `/etc/nginx/sites-available/pashify` and replace `YOUR_DOMAIN.com` with your actual domain name:

```bash
sudo nano /etc/nginx/sites-available/pashify
```

Link the configuration to `sites-enabled` and test Nginx:

```bash
sudo ln -s /etc/nginx/sites-available/pashify /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

---

## 🔒 Step 6: Secure with Let's Encrypt HTTPS (Certbot)

Generate SSL certificates automatically:

```bash
sudo certbot --nginx -d YOUR_DOMAIN.com -d www.YOUR_DOMAIN.com
```

Certbot will automatically verify ownership, issue certificates, and update your Nginx SSL paths.

---

## ☁️ Step 7: Cloudflare Integration

If using Cloudflare:

1. **DNS Management:** Add an `A` record pointing `YOUR_DOMAIN.com` to your VPS IPv4 address with Proxy Status set to **Proxied (Orange Cloud)**.
2. **SSL/TLS Mode:** Set SSL/TLS Encryption Mode to **Full (Strict)**.
3. **WebSockets:** Under **Network**, ensure **WebSockets** is toggled ON.
4. **Security Settings:** Under **Security ➔ Settings**, set Security Level to **Medium** or **High**.

---

## 📊 Maintenance & Logging Commands

- **Check Service Status:** `sudo systemctl status pashify`
- **Restart Application:** `sudo systemctl restart pashify`
- **View Live Application Logs:** `sudo journalctl -u pashify -f`
- **Reload Nginx:** `sudo systemctl reload nginx`
