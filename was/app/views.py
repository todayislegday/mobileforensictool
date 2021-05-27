from . import parsing_xml
from django.shortcuts import render, get_object_or_404, redirect
from django import template
from django.template import loader
from django.http import HttpResponse,JsonResponse
from django.db.models import Value,TextField
from .models import contacts_model,message1_model,message2_model,map_model,calllog_model,mms_model,chrome2_model,chrome3_model,chrome4_model,chrome5_model,chrome6_model,Sam1_model, Sam2_model,Sam3_model,Sam4_model,Sam5_model,webdowndata_model,webext_model,Appinslog_model,Media_model
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import os,mmap


# 루트 디렉터리로 처음 띄울 페이지 지정
def index(request):
 try:
    context={}
    from .crawling import image1
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


    context['recentcall']=calllog_model.objects.raw('select _id,name,number,DATETIME(ROUND(date/ 1000), "unixepoch","localtime") AS date from calls order by date desc')[:5]

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
            
            context['calllog']=calllog_model.objects.raw("SELECT _id,datetime((date / 1000), 'unixepoch','localtime') AS date FROM calls ORDER BY date ASC")
            context['contact']=c
            context['page']=page_obj
            
        elif context['url']=="message.html": ##어진
            page = request.GET.get('page', '1')

            m=message1_model.objects.raw('SELECT parts._id,parts.text,messages._id,DATETIME(ROUND(messages.created_timestamp / 1000), "unixepoch","localtime") AS created_timestamp,messages.recipients FROM parts,messages where parts._id==messages._id')#raw queryset으로 할수없이 만들었다 ...삽질 ..
            paginator = Paginator(m, 10) 
            page_obj = paginator.get_page(page)

            context['page']=page_obj
            context['msg']=m

        elif context['url']=="wifi.html": ##귀수
            path=os.path.dirname(os.path.abspath(__file__))
            f = open(f"{path}/../../경로.txt", 'r')
            OUTPATH=f.readlines()[1]
            wifi=parsing_xml.xml_parsing(OUTPATH)
            page = request.GET.get('page', '1')

            
            paginator = Paginator(wifi, 10) 
            page_obj = paginator.get_page(page)
            context['page']=page_obj
    
        elif context['url']=="geo-Artifact.html":  ##재식
            if 'id' in request.GET:##ajax 처리
                id=request.GET['id']
                OUTPATH="/static/assets/images/"
                a=map_model.objects.raw("select _id,latitude,longitude,_display_name,replace(_data,'/storage/emulated','/static/assets/images/media') as data,DATETIME(ROUND(datetaken / 1000), 'unixepoch','localtime') AS datetaken from files where _id=%s" %id)
                return JsonResponse(serializers.serialize('json',a),safe=False)
                
            map_list=map_model.objects.all().order_by('datetaken')
            print(map_list)
            map_dict={}
            i=1
            for m in map_list:#queryset->dict(list[])
                if m.lat!=None and m.longt!=None:
                    map_dict[str(i)]=list()
                    map_dict[str(i)].append(m.id)
                    map_dict[str(i)].append(m.lat)
                    map_dict[str(i)].append(m.longt)
                    map_dict[str(i)].append(m.datetaken)
                    map_dict[str(i)].append("안녕")
                    i+=1
            print(map_dict)  
            context['geo']=map_dict

        elif context['url']=="chrome-history.html":#지호
            page = request.GET.get('page', '1')

            c=chrome3_model.objects.raw("SELECT id, url, title, datetime(( last_visit_time/1000000)-11644473600,'unixepoch','localtime') as last_visit_time, visit_count FROM urls ")
            paginator = Paginator(c, 10) 
            page_obj = paginator.get_page(page)

            context['page']=page_obj
        elif context['url']=="chrome-download.html":#지호
            page = request.GET.get('page', '1')

            c=chrome5_model.objects.raw("SELECT id, current_path, target_path,datetime(( start_time/1000000)-11644473600,'unixepoch','localtime') as start_time, datetime((end_time/1000000)-11644473600,'unixepoch','localtime') as end_time,tab_url,original_mime_type, received_bytes, total_bytes FROM downloads ")    
            paginator = Paginator(c, 10) 
            page_obj = paginator.get_page(page)

            context['page']=page_obj
        elif context['url']=="chrome-search.html":#지호
            page = request.GET.get('page', '1')

            c=chrome2_model.objects.raw("SELECT keyword_id,term,normalized_term FROM keyword_search_terms")
            paginator = Paginator(c, 10) 
            page_obj = paginator.get_page(page)

            context['page']=page_obj

        elif context['url']=="sam-history.html":#지호
            page = request.GET.get('page', '1')

            c=Sam2_model.objects.raw("SELECT id, url, title, datetime(( last_visit_time/1000000)-11644473600,'unixepoch','localtime') as last_visit_time, visit_count FROM urls ")
            paginator = Paginator(c, 10) 
            page_obj = paginator.get_page(page)

            context['page']=page_obj
        elif context['url']=="sam-download.html":#지호
            page = request.GET.get('page', '1')

            c=Sam4_model.objects.raw("SELECT id, current_path, target_path,datetime(( start_time/1000000)-11644473600,'unixepoch','localtime') as start_time, datetime((end_time/1000000)-11644473600,'unixepoch','localtime') as end_time,tab_url,original_mime_type, received_bytes, total_bytes FROM downloads ")    
            paginator = Paginator(c, 10) 
            page_obj = paginator.get_page(page)

            context['page']=page_obj
        elif context['url']=="sam-search.html":#지호
            page = request.GET.get('page', '1')

            c=Sam1_model.objects.raw("SELECT keyword_id,term,normalized_term FROM keyword_search_terms")
            paginator = Paginator(c, 10) 
            page_obj = paginator.get_page(page)

            context['page']=page_obj
        
        elif context['url']=="time-line.html":#용하
            mms=mms_model.objects.raw("SELECT _id,address,content,datetime((date / 1000), 'unixepoch','localtime') AS date FROM messages ORDER BY date ASC")
            calllog=calllog_model.objects.raw("SELECT _id,datetime((date / 1000), 'unixepoch','localtime') FROM calls ORDER BY date ASC")
            chromekeyword=chrome2_model.objects.all()
            chromeurlhistory=chrome3_model.objects.raw("SELECT urls.id, urls.url, urls.title, datetime(visits.visit_time/1000000 + (strftime('%%s','1601-01-01')),'unixepoch','localtime') AS visit_time FROM urls, visits WHERE urls.id=visits.url ORDER BY visits.visit_time ASC")
            chromedown=chrome5_model.objects.all()
            chromedownurl=chrome6_model.objects.all()
            Samkeyword=Sam1_model.objects.all()
            Samurlhistory=Sam3_model.objects.raw("SELECT urls.id, urls.url, urls.title, datetime(visits.visit_time/1000000 + (strftime('%%s', '1601-01-01')), 'unixepoch','localtime') FROM urls, visits WHERE urls.id=visits.url ORDER BY visits.visit_time ASC")
            Samdown=Sam4_model.objects.all()
            Samdownurl=Sam5_model.objects.all()
            webdowndata=webdowndata_model.objects.all();
            webext=webext_model.objects.raw("select datetime(date_added, 'unixepoch','localtime') from downloads")       
            appinslog=Appinslog_model.objects.raw("select datetime(first_download_ms/1000, 'unixepoch','localtime'),datetime(delivery_data_timestamp_ms/1000, 'unixepoch','localtime'),datetime(last_update_timestamp_ms/1000, 'unixepoch','localtime'),datetime(install_request_timestamp_ms/1000, 'unixepoch','localtime') from appstate")
            media=Media_model.objects.all()
            
            ###함수로 빼기#################
            mms_dict={}
            i=0
            for m in mms:#queryset->dict(list[])
                mms_dict[i]=list()
                mms_dict[i].append(m.id)
                mms_dict[i].append(m.address)
                mms_dict[i].append(m.content)
                mms_dict[i].append(m.date)
                i+=1
            ###################################
            print(mms_dict)  
            
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
            print(call_dict)
            context['calllog'] = call_dict

            context['mms']=mms_dict
            # context['calllog']=calllog
            context['chromekeyword']=chromekeyword
            context['chromeurlhistory']=chromeurlhistory
            context['chromedown']=chromedown
            context['chromedownurl']=chromedownurl
            context['Samkeyword']=Samkeyword
            context['Samurlhistory']=Samurlhistory
            context['Samdown']=Samdown
            context['Samdownurl']=Samdownurl
            context['webdowndata']=webdowndata
            context['webext']=webext
            context['appinslog']=appinslog
            context['media']=media
        
        
        elif context['url']=="keyword-view.html":
            text=message1_model.objects.values('text')

            ###############################
            c=list()
            for a in text:#쿼리셋->list
                c.append(a['text'])
            litost=" ".join(map(str,c)) #list를 전체 문자열로 만든다.
            
            c=litost.split()#중복이 있는 list
            list1=set(c)
            list1=list(list1)#중복이 제거된 list
            
            list2=list()
            list3=list()
            for text in c:
                list2.append({"text":text})
            for text in list1:
                list3.append({"text":text})
            a=1

            for a in list2:
                find =a['text']
                for e in list3:
                    if find==e['text']:
                        try:e['weight']=e['weight']+1
                        except:e['weight']=1
            for e in list3:
                e['html']={"title":f"빈도수:{e['weight']}"}  

            context['words']=list3
 ###########################################################  


        print(context)
        return render(request,context['url'],context)
    
    except template.TemplateDoesNotExist:

        return render(request,'page-404.html',context)

    except Exception as e:
        print(e)
        return render(request,'page-500.html',context)
       
