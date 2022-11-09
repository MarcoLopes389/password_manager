import json

from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.request import HttpRequest
from rest_framework.response import Response

from .errors import ValidationError
from .models import Password, User
from .services import offuscator
from .validators import password_validator


@api_view(['GET', 'DELETE'])
@parser_classes([JSONParser])
def one_user(request: HttpRequest, id: int):
    if request.method == 'GET':
        return Response(data=User.objects.all().filter(pk=id).values(), status=200)
    
    User.objects.filter(pk=id).delete()
    return Response(status=203)

@api_view(['GET'])
@parser_classes([JSONParser])
def all_users(request: HttpRequest):
    users = User.objects.values()
    print(users)
    return Response(data=users, status=200)

@api_view(['POST'])
@parser_classes([JSONParser])
def create_user(request: HttpRequest):
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
    

@api_view(['POST'])
def create_password(request: HttpRequest):
    if not request.body:
        return Response(status=400)
    body = json.loads(request.body)

    try:
        password_validator(body)
    except ValidationError as e:
        print(e)
        return Response(status=400, data={'error': True, 'message': e.message})

    user = User.objects.filter(pk=body['owner']).get()

    if not user:
        return Response(status=400, data={'error': True, 'message': 'User not exists'})

    password = Password()

    password.value = offuscator(body['password'])
    password.expires = body['expires']
    password.owner = user

    password.save()

    return Response(status=201)


