from django.conf.urls import url
from account import views

# SET THE NAMESPACE!
app_name = 'account'

urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]