#!/data/data/com.termux/files/usr/bin/bash

echo "🔍 تشخيص مشكلة الاتصال"
echo "========================"

# هل التطبيق يعمل؟
echo -n "📋 التطبيق: "
if ps aux | grep -q "[p]ython.*main.py"; then
    echo "✅ يعمل"
else
    echo "❌ لا يعمل"
fi

# اختبار الاتصال المحلي
echo -n "🌐 localhost:5000: "
if curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:5000 2>/dev/null | grep -q "200\|404"; then
    echo "✅ متاح"
else
    echo "❌ غير متاح"
fi

# عناوين IP المتاحة
echo "📡 عناوين IP:"
ip -4 addr show | grep inet | grep -v 127.0.0.1

# المنفذ 5000
echo -n "🔌 المنفذ 5000: "
if netstat -tuln 2>/dev/null | grep -q ":5000"; then
    echo "✅ مفتوح"
else
    echo "❌ مغلق"
fi
