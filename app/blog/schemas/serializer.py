from marshmallow import fields, validates, ValidationError
from flask_marshmallow import Marshmallow
from app.blog.models.Model import BlogPost, BlogCategory

ma = Marshmallow()


def configure(app):
    ma.init_app(app)

class BlogCategorySchema(ma.ModelSchema):
    class Meta:
        model = BlogCategory

    name = fields.Str(required=True)


class BlogPostSchema(ma.ModelSchema):
    class Meta:
        model = BlogPost

    category_id = fields.Int(required=True)
    title = fields.Str(required=True)
    text = fields.Str(required=True)
    
