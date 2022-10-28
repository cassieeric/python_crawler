# -*- coding: utf-8 -*-
from selenium import webdriver
browser = webdriver.Chrome()
browser.get("http://www.baidu.com")
browser.find_element_by_id("kw")
browser.find_element_by_name("wd")
browser.find_element_by_class_name("s_ipt")
browser.find_element_by_tag_name("input")
browser.find_element_by_link_text("hao123")

# Xpath定位方法
browser.find_element_by_xpath("//*[@id='kw']")
browser.find_element_by_xpath("//*[@name='wd']")
browser.find_element_by_xpath("//input[@class='s_ipt']")
browser.find_element_by_xpath("/html/body/form/span/input")
browser.find_element_by_xpath("//span/span[@class='soutu-btn']/input")
browser.find_element_by_xpath("//form[@id='form']/span/input")
browser.find_element_by_xpath("//input[@id='kw' and @name='wd']")

# CSS Selector定位方法
browser.find_element_by_css_selector("#kw")
browser.find_element_by_css_selector("[name=wd]")
browser.find_element_by_css_selector(".s_ipt")
browser.find_element_by_css_selector("html>body>form>span>input")
browser.find_element_by_css_selector("span.soutu-btn>input#kw")
browser.find_element_by_css_selector("span.soutu-btn>span[name='wd']")
browser.find_element_by_css_selector("form#form>span>input")

