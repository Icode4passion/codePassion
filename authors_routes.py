from flask import Blueprint ,jsonify, make_response
from flask import request
from api.utils.responses import response_with
from api.utils import responses as resp 
from api.models.authors import Author , AuthorSchema 
from api.models.books import Books , BookSchema
from api.utils.database import db


author_routes = Blueprint("author_routes", __name__)



@author_routes.route('/', methods=['POST']) 
def create_author():
    try:     
        data = request.get_json()
        author_schema = AuthorSchema()
        author, error = author_schema.load(data)
        result = author_schema.dump(author.create()).data       
        return response_with(resp.SUCCESS_201, value={"author": result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)


@author_routes.route('/',methods=['GET'])
def get_author_list():
    fetched = Author.query.all()
    author_schema = AuthorSchema(many=True , only=['first_name','last_name','id'])
    authors,error = author_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"authors": authors})

