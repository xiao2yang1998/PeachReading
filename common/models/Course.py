# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from app import db


class Course(db.Model):
    __tablename__ = 'setcourse_info'
    scourse_id = db.Column(db.String(15), primary_key=True)
    scourse_title = db.Column(db.String(60), nullable=False, server_default=db.FetchedValue())
    scourse_theme = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue())
    scourse_stage = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue())
    pageimg_urls = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue())
    scourseIntro = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue())
    buylink = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue())
    scourse_credit = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())

