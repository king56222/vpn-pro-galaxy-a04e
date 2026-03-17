# utils.py - أدوات مساعدة

import os
import json
import hashlib
from datetime import datetime

class VPNUtils:
    @staticmethod
    def get_device_info():
        return {
            'device': 'Samsung Galaxy A04e',
            'platform': 'Android',
            'termux': os.path.exists('/data/data/com.termux')
        }
    
    @staticmethod
    def format_bytes(bytes):
        for unit in ['B', 'KB', 'MB', 'GB']:
            if bytes < 1024:
                return f"{bytes:.1f} {unit}"
            bytes /= 1024
        return f"{bytes:.1f} GB"
    
    @staticmethod
    def is_connected():
        try:
            import socket
            socket.create_connection(("8.8.8.8", 53), timeout=3)
            return True
        except:
            return False
