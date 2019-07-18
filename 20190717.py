# -*- coding:utf-8 -*-
# @Time   : 2019/7/18 22:28
# @File   : 20190717.py
# @Author :Vsonli
from selenium import webdriver


driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.maximize_window()

driver.get('https://www.ketangpai.com/Main/index.html')

#返回上一个页面
driver.back()
#进行到下一个页面
driver.forward()
#刷新
driver.refresh()
'''
6种  单一属性找元素 ID  NAME CLASS TAGNAME

2种   各种方式找元素 CSS  XPATH
'''
#is_enabled：元素当前是否可用
#is_displayed：元素是否可见
ele = driver.find_element_by_id('kw')  #WebElement类
print(ele.get_attribute('class'))  #获取属性值
driver.find_elements_by_name('wd')  #元素列表
driver.find_element_by_class_name('bg') #class有多个值，只能填一个class属性
driver.find_element_by_tag_name('span') #标签名称 可以有多个值，用elements

driver.find_element_by_link_text('更多产品')    #精确匹配文本值
driver.find_element_by_partial_link_text('产品')  #通过部分内容匹配文本值


'''
120.78.128.25:8765/index/login.html
Xpath，序列从1开始
账号输入框：
    /html/body/div[2]/div/form/div[1]/imput
    绝对定位：/开头,严格按照层级，再按照同级元素的位置进行寻找
        但是如果某个元素被人修改了，例如原本的div[2]前面多了个div，变成了div[3]，就会有问题
    
    相对定位：//开头   在参照物之下，只要符合条件的元素存在就可以
        
    
'''
#driver.close()：关闭窗口，quit()关闭会话，关闭浏览器/杀掉chromedriver进程
driver.quit()
