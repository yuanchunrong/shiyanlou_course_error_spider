#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from lxml import etree
import requests

start_page = input("please enter the start_page_num:")
end_page = input("please enter the end_page_num:")
month = input("please enter the month:")

urls = []
usernames = []
username_nums = {}

for i in range(int(start_page),int(end_page)+1):
    index_url = 'https://www.shiyanlou.com/questions/?type=course_error&page={}'.format(i)
    data = requests.get(index_url).text

    s = etree.HTML(data)
    file = s.xpath('//div[@class="tab-content"]/div/ul/li')

    for div in file:
        href = div.xpath('./div[1]/div[2]/h4/a/@href')[0]
        time = div.xpath('./div[1]/div[2]/div/span[1]/text()')[0]

        if (1 <= int(month)) and (int(month) <= 8):
            correct_month = '0' + month
            next_month = '0' + str(int(month)+1)
        elif int(month)==9:
            correct_month = '0' + month
            next_month = '10'
        elif int(month)==10 or int(month)==11:
            correct_month = month
            next_month = str(int(month)+1)
        elif int(month)==12:
            correct_month = month
            next_month = '01'

        start_time = '2018-' + correct_month + '-01 00:00:00'
        end_time = '2018-' + next_month + '-01 00:00:00'
        if not '前' in time:
            if (start_time <= time) and (time < end_time):
                correct_url = 'https://www.shiyanlou.com' + href
                urls.append(correct_url)


with open('check_data.txt','w',encoding='utf-8') as f:
    for url in urls:
        data = requests.get(url).text
        s = etree.HTML(data)
        file = s.xpath('//div[@class="content question-detail"]')

        for div in file:
            title = div.xpath('./div[1]/span[1]/text()')
            username = div.xpath('./div[2]/div[2]/a/text()')[0].strip()
            time = div.xpath('./div[2]/span[1]/text()')[0]
            answer_contents = div.xpath('./div[4]/div[1]/div[2]/div[1]/textarea/text()')
            if answer_contents:
                if ("谢谢" in answer_contents[0]) or ("感谢" in answer_contents[0]) or ("指正" in answer_contents[0]) or ("修复" in answer_contents[0]) or ("修改" in answer_contents[0]) or ("修正" in answer_contents[0]) or ("纠正" in answer_contents[0]) or ("更正" in answer_contents[0]) or ("完善" in answer_contents[0]):
                    url_file = open('urls.txt','a')
                    url_file.write("{}\r\n".format(url))
                    url_file.close()
                    usernames.append(username)
                    f.write("{},{},{},{},{}\r\n".format(url,title,username,time,answer_contents))


for i in usernames:
    if usernames.count(i) >= 1:
        username_nums[i] = usernames.count(i)

sorted_username_nums = sorted(username_nums.items(),key = lambda x:x[1],reverse=True)


with open('usernames.txt','w',encoding='utf-8') as f:
    for line in sorted_username_nums:
        f.write("{}:{}\n".format(line[0],line[1]))

