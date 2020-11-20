import requests

class URLMaker:
    
    url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest'
    key = '806e107dcaa31879ec24d5a00b8ddc99'  # api key


    def __init__(self, key):
        self.key = key


    def get_url(self, category='boxoffice', feature='searchWeeklyBoxOfficeList'):
        return f'{self.url}/{category}/{feature}.json?key={self.key}'   



def filmo_count(people, movie):
    url_maker = URLMaker('806e107dcaa31879ec24d5a00b8ddc99')
    url = url_maker.get_url('people', 'searchPeopleList')
    # return url

    payload = {
        'peopleNm' : people,
        'filmoNames' : movie
    }

    r = requests.get(url, params=payload)
    movies_dict = r.json()
    print(movies_dict)
    movies_dict.get("peopleListResult").get("peopleList")

    moviedata = movies_dict.get("peopleListResult").get("peopleList")
    for i in moviedata:
        movielist = i.get('filmoNames').split('|')
        return len(movielist)



if __name__ == '__main__':
     # 배우 이름과 작품을 이용하여 총 해당 배우가 몇 작품에 출연했는지 출력합니다.
     print(filmo_count('다우니', '아이언맨'))

