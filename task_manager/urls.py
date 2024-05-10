from django.urls import path
from .import views 

app_name = 'task_manager'

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/login/', views.login_view, name='login_view'),
    path('update_task/<int:id>/', views.update_task, name='update_task'),  

]
