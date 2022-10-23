from marshmallow import Schema, fields


class ItemTagsSchema(Schema):
    message = fields.Str()
    item = fields.Nested("ItemSchema")
    tag = fields.Nested("TagSchema")
