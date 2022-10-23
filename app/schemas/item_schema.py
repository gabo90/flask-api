from marshmallow import Schema, fields


class ItemBaseSchema(Schema):
    name = fields.Str(required=True)
    price = fields.Float(required=True)


class ItemSchema(ItemBaseSchema):
    id = fields.Int(dump_only=True)
    store_id = fields.Int(required=True, load_only=True)
    store = fields.Nested("StoreBaseSchema", dump_only=True)
    tags = fields.List(fields.Nested('TagBaseSchema'), dump_only=True)


class ItemUpdateSchema(ItemBaseSchema):
    pass
