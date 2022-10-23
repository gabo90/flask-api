from marshmallow import Schema, fields


class TagBaseSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)


class TagSchema(TagBaseSchema):
    store_id = fields.Int(load_only=True)
    store = fields.Nested("StoreBaseSchema", dump_only=True)
    items = fields.List(fields.Nested('ItemBaseSchema'), dump_only=True)
