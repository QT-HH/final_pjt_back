import requests
from urllib.parse import urlparse
import json

class URLMaker():

    # 네이버 오픈API 이용
    url = 'https://api.themoviedb.org/3/movie/popular?api_key=22d75ec27e1fc0e7b3cf07ba02bcb1d5'

# 

    # 인스턴스 생성과 함께 id, password, 검색어 설정
    def __init__(self,page):
        self.page = page

    # 기본 url 설정
    def get_url(self):
        return f'{self.url}language=k&o-KR&page={self.page}'
# {self.query}


def movieInfo(query):

    # 인스턴스 생성
    url_maker = URLMaker(query)
    
    # url 설정
    url = url_maker.get_url()
    # print(url)

    # 데이터 요청후 json파일로 변환
    movies_dict = requests.get(urlparse(url).geturl(),headers={'Authorization':'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMmQ3NWVjMjdlMWZjMGU3YjNjZjA3YmEwMmJjYjFkNSIsInN1YiI6IjVmYjcxMGVlZDNkMzg3MDA0MWQ2NjMyMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.6C2J2vrpLZS8_p2YPsppIbH04RpX3Mt3cqVOQhX2m1I','Content-Type':'application/json;charset=utf-8'})
    movies = movies_dict.json()
    return movies['results']
    

if __name__=='__main__':
    movieData = []
    
    for i in range(1,6):
        x = movieInfo(i)
        for j in range(20):
            data = {}
            data["model"] = "movies.movie"
            data["fields"] = x[j]
            movieData.append(data)

    with open('moviess.json','w',encoding="utf-8") as make_file:
        json.dump(movieData,make_file,ensure_ascii=False,indent="\t")

