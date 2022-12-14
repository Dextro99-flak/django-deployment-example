from django.urls import path
from main_app import views


urlpatterns = [
    path('', views.index, name='index_page'),
    path('add', views.add_task, name='add_task'),
    path('delete', views.delete_task, name='delete_task'),
    path('complete/<task_id>', views.complete_task, name='complete_task'),
    path('delete_all', views.delete_all, name='delete_all_tasks'),
    path('register',views.register, name='register_page'),
    path('login',views.user_login, name='login_page'),
    path('logout', views.user_logout, name='logout_page')
]