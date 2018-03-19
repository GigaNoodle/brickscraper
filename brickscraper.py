#currently grabs the set name and the number of pieces and
#outputs them to terminal.
import scrapy

class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider"
    start_urls = ['http://brickset.com/sets/year-2016']

    def parse(self, response):
        SET_SELECTOR = '.set'
        #infile1 = open("scrapedata.txt", "w")

        for brickset in response.css(SET_SELECTOR):
            
            NAME_SELECTOR = 'h1 ::text'
            PIECE_SELECTOR = 'dd ::text'
            yield {
                'name': brickset.css(NAME_SELECTOR).extract_first(),
                'pieces': brickset.css(PIECE_SELECTOR).extract_first(),

            }
            #infile1.write()
            #infile1.close()
            #infile1.write(NAME_SELECTOR)
            #infile1.write(PIECE_SELECTOR)
