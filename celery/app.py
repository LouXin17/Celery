from flask import Flask, request
from flask_restx import Api, Resource, fields  # restx輸出格式
from task import add, ClassNvs, celery_app
from celery.result import AsyncResult


app = Flask(__name__)
api = Api(app, doc='/api/doc', title='Test Form')  # doc: Swagger的路由位置 /doc


Default_Input = api.model('輸入', {  # 預設輸入
    'x': fields.Integer(required=True),
    'y': fields.Integer(required=True)
})

Get_Status = api.model('工作_Status', {  # 取得工作狀態
    'status': fields.String(required=True),
    'ans': fields.String(required=True),
})

Get_taskID_output = api.model('WorkID', {  # 取得並輸出工作ID
    'ID': fields.String(required=True)
})


@api.route('/get_task_status')
class GetTaskStatus(Resource):
    @api.doc(params={'Tasks ID': 'ID'})
    @api.marshal_with(Get_Status)  # marshal_with输出字段(取得工作狀態)
    def get(self):
        data = request.args.get('Tasks ID')  # 取得工作ID
        output = AsyncResult(data, app=celery_app)  # 異同步執行
        return {
            'status': '0',          'ans': output.result
        }


@api.route('/post_taskID')
class PostTaskID(Resource):
    @api.expect(Default_Input)  # 預設輸入
    @api.marshal_with(Get_taskID_output)  # marshal_with输出字段(取得並輸出工作ID)
    def post(self):
        data = api.payload
        return {
            'ID': add.delay(data['x'], data['y']).id
        }


@ api.route('/class_post_taskID')
class ClassPostTaskID(Resource):
    @ api.expect(Default_Input)
    @ api.marshal_with(Get_taskID_output)
    def post(self):
        data = api.payload
        return {
            'ID': ClassNvs.delay(data['x'], data['y']).id
        }


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
