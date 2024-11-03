import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import BarstoolItem

class BarstoolSpider(CrawlSpider):
    name = "pizza_spider"
    allowed_domains = ["onebite.app"]
    start_urls = ["https://onebite.app/reviews/dave?page=1&minScore=0&maxScore=10"]

    rules = (
        Rule(LinkExtractor(allow=(r"page=",)), callback='parse_page', follow=True),
    )

    def parse_page(self, response):
        reviews = response.css('div.jsx-2655995184.reviewCard')
        for review in reviews:
            item = BarstoolItem()
            item['restaurant'] = review.css('h2.jsx-2655995184.reviewCard__title::text').get()
            item['dave_score'] = review.css('p.jsx-407081529.rating__score::text').get()
            city_state = review.css('p.jsx-2655995184.reviewCard__location::text').get()
            #item['city_and_state'] = review.css('p.jsx-2655995184.reviewCard__location::text').get()
            if ',' in city_state:
                item['city'], item['state'] = [part.strip() for part in city_state.split(',', 1)]
            else:
                item['city'] = city_state
                item['state'] = None
            item['dave_visit_time'] = review.css('p.jsx-107e6328b2507bd6.userMeta__timestamp::text').get()
            yield item