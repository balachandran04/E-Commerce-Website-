from django.urls import path
from home import views
urlpatterns=[
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login_page,name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('Collections/', views.Collections, name='Collections'),
    path('Collections/<str:name>', views.Collectionsview, name='Collections'),
    path('Collections/<str:cname>/<str:pname>', views.product_details, name='product_details'),
    path('addtocart/', views.add_to_cart, name='addtocart'),

]