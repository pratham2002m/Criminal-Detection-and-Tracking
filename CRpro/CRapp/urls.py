from django.urls import path
from CRapp import views
from django.contrib.auth import views as auth_views


urlpatterns = [


    # $ection : Others ❤️

    # url for homepage ................................................................................#
    path('',views.index,name="home"), 



    # $ection for police ❤️

    # url for police registration ......................................................................#
    path('register_police/', views.PoliceView.as_view(), name="register_police"),
    # url for police login .......................................................................#
    path('sign_police/', views.sign_police, name="sign_police"),
    # url for police logout .......................................................................#
    path('letsout/', views.letsout, name="letsout"),
    #url for page after police sign in .....................................................................#.
    path('signpg_police/', views.signpg_police, name="signpg_police"),
    # url for profile page of police station................................................................#.
    path('profile_police/', views.profile_police, name="profile_police"),
    # url for police data updation .....................................................................#
    path("update_police_data/", views.update_police_data, name="update_police_data"),

   
     # $ection for criminal ❤️

    # url for criminal adding.................................................................................#
    path('add_criminal/',views.add_criminal,name="add_criminal"),
    # url for criminal data.................................................................................#
    path('show_criminal/',views.show_criminal,name="show_criminal"),
    # url for delete the criminal data...................................................................#
    path('delete/<int:id>/',views.deletedata,name="deletedata"),
    # url for updating the criminal data.......................................................................#
    path('update/<int:id>/',views.updatedata,name="updatedata"),
    # url for searching in criminal data.......................................................................#
    path('search/', views.search, name="search"),





]
