# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
# import time
# from selenium.webdriver import ActionChains

# if __name__ == '__main__':

    # 动态渲染页面爬取
    # browser = webdriver.Chrome()
    # browser.get("https://www.baidu.com")
    # inputs = browser.find_element_by_id('kw')
    # inputs.send_keys('Python')
    # inputs.send_keys(Keys.ENTER)
    # wait = WebDriverWait(browser, 10)
    # wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
    # print(browser.current_url)
    # print(browser.get_cookies())
    # print(browser.page_source)
    # finally:
    #     browser.close()

    # 1.声明浏览器对象
    # browser = webdriver.Chrome()
    # browser = webdriver.Firefox()
    # browser = webdriver.Edge()
    # browser = webdriver.PhantomJS()

    # 2.访问页面
    # 用get()方法来请求网页，参数传入链接URL即可。比如，这里用get()方法访问淘宝，然后打印出源代码

    # browser = webdriver.Chrome()
    # browser.get('https://www.taobao.com')
    # print(browser.page_source)
    # browser.close()

    # 3.查找结点
    # Selenium可以驱动浏览器完成各种操作，比如填充表单、模拟点击等,
#     Selenium提供了一系列查找节点的方法，我们可以用这些方法来获取想要的节点，以便下一步执行一些动作或者提取信息。
#     3.1 单个节点
#     find_element_by_name()是根据name值获取，find_element_by_id()是根据id获取。另外，还有根据XPath、CSS选择器等获取的方式。
#     选择一个节点的方法
        # find_element_by_id
        # find_element_by_name
        # find_element_by_xpath
        # find_element_by_link_text
        # find_element_by_partial_link_text
        # find_element_by_tag_name
        # find_element_by_class_name
        # find_element_by_css_selector
#     另外，Selenium还提供了通用方法find_element()，它需要传入两个参数：查找方式By和值。
#       实际上，它就是find_element_by_id()这种方法的通用函数版本，比如find_element_by_id(id)就等价于find_element(By.ID, id)，二者得到的结果完全一致。

    # browser = webdriver.Chrome()
    # browser.get('https://www.taobao.com')
#     input_first = browser.find_element_by_id('q')
#     input_second = browser.find_element_by_css_selector('#q')
#     input_third = browser.find_element_by_xpath('//*[@id="q"]')
#
#     print(input_first, input_second, input_third)
#     browser.close()
#     input_gen = browser.find_element(By.ID, 'q')
#     print(input_gen)

#     3.2获取多个节点
#     在获取单个节点的函数基础上加入s
#     如果用find_elements()方法，则结果是列表类型，列表中的每个节点是WebElement类型。
#
    # 这里列出所有获取多个节点的方法：
    # find_elements_by_id
    # find_elements_by_name
    # find_elements_by_xpath
    # find_elements_by_link_text
    # find_elements_by_partial_link_text
    # find_elements_by_tag_name
    # find_elements_by_class_name
    # find_elements_by_css_selector

#     lis = browser.find_elements_by_css_selector(".service-bd li")
#
#     print(type(lis))
#     print(lis)
#     browser.close()

#     4. 节点交互

    # browser = webdriver.Chrome()
    # browser的在位运算
    # browser.get('https://www.taobao.com')
    # inputs = browser.find_element_by_css_selector("#q")
    # inputs.send_keys('iPhone')
    # time.sleep(10)
    # inputs.clear()
    # inputs.send_keys("iPad")
    # button = browser.find_element_by_css_selector(".btn-search")
    # button.click()

# 5.动作链
from selenium import webdriver
from selenium.webdriver import ActionChains
# 另外一些操作，它们没有特定的执行对象，比如鼠标拖曳、键盘按键等，这些动作用另一种方式来执行，那就是动作链。

# if __name__ == '__main__':
    # browser = webdriver.Chrome()
    # url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
    # browser.get(url)
    # browser.switch_to.frame('iframeResult')
    # source = browser.find_element_by_css_selector('#draggable')
    # target = browser.find_element_by_css_selector('#droppable')
    #
    # action = ActionChains(browser)
    # action.drag_and_drop(source, target)
    # action.perform()

    # 执行JavaScript
    # browser执行execute_script()方法

    # browser = webdriver.Chrome()
    # browser.get('https://www.zhihu.com/explore')
    # browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    # browser.execute_script('alert("To Bottom")')

#  6.获取节点信息
#     6.1 获取属性
#     .get_attribute()
#     6.2 获取文本
#     .text
#     6.3 获取id， 位置，标签名和大小

#     browser = webdriver.Chrome()
#     browser.get('https://www.zhihu.com/explore')
#     # logo = browser.find_element_by_css_selector(".zu-top-link-logo")
#     # print(logo)
#     # print(logo.get_attribute('class'))
#     # print(logo.get_attribute('name'))
#     inputs = browser.find_element_by_class_name('zu-top-add-question')
#     print(inputs.text)
#     print(inputs.id)
#     print(inputs.location)
#     print(inputs.tag_name)
#     print(inputs.size)
#     browser.close()

# 7.切换Frame
#     使用browser的switch_to进行切换

# 8.延时等待
#   隐式等待
# browser.implicitly_wait(time)

# 显示等待
'''
用例
    wait = WebDriverWait(browser, 10)
    input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
    print(input, button)

首先引入WebDriverWait这个对象，指定最长等待时间，然后调用它的until()方法，传入要等待条件expected_conditions。比如，这里传入了presence_of_element_located这个条件，代表节点出现的意思，其参数是节点的定位元组，也就是ID为q的节点搜索框。

这样可以做到的效果就是，在10秒内如果ID为q的节点（即搜索框）成功加载出来，就返回该节点；如果超过10秒还没有加载出来，就抛出异常。

对于按钮，可以更改一下等待条件，比如改为element_to_be_clickable，也就是可点击，所以查找按钮时查找CSS选择器为.btn-search的按钮，如果10秒内它是可点击的，也就是成功加载出来了，就返回这个按钮节点；如果超过10秒还不可点击，也就是没有加载出来，就抛出异常。

# 等待条件详见博客
'''

# 9. 平常使用浏览器时都有前进和后退功能，
# browser.back()
# time.sleep(1)
# browser.forward()

# 10. Cookies
# 获取、添加、删除Cookies
# print(browser.get_cookies())
# browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'germey'})
# print(browser.get_cookies())
# browser.delete_all_cookies()

########################################################################################################################

#   Selenium爬去淘宝商品

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
# import time
# from selenium.webdriver import ActionChains
# from selenium.common.exceptions import TimeoutException
# from urllib.parse import quote
# from pyquery import PyQuery as pq
# import pymongo
#
#
# # headless 无页面操作
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# # chrome_options.add_argument("user-agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'")
# # 这里chrome_options使用这个设置可以避免网站检测到你使用的是无界模式进行反抓取。
# # 下边另外的两项设置，不进行设置时在桌面版linux系统，或者mac系统上会打开有界面的chrome.调试时可以注释掉下边两行使用有界面版chrome来调试程序。
# # chrome_options.add_argument('--headless')
# # chrome_options.add_argument('--disable-gpu')
#
# browser = webdriver.Chrome(chrome_options= chrome_options, executable_path='/home/ubuntu/Chrome/chromedriver')
#
#
#
# wait = WebDriverWait(browser, 10)
# KEYWORD = 'iPad'
# MONGO_URL = 'localhost'
# MONGO_DB = 'taobao'
# MONGO_COLLECTION = 'products'
#
# def index_page(page):
#     print("正在爬第", page, '页')
#     try:
#         url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
#         browser.get(url=url)
#         if page > 1:
#             inputs = wait.until(
#                 EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input'))
#             )
#             submits = wait.until(
#                 EC.element_to_be_clickable((By.CSS_SELECTOR, "#mainsrp-pager div.form > span.btn.J_Submit"))
#             )
#             inputs.clear()
#             inputs.send_keys(page)
#             submits.click()
#         wait.until(
#             EC.text_to_be_present_in_element((By.CSS_SELECTOR,  '#mainsrp-pager li.item.active > span'), str(page))
#         )
#         wait.until(
#             EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item'))
#         )
#         get_products()
#     except TimeoutException:
#         index_page(page)
#
# def get_products():
#     html = browser.page_source
#     doc = pq(html)
#     items = doc("#mainsrp-itemlist .items .item").items()
#     for item in items:
#         product = {
#             'image':item.find('.pic .img').attr('data-src'),
#             'price':item.find('.ctx-box .price').text(),
#             'deal':item.find('.ctx-box .deal-cnt').text(),
#             'title':item.find('.title').text(),
#             'shop':item.find('.shop').text(),
#             'location':item.find('.location').text()
#         }
#         print(product)
#         save_mongodb(product)
#
# def save_mongodb(product):
#     client = pymongo.MongoClient(MONGO_URL, port=27017)
#     db = client[MONGO_DB]
#
#     try:
#         products = db[MONGO_COLLECTION]
#         if products.insert_one(product):
#             print("存储成功")
#     except Exception as e:
#         print("存储失败")
#         print(e)
#
# def main():
#     MAXPAGE = 20
#     for i in range(1, MAXPAGE+1):
#         index_page(i)
#
# if __name__ == '__main__':
#     main()
#     browser.close()
#     browser.quit()



# ############# 爬虫代理





