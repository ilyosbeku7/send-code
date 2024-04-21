from django.urls import path
from .views import send_otp, verifiy_otp

urlpatterns=[
    path('register/', send_otp, name='register/'),
    path('verify/', verifiy_otp, name='verifiy_otp/')
]

