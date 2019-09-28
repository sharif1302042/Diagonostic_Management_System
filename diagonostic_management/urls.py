from django.urls import path
from diagonostic_management import views
urlpatterns = [
    path('home/',views.Home.as_view(), name='home'),
    path('dashboard/',views.Dashboard.as_view(), name='dashboard'),
    path('login/',views.Login.as_view(), name='login'),
    path('signup/',views.SignUp.as_view(), name='signup'),

    path('doctor/list/',views.DoctorList.as_view(), name='doctor/list'),
    path('doctor/details/',views.DoctorDetails.as_view(), name='doctor/details/'),

]
