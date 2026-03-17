#!/data/data/com.termux/files/usr/bin/python3
# update_servers.py - تحديث السيرفرات تلقائياً

import os
import sys
import json
import time
from datetime import datetime

# إضافة المسار الرئيسي
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.server_tester import ServerTester
from src.utils import VPNUtils

def backup_servers():
    """عمل نسخة احتياطية من ملف السيرفرات"""
    servers_file = 'config/servers.json'
    backup_file = f'config/servers_backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
    
    if os.path.exists(servers_file):
        import shutil
        shutil.copy2(servers_file, backup_file)
        print(f"✅ تم إنشاء نسخة احتياطية: {backup_file}")
        return backup_file
    return None

def add_new_servers():
    """إضافة سيرفرات جديدة"""
    new_servers = [
        {
            "id": 11,
            "name": "🇨🇭 Switzerland - Zurich",
            "host": "159.100.241.12",
            "port": 51820,
            "country": "Switzerland",
            "city": "Zurich",
            "flag": "🇨🇭",
            "provider": "Hetzner",
            "speed": "1Gbps"
        },
        {
            "id": 12,
            "name": "🇸🇪 Sweden - Stockholm",
            "host": "194.132.209.45",
            "port": 51820,
            "country": "Sweden",
            "city": "Stockholm",
            "flag": "🇸🇪",
            "provider": "OVH",
            "speed": "500Mbps"
        }
    ]
    
    servers_file = 'config/servers.json'
    try:
        with open(servers_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # إضافة السيرفرات الجديدة
        next_id = max(s['id'] for s in data['servers']) + 1
        for server in new_servers:
            server['id'] = next_id
            data['servers'].append(server)
            next_id += 1
        
        data['total'] = len(data['servers'])
        data['last_updated'] = datetime.now().isoformat()
        
        with open(servers_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        print(f"✅ تم إضافة {len(new_servers)} سيرفر جديد")
    except Exception as e:
        print(f"❌ خطأ في إضافة السيرفرات: {e}")

def main():
    print("=" * 50)
    print("🔄 تحديث قائمة السيرفرات")
    print("=" * 50)
    
    # التحقق من الاتصال
    if not VPNUtils.is_connected():
        print("❌ لا يوجد اتصال بالإنترنت")
        sys.exit(1)
    
    # نسخة احتياطية
    backup = backup_servers()
    
    # اختبار السيرفرات الحالية
    tester = ServerTester()
    results = tester.test_all_servers()
    
    # عرض النتائج
    print("\n📊 نتائج الاختبار:")
    online = sum(1 for r in results if r['status'] == 'online')
    print(f"✅ سيرفرات متصلة: {online}")
    print(f"❌ سيرفرات غير متصلة: {len(results) - online}")
    
    if online < len(results) * 0.7:  # إذا كانت نسبة النجاح أقل من 70%
        print("\n⚠️ نسبة النجاح منخفضة، جاري إضافة سيرفرات جديدة...")
        add_new_servers()
        
        # إعادة الاختبار
        tester = ServerTester()
        tester.test_all_servers()
    
    # تحديث الملف
    tester.update_servers_file()
    
    print("\n✅ تم تحديث السيرفرات بنجاح")
    print(f"📁 النسخة الاحتياطية: {backup}")

if __name__ == '__main__':
    main()
