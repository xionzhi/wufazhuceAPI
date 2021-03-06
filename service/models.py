"""
@Time    : 2018-11-12 16:02:49
@Author  : xionzhi
@File    : models.py
@Software: vscode
"""
from service import db

from sqlalchemy.dialects.mysql import INTEGER, TEXT


class PhotoModel(db.Model):
    __tablename__ = 'wufazhuce_photo'

    photo_id = db.Column(INTEGER, primary_key=True)
    photo_url = db.Column(TEXT)
    photo_date = db.Column(TEXT)
    photo_text = db.Column(TEXT)
    wufazhuce_url = db.Column(TEXT)


class ArticleModel(db.Model):
    __tablename__ = 'wufazhuce_article'

    article_id = db.Column(INTEGER, primary_key=True)
    article_title = db.Column(TEXT)
    article_author = db.Column(TEXT)
    article_text = db.Column(TEXT)
    article_body = db.Column(TEXT)


class QuestionModel(db.Model):
    __tablename__ = 'wufazhuce_question'

    question_id = db.Column(INTEGER, primary_key=True)
    question_title = db.Column(TEXT)
    question_text = db.Column(TEXT)
    question_body = db.Column(TEXT)
