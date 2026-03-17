# web_interface.py - واجهة الويب

from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import os

class WebInterface:
    def __init__(self, vpn_manager, config):
        self.vpn_manager = vpn_manager
        self.config = config
        self.app = Flask(__name__,
                        template_folder=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates'),
                        static_folder=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static'))
        CORS(self.app)
        self.setup_routes()
    
    def setup_routes(self):
        @self.app.route('/')
        def index():
            return render_template('index.html')
        
        @self.app.route('/api/servers')
        def get_servers():
            return jsonify({"servers": self.vpn_manager.get_servers()})
        
        @self.app.route('/api/status')
        def get_status():
            return jsonify(self.vpn_manager.get_status())
        
        @self.app.route('/api/connect', methods=['POST'])
        def connect():
            data = request.json
            success, message = self.vpn_manager.connect(int(data['server_id']))
            return jsonify({"success": success, "message": message})
        
        @self.app.route('/api/disconnect', methods=['POST'])
        def disconnect():
            success, message = self.vpn_manager.disconnect()
            return jsonify({"success": success, "message": message})
        
        @self.app.route('/api/test-speed')
        def test_speed():
            return jsonify(self.vpn_manager.test_speed())
    
    def run(self, port=5000, debug=False):
        print(f"🚀 تشغيل الخادم على المنفذ {port}")
        self.app.run(host='0.0.0.0', port=port, debug=debug, threaded=True)
