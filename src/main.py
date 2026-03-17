#!/data/data/com.termux/files/usr/bin/python3
# main.py - النقطة الرئيسية للتطبيق

import os
import sys
import json
import signal
import traceback

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

print("=" * 50)
print("🚀 VPN Pro for Samsung Galaxy A04e")
print("=" * 50)

try:
    from src.vpn_manager import VPNManager
    from src.web_interface import WebInterface
    print("✅ تم تحميل الوحدات بنجاح")
except Exception as e:
    print(f"❌ خطأ في التحميل: {e}")
    sys.exit(1)

class VPNApplication:
    def __init__(self):
        self.config = self.load_config()
        self.vpn_manager = VPNManager(self.config)
        self.web_interface = WebInterface(self.vpn_manager, self.config)
    
    def load_config(self):
        config_path = os.path.join(parent_dir, 'config', 'settings.json')
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return {"port": 5000, "debug": True}
    
    def run(self):
        port = self.config.get('port', 5000)
        debug = self.config.get('debug', True)
        
        print(f"📡 تشغيل الخادم على http://localhost:{port}")
        self.web_interface.run(port=port, debug=debug)

if __name__ == "__main__":
    app = VPNApplication()
    app.run()
