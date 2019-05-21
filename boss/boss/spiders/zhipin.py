# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class ZhipinSpider(CrawlSpider):
    name = 'zhipin'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/c101020100/?query=python&page=3&page-1']

    rules = (
        # 匹配职位列表页的规则
        Rule(LinkExtractor(allow=r'.+\?query=python&page=\d&ka=page-1'),
             follow=True),
        Rule(LinkExtractor(allow=r'.+job_detail/\w+~.html'),
             callback="parse_job",
             follow=False),
    )

    def parse_job(self, response):
        title = response.xpath("//div[@class='name']/h1/text()").get("").strip()
        salary = response.xpath("//span[@class='salary']/text()").get("").strip()
        info_job = response.xpath("//div[@class='job-primary detail-box']/div[@class='info-primary']/p/text()").getall()
        city = info_job[0]
        work_years = info_job[1]
        education = info_job[2]
        company = response.xpath("//div[@class='company-info']//a/@title").get("").strip()
        content = response.xpath("//div[@class='text']/text()").getall()
        content = '\n'.join(content)
        from boss.items import BossItem
        item = BossItem(name=title,salary=salary,
                        city=city,work_years=work_years,
                        education=education,company=company,
                        content=content)
        yield item
