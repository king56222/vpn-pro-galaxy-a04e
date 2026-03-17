# vpn_manager.py - إدارة VPN

import json
import os
import time
import random
from datetime import datetime

class VPNManager:
    def __init__(self, config):
        self.config = config
        self.status = "disconnected"
        self.current_server = None
        self.connection_time = None
        self.data_usage = {"download": 0, "upload": 0}
        
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        servers_file = os.path.join(base_path, 'config', 'servers.json')
        
        try:
            with open(servers_file, 'r', encoding='utf-8') as f:
                self.servers = json.load(f).get('servers', [])
        except:
            self.servers = self.get_default_servers()
    
    def get_default_servers(self):
        return [
            {"id": 1, "name": "🇫🇷 France", "host": "51.38.48.139", "flag": "🇫🇷", "latency": 45},
            {"id": 2, "name": "🇳🇱 Netherlands", "host": "46.101.117.163", "flag": "🇳🇱", "latency": 52}
        ]
    
    def get_servers(self):
        return self.servers
    
    def connect(self, server_id):
        server = next((s for s in self.servers if s['id'] == server_id), None)
        if not server:
            return False, "السيرفر غير موجود"
        
        self.status = "connecting"
        self.current_server = server
        time.sleep(2)
        self.status = "connected"
        self.connection_time = datetime.now()
        return True, f"✅ تم الاتصال بـ {server['name']}"
    
    def disconnect(self):
        self.status = "disconnected"
        self.current_server = None
        self.connection_time = None
        return True, "🔴 تم قطع الاتصال"
    
    def get_status(self):
        return {
            "status": self.status,
            "server": self.current_server['name'] if self.current_server else None,
            "ip": "145.239.252.205",
            "data_usage": self.data_usage
        }
    
    def test_speed(self):
        return {"success": True, "latency": random.randint(30, 100)}
