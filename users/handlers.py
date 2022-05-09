import json
from flask import Flask, render_template, request
from .logic.data_comments import get_data,add_data,delete_data,update_data
from users.validation.schemas.comments_schema import CommentsSchema
from users.model.comments_info import Comments
from .app import app
from users import config


@app.route('/home',methods=['GET'])
def index():
	data=get_data()
	return data

@app.route('/sign', methods=["GET"])
def sign():
	return render_template('sign.html')

@app.route('/process', methods=['POST'])
def process():
	id=request.json['id']
	name = request.json['name']
	comment = request.json['comment']

	signature = Comments(id=id,name=name, comment=comment)
	add_data(signature)

	return "Successfully added."

@app.route('/delete/<id>',methods=['DELETE'])
def delete_comment(id):
		data_del=Comments.query.get(id)
		delete_data(data_del)
		
		return 'Successfully Deleted.'

@app.route('/update/<id>',methods=['PUT'])
def update_comment(id):
	data_update=Comments.query.get(id)
	update_data(data_update)
	
	return 'Successfully Updated.'