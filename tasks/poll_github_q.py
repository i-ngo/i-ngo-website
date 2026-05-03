from django_q.tasks import async_task
from django.conf import settings
from landing.models import GithubHistory
import requests

def poll():
	url = 'https://api.github.com/search/commits?q=author:i-ngo+is:public&sort=author-date&order=desc&per_page=50'
	headers = {
	"Accept": "application/vnd.github+json",
	"Authorization": f"Bearer {settings.GIT_SECRET}"
	}
	try:
		r = requests.get(url)
		r.raise_for_status()
	except requests.exceptions.RequestException as e:
		print(f"GitHub API Request failed: {e}")
		return

	data = r.json()
	commit_history = []
	
	for commit in data.get("items", []):
		commit_data = commit.get("commit", {})
		commit_author = commit_data.get("author")
		commit_repo = commit.get("repository", {})

		repo_name = commit_repo.get("full_name")
		repo_url = commit_repo.get("html_url")
		commit_url = commit.get("html_url")
		commit_id = commit.get("sha")[:7]
		message = commit_data.get("message")
		uploaded_at = commit_author.get("date")
		
		if not commit_id:
			continue
		
		commit_history.append(
			GithubHistory(
				repo_name=repo_name,
				repo_url=repo_url,
				commit_url=commit_url,
				commit_id=commit_id,
				message=message,
				uploaded_at=uploaded_at
			)
		)

	if commit_data:
		GithubHistory.objects.bulk_create(commit_history, ignore_conflicts=True)
		print(f"Successfully saved {len(commit_history)} commits.")
