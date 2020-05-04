from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseNotFound


# Create your views here.
from tweets.models import Tweet


def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, "pages/home.html", context={}, status=200)


def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweets_list = [{"id": x.id, "content": x.content} for x in qs]
    print(tweets_list)

    data = {
        "response": tweets_list
    }
    return JsonResponse(data)


def tweet_detail_view(request, tweet_id, *args, **kwargs):
    data = {
        "id": tweet_id,
        # "content": obj.content,
        # "image_path": obj.image.url
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data["content"] = obj.content
    except:
        # return HttpResponseNotFound('<h1>Page not found</h1>')
        data['message'] = 'Not found'
        status = 404
    # return HttpResponse(f"<h1>Hello {tweet_id} - {obj.content}</h1>")

    return JsonResponse(data, status=status)
