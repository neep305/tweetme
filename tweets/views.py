from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseNotFound


# Create your views here.
from tweets.models import Tweet


def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>Hello World</h1>")


def tweet_detail_view(request, tweet_id, *args, **kwargs):
    try:
        obj = Tweet.objects.get(id=tweet_id)
    except:
        return HttpResponseNotFound('<h1>Page not found</h1>')

    # return HttpResponse(f"<h1>Hello {tweet_id} - {obj.content}</h1>")
    data = {
        "id": tweet_id,
        "content": obj.content,
        # "image_path": obj.image.url
    }

    return JsonResponse(data)
