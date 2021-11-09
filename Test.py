from Requests_POM.sign_up_user import Sign_up
from Requests_POM.sign_in_user import Sign_in
from Requests_POM.list_users import listuser
from Requests_POM.user_load import userload
from Requests_POM.create_user import createuser
from Requests_POM.update_user import updateuser

print ("###STARTING USER SIGNUP API###")
###########################################################################API 2 STARTS HERE########################################################################

s=Sign_up()
s.post_user("eve.holt@reqres.in","pistol","https://reqres.in/api/register")
s.get_user("eve.holt@reqres.in","pistol","https://reqres.in/api/users/23")
s.post_user("asdssad@sadas","pistol","https://reqres.in/api/register")
s.post_user("peter@klaven","sdadasd","https://reqres.in/api/register")
s.post_user("peter@klaven","","https://reqres.in/api/register")
s.post_user("peter@klaven","","https://reqres.in/api/register")


print ("###STARTING USER LOGIN API###")
###########################################################################API 2 STARTS HERE########################################################################

q=Sign_in()

q.post_user("eve.holt@reqres.in","cityslicka","https://reqres.in/api/login")
q.post_user("eve.holtSADAin","cityslicka","https://reqres.in/api/login")
q.post_user("eve.holt@reqres.in","citysASDAASa","https://reqres.in/api/login")
q.post_user("eve.holt@reqres.in","","https://reqres.in/api/login")
q.get_user("eve.holt@reqres.in","pistol","https://reqres.in/api/unknown/23")

q.post_user("eve.holt@reqres.in","pistol","")


print ("###STARTING USER LIST###")
###########################################################################API 3 STARTS HERE########################################################################

u=listuser()

u.listget("https://reqres.in/api/users?page=2")

print ("###STARTING USER LOAD##")
###########################################################################API 4 STARTS HERE########################################################################

k=userload()
k.get_user("https://reqres.in/api/users/2")

print ("###STARTING USER CREATE##")
###########################################################################API 5 STARTS HERE########################################################################

v=createuser()
v.create_user("morpheus","leader","https://reqres.in/api/users")
v.create_user("","leader","https://reqres.in/api/users")

print ("###STARTING USER UPDATE##")
###########################################################################API 6 STARTS HERE########################################################################

i=updateuser()
i.update_user("morpheus","zion resident","https://reqres.in/api/users/2")

print ("###STARTING DELAY TIME##")
###########################################################################API 7 STARTS HERE########################################################################


t=userload()
t.get_user("https://reqres.in/api/users?delay=3")






