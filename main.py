#!/usr/bin/env python
# Simple Python web scraper to capture some elements in
# HTML page (eg. price fluctuation of 3 products)
from lxml import html
import requests

def fetch():
    ssd_page = requests.get('http://www.emag.ro/solid-state-drive-ssd-samsung-850-evo-2-5-250gb-sata-iii-mz-75e250b-eu/pd/DCJ9BMBBM/')
    ram_page = requests.get('http://www.emag.ro/memorie-kingston-8gb-1600mhz-ddr3-non-ecc-cl11-sodimm-kvr16ls11-8/pd/D7LCXBBBM/')
    rack_page = requests.get('http://www.emag.ro/rack-extern-njoy-speedbox-2-5-usb-3-0-negru-phas-2530s0s-ap01b/pd/D8FC6BBBM/')

    ssd_tree = html.fromstring(ssd_page.content)
    ram_tree = html.fromstring(ram_page.content)
    rack_tree = html.fromstring(rack_page.content)

    ssd_price = ssd_tree.xpath('//*[@id="main-container"]/section[1]/div/div/div[1]/div[2]/div[2]/div/form/div/div[2]/div[1]/p[3]/text()')
    ram_price = ram_tree.xpath('//*[@id="main-container"]/section[1]/div/div/div[1]/div[2]/div[2]/div/form/div/div[2]/div[1]/p/text()')
    rack_price = rack_tree.xpath('//*[@id="main-container"]/section[1]/div/div/div[1]/div[2]/div[2]/div/form/div/div[2]/div[1]/p/text()')

    # debugging to cleanup print result
    # print((ssd_price[0]).replace(' ',''))

    print('250 GB Samsung SSD: ', ssd_price)
    print('8 GB RAM DDR3 Kingston: ', ram_price)
    print('nJoy Rack 2.5inch: ', rack_price)


if __name__ == "__main__":
    fetch()
