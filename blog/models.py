from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)  # 카테고리 이름
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)  # 한글 인코딩

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/blog/category/{}'.format(self.slug)

    class Meta:
        verbose_name_plural = "Categories"


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    pub_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    photo = models.ImageField(upload_to='blog/images/%Y/%m/%d/', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    # 카테고리가 삭제되어도 post 유지 / 미분류 가능

    def __str__(self):
        return self.title
