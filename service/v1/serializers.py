"""
@Time    : 2018-11-12 16:02:49
@Author  : xionzhi
@File    : serializers.py
@Software: vscode
"""
from service import ma

from service.models import PhotoModel, ArticleModel, QuestionModel


class PhotoSchema(ma.ModelSchema):
    class Meta:
        model = PhotoModel


class ArticleSchema(ma.ModelSchema):
    class Meta:
        model = ArticleModel


class QuestionSchema(ma.ModelSchema):
    class Meta:
        model = QuestionModel
