from django.conf import settings
from landing.models import YoutubeHistory
import requests

def poll():
    url = f'https://youtube.googleapis.com/youtube/v3/activities?part=snippet%2CcontentDetails&channelId={settings.YOUTUBE_CHANNEL}&maxResults=25&key={settings.YOUTUBE_SECRET}'
    
    try:
        r = requests.get(url)
        r.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"YouTube API Request failed: {e}")
        return

    data = r.json()
    video_data = []
    
    for video in data.get("items", []):
        snippet = video.get("snippet", {})
        content_details = video.get("contentDetails", {})
        
        if snippet.get("type") != "upload":
            continue
            
        title = snippet.get("title")
        
        upload_data = content_details.get("upload", {})
        video_id = upload_data.get("videoId")
        
        if not video_id:
            continue
            
        thumbnails = snippet.get("thumbnails", {})
        thumb_obj = (
            thumbnails.get("maxres") or 
            thumbnails.get("high") or 
            thumbnails.get("medium") or 
            thumbnails.get("default", {})
        )
        thumbnail_url = thumb_obj.get("url", "")
        
        uploaded_at = snippet.get("publishedAt")
        
        video_data.append(
            YoutubeHistory(
                title=title,
                video_id=video_id,
                thumbnail_url=thumbnail_url,
                uploaded_at=uploaded_at
            )
        )

    if video_data:
        YoutubeHistory.objects.bulk_create(video_data, ignore_conflicts=True)
        print(f"Successfully saved {len(video_data)} videos.")
