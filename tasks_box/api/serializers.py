from marshmallow import Schema, fields


class TasksList(Schema):
    id = fields.Str()
    timestamp = fields.Str()
    content = fields.Str()
    done = fields.Str()
