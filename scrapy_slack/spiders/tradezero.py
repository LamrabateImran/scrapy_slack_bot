import scrapy
import os
from scrapy import cmdline

class TradezeroSpider(scrapy.Spider):
    name = 'tradezero'
    allowed_domains = ['https://www.tradezero.co/hotshorts']
    start_urls = ['https://www.tradezero.co/hotshorts']

    def parse(self, response):
        words = response.css('.anchor::text').extract()
        #send slack message
        def listToString(s): 
            # initialize an empty string
            str1 = " " 
            # return string  
            return (str1.join(s))
        data = listToString(words)
        payload ={"text":data.replace('$','')}
        #write cmd command 
        cmd = """curl -X POST -H 'Content-type: application/json' --data \"{0}\" https://hooks.slack.com/services/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"""
        sf = cmd.format(payload)
        os.system(sf)
        scraped_info = {
                            'Words' : words,
                        }
        yield scraped_info

cmdline.execute("scrapy crawl tradezero".split())
        
#/Library/Frameworks/Python.framework/Versions/3.10/bin/python3 /Users/ab/Documents/slack/scrapy_slack/scrapy_slack/spiders/tradezero.py