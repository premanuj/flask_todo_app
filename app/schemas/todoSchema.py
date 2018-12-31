from app.ma import ma
from marshmallow import fields, validate, exceptions as marsh_exceptions


class TodoSchema(ma.Schema):
    title = fields.String(required=True, validate=validate.Length(1, 50))
    description = fields.String(required=False)
