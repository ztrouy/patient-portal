from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from gondorapi.views import AuthViewSet, UserViewSet, StateViewSet, AppointmentViewSet, AddressViewSet, RecordViewSet

router = routers.DefaultRouter(trailing_slash=False)

router.register(r"users", UserViewSet, "user")
router.register(r"states", StateViewSet, "state")
router.register(r"appointments", AppointmentViewSet, "appointment")
router.register(r'addresses', AddressViewSet, 'address')
router.register(r"records", RecordViewSet, 'record')

urlpatterns = [
    path('', include(router.urls)),
    path("register", AuthViewSet.as_view({"post": "register_patient"}), name="register"),
    path("login", AuthViewSet.as_view({"post": "login"}), name="login"),
    path("me", AuthViewSet.as_view({"post": "authenticate_user"}), name="me"),
]

