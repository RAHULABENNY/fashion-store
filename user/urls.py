from django.urls import path
from .views import home,login_view,signup_view
urlpatterns = [
  path('',home,name='home'),
  path('login_view/',login_view,name="login"),
  path('signup_view/',signup_view,name="signup")
]
