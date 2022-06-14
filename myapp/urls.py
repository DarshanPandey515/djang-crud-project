from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('adddata',views.adddata, name='adddata'),
    path('deletestudent/<int:id>',views.deletestudent, name='deletestudent'),
    path('edit/<int:id>',views.edit, name='edit'),
    path('search',views.search, name='search'),

]

