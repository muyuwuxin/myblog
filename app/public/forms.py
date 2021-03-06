#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length
from flaskckeditor import CKEditor
from flask_pagedown.fields import PageDownField


class PostForm(FlaskForm, CKEditor):
    title = StringField(label="标题", validators=[DataRequired(),
                                                Length(min=5, max=50, message='标题必须字数在5与20之间!')],
                        render_kw={"required": "required"})
    style = SelectField('类型', coerce=str)
    category = SelectField('分类', coerce=str)
    tags = StringField(label='文章标签')
    body = TextAreaField(label="正文", validators=[DataRequired(),
                                                 Length(min=10, message='文章内容必须大于10个字!')],
                         render_kw={"required": "required"})
    submit = SubmitField('发表', render_kw={'class': "btn btn-info btn-block"})


class CommentForm(FlaskForm):
    body = PageDownField(label='评论', validators=[DataRequired(),
                                                 Length(min=5, message='评论内容必须大于5个字!')],
                         render_kw={"required": "required"})
    submit = SubmitField(render_kw={'class': "btn btn-info btn-block"})


class SearchForm(FlaskForm):
    search = StringField('search', validators=[DataRequired("请输入一个关键词")])
