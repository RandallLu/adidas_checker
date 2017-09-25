from termcolor import colored

class util:

    user_Agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2)AppleWebKit/537.36 (KHTML, like Gecko) Chrome 55.0.2883.5 Safari/537.36"

    header ={
    "User-Agent": user_Agent,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4",
    "Accept-Encoding":"gzip, deflate",
    "Upgrade-Insecure-Requests": "1",
    "Connection": "close"
    }

    stock_url = "http://www.adidas.com/on/demandware.store/Sites-adidas-US-Site/en_US/Product-GetVariants?pid="

    order_url = "https://www.adidas.com/us/order-tracker"

    def red(string):
        return colored(string, "red")

    def green(string):
        return colored(string, "green")

    def yellow(string):
        return colored(string, "red")
