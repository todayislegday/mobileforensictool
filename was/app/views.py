
from django.shortcuts import render, get_object_or_404, redirect
from django import template
from django.template import loader
from django.http import HttpResponse,JsonResponse
from django.db.models import Value,TextField
from .models import contacts_model,message1_model,message2_model,map_model,calllog_model,mms_model,chrome2_model,chrome3_model,chrome4_model,chrome5_model,chrome6_model,Sam1_model, Sam2_model,Sam3_model,Sam4_model,Sam5_model,webdowndata_model,webext_model,Appinslog_model,Media_model
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import os
# 루트 디렉터리로 처음 띄울 페이지 지정
def index(request):
    return render(request,'main.html')

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

            c=contacts_model.objects.all()
            paginator = Paginator(c, 10) 
            page_obj = paginator.get_page(page)

            context['contact']=page_obj
            
        elif context['url']=="message.html": ##어진
            page = request.GET.get('page', '1')

            m=message1_model.objects.raw('SELECT parts._id,parts.text,messages._id,DATETIME(ROUND(messages.created_timestamp / 1000), "unixepoch","localtime") AS created_timestamp,messages.recipients FROM parts,messages where parts._id==messages._id')#raw queryset으로 할수없이 만들었다 ...삽질 ..
            paginator = Paginator(m, 10) 
            page_obj = paginator.get_page(page)

            context['page']=page_obj
        elif context['url']=="smart-info.html":
            print("hi")
        elif context['url']=="geo-Artifact.html":  ##재식
            if 'id' in request.GET:##ajax 처리
                id=request.GET['id']
                OUTPATH="/static/assets/images/"
                print(OUTPATH)
                a=map_model.objects.raw("select _id,latitude,longitude,_display_name,replace(_data,'/storage/emulated','/static/assets/images/media') as data,DATETIME(ROUND(datetaken / 1000), 'unixepoch','localtime') AS datetaken from files where _id=%s" %id)
                return JsonResponse(serializers.serialize('json',a),safe=False)
                
            map_list=map_model.objects.all()
            map_dict={}
            i=1
            for map in map_list:#queryset->dict(list[])
                if map.lat!=None and map.longt!=None:
                    map_dict[str(i)]=list()
                    map_dict[str(i)].append(map.id)
                    map_dict[str(i)].append(map.lat)
                    map_dict[str(i)].append(map.longt)
                    i+=1
            print(map_dict)  
            context['geo']=map_dict
        
        elif context['url']=="time-line.html":#용하
            mms=mms_model.objects.raw("SELECT _id,address,content,datetime((date / 1000), 'unixepoch','localtime') AS date FROM messages ORDER BY date ASC")
            calllog=calllog_model.objects.raw("SELECT datetime((date / 1000), 'unixepoch','localtime') FROM calls ORDER BY date ASC")
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
            for map in mms:#queryset->dict(list[])
                mms_dict[i]=list()
                mms_dict[i].append(map.id)
                mms_dict[i].append(map.address)
                mms_dict[i].append(map.content)
                mms_dict[i].append(map.date)
                i+=1
            ###################################
            print(mms_dict)  

            context['mms']=mms_dict
            context['calllog']=calllog
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
 ###########################################################  


        print(context)
        return render(request,context['url'],context)
    
    except template.TemplateDoesNotExist:

        return render(request,'page-404.html',context)

    except Exception as e:
        print(e)
        return render(request,'page-500.html',context)
       