import requests
def booksearch(keyword,Json,Headers):
    url='https://findcumt.libsp.com/find/unify/search'
    r = requests.post(url,json=Json,headers=Headers)
    book_json=r.json()
    bookmassage=[]
    print(book_json)
    for j in range(0,10):
        book=((((book_json["data"])['searchResult'])[j]))
        author=book['author']
        name=book['title']
        isbn=book['isbn']
        publisher=book['publisher']
        ID=book['recordId']
        groupPhysicalCount=book['groupPhysicalCount']
        groupECount=book['groupECount']
        dict={"书名":name,"作者":author,"isbn":isbn,"出版社":publisher,"bookID":ID,"纸本馆藏":groupPhysicalCount,"电子馆藏":groupECount}
        bookmassage.append(dict)
    print(bookmassage)

def IDsearch(bookid,Json,Headers):
    url='https://findcumt.libsp.com/find/physical/groupitems'
    r=requests.post(url,json=Json,headers=Headers)
    bookid_data=r.json()
    print("馆藏地".ljust(40),"条码号".ljust(17),"属性".ljust(20))
    for i in bookid_data["data"]:
        print(i['locationName'].ljust(30),i['barcode'].ljust(20),i["processType"].ljust(20))



mehter=eval(input("输入1搜索图书，输入2搜索图书馆藏信息"))
if mehter==1:
    keyword=input("请输入关键词：")
    data= {"docCode":[None],
"searchFieldContent":keyword,
"searchField":"keyWord",
"matchMode":"2",
"sortField":"relevance",
"sortClause":"asc",
"page":"1",
"rows":"10",
"indexSearch":"1",
}
    headers = {
"Host": "findcumt.libsp.com",
"groupCode": "200069",
"Connection": "keep-alive",
"Accept":'application/json, text/plain, */*',
"Referer": 'https://findcumt.libsp.com/',
"Accept-Encoding": "gzip, deflate,br",
"Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
'Origin':'https://findcumt.libsp.com',
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.6241 SLBChan/30"
}
    booksearch(keyword,data,headers)
elif mehter==2:
    bookid=input("请输入图书ID：")
    headers = {
"Host": "findcumt.libsp.com",
"groupCode": "200069",
"Connection": "keep-alive",
"Accept":'application/json, text/plain, */*',
"Referer": 'https://findcumt.libsp.com/',
"Accept-Encoding": "gzip, deflate,br",
"Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.6241 SLBChan/30"
}
    data={"recordId":bookid}
    IDsearch(bookid,data,headers)
else:
    print("输入错误请重新输入")