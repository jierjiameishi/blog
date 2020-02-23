from django.db import models
from django.utils import timezone


class Comment(models.Model):
    name = models.CharField('名字', max_length=50)
    email = models.EmailField('邮箱')
    url = models.URLField('网址', blank=True)
    text = models.TextField('内容')
    created_time = models.DateTimeField('创建时间', default=timezone.now)
    post = models.ForeignKey('jier.Post', verbose_name='文章', on_delete=models.CASCADE)
    # 由于一篇文章可以又多个评论，但是一个评论只能属于一篇文章，所以采用 ForeignKey，即一对多。

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
        ordering = ['-created_time']

    def __str__(self):
        return '{}: {}'.format(self.name, self.text[:20])
# Create your models here.
