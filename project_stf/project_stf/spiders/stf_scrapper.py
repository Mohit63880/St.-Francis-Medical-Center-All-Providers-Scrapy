"""
    To run this file first install some required library
    1. scrapy  (pip install scrapy)
    2. beautifulsoup (pip install bs4)
    3. requests (pip install requests)
    4. lxml (pip install lxml)
"""

from gc import callbacks

import bs4
import scrapy
from scrapy import FormRequest
from scrapy.exceptions import CloseSpider
from bs4 import BeautifulSoup
import requests
import lxml




class StfSpider(scrapy.Spider):
    name = 'stf_scrapper'
    start = 1
    incremented_by = 1
    allowed_domains = ['www.stfrancismedicalcenter.com']
    start_urls = [
        'https://www.stfrancismedicalcenter.com/find-a-provider/?fbclid=IwAR0Gwi2H4D1uqJTOQnCsPcbGhf8EH8_B7z-ZdbsPr8xsMN-9TbY4E-EoPc4']

    def parse(self, response):
        if self.start <= 36:
            yield FormRequest.from_response(
                response,
                formxpath="//form[@id='Form_FindAPhysician']",
                formdata={
                    '_m_': 'FindAPhysician',
                    'PhysicianSearch$HDR0$PhysicianName': '',
                    'PhysicianSearch$HDR0$SpecialtyIDs': '',
                    'PhysicianSearch$HDR0$Distance': '5',
                    'PhysicianSearch$HDR0$ZipCodeSearch': '',
                    'PhysicianSearch$HDR0$Keywords': '',
                    'PhysicianSearch$HDR0$LanguageIDs': '',
                    'PhysicianSearch$HDR0$Gender': '',
                    'PhysicianSearch$HDR0$InsuranceIDs': '',
                    'PhysicianSearch$HDR0$AffiliationIDs': '',
                    'PhysicianSearch$HDR0$NewPatientsOnly': '',
                    'PhysicianSearch$HDR0$InNetwork': '',
                    'PhysicianSearch$HDR0$HasPhoto': '',
                    'PhysicianSearch$FTR01$PagingID': f"{self.start}"
                },
                callback=self.aftersf
            )
        else:
            raise CloseSpider("End of session")

        self.start += self.incremented_by
        yield scrapy.Request(
            url='https://www.stfrancismedicalcenter.com/find-a-provider/?fbclid=IwAR0Gwi2H4D1uqJTOQnCsPcbGhf8EH8_B7z-ZdbsPr8xsMN-9TbY4E-EoPc4',
            callback=self.parse
        )
    def aftersf(self, response):
        for item in response.xpath("//li[@data-role='tr']"):
            url=response.urljoin(item.xpath(".//a/@href").get())
            yield response.follow(url=url,callback=self.getData)
            
    def getData(self,response):
        Address=self.NoneVal(response.xpath(".//article/div[1]/ul/li/address").extract())
        Practice=self.NoneVal(response.xpath(".//article/div[1]/ul/li/strong/text()").get())
        try:
            Address=Address[0].replace("<address>","").replace("</address>","").split("<br>")
        except:
            pass
        try:
            cityStateZip=Address[1].split(",")
            City=cityStateZip[0]    
        except:
            City=""
        try:
            stateZip=cityStateZip[1].strip().split(" ")
            State=stateZip[0]
        except:
            State=""
        try:
            Zip=stateZip[1]    
        except:
            Zip=""
        try:
            Address=', '.join(Address[:2]).strip()
        except:
            Address=""
        yield{
            "Full_Name": self.NoneVal(response.xpath(".//article/h1/text()").get()),
            "Specialty":self.NoneVal(response.xpath(".//li[2]/div/span/a/text()").get()),
            "Add_Speciallity":self.NoneVal(response.xpath(".//li[3]/span/a/text()").get()),
            'Full_Address':f"{Practice}{Address}",
            "Phone": self.NoneVal(response.xpath(".//address/a/text()").get()),
            'Practice':Practice,
            'Address':Address,
            'City':City,
            'State':State,
            'Zip':Zip,
            'URL':str(response).replace("<200","").replace(">","").strip()
        }
    def NoneVal(self,val):
        return val if val!=None else ""
            