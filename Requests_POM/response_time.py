import requests

class response():

    def get_user(self,l):
        r=requests.get(l)
        print(r)