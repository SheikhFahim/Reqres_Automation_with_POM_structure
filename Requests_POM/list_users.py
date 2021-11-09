import requests

class listuser():

    def listget(self,l):
        r=requests.get(l)
        print(r)