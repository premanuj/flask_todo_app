from app.ma import ma
from marshmallow import fields, validate, exceptions as marsh_exceptions


class TodoSchema(ma.Schema):
    id = fields.Integer(required=False)
    title = fields.String(required=True, validate=validate.Length(1, 50))
    description = fields.String(required=False)
    created_at = fields.DateTime(required=False)
