from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    ## owner
    path('ownerIndex/', views.ownerIndex, name='ownerIndex'),
    path('ownerUpdate/', views.ownerUpdate, name='ownerUpdate'),
    path('ownerNewRequest/', views.ownerNewRequest, name='ownerNewRequest'),
    # path('ownerRequest/<int:request_id>/', views.ownerRequest, name='currentRequst'),
    path('ownerCurrentRequest/', views.ownerCurrentRequest, name='ownerCurrentRequest'),
    path('ownerCurrentRequest/<int:request_id>/delete/', views.requestDelete, name='requestDelete'),
    path('ownerCurrentRequest/<int:request_id>/edit/', views.requestEdit, name='requestEdit'),
]
