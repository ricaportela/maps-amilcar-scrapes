from scrapy.spiders import Spider
from scrapy.crawler import CrawlerProcess
from scrapy_splash import SplashRequest
from scrapy_selenium import SeleniumRequest


class MapListing(Spider):
    name = "map_listings"

    # url = "http://www.google.com/maps/search/aeroporto+internacional+brasilia+-+df+/@-15.869741,-47.9329117,15z/data=!3m1!4b1"
    url = "http://www.google.com/maps/search/escolas+asa+norte+-+df+/@-15.7953701,-47.9749206,12z"

    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
    }

    def start_requests(self):
        # yield scrapy.Request(url=self.url, headers=self.headers, callback=self.parse)
        # yield SplashRequest(
        #     self.url,
        #     self.parse,
        #     headers=self.headers,
        #     args={"wait": 2, "lua_source": script, "timeout": 3600},
        #     endpoint="execute"
        # )
        script = """
                    function main(splash)
                        assert(splash:go(splash.args.url))
                        assert(splash:wait(5))
                        assert(splash:runjs("window.scrollTo(0,document.body.scrollHeight)"))
                        assert(splash:wait(5))
                        return {
                            html = splash:html(),
                            url = splash:url(),
                        }
                    end
                """
        yield SplashRequest(
            self.url,
            self.parse,
            headers=self.headers,
            args={
                "wait": 5,
                "lua_source": script,
                "timeout": 15
            },
            endpoint="execute"
        )

        # yield SeleniumRequest(
        #     url=self.url,
        #     wait_time=3,
        #     screenshot=True,
        #     callback=self.parse,
        #     dont_filter=True,
        #     script="window.scrollBy(0, window.innerHeight);"
        # )

    def parse(self, response):
        for div in response.xpath(
            '//div[contains(@aria-label, "Resultados")]/div/div[./a]'
        ):
            descricao = div.xpath("./a/@aria-label").extract_first("")
            yield {"descricao": descricao}


# run scraper
# process = CrawlerProcess()
# process.crawl(MapListing)
# process.start()


# scrollable_div = driver.find_element_by_css_selector(
#  'div.section-layout.section-scrollbox.scrollable-y.scrollable-show'
#                      )
# driver.execute_script(
#                'arguments[0].scrollTop = arguments[0].scrollHeight',
#                 scrollable_div
#                )
