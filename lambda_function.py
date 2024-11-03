import json
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from pizzareview.spiders.pizza_spider import BarstoolSpider  # Changed from PizzaSpider to BarstoolSpider

def lambda_handler(event, context):
    try:
        settings = get_project_settings()
        
        settings.update({
            'FEEDS': {
                '/tmp/pizza_spider_test.csv': {
                    'format': 'csv',
                    'overwrite': True
                }
            }
        })
        
        process = CrawlerProcess(settings)
        process.crawl(BarstoolSpider)  # Changed from PizzaSpider to BarstoolSpider
        process.start()
        
        with open('/tmp/pizza_spider_test.csv', 'r') as f:
            csv_content = f.read()
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Spider completed successfully',
                'csv_content': csv_content
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error occurred: {str(e)}')
        }