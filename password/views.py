import json

from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.request import HttpRequest
from rest_framework.response import Response

from .models import User


@api_view(['GET', 'POST'])
@parser_classes([JSONParser])
def user_list(request: HttpRequest):
    if request.method == 'GET':
        return Response(data=User.objects.values(), status=200)
    if request.method == 'POST':
        if not request.body:
            return Response(status=400)

        body = json.loads(request.body)

        user = User()

        try:
            user.nick = body['nick']
            user.name = body['name']
            user.email = body['email']
            user.phone = body['phone']
            user.wordpass = body['wordpass']
            user.save()
        except KeyError:
           return Response(status=400, data={'error': True, 'message': 'Bad Request'})
        except Exception as e:
            raise e

        return Response(status=201)
    
