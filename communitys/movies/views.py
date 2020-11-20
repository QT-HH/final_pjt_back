from django.shortcuts import render
from .models import Movie

# Create your views here.
import requests
from urllib.parse import urlparse
import json

class URLMaker():

    # 네이버 오픈API 이용
    url = 'https://openapi.naver.com/v1/search/movie.json?query='

# 

    # 인스턴스 생성과 함께 id, password, 검색어 설정
    def __init__(self,id,password,query):
        self.id = id
        self.password = password
        self.query = query

    # 기본 url 설정
    def get_url(self):
        return f'{self.url}{self.query}&yearfrom=2020&yearto=2020&display=100'
# {self.query}


def movieInfo(query):

    # 인스턴스 생성
    url_maker = URLMaker('sztT9GeLp64_NwCad2qv','WUwOdxU8Sa',query)
    
    # url 설정
    url = url_maker.get_url()
    print(url)

    # 데이터 요청후 json파일로 변환
    movies_dict = requests.get(urlparse(url).geturl(),headers={'X-Naver-Client-Id':url_maker.id,'X-Naver-Client-Secret':url_maker.password})
    movies = movies_dict.json().get('items')
    
    for movie in movies:
        Movie.title = movie['title']
        Movie.link = movie['link']
        Movie.image = movie['image']
        Movie.subtitle = movie['subtitle']
        Movie.pudDate = movie['pudDate']
        Movie.director = movie['director']
        Movie.actor = movie['actor']
        Movie.userRating = movie['userRating']

        Movie.save()

