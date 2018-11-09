from service import api

from .views import PhotoView, ArticleView, QuestionView, TestView


api.add_resource(TestView, '/v1')
api.add_resource(PhotoView, '/v1/photo')
api.add_resource(ArticleView, '/v1//article')
api.add_resource(QuestionView, '/v1//question')
