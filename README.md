# TencentJobsCrawling
使用scrapy爬取腾讯招聘信息，爬去地址为：https://hr.tencent.com/position.php ，
爬取的信息包括：招聘岗位，岗位类别，招聘人数，工作地点，发布时间和招聘具体链接。

## 1.创建项目
在cmd使用scrapy startproject+项目名称在所选路径创建项目

## 2.编辑items
使用scrapy.Field()为每一项定义爬取区域

## 3.编辑spiders
在项目文件夹内，使用命令创建一个爬虫：
scrapy genspider+爬虫名称+初始url，之后到spiders文件下，编辑spiders.py文件，这里使用xpath进行网页内容的解析，用extract_first()方法进行提取。

## 4.编辑pipelines
这里编辑了两段代码，分别将item数据保存为json文件和csv文件

## 5.编辑settings
在settings.py中，注册爬虫的管道信息，如：ITEM_PIPELINES = {
    'tencent.pipelines.TencentPipeline': 300,
}

## 6.运行程序
在项目文件夹内使用命令行，scrapy crawl+爬虫名称，运行爬虫
