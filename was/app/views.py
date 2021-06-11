from . import parsing_xml
from django.shortcuts import render, get_object_or_404, redirect
from django import template
from django.template import loader
from django.http import HttpResponse,JsonResponse
from django.db.models import Value,TextField
from .models import contacts_model,message1_model,message2_model,map_model,calllog_model,mms_model,chrome2_model,chrome3_model,chrome4_model,chrome5_model,chrome6_model,Sam1_model, Sam2_model,Sam3_model,Sam4_model,Sam5_model,webdowndata_model,webext_model,Appinslog_model,Media_model,calendar_model,kakao1_model,kakao2_model
from .countkeyword import count
from .crawling import image1
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import os,mmap


# 루트 디렉터리로 처음 띄울 페이지 지정
def index(request):
 try:
    context={}
    path=os.path.dirname(os.path.abspath(__file__))
    f = open(f"{path}/build.prop", 'r')#경로 추후 
           
    lines = f.readlines()
    for line in lines:
        if 'ro.product.system.model' in line:
            lines1 = line.split("=") 
            context['model']=line.split("=")[1].strip('\n') #model
        elif 'ro.system.build.version.release' in line:
            lines1 = line.split("=") 
            context['osversion']=line.split("=")[1].strip('\n')
        elif 'ro.product.system.manufacturer' in line:
            lines1 = line.split("=") 
            context['manufacturer']=line.split("=")[1].strip('\n')
        elif 'ro.build.characteristics' in line:
            lines1 = line.split("=") 
            context['sdcard']=line.split("=")[1].strip('\n')
        elif 'ro.product.local' in line:
            context['local']=line.split("=")[1].strip('\n')
                    
                   
            context['imgpath']=image1(context['model'])#크롤링 함수,pip install bs4,lxml


    context['recentcall']=calllog_model.objects.raw('select _id,name,number,DATETIME(ROUND(date/ 1000), "unixepoch","localtime") AS date from calls where m_content IS NULL order by date desc')[:5]
   
    calendar1=calendar_model.objects.raw('select _id,title ,DATETIME(ROUND(dtstart / 1000), "unixepoch","localtime")  as start,DATETIME(ROUND(dtend / 1000), "unixepoch","localtime")  as end from Events where eventTimezone="Asia/Seoul"')
    calendar2=calendar_model.objects.raw('select _id,title ,DATETIME(ROUND(dtstart / 1000), "unixepoch")  as start,DATETIME(ROUND(dtend / 1000), "unixepoch")  as end from Events where eventTimezone="UTC"')
    
    print(calendar1)
    print(calendar2)
    
    calendar_list = []
    i = 0
    for c in calendar1:
        dic={"id":c.id,"title":c.title,"start":c.start,"end":c.end}
        calendar_list.append(dic)

    for c in calendar2:
        dic={"id":c.id,"title":c.title,"start":c.start,"end":c.end}
        calendar_list.append(dic)
    context['calendar']=calendar_list
    
    print(context['calendar'])


    return render(request,'Dashboard.html',context)
 
 except Exception as e:
        print(e)
        return render(request,'page-500.html',context)

def pages(request):
    context = {}#렌더링된 html페이지에 사용할 변수를 넣는다.
                # All resource paths end in .html.
                # Pick out the html file name from the url. And load that template.
    try:
        load_template= request.path.split('/')[-1]  #경로명에서 /를 빼고 뒤에 파일명 .html(랜더)띄워준다.
        context['url'] = load_template              #랜더링 하는 이유는 html문안에 변수나 반복문이 사용가능해요
                                                    #db에서 내용을 가져오면 context dict자료형에 넣어서 사용하세요:)



##################함수로 빼낼 부분########################
        if context['url']=="contact.html": ##어진
            page = request.GET.get('page', '1')

            c=contacts_model.objects.values()
            paginator = Paginator(c, 10) 
            page_obj = paginator.get_page(page)
            
            context['calllog']=calllog_model.objects.raw("SELECT _id,datetime((date / 1000), 'unixepoch','localtime') AS date FROM calls where m_content IS NULL ORDER BY date ASC ") #메시지 아닌것만
            context['contact']=c
            context['page']=page_obj
            
        elif context['url']=="message.html": ##어진
            page = request.GET.get('page', '1')

            m= mms_model.objects.raw(
                "SELECT _id,address,content,datetime((date / 1000), 'unixepoch','localtime') AS date FROM messages ORDER BY date ASC")
            paginator = Paginator(m, 10) 
            page_obj = paginator.get_page(page)

            context['page']=page_obj
            context['content']=m
            
            text=mms_model.objects.values('content')
            
            context['words']=count(text,'content')

        elif context['url']=="wifi.html": ##귀수
            path=os.path.dirname(os.path.abspath(__file__))
            f = open(f"{path}/../../경로.txt", 'r')
            OUTPATH=f.readlines()[1]
            wifi=parsing_xml.xml_parsing(OUTPATH)
            page = request.GET.get('page', '1')

            
            paginator = Paginator(wifi, 10) 
            page_obj = paginator.get_page(page)
            context['page']=page_obj
            context['content']=wifi

        elif context['url']=="geo-Artifact.html":  ##재식
           
            if 'id' in request.GET:##ajax get 처리
                OUTPATH="/static/assets/images/"
                a=map_model.objects.raw("select _id,latitude,longitude,_display_name,replace(_data,'/storage/emulated','/static/assets/images/media') as data,DATETIME(ROUND(datetaken / 1000), 'unixepoch','localtime') AS datetaken from files where  (latitude>=%s AND latitude<=%s) AND (longitude>=%s AND longitude<=%s)  AND (%s<=datetaken AND datetaken<=%s) ORDER BY datetaken ASC" %((float)(request.GET['lat'])-0.000001,(float)(request.GET['lat'])+0.000001,(float)(request.GET['lng'])-0.000001,(float)(request.GET['lng'])+0.000001,request.GET['startDate'],request.GET['endDate']))#오차 처리
                return JsonResponse(serializers.serialize('json',a),safe=False)
            
            if request.method=="POST":##ajax post 처리
                print(request.POST)
                a=map_model.objects.raw("select _id,latitude,longitude,datetaken from files where (%s<=latitude AND latitude<=%s) AND (%s<=longitude AND longitude<=%s) AND (%s<=datetaken AND datetaken<=%s) ORDER BY datetaken ASC" %(request.POST['swlat'],request.POST['nelat'],request.POST['swlng'],request.POST['nelng'],request.POST['startDate'],request.POST['endDate'] ))
                return JsonResponse(serializers.serialize('json',a),safe=False)

            map_list=map_model.objects.all().order_by('datetaken')
            map_dict={}
            i=1
            for m in map_list:#queryset->dict(list[])
                if m.lat!=None and m.longt!=None:
                    map_dict[str(i)]=list()
                    map_dict[str(i)].append(m.id)
                    map_dict[str(i)].append(m.lat)
                    map_dict[str(i)].append(m.longt)
                    map_dict[str(i)].append(m.datetaken)
                    i+=1
            context['geo']=map_dict
            print(map_dict)

        elif context['url']=="chrome-history.html":#지호
            page = request.GET.get('page', '1')

            c=chrome3_model.objects.raw("SELECT id, url, title, datetime(( last_visit_time/1000000)-11644473600,'unixepoch','localtime') as last_visit_time, visit_count FROM urls ")
            paginator = Paginator(c, 10) 
            page_obj = paginator.get_page(page)

            context['page']=page_obj
            context['content']=c
        elif context['url']=="chrome-download.html":#지호
            page = request.GET.get('page', '1')

            c=chrome5_model.objects.raw("SELECT id, current_path, target_path,datetime(( start_time/1000000)-11644473600,'unixepoch','localtime') as start_time, datetime((end_time/1000000)-11644473600,'unixepoch','localtime') as end_time,tab_url,original_mime_type, received_bytes, total_bytes FROM downloads ")    
            paginator = Paginator(c, 10) 
            page_obj = paginator.get_page(page)

            context['page']=page_obj
            context['content']=c

        elif context['url']=="chrome-search.html":#지호
            page = request.GET.get('page', '1')

            c=chrome2_model.objects.raw("SELECT keyword_id,term,normalized_term FROM keyword_search_terms")
            text=chrome2_model.objects.values('term')
            paginator = Paginator(c, 10) 
            page_obj = paginator.get_page(page)

            context['words']=count(text,'term')
            context['page']=page_obj
            context['content']=c
        elif context['url']=="sam-history.html":#지호
            page = request.GET.get('page', '1')

            c=Sam2_model.objects.raw("SELECT id, url, title, datetime(( last_visit_time/1000000)-11644473600,'unixepoch','localtime') as last_visit_time, visit_count FROM urls ")
            paginator = Paginator(c, 10) 
            page_obj = paginator.get_page(page)

            context['page']=page_obj
            context['content']=c
        elif context['url']=="sam-download.html":#지호
            page = request.GET.get('page', '1')

            c=Sam4_model.objects.raw("SELECT id, current_path, target_path,datetime(( start_time/1000000)-11644473600,'unixepoch','localtime') as start_time, datetime((end_time/1000000)-11644473600,'unixepoch','localtime') as end_time,tab_url,original_mime_type, received_bytes, total_bytes FROM downloads ")    
            paginator = Paginator(c, 10) 
            page_obj = paginator.get_page(page)

            context['page']=page_obj
            context['content']=c
        elif context['url']=="sam-search.html":#지호
            page = request.GET.get('page', '1')

            c=Sam1_model.objects.raw("SELECT keyword_id,term,normalized_term FROM keyword_search_terms")
            paginator = Paginator(c, 10) 
            page_obj = paginator.get_page(page)
            
            text=Sam1_model.objects.values('term')
            context['words']=count(text,'term')
            context['page']=page_obj
            context['content']=c
        elif context['url'] == "time-line.html":  # 용하
            mms = mms_model.objects.raw(
                "SELECT _id,address,content,datetime((date / 1000), 'unixepoch','localtime') AS date FROM messages ORDER BY date ASC")
            calllog = calllog_model.objects.raw(
                "SELECT _id,datetime((date / 1000), 'unixepoch','localtime') AS date  FROM calls  where m_content IS NULL  ORDER BY date ASC")
            chromekeyword = chrome2_model.objects.all()
            chromeurlhistory = chrome3_model.objects.raw(
                "SELECT urls.id, urls.url, urls.title, datetime(visits.visit_time/1000000 + (strftime('%%s','1601-01-01')),'unixepoch','localtime') AS visit_time FROM urls, visits WHERE urls.id=visits.url ORDER BY visits.visit_time ASC")
            chromedown = chrome5_model.objects.all()
            chromedownurl = chrome6_model.objects.all()
            Samkeyword = Sam1_model.objects.all()
            Samurlhistory = Sam3_model.objects.raw(
                "SELECT urls.id, urls.url, urls.title, datetime(visits.visit_time/1000000 + (strftime('%%s', '1601-01-01')), 'unixepoch','localtime') AS visit_time FROM urls, visits WHERE urls.id=visits.url ORDER BY visits.visit_time ASC")
            Samdown = Sam4_model.objects.all()
            Samdownurl = Sam5_model.objects.all()
            webdowndata = webdowndata_model.objects.all()
            webext = webext_model.objects.raw(
                "SELECT _id, datetime(date_added, 'unixepoch', 'localtime') AS date_added FROM downloads ORDER BY date_added ASC")
            appinslog=Appinslog_model.objects.raw("select package_name,datetime(first_download_ms/1000, 'unixepoch','localtime') AS first_download_ms,datetime(delivery_data_timestamp_ms/1000, 'unixepoch','localtime') AS delivery_data_timestamp_ms,datetime(last_update_timestamp_ms/1000, 'unixepoch','localtime') AS last_update_timestamp_ms,datetime(install_request_timestamp_ms/1000, 'unixepoch','localtime') AS install_request_timestamp_ms from appstate")
            media = Media_model.objects.raw(
                "SELECT _id, datetime(date_added, 'unixepoch', 'localtime') AS date_added ,replace(_data,'/storage/emulated','/static/assets/images/media')AS _data FROM files ORDER BY date_added ASC")
            ###함수로 빼기#################
            mms_dict = {}
            i = 0
            for m in mms:  # queryset->dict(list[])
                mms_dict[i] = list()
                mms_dict[i].append(m.id)
                mms_dict[i].append(m.address)
                mms_dict[i].append(m.content)
                mms_dict[i].append(m.date)
                mms_dict[i].append(m.box_type)
                i += 1
            ###################################

            call_dict = {}
            i = 0
            for c in calllog:
                call_dict[str(i)] = list()
                call_dict[str(i)].append(c.id)
                call_dict[str(i)].append(c.number)
                call_dict[str(i)].append(c.date)
                call_dict[str(i)].append(c.duration)
                call_dict[str(i)].append(c.type)
                i += 1

            ####################################

            chrome_dict = {}
            i = 0
            for ch in chromeurlhistory:
                chrome_dict[str(i)] = list()
                chrome_dict[str(i)].append(ch.id)
                chrome_dict[str(i)].append(ch.url)
                chrome_dict[str(i)].append(ch.title)
                chrome_dict[str(i)].append(ch.visit_time)
                i += 1

            sam_dict = {}
            i = 0
            for s in Samurlhistory:
                sam_dict[str(i)] = list()
                sam_dict[str(i)].append(s.id)
                sam_dict[str(i)].append(s.url)
                sam_dict[str(i)].append(s.title)
                sam_dict[str(i)].append(s.visit_time)
                i += 1

            #####################################

            download_dict = {}
            i = 0
            for d in webext:
                download_dict[str(i)] = list()
                download_dict[str(i)].append(d.id)
                download_dict[str(i)].append(d.date_added)
                download_dict[str(i)].append(d.owner_package_name)
                download_dict[str(i)].append(d.download_uri)
                download_dict[str(i)].append(d._data)
                i += 1

            ######################################

            media_dict = {}
            i = 0
            for md in media:
                media_dict[str(i)] = list()
                media_dict[str(i)].append(md.id)
                media_dict[str(i)].append(md.date_added)
                media_dict[str(i)].append(md.bucket_display_name)
                media_dict[str(i)].append(md.owner_package_name)
                media_dict[str(i)].append(md.data)
                i += 1

            context['mms'] = mms_dict
            context['calllog'] = call_dict
            context['chromekeyword'] = chromekeyword
            context['chromeurlhistory'] = chrome_dict
            context['chromedown'] = chromedown
            context['chromedownurl'] = chromedownurl
            context['Samkeyword'] = Samkeyword
            context['Samurlhistory'] = sam_dict
            context['Samdown'] = Samdown
            context['Samdownurl'] = Samdownurl
            context['webdowndata'] = webdowndata
            context['webext'] = download_dict
            context['appinslog'] = appinslog
            context['media'] = media_dict

        elif context['url']=="appins-log.html":
            page = request.GET.get('page', '1')

            m = Appinslog_model.objects.raw("select package_name,datetime(first_download_ms/1000, 'unixepoch','localtime') AS first_download_ms,datetime(delivery_data_timestamp_ms/1000, 'unixepoch','localtime') AS delivery_data_timestamp_ms,datetime(last_update_timestamp_ms/1000, 'unixepoch','localtime') AS last_update_timestamp_ms,datetime(install_request_timestamp_ms/1000, 'unixepoch','localtime') AS install_request_timestamp_ms from appstate")
            paginator = Paginator(m, 10) 
            page_obj = paginator.get_page(page)

            context['page']=page_obj
            context['content']=m
        elif context['url']=="media.html":
            page = request.GET.get('page', '1')

            m = Media_model.objects.raw("SELECT _id, datetime(date_added, 'unixepoch', 'localtime') AS date_added ,replace(_data,'/storage/emulated','/static/assets/images/media')AS _data FROM files ORDER BY date_added ASC")
            paginator = Paginator(m, 10) 
            page_obj = paginator.get_page(page)

            context['page']=page_obj
            context['content']=m
        elif context['url']=="kakaotalk.html": #재훈
            #context['chrooms']=kakao1_model.objects.all() 채팅방 실제 생성
            context['friends']=kakao2_model.objects.raw("select * from friends_dec where v  not like '%%plusFriendProfile%%' ")
            context['plusfriends']=kakao2_model.objects.raw("select * from friends_dec where v  like '%%plusFriendProfile%%' ")
        
 ###########################################################  
        
    

        return render(request,context['url'],context)
    
    except template.TemplateDoesNotExist:

        return render(request,'page-404.html',context)

    except Exception as e:
        print(e)
        return render(request,'page-500.html',context)
       