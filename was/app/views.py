
from django.shortcuts import render, get_object_or_404, redirect
from django import template
from django.template import loader
from django.http import HttpResponse
from django.db.models import Value,TextField
from .models import message1_model,message2_model,map_model
from django.core.paginator import Paginator


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
        if context['url']=="message.html": ##어진
            page = request.GET.get('page', '1')

            c=message1_model.objects.raw('SELECT * FROM parts,messages where parts._id==messages._id')#raw queryset으로 할수없이 만들었다 ...삽질 ..
           
            paginator = Paginator(c, 10) 
            page_obj = paginator.get_page(page)

            context['page']=page_obj

        elif context['url']=="geo-Artifact.html":  ##재식
            context['geo']=map_model.objects.all()
 ###########################################################  


        print(context)
        return render(request,context['url'],context)
    
    except template.TemplateDoesNotExist:

        return render(request,'page-404.html',context)

    except Exception as e:
        print(e)
        return render(request,'page-500.html',context)
       