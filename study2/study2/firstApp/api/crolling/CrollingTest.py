from rest_framework.decorators import api_view,permission_classes
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from rest_framework import status
from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests
from ...models import Question



#내부망 이슈로 테스트 못함.....
@api_view(['GET'])
def colTest(req): 
    html = requests.get('https://search.naver.com/search.naver?query=날씨', verify=False) 
    # pprint(html.text)
    
    soup = bs(html.text, 'html.parser')
    data1 = soup.find('ul', {'class':'today_chart_list'} )
    # pprint(data1)
    data2 = data1.findAll('li')
    # pprint(data2)
    el1 = data2[0] 
    el2 = data2[1]
    el3 = data2[2]
    el4 = data2[3]
    

    
    responseData = {
        el1.find('strong', {'class':'title'}).text : el1.find('span', {'class':'txt'}).text,
        el2.find('strong', {'class':'title'}).text : el2.find('span', {'class':'txt'}).text,
        el3.find('strong', {'class':'title'}).text :  el3.find('span', {'class':'txt'}).text,
        el4.find('strong', {'class':'title'}).text : el4.find('span', {'class':'txt'}).text
    }
    pprint(responseData)

    #json_dumps_params={'ensure_ascii':False} 한글이 아스키코드로 response되는 경우 해당 파라미터를 추가하면 해결됨
    return JsonResponse(responseData, safe=False, json_dumps_params={'ensure_ascii':False}, status = status.HTTP_200_OK)