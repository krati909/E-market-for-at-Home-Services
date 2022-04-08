from django.db import connection
from django.shortcuts import render

# Create your views here.
def update_cancle(request):
    appointment_id = request.GET['appointment_id']
    name = request.GET['name']
    cursor = connection.cursor()
    query2 = "select * from appointment where appoint_id='" + appointment_id + "'"
    cursor.execute(query2)
    data = cursor.fetchone()
    data = {'appointment_id':data[0] , 'time': data[2], 'date': data[3], 'Address': data[5], 'worker_id': data[4]}
    return render(request, 'update_cancle.html',data)
def update(request):
    appointment_id = request.GET['appointment_id']
    time= request.GET['time']
    date = request.GET['date']
    cursor = connection.cursor()
    query = "update appointment set time=%s,date=%s where appoint_id='" + appointment_id + "'"
    value = (time,date)
    cursor.execute(query, value)
    return render(request,"end_page.html",{'message':"Your appointment has been updated"})
def cancle(request):
    appointment_id= request.GET['appointment_id']
    cursor = connection.cursor()
    query = "delete from appointment where appoint_id='" + appointment_id + "'"
    cursor.execute(query)
    return render(request, "end_page.html",{'message':"Your appointment has been Cancled"})
