# -*- coding:utf-8 -*-
import requests
import bs4

def GetPageMain():
	lst=[]
	sturl='http://xianhuo.dzsc.com/agentlist.aspx?page={page}'
	for i in range(1,5):
		r=requests.get(sturl.format(page=str(i)))
		txt=r.text
		soup=bs4.BeautifulSoup(txt, 'html.parser')

		bl = soup.find_all(name='div', attrs={"class": "bradlist"})
		for oneb in bl:
			nm=oneb.find(name='a', attrs={"class": "f14"})
			if nm is None:
				continue
			name=nm.get_text()
			nm1 = oneb.find(name='b', attrs={"class": "daili"})
			daili = nm1.get_text()
			nm2 = oneb.find(name='a', attrs={"class": "enter"})
			#lst.append(nm2['href'].split('.')[0].split('/')[-1]+'\t'+name+'\t'+daili)
			lst.append(nm2['href'].split('.')[0].split('/')[-1])

	# with open('qy.txt','w') as fw:
	# 	fw.write('\n'.join(lst))
	return lst



def GetPageMain1():
	lst=[]
	sturl='http://xianhuo.dzsc.com/agentlist.aspx?page={page}'
	for i in range(1,5):
		r=requests.get(sturl.format(page=str(i)))
		txt=r.text
		soup=bs4.BeautifulSoup(txt, 'html.parser')
		alist=soup.find_all(name='a', attrs={"class": "enter"})
		for onea in alist:
			lst.append(onea['href'])
	return lst



def GetShangPin(tb):
	lst=[]
	goods=tb.find_all(name='dd')
	for ga in goods:
		g=ga.find_all(name='span')
		if g and len(g)==7:
			lst.append([g[0].get_text(),g[1].get_text(),g[2].get_text(),g[3].get_text(),
			            g[4].get_text(),g[5].get('title')])
			a=g[6].find('a')
			if a is not None:
				lst[-1].append(a.get('href'))

	return lst



def GetChildPage():
	sturls=GetPageMain1()
	st=True
	for u in sturls:
		r = requests.get(u)
		txt = r.text
		soup = bs4.BeautifulSoup(txt, 'html.parser')
		divlist=soup.find_all(name='div', attrs={"class": "stocklist"})
		if divlist and len(divlist)>0:
			tb=divlist[0]

			with open(u.split('.')[0].split('/')[-1]+'.csv','a',encoding='utf-8') as fw:
				clst=GetShangPin(tb)
				llll=[('\t'.join(x)).replace('\x0a','') for x in clst]
				fw.write('\n'.join(llll)+'\n')
				idx=0
				print(u,idx)
				page = soup.find(name='div', attrs={"class": "page"})
				u0=None
				if page is not None:
					u0 = page.find('ul')
				l0=None
				if u0 is not None:
					l0 = u0.li
				if l0 is not None and l0.next:
					tpb=l0.next
					tp=str(tpb)
					p=tp.split()[0].split('/')
					if len(p)>1:
						f=p[1].replace('页','').strip()
						fint=int(f)
						for jj in range(2,fint+1):
							nu=u[:-1]+'_'+str(jj)+'/'
							print(nu, jj)
							r1 = requests.get(nu)
							txt1 = r1.text
							soup1 = bs4.BeautifulSoup(txt1, 'html.parser')
							divlist1 = soup1.find_all(name='div', attrs={"class": "stocklist"})
							if divlist1 and len(divlist1) > 0:
								tb1 = divlist1[0]
								clst1 = GetShangPin(tb1)
								llll1 = [('\t'.join(x)).replace('\x0a','') for x in clst1]
								fw.write('\n'.join(llll1)+'\n')


def GetShangPin1(tb):
	lst=[]
	goods=tb.find_all(name='li')
	for ga in goods:
		g=ga.find_all(name='div')
		if g and len(g)==7:
			if g[0].get_text()=='型号':
				continue
			lst.append([g[0].get_text(),g[1].get_text(),g[2].get_text(),g[3].get_text(),
			            g[4].get_text(),g[5].get_text()])
			a=g[6].find('a')
			if a is not None:
				lst[-1].append(a.get('href'))

	return lst
def GetChildPage1(sturls):
	st=True
	for u in sturls:
		r = requests.get(u)
		txt = r.text
		soup = bs4.BeautifulSoup(txt, 'html.parser')
		divlist=soup.find_all(name='div', attrs={"class": "table-item"})
		if divlist and len(divlist)>0:
			tb=divlist[0]

			with open(u.split('.')[0].split('/')[-1]+'.csv','a',encoding='utf-8') as fw:
				clst=GetShangPin1(tb)
				llll=[('\t'.join(x)).replace('\x0a','') for x in clst]
				fw.write('\n'.join(llll)+'\n')
				idx=0
				print(u,idx)
				page = soup.find(name='div', attrs={"class": "pagination"})
				u0=None
				if page is not None:
					u0 = page.find_all('a')
				l0=None
				if u0 is not None:
					l0 = u0[-2]
				if l0 is not None:
					tp=l0.get_text()
					p=tp
					if len(p)>0:
						f=p.strip()
						fint=int(f)
						for jj in range(2,fint+1):
							nu=u[:-1]+'_'+str(jj)+'/'
							print(nu, jj)
							r1 = requests.get(nu)
							txt1 = r1.text
							soup1 = bs4.BeautifulSoup(txt1, 'html.parser')
							divlist1 = soup1.find_all(name='div', attrs={"class": "table-item"})
							if divlist1 and len(divlist1) > 0:
								tb1 = divlist1[0]
								clst1 = GetShangPin1(tb1)
								llll1 = [('\t'.join(x)).replace('\x0a','') for x in clst1]
								fw.write('\n'.join(llll1)+'\n')



import os
def mg():
	filepath='excel'
	files = os.listdir(filepath)
	lstf=[]
	for fi in files:
		fi_d = os.path.join(filepath, fi)
		if os.path.isdir(fi_d):
			pass
		else:
			pt=fi_d
			if pt.split('.')[-1]!='csv':
				continue
			lstf.append(fi.split('.')[0])
			with open('excel/all.txt','a') as fw:
				with open(pt,'r') as fr:
					print(pt)
					fw.writelines(fr.readlines())

	return lstf


def compare():
	l1=GetPageMain()
	l2=mg()
	u='http://{}.dzsc.com/spot/'
	ul=[]
	for l in l1:
		if l not in l2:
			ul.append(u.format(l))
	GetChildPage1(ul)

#mg()
#GetChildPage()

#GetPageMain()

#compare()
