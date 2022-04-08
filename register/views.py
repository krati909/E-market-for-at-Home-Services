from django.db import connection
from django.shortcuts import render

# Create your views here.
def reg_page(request):
    return render(request, 'registerpro.html')

def register(request):
        name = request.POST.get("workername")
        contact = request.POST.get("contact")
        address = request.POST.get("address")
        email = request.POST.get("email")
        psw = request.POST.get("pswname")
        gender = request.POST.get("gender")
        service = request.POST.get("service")
        cursor = connection.cursor()
        query = "insert into workers (Name,Contact_number,Address,Email,Password,work,gender) values (%s,%s,%s,%s,%s,%s,%s)"
        value = (name, contact, address, email, psw,service,gender)
        cursor.execute(query, value)
        data = cursor.fetchone()
        return render(request, 'end_page.html',{'message':"you have been registered. we will contact you soon"})