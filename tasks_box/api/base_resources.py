from flask_restful import Resource
from typing import Dict, List, Any, Tuple
from .utils import read_file, save_to_file
from .serializers import TasksList
from .cache import cache
from datetime import datetime


class BaseTaskResource(Resource):
    tasks_serializer = TasksList(many=True)
    task_serializer = TasksList(many=False)

    @cache.cached(key_prefix='stores_data')
    def get_tasks(self) -> List[Dict[str, str]]:
        return read_file()

    def save_data(self, new_data) -> None:
        cache.clear()
        save_to_file(new_data)

    def save_task(self, new_task) -> Dict[str, str]:
        self.data = self.get_tasks()
        task = {
            "id": max([x['id'] for x in self.data]) + 1,
            "timestamp": datetime.timestamp(datetime.now()),
            "content": new_task.get('content'),
            "done": False
        }
        self.data.append(task)
        self.save_data(self.data)
        return task

    def update_task(self, task: Dict, update: Dict) -> Dict[str, str]:
        self.data = self.get_tasks()
        self.data.remove(task)
        if updated_content := update.get("content", None):
            task["content"] = updated_content
        elif updated_status := update.get("done", None):
            task["done"] = updated_status
        else:
            raise KeyError
        self.data.append(task)
        self.save_data(self.data)
        return task

