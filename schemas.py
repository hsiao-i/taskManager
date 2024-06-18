from marshmallow import Schema, fields

class PlainUserSchema(Schema):
    id = fields.Int(dump_only=True)
    uuid = fields.Str(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True) # load_only=True 是為了避免密碼被洩漏出去，當前端要取得使用者資料時，確保不會取得密碼
    email = fields.Email( options={'check_deliverability': True})
    phone = fields.Str()
    role = fields.Str()



class UserSchema(PlainUserSchema):
    tags = fields.List(fields.Nested(PlainTagSchema), dump_only=True) 
    # fields.List(fields.Nested() 的話，就會是一個陣列包物件的感覺 (有多個 tag)


class PlainTodoSchema(Schema):
    id = fields.Int(dump_only=True)
    uuid = fields.Str(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str()
    

class TodoSchema(PlainTodoSchema):
    tags = fields.List(fields.Nested(PlainTagSchema), dump_only=True)


class PlainTagSchema(Schema):
    id = fields.Int(dump_only=True)
    uuid = fields.Str(dump_only=True)
    name = fields.Str(required=True)

class TagSchema(PlainTagSchema):
    user_id = fields.Int(required=True, load_only=True)
    user = fields.Nested(PlainUserSchema, dump_only=True) # 表示為單個物件的樣子
    
    