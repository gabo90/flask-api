from marshmallow import Schema, fields


class StoreBaseSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)


class StoreSchema(StoreBaseSchema):
    items = fields.List(fields.Nested('ItemBaseSchema'), dump_only=True)
    tags = fields.List(fields.Nested('TagBaseSchema'), dump_only=True)
