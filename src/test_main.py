import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from .main import create_app
from .database.models import setup_db, Post, Comment


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

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass


if __name__ == "__main__":
    unittest.main()
