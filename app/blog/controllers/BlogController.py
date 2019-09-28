from flask import Blueprint, current_app, jsonify, request
from app.blog.models.Model import BlogCategory, BlogPost
from app.blog.schemas.serializer import BlogCategorySchema, BlogPostSchema

bp = Blueprint('blog', __name__, url_prefix='/')


def configure(app):
    app.register_blueprint(bp)


@bp.route('', methods=['GET'])
def index():
    return 'Todos os posts 2'

@bp.route('/<int:id>', methods=['GET'])
def viewPost(id):
    bs = BlogPostSchema()
    query = BlogPost.query.get(id)
    return bs.jsonify(query)

@bp.route('', methods=['POST'])
def newPost():
    data = request.json
    bps = BlogPostSchema()
    newPost = bps.load(data)

    current_app.db.session.add(newPost)
    current_app.db.session.commit()
    
    return bps.jsonify(newPost)


@bp.route('/<int:id>', methods=['PUT'])
def updatePost(id):
    data = request.json
    bs = BlogPostSchema()
    query = BlogPost.query.filter(BlogPost.id == id)
    query.update(data)
       
    current_app.db.session.commit()
    
    
    return bs.jsonify(query.first()), 201


@bp.route('/<int:id>', methods=['DELETE'])
def deletePost(id):
    BlogPost.query.filter(BlogPost.id == id).delete() 
    current_app.db.session.commit()
    return jsonify('Removido com Sucesso!')


@bp.route('/category', methods=['POST'])
def newCategory():
    data = request.json
    bs = BlogCategorySchema()
    category = bs.load(data)

    current_app.db.session.add(category)
    current_app.db.session.commit()
    
    
    return bs.jsonify(category), 201


@bp.route('/category/<int:id>', methods=['PUT'])
def updateCategory(id):
    data = request.json
    bs = BlogCategorySchema()
    query = BlogCategory.query.filter(BlogCategory.id == id)
    query.update(data)
       
    current_app.db.session.commit()    
    return bs.jsonify(query.first()), 201


@bp.route('/category/<int:id>', methods=['DELETE'])
def deleteCategory(id):
    BlogCategory.query.filter(BlogCategory.id == id).delete() 
    current_app.db.session.commit()
    return jsonify('Removido com Sucesso!')
