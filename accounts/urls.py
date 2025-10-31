from django.urls import path
from .views import customer_signup,login_view,logout_view,edit_profile

urlpatterns = [
    path('signup/customer/', customer_signup, name='customer_signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('edit_profile/',edit_profile,name="edit_profile")
]