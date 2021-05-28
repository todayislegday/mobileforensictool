#단어들의 빈도수를 센다.

def count(inputli,key):
            ###############################
            c=list()
            for a in inputli:#쿼리셋->list
                c.append(a[key])
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

            return list3