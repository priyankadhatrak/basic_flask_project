from flask import Flask, jsonify, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from ..app import app

db = SQLAlchemy(app)

class Comments(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20))
	comment = db.Column(db.String(1000))

	def __init__(self,id,name,comment):
		self.id=id
		self.name=name
		self.comment=comment

	def add(data):
		return db.session.add(data)

	def save():
		return db.session.commit()

	def delete(data1):
		return db.session.delete(data1)

	def allQuery():
		return Comments.query.all()

	def singleQuery(id):
		return Comments.query.get(id)