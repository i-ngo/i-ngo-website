from django.urls import path
from . import views

urlpatterns = [
	path("", views.landing_page, name="landing"),
	path("feed/", views.feed_page, name="feed"),
	path("projects/", views.projects_page, name="projects"),
	path("contact/", views.contact_page, name="contact"),
]
