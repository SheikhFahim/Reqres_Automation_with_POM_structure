import requests

class updateuser():

    def update_user(self,e,p,l):
        payload = {"name": e, "job": p}
        r=requests.put(l,data=payload)
        print(r)