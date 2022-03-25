from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Feed, Reply
import os
from uuid import uuid4
from Weddingram.settings import MEDIA_ROOT


def about(request):
    return render(request, 'Weddingram/about.html')

def copyright(request):
    return render(request, 'Weddingram/copyright.html')

def weddingvows(request):
    return render(request, 'Weddingram/weddingvows.html')

def profile(request):
    return render(request, 'Weddingram/profile.html')

def location(request):
    return render(request, 'Weddingram/location.html')

def index(request):
    return render(request, 'Weddingram/index.html')

class Main(APIView):
    def get(self, request):
        feed_object_list = Feed.objects.all().order_by('-id')
        feed_list = []

        for feed in feed_object_list:
            reply_objects_list = Reply.objects.filter(feed_id=feed.id)
            reply_list = []
            for reply in reply_objects_list:
                reply_list.append(dict(feed_id=reply.feed_id,
                                       comment=reply.comment,
                                       writer_id=reply.writer_id
                                       ))
            feed_list.append(dict(id=feed.id,
                                  image=feed.image,
                                  content=feed.content,
                                  tag=feed.tag,
                                  write_date=feed.write_date,
                                  reply_list=reply_objects_list
                                  ))

        return render(request, 'Weddingram/main.html', context=dict(feed_list=feed_list))


class UploadFeed(APIView):
    def post(self, request):
        file = request.FILES['file']
        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)
        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
                content = request.data.get('content')
                image = uuid_name
                tag = request.data.get('tag')

        Feed.objects.create(content=content,
                            image=image,
                            like_count=0,
                            tag=tag)

        return Response(status=200)


class UploadReply(APIView):
    def post(self, request):
        feed_id = request.data.get('feed_id', None)
        writer_id = request.data.get('writer_id', None)
        comment = request.data.get('comment', None)

        Reply.objects.create(feed_id=feed_id, writer_id=writer_id, comment=comment)

        return Response(status=200)