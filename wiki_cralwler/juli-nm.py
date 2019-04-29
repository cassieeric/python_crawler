# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

mainurl='https://en.wikipedia.org'
sturl='/wiki/Marie_Curie'


linktype = ['Doctoral advisor', 'Doctoral students', 'Born', 'Died','Nationality', 'Awards', 'Fields']

uidfile='uid.txt'
shipfile='ship.txt'
uidlist={}

inib=['','','','','', '']
#名字  地址  id
newfile='link.txt'


newurllist=[]



# with open(uidfile,'w') as fw:
#    fw.write('Marie_Curie\t/wiki/Marie_Curie\t0')

count = 0
finishlist = {}
uid = 0
with open(uidfile, 'r') as rf:
    lines = rf.readlines()
    for line in lines:
        line = line.strip().split('\t')
        uidlist[line[1]] = [line[0], line[2]]
        uid += 1

def getonepage(url):
    lstrship = []
    newurl = []
    lstuid = []
    blist = {}
    if len(url)<6 or url[:6]!='/wiki/':
        return lstrship,newurl,lstuid,blist


    global uid,uidlist,count
    count+=1
    print(mainurl+url,count)
    html=requests.get(mainurl+url)

    #print(html.text)
    bs=BeautifulSoup(html.text)
    a=bs.find_all(name='table',attrs={"class":"infobox"})
    if a and len(a)>0:
        for idx, tr in enumerate(a[0].find_all('tr')):
            th=tr.find('th')
            if th:
                head=tr.find('th').get_text()
                if head in linktype:
                    if head==linktype[0]:
                        #myid tid
                        td=tr.find('td')
                        if td:
                            a=td.find_all('a')
                            for a1 in a:
                                hf=a1.get('href')
                                nm=a1.get_text()
                                if nm is None or len(nm)==0:
                                    continue
                                if '['==nm[0] and '#' in nm:
                                    continue
                                if hf and hf not in uidlist:
                                    uidlist[hf] = [nm, uid]
                                    lstuid.append('\t'.join([nm, hf, str(uid)]))
                                    newurl.append(hf)
                                    uid += 1
                                itemuid = str(uidlist[url][1]) + '\t'+str(uidlist[hf][1])
                                lstrship.append(itemuid)
                            if a is None or len(a)==0:
                                hf =''
                                nm = td.get_text()
                                if nm and nm not in uidlist:
                                    uidlist[nm] = [nm, uid]
                                    lstuid.append('\t'.join([nm, hf, str(uid)]))
                                    itemuid = str(uidlist[url][1]) + '\t' + str(uid)
                                    lstrship.append(itemuid)
                                    uid += 1

                    elif head==linktype[1]:
                        # myid tid
                        td = tr.find('td')
                        if td:
                            a = td.find_all('a')
                            for a1 in a:
                                hf = a1.get('href')
                                nm = a1.get_text()
                                if nm is None or len(nm)==0:
                                    continue
                                if  '['==nm[0] and '#' in nm:
                                    continue
                                if hf and hf not in uidlist:
                                    newurl.append(hf)
                                    uidlist[hf] = [nm, uid]
                                    lstuid.append('\t'.join([nm, hf, str(uid)]))
                                    uid += 1
                                itemuid = str(uidlist[hf][1])+'\t'+str(uidlist[url][1])
                                lstrship.append(itemuid)
                            if a is None or len(a)==0:
                                hf =''
                                nm = td.get_text()
                                if nm and nm not in uidlist:
                                    uidlist[nm] = [nm, uid]
                                    lstuid.append('\t'.join([nm, hf, str(uid)]))
                                    itemuid = str(uidlist[url][1]) + '\t' + str(uid)
                                    lstrship.append(itemuid)
                                    uid += 1

                    elif head == linktype[2]:
                        td = tr.find('td')
                        if td:
                            a = td.find_all('span')
                            for a1 in a:
                                nm = a1.get_text()
                                if url not in blist:
                                    blist[url] = inib.copy()
                                    blist[url][0] = url
                                blist[url][1] = nm
                                break
                    elif head == linktype[3]:
                        td = tr.find('td')
                        if td:
                            a = td.find_all('span')
                            for a1 in a:
                                nm = a1.get_text()
                                if url not in blist:
                                    blist[url] = inib.copy()
                                    blist[url][0] = url
                                blist[url][2] = nm
                                break
                    elif head == linktype[4]:
                        td = tr.find('td')
                        if td:
                            nm = td.get_text()
                            if url not in blist:
                                blist[url] = inib.copy()
                                blist[url][0] = url
                            blist[url][3] = nm


                    elif head == linktype[5]:
                        td = tr.find('td')
                        if td:
                            a = td.find_all('a')
                            for a1 in a:
                                nm = a1.get_text()
                                if url not in blist:
                                    blist[url] = inib.copy()
                                    blist[url][0] = url
                                blist[url][4] = nm
                                break

                    elif head == linktype[6]:
                        td = tr.find('td')
                        if td:
                            a = td.find_all('a')
                            for a1 in a:
                                nm = a1.get_text()
                                if url not in blist:
                                    blist[url] = inib.copy()
                                    blist[url][0] = url
                                blist[url][5] = nm
                                break
    if len(blist.keys())>0:
        return lstrship, newurl, lstuid, blist
    else:
        return lstrship, newurl, lstuid, ''


def GetSt(myurl):
    lstrship, newurl,lstuid, alist=getonepage(myurl)
    if len(lstrship)>0:
        with open(shipfile,'a') as apw:
            apw.write('\r\n'+'\r\n'.join(lstrship))
    if len(lstuid)>0:
        with open(uidfile, 'a', encoding='utf-8') as apw:
            apw.write('\r\n'+'\r\n'.join(lstuid))
    with open('blist.txt', 'a', encoding='utf-8') as apw:
        if type(alist)==type({}):
            ll=alist.values()
            ll1=['\t'.join(x) for x in ll ]
            apw.write('\r\n' + '\r\n'.join(ll1))

    for url in newurl:
        GetSt(url)


GetSt(sturl)

