import requests

class userload():

    def get_user(self,l):
        r=requests.get(l)
        print(r)