# -*- coding: utf-8 -*-
from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class Globe_info(models.Model):
    company_name = models.CharField(max_length=50, verbose_name='公司名称')
    phone = models.CharField(max_length=20, verbose_name='联系电话', blank=True, null=True)
    fax = models.CharField(max_length=20, verbose_name='传真号码', blank=True, null=True)
    address = models.CharField(max_length=100, verbose_name='地址', blank=True, null=True)
    banner_pic1 = models.ImageField(upload_to='pics', verbose_name='轮播图片1', blank=True, null=True)
    banner_pic2 = models.ImageField(upload_to='pics', verbose_name='轮播图片2', blank=True, null=True)
    banner_pic3 = models.ImageField(upload_to='pics', verbose_name='轮播图片3', blank=True, null=True)
    banner_pic4 = models.ImageField(upload_to='pics', verbose_name='轮播图片4', blank=True, null=True)
    banner_pic5 = models.ImageField(upload_to='pics', verbose_name='轮播图片5', blank=True, null=True)

    def __str__(self):
        return self.company_name
    class Meta:
        verbose_name = '网站信息'
        verbose_name_plural = verbose_name


class Single_page(models.Model):
    single_page_url = models.CharField(max_length=50, unique=True, verbose_name='单页URL')
    single_page_title = models.CharField(max_length=50, verbose_name='标题')
    single_page_pic = models.ImageField(upload_to='pics', verbose_name='图片', blank=True, null=True)
    single_page_intro = HTMLField(verbose_name='内容简介', blank=True, null=True)
    single_page_content = HTMLField(verbose_name='内容正文')
    single_page_date = models.DateTimeField(verbose_name='添加时间')

    def __str__(self):
        return self.single_page_title
    class Meta:
        verbose_name = '管理单页内容'
        verbose_name_plural = verbose_name

class News_class(models.Model):
    news_class_name = models.CharField(max_length=50, verbose_name='新闻分类')
    news_class_parent = models.ForeignKey('self', verbose_name='上级分类', blank=True, null=True)
    news_class_pic = models.ImageField(upload_to='pics', verbose_name='图片', blank=True, null=True)
    news_class_intro = HTMLField(verbose_name='分类简介', blank=True, null=True)

    def __str__(self):
        return self.news_class_name
    class Meta:
        verbose_name = '管理新闻分类'
        verbose_name_plural = verbose_name

class News_content(models.Model):
    news_content_class = models.ForeignKey(News_class, verbose_name='所属分类')
    news_content_title = models.CharField(max_length=100, verbose_name='新闻标题')
    news_content_intro = HTMLField(verbose_name='内容简介', blank=True, null=True)
    news_content_pic = models.ImageField(upload_to='pics', verbose_name='图片', blank=True, null=True)
    news_content_content = HTMLField(verbose_name='正文')
    news_content_order = models.IntegerField(verbose_name='排序', default=0)
    news_content_show = models.BooleanField(verbose_name='是否显示', default=True)
    news_content_rec = models.BooleanField(verbose_name='是否推荐')
    news_content_date = models.DateTimeField(verbose_name='添加时间')

    def __str__(self):
        return self.news_content_title
    class Meta:
        verbose_name = '管理新闻内容'
        verbose_name_plural = verbose_name
        ordering = ['news_content_order', '-news_content_date']


class Product_class(models.Model):
    product_class_name = models.CharField(max_length=100, verbose_name='产品分类')
    product_class_parent = models.ForeignKey('self', verbose_name='上级分类', blank=True, null=True, default=0)
    product_class_pic = models.ImageField(upload_to='pics', verbose_name='图片', blank=True, null=True)
    product_class_intro = HTMLField(verbose_name='简介', blank=True, null=True)

    def __str__(self):
        return self.product_class_name
    class Meta:
        verbose_name = '管理产品分类'
        verbose_name_plural = verbose_name


class Product_content(models.Model):
    product_content_class = models.ManyToManyField(Product_class, verbose_name='所属分类')
    product_content_name = models.CharField(max_length=100, verbose_name='产品名称')
    product_content_spec = models.CharField(max_length=100, verbose_name='产品规格', blank=True, null=True)
    product_content_price = models.CharField(max_length=100, verbose_name='产品价格', blank=True, null=True)
    product_content_order = models.IntegerField(verbose_name='排序', default=0)
    product_content_intro = HTMLField(verbose_name='产品简介')
    product_content_pic = models.ImageField(upload_to='pics', verbose_name='图片', blank=True, null=True)
    product_content_content = HTMLField(verbose_name='详细内容', blank=True, null=True)
    product_content_show = models.BooleanField(verbose_name='是否显示', default=True)
    product_content_rec = models.BooleanField(verbose_name='是否推荐', default=True)
    product_content_new = models.BooleanField(verbose_name='最新产品', default=True)
    product_content_date = models.DateTimeField(verbose_name='添加时间')

    def __str__(self):
        return self.product_content_name
    class Meta:
        verbose_name = '管理产品内容'
        verbose_name_plural = verbose_name
        ordering = ['product_content_order', '-product_content_date']


class message(models.Model):
    message_name = models.CharField(max_length=100, verbose_name='姓名')
    message_phone = models.CharField(max_length=100, verbose_name='电话')
    message_qq = models.CharField(max_length=100, verbose_name='QQ')
    message_mail = models.CharField(max_length=100, verbose_name='邮箱')
    message_content = models.TextField(verbose_name='留言内容')
    message_date = models.CharField(max_length=100, verbose_name='留言时间')

    def __str__(self):
        return self.message_name
    class Meta:
        verbose_name = '留言'
        verbose_name_plural = verbose_name
        ordering = ['-message_date', '-id']
