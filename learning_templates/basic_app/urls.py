from django.urls import path,include
from . import views

app_name = 'basic_app'
urlpatterns =[
    path('index/',views.index,name = 'index'),
    path('other/',views.other,name = 'other'),
    path('relurls/',views.relurls,name = 'relurls'),
    
]