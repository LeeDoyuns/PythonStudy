from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
# from .api.config.serializeable import QuestionSerializer as question
from .models import Question,Choice
from rest_framework.permissions import AllowAny

# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
def index(request):
    pass
    # objt = question(data = request.data)
    # if(objt.is_valid()):
    #     objt.save();
    # print(Question.objects.all())
    # return HttpResponse(objt.data)