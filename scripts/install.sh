#!/data/data/com.termux/files/usr/bin/bash

echo "📦 تثبيت VPN Pro لجهاز Galaxy A04e"
pkg update -y
pkg install python python3 nodejs -y
pip install flask flask-cors requests
echo "✅ تم التثبيت بنجاح"
