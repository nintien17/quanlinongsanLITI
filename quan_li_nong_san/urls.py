from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='trangchu'),
    path('dangKy', views.dangky, name='dangKy',),
    path('dangNhap', views.dangnhap, name='dangNhap',),
    path('traicaytuoi', views.traicaytuoi, name='traicaytuoi'),
    path('sanphamkhac', views.sanphamkhac, name='sanphamkhac'),
    path('blogvitamin', views.blogvitamin, name='blogvitamin'),
    path('contact', views.contact, name='contact'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('checkoutfn', views.checkoutfn, name='checkoutfn'),
    path('fruitsdetail', views.fruitsdetail, name='fruitsdetail'),
    path('fruitslist', views.fruitslist, name = 'fruitslist'),
    path('addfruit', views.addfruit, name = 'addfruit'),
    path('thongke', views.thongke, name = 'thongke'),
    path('nhaccENVY', views.nhaccENVY, name = 'nhaccENVY'),
    path('nhaccNhatBan', views.nhaccNhatBan, name = 'nhaccNhatBan'),

    path('updatefruit/<int:id>', views.updatefruit, name = 'updatefruit'),
    path('deletefruit/<int:id>', views.deletefruit, name = 'deletefruit'),
]


