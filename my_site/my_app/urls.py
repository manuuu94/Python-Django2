from django.urls import path
from . import views

#register the app namespace to use the path names in the html.
app_name = 'my_app' 


urlpatterns = [
    #path('',views.index,name='index'), # /my_apps is where it should show when it is later connected, because it was left empty. -->connected to PROJECT level urls.py
    path('index2/',views.index2,name='index2'),  #/my_apps/index2 - no longer empty 
    path('',views.example_view,name='example'),
    path('variable/',views.variable_view,name='variable'),
]





#Views holds the functions. URLS hold the path in the website where the View will show. 