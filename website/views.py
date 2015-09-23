# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Product_class, Product_content, Single_page, News_class, News_content, message
import xml.etree.ElementTree as etree
import urllib.request
from django.utils.encoding import smart_str
from django.core.paginator import Paginator
from PIL import Image, ImageDraw, ImageFont
import random
import datetime
# Create your views here.


def index(req):
    p = Product_content.objects.filter(product_content_rec=True).order_by('product_content_order', 'id')[:6]
    s = Single_page.objects.filter(single_page_url='gsjj').values('single_page_intro')[0]
    n = News_content.objects.filter(news_content_class_id=1,news_content_rec=True).order_by('news_content_order', '-news_content_date')[:6]
    rss_url = 'http://rss.sina.com.cn/news/china/focus15.xml'
    data = urllib.request.urlopen(rss_url).read()
    data = etree.fromstring(smart_str(data))
    data = data.iter(tag='item')
    news = []
    i = 1
    for item in data:
        news.append(item)
        i = i + 1
        if i > 3:
            break
    news1 = {}
    news2 = {}
    news3 = {}
    news1['title'], news1['link'], news1['date'], news1['descrip'] = news[0][0].text, news[0][1].text, news[0][5].text, news[0][7].text
    news2['title'], news2['link'], news2['date'], news2['descrip'] = news[1][0].text, news[1][1].text, news[1][5].text, news[1][7].text
    news3['title'], news3['link'], news3['date'], news3['descrip'] = news[2][0].text, news[2][1].text, news[2][5].text, news[2][7].text
    context = {'product': p, 'single': s, 'news': n, 'news1': news1, 'news2': news2, 'news3': news3}
    return render(req, 'index.html', context)


def single(req, url):
    single_content = Single_page.objects.get(single_page_url=url)
    context = {'content': single_content}
    return render(req, 'single.html', context)


def news_list(req, nc):
    news_class = News_class.objects.get(id=nc)
    news = News_content.objects.filter(news_content_class=nc).order_by('news_content_order', '-news_content_date', '-id')
    pg = Paginator(news, 10)
    try:
        page = int(req.GET.get('page'))
        if not page or page < 1:
            raise TypeError
    except (ValueError, TypeError):
        page = 1
    try:
        news = pg.page(page)
    except:
        news = pg.page(1)
    context = {'news': news, 'news_class': news_class, 'pg':pg}
    return render(req, 'news.html', context)


def news_show(req, nid):
    news_content = News_content.objects.get(id=nid)
    news_class = News_class.objects.get(id=news_content.news_content_class_id)
    context = {'news_content': news_content, 'news_class': news_class}
    return render(req, 'news_show.html', context)


def products_list(req, pc):
    if pc == '':
        p_list = Product_content.objects.all()
        p_class = ''
    else:
        p_list = Product_content.objects.filter(product_content_class=pc, product_content_show=True)
        p_class = Product_class.objects.get(id=pc)
    pg = Paginator(p_list, 9)
    try:
        page = int(req.GET.get('page'))
        if not page or page < 1:
            raise TypeError
    except:
        page = 1
    try:
        p_list = pg.page(page)
    except:
        p_list = pg.page(1)
    context = {'p_list': p_list, 'p_class': p_class, 'pg': pg}
    return render(req, 'products.html', context)


def products_show(req, pid):
    p_content = Product_content.objects.get(id=pid)
    p_class = p_content.product_content_class.all()
    context = {'p_content': p_content, 'p_class': p_class}
    return render(req, 'products_show.html', context)


def message_show(req):
    w = 100
    h = 40
    font_file = 'static/fonts/simhei.ttf'
    fnt = ImageFont.truetype(font_file, 25)
    char_list = '''
无题李商隐相见时难别亦难东风无力百花残春蚕到死丝方尽蜡炬成灰泪始干晓镜但愁云鬓改夜吟应觉月光寒蓬山此去无多路青鸟殷勤为探看江淮汽车祝大家
龙年大发身体健康的一是在了不和有大这主中人上为们地个用工时要动国产以我到他会作来分生对于学下级就年阶义发成部民可出能方进同行面说种过命度
革而多子后自社加小机也经力线本电高量长党得实家定深法表着水理化争现所二起政三好十战无农使性前等反体合斗路图把结第里正新开论之物从当两些还
天资事队批如应形想制心样干都向变关点育重其思与间内去因件日利相由压员气业代全组数果期导平各基或月毛然问比展那它最及外没看治提五解系林者米
群头意只明四道马认次文通但条较克又公孔领军流入接席位情运器并飞原油放立题质指建区验活众很教决特此常石强极土少已根共直团统式转别造切九你取
西持总料连任志观调七么山程百报更见必真保热委手改管处己将修支识病象几先老光专什六型具示复安带每东增则完风回南广劳轮科北打积车计给节做务被
整联步类集号列温装即毫知轴研单色坚据速防史拉世设达尔场织历花受求传口断况采精金界品判参层止边清至万确究书术状厂须离再目海交权且儿青才证低
越际八试规斯近注办布门铁需走议县兵固除般引齿千胜细影济白格效置推空配刀叶率述今选养德话查差半敌始片施响收华觉备名红续均药标记难存测士身紧
液派准斤角降维板许破述技消底床田势端感往神便贺村构照容非搞亚磨族火段算适讲按值美态黄易彪服早班麦削信排台声该击素张密害侯草何树肥继右属市
严径螺检左页抗苏显苦英快称坏移约巴材省黑武培著河帝仅针怎植京助升王眼她抓含苗副杂普谈围食射源例致酸旧却充足短划剂宣环落首尺波承粉践府鱼随
考刻靠够满夫失包住促枝局菌杆周护岩师举曲春元超负砂封换太模贫减阳扬江析亩木言球朝医校古呢稻宋听唯输滑站另卫字鼓刚写刘微略范供阿块某功套友
限项余倒卷创律雨让骨远帮初皮播优占死毒圈伟季训控激找叫云互跟裂粮粒母练塞钢顶策双留误础吸阻故寸盾晚丝女散焊功株亲院冷彻弹错散商视艺灭版烈
零室轻血倍缺厘泵察绝富城冲喷壤简否柱李望盘磁雄似困巩益洲脱投送奴侧润盖挥距触星松送获兴独官混纪依未突架宽冬章湿偏纹吃执阀矿寨责熟稳夺硬价
努翻奇甲预职评读背协损棉侵灰虽矛厚罗泥辟告卵箱掌氧恩爱停曾溶营终纲孟钱待尽俄缩沙退陈讨奋械载胞幼哪剥迫旋征槽倒握担仍呀鲜吧卡粗介钻逐弱脚
怕盐末阴丰编印蜂急拿扩伤飞露核缘游振操央伍域甚迅辉异序免纸夜乡久隶缸夹念兰映沟乙吗儒杀汽磷艰晶插埃燃欢铁补咱芽永瓦倾阵碳演威附牙芽永瓦斜
灌欧献顺猪洋腐请透司危括脉宜笑若尾束壮暴企菜穗楚汉愈绿拖牛份染既秋遍锻玉夏疗尖殖井费州访吹荣铜沿替滚客召旱悟刺脑措贯藏敢令隙炉壳硫煤迎铸
粘探临薄旬善福纵择礼愿伏残雷延烟句纯渐耕跑泽慢栽鲁赤繁境潮横掉锥希池败船假亮谓托伙哲怀割摆贡呈劲财仪沉炼麻罪祖息车穿货销齐鼠抽画饲龙库守
筑房歌寒喜哥洗蚀废纳腹乎录镜妇恶脂庄擦险赞钟摇典柄辩竹谷卖乱虚桥奥伯赶垂途额壁网截野遗静谋弄挂课镇妄盛耐援扎虑键归符庆聚绕摩忙舞遇索顾胶
羊湖钉仁音迹碎伸灯避泛亡答勇频皇柳哈揭甘诺概宪浓岛袭谁洪谢炮浇斑讯懂灵蛋闭孩释乳巨徒私银伊景坦累匀霉杜乐勒隔弯绩招绍胡呼痛峰零柴簧午跳居
尚丁秦稍追梁折耗碱殊岗挖氏刃剧堆赫荷胸衡勤膜篇登驻案刊秧缓凸役剪川雪链渔啦脸户洛孢勃盟买杨宗焦赛旗滤硅炭股坐蒸凝竟陷枪黎救冒暗洞犯筒您宋
弧爆谬涂味津臂障褐陆啊健尊豆拔莫抵桑坡缝警挑污冰柬嘴啥饭塑寄赵喊垫康遵牧遭幅园腔订香肉弟屋敏恢忘衣孙龄岭骗休借丹渡耳刨虎笔稀昆浪萨茶滴浅
拥穴覆伦娘吨浸袖珠雌妈紫戏塔锤震岁貌洁剖牢锋疑霸闪埔猛诉刷狠忽灾闹乔唐漏闻沈熔氯荒茎男凡抢像浆旁玻亦忠唱蒙予纷捕锁尤乘乌智淡允叛畜俘摸锈
扫毕璃宝芯爷鉴秘净蒋钙肩腾枯抛轨堂拌爸循诱祝励肯酒绳穷塘燥泡袋朗喂铝软渠颗惯贸粪综墙趋彼届墨碍启逆卸航雾冠丙街莱贝辐肠付吉渗瑞惊顿挤秒悬
姆烂森糖圣凹陶词迟蚕亿矩三于干亏士工土才寸下大丈与万上小口巾山千乞川亿个
'''
    chars = []
    for i in range(4):
        chars.append(random.choice(char_list))
    req.session['vcode'] = chars
    pic = Image.new('RGB', (w, h), (255, 255, 255))
    vcode_pic = ImageDraw.Draw(pic)
    for a in range(4):
        vcode_pic.text((5 + a * 20, 5), chars[a], (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), fnt)
    del vcode_pic
    for x in range(w):
        for y in range(h):
            if pic.getpixel((x, y)) == (255, 255, 255):
                pic.putpixel((x, y), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    pic.save('static/images/vcode.jpg')
    return render(req, 'message.html')


def save(req):
    if req.method == 'POST':
        if req.POST.get('vcode') != req.session['vcode']:
            return HttpResponse("<script LANGUAGE='javascript'>alert('请输入正确的验证码！');history.go(-1);</script>")
        message_name =  req.POST.get('name')
        message_phone = req.POST.get('phone')
        message_qq = req.POST.get('qq')
        message_mail = req.POST.get('mail')
        message_content = req.POST.get('content')
        message_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        add = message(message_name=message_name, message_phone=message_phone, message_qq=message_qq, message_mail=message_mail, message_content=message_content, message_date=message_date)
        add.save()
        return HttpResponseRedirect('/message/')
    