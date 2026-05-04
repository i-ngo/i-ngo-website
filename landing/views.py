from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from landing.models import YoutubeHistory, GithubHistory, Project
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
	project_qs = Project.objects.order_by('-id')
	
	project_paginator = Paginator(project_qs, 9)
	
	prj_page_number = request.GET.get('project_page', 1)
	
	project_page = project_paginator.get_page(prj_page_number)
	
	context = {
		"project_page": project_page,
	}
	return render(request, "projects.html", context)

def contact_page(request):
	return render(request, "contact.html")

def page_not_found(request, exception=None):
    return render(request, "404.html", status=404)
