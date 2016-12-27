#! /usr/bin/env/python3

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('/Applications/Firefox.app/Contents/MacOS/firefox')
browser = webdriver.Firefox(firefox_binary=binary)