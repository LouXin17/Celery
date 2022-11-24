from task import add, ClassNvs
from . import SettingTestCase

class TestTask(SettingTestCase):
    def test_add_answer(self):
        add_answer = add.apply({'x': 20, 'y': 50}) # 取得add工作ID
        self.assertEqual(add_answer.status, 'SUCCESS')

    def test_nvs_answer(self):
        nvs_answer = ClassNvs.apply({'x': 20, 'y': 50}) # 取得ClassNvs工作ID
        self.assertEqual(nvs_answer.status, 'SUCCESS')