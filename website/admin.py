# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Globe_info, Single_page, News_class, News_content, Product_class, Product_content, message
# Register your models here.


class Single_page_admin(admin.ModelAdmin):
    list_display = ('single_page_title', 'single_page_url', 'single_page_date')
    search_fields = ('single_page_title',)


class News_class_admin(admin.ModelAdmin):
    list_display = ('news_class_name', 'news_class_parent')


class News_content_admin(admin.ModelAdmin):
    list_display = ('news_content_title', 'news_content_order', 'news_content_class', 'news_content_show', 'news_content_date')
    search_fields = ('news_content_title',)


class Product_class_admin(admin.ModelAdmin):
    list_display = ('product_class_name', 'product_class_parent')


class Product_content_admin(admin.ModelAdmin):
    list_display = ('product_content_name', 'product_content_pic', 'belong_to', 'product_content_order', 'product_content_show', 'product_content_rec', 'product_content_new')
    search_fields = ('product_content_name',)

    def belong_to(self, obj):
        list = ''
        for cate in obj.product_content_class.all():
            list = cate.product_class_name + '，' + list
        return list


class message_admin(admin.ModelAdmin):
    list_display = ('message_name', 'message_phone', 'message_date')


admin.site.register(Globe_info)
admin.site.register(Single_page, Single_page_admin)
admin.site.register(News_class, News_class_admin)
admin.site.register(News_content, News_content_admin)
admin.site.register(Product_class, Product_class_admin)
admin.site.register(Product_content, Product_content_admin)
admin.site.register(message, message_admin)