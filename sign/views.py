import warnings

from django.core.checks import messages
from django.db import connection
from django.shortcuts import render, redirect

import warnings
# Create your views here.



def signup_login(request):
    return render(request, 'login_signup.html')

def signup(request):
    name = request.POST.get("name")
    psw = request.POST.get("psw")
    email = request.POST.get("email")
    mobile = request.POST.get("mob")
    address = request.POST.get("address")
    cursor = connection.cursor()
    query1 = "select * from users where email='" + email + "'"
    cursor.execute(query1)
    data = cursor.fetchone()
    if data is not None:
        return redirect('signup')                     ####### Need to improve
    else:
        query = "insert into users (Name,Contact_number,Address,Email,password) values (%s,%s,%s,%s,%s)"
        value = (name,mobile,address,email ,psw)
        cursor.execute(query, value)
        return render(request, 'index.html', data)
def signin(request):
    psw = request.POST.get("psw")
    email = request.POST.get("email")
    cursor = connection.cursor()
    query1 = "select * from users where Email='" + email + "'"
    cursor.execute(query1)
    data = cursor.fetchone()
    query2 = "select * from appointment where User_id='" + str(data[0]) + "'"
    cursor.execute(query2)
    data1 = cursor.fetchone()
    if data[5]==psw:
        data= {'User_Id':data[0],'Name':data[1],'Contact_number':data[2],'Address':data[3],'Email':data[4],'Password':data[5],'appoint_Id':data1[0],'User_id':data1[1],'time':data1[2],'date':data1[3],'worker_id':data[4],'address':data1[5]}
        return render(request,'profile.html',data)
    else:
        warnings.warn("warning message:'Email/Password is Incorrect'")
        return redirect('signup_login')
