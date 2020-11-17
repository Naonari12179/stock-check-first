
import datetime
from datetime import  timedelta
from django.db import models
from django.utils import timezone

# Create your models here.
class Categorys(models.Model):
    title = models.CharField('カテゴリー', max_length = 200)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'カテゴリー'
        verbose_name_plural = 'カテゴリー'
        
class お菓子A(models.Model):
    商品名 = models.CharField(max_length=200)
    dis_date = models.DateTimeField('賞味')
    category = models.ForeignKey(Categorys, on_delete=models.PROTECT,default=1)
    
    def __str__(self):
        return self.商品名
    def 賞味期限(self):
        best_by = self.dis_date
        return best_by.date()
    def 見切り1(self):
        sale1 = self.dis_date - timedelta(days=21)
        return sale1.date()
    def 見切り2(self):
        sale2 = self.dis_date - timedelta(days=14)
        return sale2.date()
    def 見切り3(self):
        sale3 = self.dis_date - timedelta(days=7)
        return sale3.date()
    class Meta:
        verbose_name = 'お菓子A'
        verbose_name_plural = 'お菓子A'
class お菓子B(models.Model):
    商品名 = models.CharField(max_length=200)
    dis_date = models.DateTimeField('賞味')
    category = models.ForeignKey(Categorys, on_delete=models.PROTECT,default=1)
    
    def __str__(self):
        return self.商品名
    def 賞味期限(self):
        best_by = self.dis_date
        return best_by.date()
    def 見切り1(self):
        sale1 = self.dis_date - timedelta(days=21)
        return sale1.date()
    def 見切り2(self):
        sale2 = self.dis_date - timedelta(days=14)
        return sale2.date()
    def 見切り3(self):
        sale3 = self.dis_date - timedelta(days=7)
        return sale3.date()
    class Meta:
        verbose_name = 'お菓子B'
        verbose_name_plural = 'お菓子B'

class お菓子C(models.Model):
    商品名 = models.CharField(max_length=200)
    dis_date = models.DateTimeField('賞味')
    category = models.ForeignKey(Categorys, on_delete=models.PROTECT,default=1)
    
    def __str__(self):
        return self.商品名
    def 賞味期限(self):
        best_by = self.dis_date
        return best_by.date()
    def 見切り1(self):
        sale1 = self.dis_date - timedelta(days=21)
        return sale1.date()
    def 見切り2(self):
        sale2 = self.dis_date - timedelta(days=14)
        return sale2.date()
    def 見切り3(self):
        sale3 = self.dis_date - timedelta(days=7)
        return sale3.date()
    class Meta:
        verbose_name = 'お菓子C'
        verbose_name_plural = 'お菓子C'
class 半生お菓子(models.Model):
    商品名 = models.CharField(max_length=200)
    dis_date = models.DateTimeField('賞味')
    category = models.ForeignKey(Categorys, on_delete=models.PROTECT,default=1)
    
    def __str__(self):
        return self.商品名
    def 賞味期限(self):
        best_by = self.dis_date
        return best_by.date()
    def 見切り1(self):
        sale1 = self.dis_date - timedelta(days=10)
        return sale1.date()
    def 見切り2(self):
        sale2 = self.dis_date - timedelta(days=7)
        return sale2.date()
    def 見切り3(self):
        sale3 = self.dis_date - timedelta(days=3)
        return sale3.date()
    class Meta:
        verbose_name = '半生お菓子'
        verbose_name_plural = '半生お菓子'