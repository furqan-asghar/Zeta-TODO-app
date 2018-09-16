from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class TODO(Resource):
    def get(self):
        task = {
            'id' : 1,
            'title' : 'my task',
            'description' : 'Jo bi hay',
            'done' : 1
        }
        return task


    # Get task by ID
class AddTodoTask(Resource):
    def post(self):
        task_json = request.get_json
        return {"Task added:": task_json}, 201
# Delete task from TODO list


# Get task by ID
class GetTodoTask(Resource):
    def get(self, num):
        return {'Task ID:': num}
# Delete task from TODO list

class DelTodoTask(Resource):
    def get(self, num):
        return {'Deleted Task:': num}

# update task

class UpdateTodoTask(Resource):
    def get(self, num):
        return {'Updated task:': num}


api.add_resource(TODO, "/TODO/api/v1.0/")
api.add_resource(GetTodoTask, "/TODO/api/v1.0/task/<int:num>")
api.add_resource(AddTodoTask, "/TODO/api/v1.0/task/add")
api.add_resource(DelTodoTask, "/TODO/api/v1.0/task/delete/<int:num>")
api.add_resource(UpdateTodoTask, "/TODO/api/v1.0/task/update/<int:num>")

if __name__ == '__main__':
    app.run(debug=True)
