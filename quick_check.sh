#!/data/data/com.termux/files/usr/bin/bash

echo "⚡ فحص سريع بعد التشغيل"
echo "========================"

# تشغيل التطبيق في الخلفية
cd ~/vpn-pro-galaxy-a04e
python3 src/main.py > /dev/null 2>&1 &
sleep 3

# اختبار
curl -s http://127.0.0.1:5000/api/status | python3 -m json.tool

echo "========================"
echo "افتح المتصفح على: http://127.0.0.1:5000"
