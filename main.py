#!/usr/bin/env python
# Simple Python web scraper to capture some elements in
# HTML page (eg. price of a product)
from lxml import html
import requests

def func():
    ssd_page = requests.get('http://www.emag.ro/solid-state-drive-ssd-samsung-850-evo-2-5-250gb-sata-iii-mz-75e250b-eu/pd/DCJ9BMBBM/')
    ram_page = requests.get('http://www.emag.ro/memorie-kingston-8gb-ddr3-1333mhz-non-ecc-cl9-1-5v-kvr1333d3n9-8g/pd/EBQRDBBBM/')
    rack_page = requests.get('http://www.emag.ro/rack-extern-njoy-speedbox-2-5-usb-3-0-negru-phas-2530s0s-ap01b/pd/D8FC6BBBM/')

    ssd_tree = html.fromstring(ssd_page.content)
    ram_tree = html.fromstring(ram_page.content)
    rack_tree = html.fromstring(rack_page.content)

    ssd_price = tree.xpath('//*[@id="main-container"]/section[1]/div/div/div[1]/div[2]/div[2]/div/form/div/div[2]/div[1]/p[3]/text()')
    ram_price = tree.xpath('//*[@id="main-container"]/section[1]/div/div/div[1]/div[2]/div[2]/div/form/div/div[2]/div[1]/p/text()')
    rack_price = tree.xpath('//*[@id="main-container"]/section[1]/div/div/div[1]/div[2]/div[2]/div/form/div/div[2]/div[1]/p/text()')


if __name__ == "__main__":
    func()

