from flask_testing import TestCase
from app import app

class SettingTestCase(TestCase):  # 單元測試設定檔
    def create_app(self):
        app.config['TESTING'] = True
        return app
