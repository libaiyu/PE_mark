#! python3

>>> import requests
>>> import bs4

>>> from selenium import webdriver
>>> browser = webdriver.Firefox()
>>> type(browser)
<class 'selenium.webdriver.firefox.webdriver.WebDriver'>
>>> browser.get('http://www.ecit.cn')
>>> 
