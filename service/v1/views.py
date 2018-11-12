"""
@Time    : 2018-11-12 16:02:49
@Author  : xionzhi
@File    : views.py
@Software: vscode
"""
from flask import request
from flask_restful import Resource

from service import db, logger

from .serializers import PhotoSchema, ArticleSchema, QuestionSchema
from service.models import PhotoModel, ArticleModel, QuestionModel


class PhotoView(Resource):
    def get(self):
        '''
        Photo get
        '''
        try:
            _photo_id = request.args.get('id', None, int)
            _photo_text = request.args.get('text', None, str)

            if _photo_id is not None:
                result_list = db.session.query(PhotoModel.photo_id,
                                               PhotoModel.photo_url,
                                               PhotoModel.photo_date,
                                               PhotoModel.photo_text,
                                               PhotoModel.wufazhuce_url). \
                    filter(PhotoModel.photo_id == _photo_id).first()

                return [PhotoSchema().dump(_).data for _ in [result_list]]

            if _photo_text is not None:
                result_list = db.session.query(PhotoModel.photo_id,
                                               PhotoModel.photo_url,
                                               PhotoModel.photo_date,
                                               PhotoModel.photo_text,
                                               PhotoModel.wufazhuce_url). \
                    filter(PhotoModel.photo_text.like('%{0}%'.format(_photo_text))). \
                    limit(10).all()
            else:
                result_list = []

            return [PhotoSchema().dump(_).data for _ in result_list]
        except Exception as e:
            logger.error(e)
            return {'code': 500, 'message': ' server error '}, 500

    def post(self):
        '''
        Photo post
        '''
        pass


class ArticleView(Resource):
    def get(self):
        '''
        Article get
        '''
        try:
            _article_id = request.args.get('id', None, int)
            _article_title = request.args.get('title', None, str)
            _article_author = request.args.get('author', None, str)
            _article_text = request.args.get('text', None, str)
            _article_body = request.args.get('body', None, str)

            if _article_id is not None:
                result_list = db.session.query(ArticleModel.article_id,
                                               ArticleModel.article_author,
                                               ArticleModel.article_title,
                                               ArticleModel.article_text,
                                               ArticleModel.article_body). \
                    filter(ArticleModel.article_id == _article_id).first()

                return [ArticleSchema().dump(_).data for _ in [result_list]]

            if _article_title is not None:
                result_list = db.session.query(ArticleModel.article_id,
                                               ArticleModel.article_author,
                                               ArticleModel.article_title,
                                               ArticleModel.article_text,
                                               ArticleModel.article_body). \
                    filter(ArticleModel.article_title.like('%{0}%'.format(_article_title)))
                if _article_author is not None:
                    result_list = result_list.filter(ArticleModel.article_author.like('%{0}%'.format(_article_author)))
                if _article_text is not None:
                    result_list = result_list.filter(ArticleModel.article_text.like('%{0}%'.format(_article_text)))
                if _article_body is not None:
                    result_list = result_list.filter(ArticleModel.article_body.like('%{0}%'.format(_article_body)))
                result_list = result_list.limit(10).all()
            else:
                result_list = []

            return [ArticleSchema().dump(_).data for _ in result_list]
        except Exception as e:
            logger.error(e)
            return {'code': 500, 'message': ' server error '}, 500

    def post(self):
        '''
        Article post
        '''
        pass


class QuestionView(Resource):
    def get(self):
        '''
        Question get
        '''
        try:
            _question_id = request.args.get('id', None, int)
            _question_title = request.args.get('title', None, str)
            _question_text = request.args.get('text', None, str)

            if _question_id is not None:
                result_list = db.session.query(QuestionModel.question_id,
                                               QuestionModel.question_title,
                                               QuestionModel.question_text,
                                               QuestionModel.question_body). \
                    filter(QuestionModel.question_id == _question_id).first()

                return [QuestionSchema().dump(_).data for _ in [result_list]]

            if _question_title is not None:
                result_list = db.session.query(QuestionModel.question_id,
                                               QuestionModel.question_title,
                                               QuestionModel.question_text,
                                               QuestionModel.question_body). \
                    filter(QuestionModel.question_title.like('%{0}%'.format(_question_title)))
                if _question_text is not None:
                    result_list = result_list.filter(QuestionModel.question_text.like('%{0}%'.format(_question_text)))
                result_list = result_list.limit(10).all()
            else:
                result_list = []

            return [QuestionSchema().dump(_).data for _ in result_list]
        except Exception as e:
            logger.error(e)
            return {'code': 500, 'message': ' server error '}, 500

    def post(self):
        '''
        Question post
        '''
        pass


class TestView(Resource):
    def get(self): return {'method': 'get'}, 200

    def post(self): return {'method': 'post'}, 200

    def put(self): return {'method': 'put'}, 201

    def delete(self): return {'method': 'delete'}, 204
