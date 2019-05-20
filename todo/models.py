from django.db import models
from django.utils import timezone
# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200,verbose_name='제목')
    content = models.TextField(verbose_name="내용")
    due_date = models.DateField(verbose_name="마감일",null=True,blank=True)
    priority = models.IntegerField(verbose_name="우선순위",default=1)
    success = models.BooleanField(verbose_name="완료",default=False)

    def __str__(self):
        return self.title