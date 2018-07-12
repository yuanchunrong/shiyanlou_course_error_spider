# shiyanlou_course_error_spider
主要用于实验楼网站每个月课程纠错的数量统计。

## 使用方法
```
$ sudo pip3 install -r requirements.txt
$ python3 shiyanlou_course_error_spider.py
please enter the start_page_num:   #输入开始爬取页面的ID号
please enter the end_page_num:     #输入结束爬取页面的ID号
please enter the month:            #输入需要获取数据的月份
```

生成的文件为:
+ `check_data.txt`: 经过月份以及关键词过滤后的有效纠错详情页信息，格式为：URL地址，纠错标题title，用户名username，纠错时间datetime，第一条消息回复内容answer_contents
+ `urls.txt`: 有效纠错页面的urls
+ `usernames.txt`: 有效纠错的用户名以及次数统计，格式为：username:total_nums
