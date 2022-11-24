import json
from . import SettingTestCase
from unittest.mock import patch

class GetTaskStatus(SettingTestCase):
    def  test_get_status(self):#, mock_request, AsyncResult
        response = self.client.get(
            '/get_task_status',
            query_string = { # 不包含前導問號的參數
                'Tasks ID': '90f2f775-ef6c-4c53-83e5-bfb2ecd7b816'
            }
        )
        print('回應:', response.status_code)
        self.assertEqual(response.status_code, 200)

    @patch('task.add.delay')
    def test_post_taskid(self, mock_add):
        response = self.client.post(
            '/post_taskID',
            data = json.dumps({
                'x': 20,
                'y': 50
            }),
            content_type = 'application/json'
        )
        print('回應:', response.status_code)
        self.assertTrue(mock_add.called)
        print('mock:', mock_add.called)
        self.assertEqual(response.status_code, 200)

    @patch('task.ClassNvs.delay')
    def test_class_post_taskid(self, mock_class_nvs):
        class_response = self.client.post(
            '/class_post_taskID',
            data = json.dumps({
                'x': 20,
                'y': 50
            }),
            content_type = 'application/json'
        )
        print('回應:', class_response.status_code)
        self.assertTrue(mock_class_nvs.called)
        print('mock:', mock_class_nvs.called)
        self.assertEqual(class_response.status_code, 200)