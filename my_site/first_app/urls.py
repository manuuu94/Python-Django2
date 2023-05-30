from django.urls import path #used t send the urls path
from . import views #looks into the app views folder

#these will all have /first_app/ in their path, before whatever is added here, because of the main project's URL path that we established. 
urlpatterns = [
    path('simple_view/',views.simple_view),
    path('sports/',views.sports_view),
    path('finance/',views.finance_view),
    #path('',views.home_view),
    path('<int:num_page>',views.num_page_view),
    path('<str:topic>/',views.news_views,name="topic-page"), #dynamic routing - a path converter will make sure the argument is X type. for example: <str:topic>/
    #path('<int:num1>/<int:num2>/',views.add_view), #uses path converter to make sure the argument in the path are INT
    path("",views.html_view),
    #path("test/",views.html_view2),

]





