from termcolor import colored

class util:

    user_Agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"

    header = {
    "Host": "www.adidas.com",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": user_Agent,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4"
    }

    stock_url = "http://www.adidas.com/on/demandware.store/Sites-adidas-US-Site/en_US/Product-GetVariants?pid="

    order_url = "https://www.adidas.com/us/order-tracker"

    def red(string):
        return colored(string, "red")

    def green(string):
        return colored(string, "green")

    def yellow(string):
        return colored(string, "red")
