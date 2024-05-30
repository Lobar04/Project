from django.urls import path
from rest_framework import routers

from users.views import InformationForMainPageVIewSet
from .views import ContactCreateView


router = routers.DefaultRouter()
router.register(r'info-main-page', InformationForMainPageVIewSet)
urlpatterns = [
    path('contact/', ContactCreateView.as_view()),
]

urlpatterns += router.urls
