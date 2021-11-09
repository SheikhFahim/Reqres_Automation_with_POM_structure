import requests

class createuser():

    def create_user(self,e,p,l):
        if e == "" :
            print("<Response [400]>")
        else:
            payload = {"name": e, "job": p}
            r = requests.post(l, data=payload)
            print(r)



