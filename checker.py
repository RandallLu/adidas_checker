import requests
import re
import bs4
from pprint import pprint
from termcolor import colored
from util import util
from datetime import datetime



def checkStock():
    proxy={
    # go get a public proxy
    "http":"http://{}".format("52.43.175.248:3128"),
    "https":"http://{}".format("52.43.175.248:3128")
    }

    pid = input("Please enter Pid: ")
    url = util.stock_url + pid
    header = util.header

    session = requests.session()
    res = session.get(url, headers=header)
    #res = session.get(url, headers=header, proxies=proxy)
    try:
        variants = res.json()["variations"]["variants"]
    except Exception as error:
        print("Retrive stock failed, code: {}".format(res.status_code))
        return

    ID = 0
    ATS = 0
    T_ATS = 0
    print("{}".format("Stock check".center(20," ")))
    print("-------------------")
    for each in variants:
        ID = each['id']
        ATS = each['ATS']
        T_ATS += ATS
        print("{0}|{1}".format(
        "{}".format(each['attributes']['size']).center(8," "),
        colored(str(each["ATS"]).center(12," "), 'green' if ATS!= 0 else 'red')))
        print("-------------------")
        print("Total stock: {}".format(colored(T_ATS,'green')))


def checkOrder():
    try:
        input_file = open("order.txt", "r")
    except OSError:
        # error handle
        print("cannot open order.txt file")
        print("if no such file, please create one with your order info as email:orderNo")
        return
    confirmed_orders = []
    total = 0
    for i in input_file:
        total += 1
        if i != '':
            splits = i.split(":")
            email = splits[0]
            orderNo = splits[1]
            # for each order we call the helper method once
            if checkOrderHelper(email, orderNo) == True:
                confirmed_orders.append(splits)

    confirmed_num = len(confirmed_orders)
    not_confirmed = total - confirmed_num
    print("For total {} orders, you have {} confirmed and {} not valid".format(total, confirmed_num, not_confirmed))
    input_file.close()


def checkOrderHelper(email, orderNo):
    url = util.order_url
    header = util.header
    session = requests.session()
    res = session.get(url, headers=header)
    if(res.status_code != "200"):
        print("Cannot open page, error code:", res.status_code)
        return

    #first of all we need to fill out the submit form
    soup = bs4.BeautifulSoup(res.content, "html.parser")
    actionUrl = soup.find('form', {'id' : 'dwfrm_ordersignup'})['action']
    data = {
    "dwfrm_ordersignup_orderNo": orderNo,
    "dwfrm_ordersignup_email": email,
    "dwfrm_ordersignup_signup": "Track order"
    }

    res = session.post(url, headers=header, data=data)
    soup = bs4.BeautifulSoup(res.content, "html.parser")
    # find the div where the order-step is selected
    parts = soup.find('div', {'class': 'order-step selected'})
    for part in parts:
        result = part.find('div', {'class': 'order-step-content-wrp'})
        result = (result.text).strip()
        if str(result) == "Delivered":
            print("Order {}:{} is Delivered".format(email,orderNo))
            return True
        if str(result) == "Preparing shipment":
            print("Order {}:{} is preparing shipment".format(email,orderNo))
            return True
        if str(result) == "Order processing":
            print("Order {}:{} is process".format(email,orderNo))
            return True
    #reach here then the order is not valid
    print("Order {}:{} is not valid".format(email, orderNo))
    return False


#main driver
if __name__ == '__main__':
    print(datetime.now(), "Welcome to Checker!")
    print(datetime.now(),"What do you want to do ?")
    print(datetime.now(),"A: check orders  B: check stock")
    method = input("Enter: (A/B)")
    if method == 'A':
        checkOrder()
    else:
        checkStock()
    input('\n',datetime.now(),"press any key to exit")
    print(datetime.now(),"See you next time!")
