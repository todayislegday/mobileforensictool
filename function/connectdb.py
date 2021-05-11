#들어온 경로의 db를 연결한다.
#명령문은 was에서 보내준 명령문을 실행한다.

import sqlite3


def connectdb(dbname,table,field,excutes=None):
    f = open("../경로.txt", 'r')
    path = f.readlines()[1]
    f.close()
    path+='/data/com.samsung.android.providers.contacts/databases/' #추후 파일경로 list에서 읽어옴
    conn = sqlite3.connect(f"{path}/{dbname}")#해당 경로의 db를 sqlite3로 연결
    cur = conn.cursor()
    cur.execute(f"select * from {table}")#sql 문,명령문은 
    rows = cur.fetchall() #가져온 결과의 행을 리스트로 가져옴
    # for row in rows: 
    #     print(row) 
    cur.close()
    conn.close()
    return rows
    

#print(connectdb('calllog.db','calls','*'))


