# utils.py - أدوات مساعدة

import os
import json
import hashlib
import base64
import re
from datetime import datetime
import platform
import subprocess

class VPNUtils:
    @staticmethod
    def get_device_info():
        """الحصول على معلومات الجهاز"""
        info = {
            'device': platform.node(),
            'system': platform.system(),
            'release': platform.release(),
            'machine': platform.machine(),
            'termux': os.path.exists('/data/data/com.termux')
        }
        
        # معلومات إضافية لـ Termux
        if info['termux']:
            try:
                # حجم الذاكرة
                with open('/proc/meminfo', 'r') as f:
                    for line in f:
                        if 'MemTotal' in line:
                            mem = int(line.split()[1]) // 1024
                            info['memory_mb'] = mem
                            break
                
                # إصدار Android
                if os.path.exists('/system/build.prop'):
                    with open('/system/build.prop', 'r') as f:
                        for line in f:
                            if 'ro.build.version.release' in line:
                                info['android'] = line.split('=')[1].strip()
                                break
            except:
                pass
        
        return info
    
    @staticmethod
    def format_bytes(bytes):
        """تحويل البايتات إلى صيغة مقروءة"""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if bytes < 1024.0:
                return f"{bytes:.1f} {unit}"
            bytes /= 1024.0
        return f"{bytes:.1f} PB"
    
    @staticmethod
    def format_time(seconds):
        """تنسيق الوقت"""
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        seconds = int(seconds % 60)
        
        if hours > 0:
            return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        else:
            return f"{minutes:02d}:{seconds:02d}"
    
    @staticmethod
    def generate_key():
        """توليد مفتاح عشوائي"""
        return base64.b64encode(os.urandom(32)).decode()
    
    @staticmethod
    def hash_data(data):
        """تشفير البيانات"""
        if isinstance(data, str):
            data = data.encode()
        return hashlib.sha256(data).hexdigest()
    
    @staticmethod
    def validate_ip(ip):
        """التحقق من صحة عنوان IP"""
        pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
        if re.match(pattern, ip):
            parts = ip.split('.')
            for part in parts:
                if int(part) > 255:
                    return False
            return True
        return False
    
    @staticmethod
    def is_connected():
        """التحقق من الاتصال بالإنترنت"""
        try:
            import socket
            socket.create_connection(("8.8.8.8", 53), timeout=3)
            return True
        except:
            return False
    
    @staticmethod
    def get_wifi_info():
        """الحصول على معلومات WiFi"""
        try:
            if os.path.exists('/data/data/com.termux'):
                result = subprocess.run(['dumpsys', 'wifi'], 
                                      capture_output=True, 
                                      text=True)
                for line in result.stdout.split('\n'):
                    if 'SSID' in line:
                        return line.strip()
        except:
            pass
        return "Unknown"
    
    @staticmethod
    def get_battery_level():
        """الحصول على مستوى البطارية"""
        try:
            if os.path.exists('/sys/class/power_supply/battery/capacity'):
                with open('/sys/class/power_supply/battery/capacity', 'r') as f:
                    return int(f.read().strip())
        except:
            pass
        return None
    
    @staticmethod
    def save_config(data, filename):
        """حفظ الإعدادات"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            return True
        except:
            return False
    
    @staticmethod
    def load_config(filename, default=None):
        """تحميل الإعدادات"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return default or {}
