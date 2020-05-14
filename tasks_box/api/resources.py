from flask_restful import Resource
from flask import request
# from .processor import TaskProcessor
from.base_resources import BaseTaskResource


class TaskTodo(BaseTaskResource):

    def post(self):
        """
        Use this 'POST' method to create new task.
        ---
        parameters:
         - in: body
           name: content
           type: string
           required: true
        """

        new_content = request.get_json()
        task = self.save_task(new_content)
        return self.task_serializer.dump(task)


class Task(BaseTaskResource):

    def get(self, task_id):
        """
        Use this "GET" method to display a specific task.
        ---
        parameters:
         - in: body
           name: task_id
           type: int
           required: true
        """
        tasks = self.get_tasks()
        task = [task for task in tasks if task['id'] == task_id][0]
        return self.task_serializer.dump(task)


class TaskUpdate(BaseTaskResource):

    def put(self, task_id):
        """
        Use this "PUT" method to update a specific task.
        ---
        parameters:
         - in: body
           name: task_id
           type: int
           required: true
        """
        """
        curl -i -H "Content-Type: application/json" -X PUT -d '{"done":true}' http://localhost:5000/task/1
        """
        try:
            task_update = request.get_json()
            tasks = self.get_tasks()
            task = [task for task in tasks if task['id'] == task_id][0]
            updated_task = self.update_task(task, task_update)
            return self.task_serializer.dump(updated_task)
        except Exception as e:
            return {"ErrorOccured": "You can update 'content' or 'done', update the rest of keys is not supported,"}


class Tasks(BaseTaskResource):

    def get(self):
        """
        Use this 'GET' method to display all tasks.
        ---
        parameters:
         - in: body
           type: string
        """

        tasks = self.get_tasks()
        return self.tasks_serializer.dump(tasks)
