import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy


from src.app import create_app
from src.database.models import setup_db, Post, Comment


class BlogTestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "blog_test"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_post = {
            "title": "My New Post 3",
            "date": "Tue, 08 Dec 2020 15:53:58 GMT",
            "content": "Lorem ipsum dolor sit amet,"
        }

        self.bad_request_post = {
            "content": "Lorem ipsum dolor sit amet,"
        }

        self.updated_post = {
            "title": "Modified title 123",
            "date": "Tue, 08 Dec 2020 16:53:58 GMT",
            "content": "Modified content 1232341242"
        }

        self.comment = {
            "content": "Hi your post #3 is great",
            "date": "Tue, 08 Dec 2020 16:02:48 GMT"
        }

        self.bad_request_comment = {
            "date": "Tue, 08 Dec 2020 16:02:48 GMT"
        }

        self.blog_owner_token = os.environ["BLOG_OWNER_TOKEN"]
        self.auth_user_token = os.environ["AUTH_USER_TOKEN"]

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_create_new_post(self):
        headers = {'Authorization': 'Bearer {}'.format(self.blog_owner_token)}
        res = self.client().post('/posts', json=self.new_post, headers=headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 201)
        self.assertTrue(data["post"])
        self.assertEqual(data["success"], True)

    # Auth User is not allowed to create post
    def test_create_new_post_as_auth_user(self):
        headers = {'Authorization': 'Bearer {}'.format(self.auth_user_token)}
        res = self.client().post('/posts', json=self.new_post, headers=headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data["error"], 401)
        self.assertEqual(data["success"], False)

    def test_create_new_post_bad_request(self):
        headers = {'Authorization': 'Bearer {}'.format(self.blog_owner_token)}
        res = self.client().post('/posts', json=self.bad_request_post, headers=headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data["error"], 400)
        self.assertEqual(data["message"], "Bad Request")
        self.assertEqual(data["success"], False)

    def test_create_comment(self):
        headers = {'Authorization': 'Bearer {}'.format(self.blog_owner_token)}
        res = self.client().post('/posts/3/comments', json=self.comment, headers=headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 201)
        self.assertTrue(data["comment"])
        self.assertEqual(data["success"], True)

    def test_create_comment_bad_request(self):
        headers = {'Authorization': 'Bearer {}'.format(self.blog_owner_token)}
        res = self.client().post('/posts/3/comments', json=self.bad_request_comment, headers=headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data["error"], 400)
        self.assertEqual(data["message"], "Bad Request")
        self.assertEqual(data["success"], False)

    def test_get_all_posts(self):
        res = self.client().get('/posts')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["posts"])

    def test_get_all_posts_not_found(self):
        res = self.client().get('/post')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["error"], 404)
        self.assertEqual(data["message"], "Not Found")
        self.assertEqual(data["success"], False)

    def test_get_all_post_comments(self):
        res = self.client().get('/posts/3/comments')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["comments"])

    def test_get_all_post_comments_not_found_404(self):
        res = self.client().get('/posts/3000/comments')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["error"], 404)
        self.assertEqual(data["message"], "Not Found")
        self.assertEqual(data["success"], False)

    def test_update_post(self):
        headers = {'Authorization': 'Bearer {}'.format(self.blog_owner_token)}
        res = self.client().patch('/posts/3', json=self.updated_post, headers=headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["post"])
        self.assertEqual(data["success"], True)

    def test_update_post_not_found(self):
        headers = {'Authorization': 'Bearer {}'.format(self.blog_owner_token)}
        res = self.client().patch('/posts/3000', json=self.updated_post, headers=headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["error"], 404)
        self.assertEqual(data["message"], "Not Found")
        self.assertEqual(data["success"], False)

    def test_delete_post(self):
        headers = {'Authorization': 'Bearer {}'.format(self.blog_owner_token)}
        res = self.client().delete('/posts/11', headers=headers)
        data = json.loads(res.data)

        post = Post.query.filter(Post.id == 6).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["delete"])
        self.assertEqual(data["success"], True)
        self.assertEqual(post, None)

    def test_delete_post_not_found(self):
        headers = {'Authorization': 'Bearer {}'.format(self.blog_owner_token)}
        res = self.client().delete('/posts/1000', headers=headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["error"], 404)
        self.assertEqual(data["message"], "Not Found")
        self.assertEqual(data["success"], False)

    # Auth User is not allowed to delete post
    def test_delete_post_as_auth_user(self):
        headers = {'Authorization': 'Bearer {}'.format(self.auth_user_token)}
        res = self.client().delete('/posts/11', headers=headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data["error"], 401)
        self.assertEqual(data["success"], False)


if __name__ == "__main__":
    unittest.main()
