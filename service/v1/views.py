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
                    filter(PhotoModel.photo_text.like('%{0}%'.format(photo_text))).all()
            else:
                result_list = []
            if photo_id is not None and photo_text is None:
                result_list = db.session.query(PhotoModel.photo_id,
                                               PhotoModel.photo_url,
                                               PhotoModel.photo_date,
                                               PhotoModel.photo_text,
                                               PhotoModel.wufazhuce_url). \
                    filter(PhotoModel.photo_id == photo_id).first()
                result_list = [result_list]

            result = [PhotoSchema().dump(i).data for i in result_list]

            return result
        except Exception as e:
            return {'code': 500, 'message': 'service error'}


class ArticleView(Resource):
    def get(self):
        '''
        Article get
        '''
        article_id = request.args.get('id', None, int)
        article_author = request.args.get('author', None, int)
        article_text = request.args.get('text', None, int)
        article_body = request.args.get('body', None, int)


class QuestionView(Resource):
    def get(self):
        '''
        Resource get
        '''
        pass
