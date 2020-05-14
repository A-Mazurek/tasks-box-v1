from __future__ import absolute_import
from flask_restful import Api
from flask_marshmallow import Marshmallow
from app.api.config import APP_CONFIG
from app.api.resources import TaskTodo, TaskUpdate, Tasks, Task
from app.api.cache import cache
from flask import Flask
from flasgger import Swagger


app = Flask("tasks_box")
app.config.from_mapping(APP_CONFIG)

api = Api(app)
ma = Marshmallow(app)
cache.init_app(app)
app.swagger = Swagger(app)

api.add_resource(TaskTodo, '/todo/', endpoint='new_task')
api.add_resource(Task, '/task/<int:task_id>', endpoint='task')
api.add_resource(TaskUpdate, '/update/<int:task_id>', endpoint='update task')
api.add_resource(Tasks, '/tasks/', endpoint='tasks list')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
