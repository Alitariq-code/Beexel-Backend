from django.urls import path
from rest_framework.routers import DefaultRouter
from .viewsets import EnrollViewSet, ContactUsViewSet, BlogViewSet

router = DefaultRouter()
router.register('enroll', EnrollViewSet, basename='enroll')
router.register('contactus', ContactUsViewSet, basename='contactus')
router.register('blog', BlogViewSet, basename='blog')


urlpatterns = router.urls