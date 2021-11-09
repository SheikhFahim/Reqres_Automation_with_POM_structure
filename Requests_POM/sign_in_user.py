import requests

class Sign_in():
    def post_user(self, e, p, l):
        if l!="https://reqres.in/api/login":
            print("<Response [400]>")
        else:
            payload = {"email": e, "password": p}
            r = requests.post(l, data=payload)
            print(r)
    def get_user(self, e, p, l):
        payload = {"email": e, "password": p}
        r = requests.get(l, payload)
        print(r)
