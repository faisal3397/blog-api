from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

database_name = 'blog'
database_path = 'postgres://{}/{}'.format('localhost:5432', database_name)

db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    db.create_all()


class Post(db.Model):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    date = Column(DateTime)
    content = Column(String)
    comments = relationship('Comment', cascade='all, delete', passive_deletes=True)

    def __init__(self, title, date, content):
        self.title = title
        self. date = date
        self.content = content

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'date': self.date,
            'content': self.content
        }


class Comment(db.Model):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    content = Column(String)
    post_id = Column(Integer, ForeignKey('posts.id', ondelete='CASCADE'))

    def __init__(self, date, content, post_id):
        self. date = date
        self.content = content
        self.post_id = post_id

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'date': self.date,
            'content': self.content,
            'post_id': self.post_id
        }
