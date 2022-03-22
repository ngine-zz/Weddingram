from django.db import models

# Create your models here.
class Feed(models.Model):
    content = models.TextField() #글내용
    image = models.TextField() #포스트이미지
    user_id = models.TextField() #작성자아이디
    like_count = models.IntegerField() #라이크카운트
    write_date = models.TextField() #콘텐츠작성일
    tag = models.TextField() #태그


class Reply(models.Model):
    feed_id = models.IntegerField(default=0)
    writer_id = models.TextField()
    comment = models.TextField()
