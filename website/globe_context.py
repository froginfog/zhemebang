# -*- coding:utf-8 -*-
from .models import Product_class, Globe_info, Single_page


def globe_left_class(req):
    class_list1 = Product_class.objects.filter(product_class_parent__isnull=True)
    class_list2 = Product_class.objects.filter(product_class_parent__isnull=False)
    left = {'class_list1': class_list1, 'class_list2': class_list2}
    return left


def glode_left_single(req):
    content = Single_page.objects.get(single_page_url='lxwm')
    c = {'left_single_content': content}
    return c


def site_info(req):
    info = Globe_info.objects.all().values('company_name', 'phone', 'fax', 'address')[0]
    return info


def top_pic(req):
    pic_list = Globe_info.objects.all().values('banner_pic1', 'banner_pic2', 'banner_pic3', 'banner_pic4', 'banner_pic5')[0]
    b = pic_list.copy()
    for k in b.keys():
        if b[k] == '':
            del pic_list[k]
    pic_count = len(pic_list)
    pic = {'pic_list': pic_list, 'pic_count': pic_count}
    return pic
