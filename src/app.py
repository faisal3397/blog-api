from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from src.database.models import setup_db, Post, Comment
from src.auth.auth import AuthError, requires_auth

POSTS_PER_PAGE = 10


def create_app():
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/posts')
    def get_posts():
        posts = Post.query.all()
        formatted_posts = [post.format() for post in posts]

        page = request.args.get('page', 1, type=int)
        start = (page-1) * POSTS_PER_PAGE
        end = start + POSTS_PER_PAGE

        resulted_posts = formatted_posts[start:end]
        if len(resulted_posts) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'posts': resulted_posts,
            'total_posts': len(formatted_posts)
        })

    @app.route('/posts/<int:post_id>/comments')
    def get_post_comments(post_id):
        comments = Comment.query.filter(Comment.post_id == post_id).all()

        if len(comments) == 0:
            abort(404)

        formatted_comments = [comment.format() for comment in comments]

        return jsonify({
            'success': True,
            'comments': formatted_comments
        })

    @app.route('/posts', methods=['POST'])
    @requires_auth('post:posts')
    def create_post(jwt):
        body = request.get_json()
        title = body.get('title', None)
        date = body.get('date', None)
        content = body.get('content', None)

        if title is None or date is None or content is None:
            abort(400)

        try:
            post = Post(title=title, date=date, content=content)
            post.insert()

            return jsonify({
                'success': True,
                'post': post.format()
            }), 201

        except():
            abort(400)

    @app.route('/posts/<int:post_id>', methods=['PATCH'])
    @requires_auth('patch:posts')
    def update_post(jwt, post_id):
        body = request.get_json()
        title = body.get('title')
        date = body.get('date')
        content = body.get('content')

        try:
            post = Post.query.filter(Post.id == post_id).one_or_none()

            if post is None:
                abort(404)

            post.title = title
            post.date = date
            post.content = content
            post.update()

            return jsonify({
                'success': True,
                'post': post.format()
            })

        except():
            abort(422)

    @app.route('/posts/<int:post_id>', methods=['DELETE'])
    @requires_auth('delete:posts')
    def delete_post(jwt, post_id):

        try:
            post = Post.query.filter(Post.id == post_id).one_or_none()

            if post is None:
                abort(404)

            post.delete()

            return jsonify({
                "success": True,
                "delete": post.id
            })

        except():
            abort(422)

    @app.route('/posts/<int:post_id>/comments', methods=['POST'])
    @requires_auth('post:comments')
    def create_comment(jwt, post_id):
        body = request.get_json()
        date = body.get('date', None)
        content = body.get('content', None)

        if date is None or content is None:
            abort(400)

        try:
            post = Post.query.filter(Post.id == post_id).one_or_none()

            if post is None:
                abort(404)

            comment = Comment(date=date, content=content, post_id=post_id)
            comment.insert()

            return jsonify({
                'success': True,
                'comment': comment.format()
            }), 201

        except():
            abort(400)

    # Error Handling

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad Request"
        }), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Not Found"
        }), 404

    @app.errorhandler(AuthError)
    def auth_error(error):
        return jsonify({
            "success": False,
            "error": error.status_code,
            "message": error.error
        }), error.status_code

    return app


app = create_app()
