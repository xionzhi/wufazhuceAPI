from flask import request
from flask_restful import Resource

from service import db

from .serializers import PhotoSchema, ArticleSchema, QuestionSchema
from service.models import PhotoModel, ArticleModel, QuestionModel


class PhotoView(Resource):
    def get(self):
        '''
        Photo get
        '''
        try:
            photo_id = request.args.get('id', None, int)
            photo_text = request.args.get('text', None, str)

            if photo_text is not None:
                result_list = db.session.query(PhotoModel.photo_id,
                                               PhotoModel.photo_url,
                                               PhotoModel.photo_date,
                                               PhotoModel.photo_text,
                                               PhotoModel.wufazhuce_url). \
                    filter(PhotoModel.photo_text.like('%{0}%'.format(photo_text))). \
                    limit(10).all()

            if photo_id is not None and photo_text is None:
                result_list = db.session.query(PhotoModel.photo_id,
                                               PhotoModel.photo_url,
                                               PhotoModel.photo_date,
                                               PhotoModel.photo_text,
                                               PhotoModel.wufazhuce_url). \
                    filter(PhotoModel.photo_id == photo_id).first()
                result_list = [result_list]

            result = [PhotoSchema().dump(_).data for _ in result_list]

            return result
        except Exception as e:
            print(e)
            return {'code': 500, 'message': ' server error '}, 500


class ArticleView(Resource):
    def get(self):
        '''
        Article get
        '''
        try:
            article_id = request.args.get('id', None, int)
            article_author = request.args.get('author', None, int)
            article_text = request.args.get('text', None, int)
            article_body = request.args.get('body', None, int)
        except Exception as e:
            print(e)
            return {'code': 500, 'message': ' server error '}, 500


class QuestionView(Resource):
    def get(self):
        '''
        Resource get
        '''
        try:
            question_id = request.args.get('id', None, int)
            question_author = request.args.get('author', None, int)
            question_text = request.args.get('text', None, int)
            question_body = request.args.get('body', None, int)
        except Exception as e:
            print(e)
            return {'code': 500, 'message': ' server error '}, 500
