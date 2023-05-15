from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.apps import apps
import pymysql
from datetime import date
import calendar
from calendar import HTMLCalendar
from quan_li_nong_san.forms import fruitForm
# Create your views here.

def home(request):
    return render(request, 'qlns_views/HomePage.html')

def dangky(request):
    return render(request, 'qlns_views/dangKy.html')

def dangnhap(request):
    return render(request, 'qlns_views/dangNhap.html')

def traicaytuoi(request):
    return render(request, 'qlns_views/traicaytuoi.html')

def sanphamkhac(request):
    return render(request, 'qlns_views/sanphamkhac.html')

def blogvitamin(request):
    return render(request, 'qlns_views/blogvitamin.html')

def contact(request):
    return render(request, 'qlns_views/contact.html')

def cart(request):
    return render(request, 'qlns_views/cart.html')

def fruitsdetail(request):
    return render(request, 'qlns_views/fruitsdetail.html') 

def checkout(request):
    return render(request, 'qlns_views/checkout.html')

def checkoutfn(request):
    return render(request, 'qlns_views/checkoutfn.html')  

#nhacc
def nhaccENVY(request):
    return render(request, 'qlns_views/nhaccENVY.html')

def nhaccNhatBan(request):
    return render(request, 'qlns_views/nhaccNhatBan.html')

def thongke(request):
    return render(request, 'qlns_views/thongke.html')  


# Forms----------------------------------------

def connection():
    s = '127.0.0.1'
    d = 'fruitsales'
    u = 'root'
    p = ''
    conn = pymysql.connect(host=s, user=u, password=p, database=d)
    return conn

def fruitslist(request):
    fruits = []
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Tblfruits")
    for row in cursor.fetchall():
        fruits.append({"id": row[0], "name": row[1], "xuatxu": row[2], "price": row[3]})
    conn.close()
    return render(request, 'qlns_views/fruitslist.html', {'fruits':fruits})

def updatefruit(request, id):
    cr = []
    conn = connection()
    cursor = conn.cursor()
    if request.method == 'GET':
        cursor.execute("SELECT * FROM Tblfruits WHERE id = %s", (id))
        for row in cursor.fetchall():
            cr.append({"id": row[0], "name": row[1], "xuatxu": row[2], "price": row[3]})
        conn.close()
        return render(request, 'qlns_views/addfruit.html', {'fruit':cr[0]})
    if request.method == 'POST':
        form = fruitForm(request.POST)
        if form.is_valid():
            name = str(form.cleaned_data.get("name"))
            xuatxu = str(form.cleaned_data.get("xuatxu"))
            price = float(form.cleaned_data.get("price"))
            cursor.execute("UPDATE Tblfruits SET name = %s, xuatxu = %s, price = %s WHERE id = %s", (name, xuatxu, price, id))
            conn.commit()
        conn.close()
        return redirect('fruitslist')

def addfruit(request):
    if request.method == 'GET':
        return render(request, 'qlns_views/addfruit.html')
    if request.method == 'POST':
        form = fruitForm(request.POST)
    if form.is_valid():
        id = form.cleaned_data.get("id")
        name = form.cleaned_data.get("name")
        xuatxu = form.cleaned_data.get("xuatxu")
        price = form.cleaned_data.get("price")
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Tblfruits (id, name, xuatxu, price) VALUES (%s, %s, %s, %s)", (id, name, xuatxu, price))
    conn.commit()
    conn.close()
    return redirect('fruitslist')

def deletefruit(request, id):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Tblfruits WHERE id = %s", (id))
    conn.commit()
    conn.close()
    return redirect('fruitslist')