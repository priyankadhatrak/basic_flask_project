from ..model.comments_info import Comments
from ..validation.schemas.comments_schema import CommentsSchema,comment_schema
from flask import jsonify,request

def get_data():
    dets = Comments.allQuery()
    alldets = comment_schema.dumps(dets)
    return jsonify(alldets)


def add_data(signature):
    newEntry = Comments(signature.id, signature.name, signature.comment)
    Comments.add(newEntry)
    Comments.save()

def update_data(data_update):
    update_data=Comments.singleQuery(data_update.id)
	
    name=request.json['name']
    comment=request.json['comment']
    update_data.name=name
    update_data.comment=comment
    Comments.save()
    
def delete_data(data_del):
    del_data =Comments.singleQuery(data_del.id)
    Comments.delete(del_data)
    Comments.save()
