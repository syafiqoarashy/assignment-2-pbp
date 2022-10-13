# TODO: Implement Routings Here
from django.urls import path
from todolist.views import show_todolist
from todolist.views import register
from todolist.views import login_user 
from todolist.views import logout_user
from todolist.views import create_task 
from todolist.views import delete_task
from todolist.views import complete_task
from todolist.views import show_test
from todolist.views import show_data_json

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='todolist'),
    path('test/', show_test, name='test'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('add/', create_task, name='add'),
    path('delete_task/<int:id>', delete_task, name='delete_task_id'),
    path('complete_task/<int:id>', complete_task, name='complete_task_id'),
    path('json/', show_data_json, name='show_data_json'),
]