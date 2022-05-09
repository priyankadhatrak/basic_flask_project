from flask_marshmallow import Marshmallow
from ...app import app

ma = Marshmallow(app)


class CommentsSchema(ma.Schema):
	class Meta:
		fields=('id','name','comment')

comment_schema=CommentsSchema()
comment_schema=CommentsSchema(many=True)