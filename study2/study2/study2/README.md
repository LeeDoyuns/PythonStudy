<h1>pip 명령어</h1>

1. 크롤링
pip install rest_framework

2. 웹자동화
pip install selenium
pip install web_driver_manager










**
Django project CORS 설정
1) pip install django-cors-headers
2) settings.py의 INSTALLED_APPS 에 corsheaders 추가
3) settings.py의 MIDDLEWARE에  corsheaders.middleware.CorsMiddleware 추가
4) CORS_ORIGIN_WHITELIST = [] 에 허용할 ip와 포트를 추가해준다.
5) 테스트용으로 CORS_ORIGIN_ALLOW_ALL=True 옵션을 주어 모든 도메인을 허용할 수 있다.
