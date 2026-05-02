from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from landing.models import YoutubeHistory, GithubHistory
from django.core.paginator import Paginator

def landing_page(request):
	return render(request, "landing.html")

def feed_page(request):
	github_qs = GithubHistory.objects.order_by('-uploaded_at')
	youtube_qs = YoutubeHistory.objects.order_by('-uploaded_at')

	github_paginator = Paginator(github_qs, 4)
	youtube_paginator = Paginator(youtube_qs, 2)

	gh_page_number = request.GET.get('gh_page', 1)
	yt_page_number = request.GET.get('yt_page', 1)

	github_page = github_paginator.get_page(gh_page_number)
	youtube_page = youtube_paginator.get_page(yt_page_number)

	context = {
		'github_page': github_page,
		'youtube_page': youtube_page,
	}
	return render(request, "feed.html", context)

def projects_page(request):
	return render(request, "projects.html")

def contact_page(request):
	return render(request, "contact.html")

def page_not_found(request, exception):
	attempted_url = request.path
	return render(request, "404.html")
