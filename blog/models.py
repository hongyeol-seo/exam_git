from django.db import models


class Post(models.Model):
    # 데이터베이스의 필드(컬럼): 최대 길이가 30

    title = models.CharField(max_length=30)
    
    # content = models.TextField()
    # # created_at = models.DateTimeField()
    images = models.ImageField(blank=True, upload_to="images", null=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return f"[{self.pk}] {self.title} {self.updated_at}"
    # #시간 포멧에서 날려보기

    # def get_absolute_url(self):
    #     return f'/blog/{self.pk}/'