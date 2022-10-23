from marshmallow import Schema, fields


class UserBaseSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)


class UserSchema(UserBaseSchema):
    pass
