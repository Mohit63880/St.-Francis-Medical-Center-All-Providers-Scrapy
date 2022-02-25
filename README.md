# St.-Francis-Medical-Center-All-Providers-Scrapy
Scrape all provider profile information from "https://www.stfrancismedicalcenter.com/find-a-provider/" using Scrapy

1. First you need to install some required libraries
    1. scrapy  (pip install scrapy)
    2. scrapy_cloudflare_middleware (pip install scrapy_cloudflare_middleware)
    2. beautifulsoup (pip install bs4)
    3. requests (pip install requests)
    4. lxml (pip install lxml)
    

2. write those code on your settings.py file
DOWNLOADER_MIDDLEWARES = {
    ###### The priority of 560 is important, because we want this middleware to kick in just before the scrapy built-in `RetryMiddleware`.
    'scrapy_cloudflare_middleware.middlewares.CloudFlareMiddleware': 560
}

DUPEFILTER_CLASS = "scrapy.dupefilters.BaseDupeFilter"

# Coded by : Anas bin hasan bhuiyan
Github link:- https://github.com/anas-bhuiyan/stf?fbclid=IwAR2dR7GJs-04JihAesh6Q5bs_CHU9epwAp_vj0dIhUYex8X85pn0ea5a7a0

# Upgraded by:- Mohit Anand Srivastava
Github link: -https://github.com/Mohit63880/St.-Francis-Medical-Center-All-Providers-Scrapy
Facebook:- https://www.facebook.com/mohitanand.srivastava/
Instagram:-https://www.instagram.com/mohit_anand_srivastava/
Hacker Rank:-https://www.hackerrank.com/mohitracer1234

