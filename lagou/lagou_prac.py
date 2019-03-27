import requests
import json
import xlwt

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
           'Referer': 'https://www.lagou.com/jobs/list_Python?labelWords=&fromSearch=true&suginput='}
cookie = {'Cookie': 'user_trace_token=20170511090658-22147103-35e6-11e7-bbcb-5254005c3644; LGUID=20170511090658-22147724-35e6-11e7-bbcb-5254005c3644; JSESSIONID=ABAAABAAAGGABCB6C3F9494954BF306F100881C53979986; _gat=1; PRE_UTM=m_cf_cpt_sogou_pc; PRE_HOST=www.sogou.com; PRE_SITE=https%3A%2F%2Fwww.sogou.com%2Fsgo%3Fquery%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%26pid%3Dsogou-wsse-ae06fbdc519bddaa-1661%26st%3D5%26func%3Dcb312606%26st2%3D2%26pos%3D5%26lkx%3D0%26dti%3D0_7111_541_0_131_814_0_0_0_0_0%26reqid%3D00130FCE%26ie%3Dutf8; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F%3Futm_source%3Dm_cf_cpt_sogou_pc; _putrc=DC4F7281CC0D89BA; login=true; unick=%E5%BD%AD%E4%B8%9C%E6%88%90; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; _ga=GA1.2.253575676.1494464824; _gid=GA1.2.788897204.1507702863; LGSID=20171011142100-5a11873c-ae4c-11e7-88dd-525400f775ce; LGRID=20171011142133-6da4e78a-ae4c-11e7-948c-5254005c3644; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1507517370,1507553208,1507602637,1507702863; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1507702896; TG-TRACK-CODE=search_code; SEARCH_ID=09a50e59bf20492ca05b914e5876cd20; index_location_city=%E5%85%A8%E5%9B%BD'}

items = []
def get_html(url):
    request = requests.get(url, cookies=cookie, headers=headers)
    response = request.text
    # response = request.content.decode('utf-8')
    html = json.loads(response)
    # print(html)
    for i in range(15):
        item = []
        item.append(str(html['content']['positionResult']['result'][i]['positionName']))
        item.append(str(html['content']['positionResult']['result'][i]['companyFullName']))
        item.append(str(html['content']['positionResult']['result'][i]['salary']))
        item.append(str(html['content']['positionResult']['result'][i]['city']))
        item.append(str(html['content']['positionResult']['result'][i]['positionAdvantage']))
        item.append(str(html['content']['positionResult']['result'][i]['companyLabelList']))
        item.append(str(html['content']['positionResult']['result'][i]['firstType']))
        items.append(item)
    return items

def write_excel(items):
    newTable = 'lagou_1.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('test')
    head_data = ['职位名称', '公司名称', '薪资', '工作地点', '福利', '提供条件', '工作类型']
    for column in range(0, 7):
        ws.write(0, column, head_data[column], xlwt.easyxf('font: bold on'))

    index = 1
    for item in items:
        for i in range(0, 7):
            print(item[i])
            ws.write(index, i, item[i])
        index += 1
    wb.save(newTable)

if __name__ == '__main__':
    # start_url = 'https://www.lagou.com/jobs/list_Python?labelWords=&fromSearch=true&suginput='
    start_url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&isSchoolJob=0'
    data_info = get_html(start_url)
    write_excel(data_info)
