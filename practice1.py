import urllib.request as req
import urllib.parse as par
import urllib.error as err
from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener
import socket

# ################
# 发送请求
# ################


# 1 urlopen()的使用， 可以完成最基本的简单网页的GET请求抓取
# response = req.urlopen("https://www.python.org")
# print(response.read().decode("UTF-8"))
# print(type(response))

'''
一个HTTPResposne类型的对象。它主要包含
read()、readinto()、getheader(name)、getheaders()、fileno()等方法，
以及msg、version、status、reason、debuglevel、closed等属性
'''
# ps: nginx是一个反代理服务器
# print(response.status)  # 获取响应状态码
# print(response.getheaders())
# print(response.getheader('Server'))

'''
urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)
urlopen()的参数
data参数
data参数是可选的。如果要添加该参数，并且如果它是字节流编码格式的内容，即bytes类型，
则需要通过bytes()方法转化。另外，如果传递了这个参数，则它的请求方式就不再是GET方式，而是POST方式。
'''
# data = bytes(par.urlencode({'word': 'hello'}),encoding="utf8")
# response = req.urlopen(url='http://httpbin.org/post', data=data)
# print(response.read())
'''
timeout参数
timeout参数用于设置超时时间，单位为秒，意思就是如果请求超出了设置的这个时间，还没有得到响应，就
会抛出异常。如果不指定该参数，就会使用全局默认时间。它支持HTTP、HTTPS、FTP请求。
'''
# response = req.urlopen(url='http://httpbin.org/get', timeout=1)
# print(response.read())

# try:
#     response = req.urlopen(url='http://httpbin.org/get', timeout=1)
#     print(response.read())
# except err.URLError as e:
#     if isinstance(e.reason, socket.timeout):
#         print('TIME OUT')


'''
context参数，必须是ssl.SSLContext类型没用指定来SSL设置
cafile和capath这两个参数分别指定CA证书和它的路径，这个在请求HTTPS链接时会有用。

cadefault参数现在已经弃用了，其默认值为False
'''

# 2 Request()
'''
用urlopen()方法来发送这个请求，只不过这次该方法的参数不再是URL，而是一个
Request类型的对象。通过构造这个数据结构，一方面我们可以将请求独立成一个对象，
另一方面可更加丰富和灵活地配置参数。
'''
# request = req.Request('https://python.org')
# response = req.urlopen(request)
# print(response.read().decode('utf-8'))

'''
class urllib.request.Request(url, data=None, headers={}, origin_req_host=None, 
unverifiable=False, method=None)
第一个参数url用于请求URL，这是必传参数，其他都是可选参数。
第二个参数data如果要传，必须传'bytes'（字节流）类型的。
        如果它是字典，可以先用urllib.parse模块里的urlencode()编码。
第三个参数headers是一个字典，它就是请求头，我们可以在构造请求时通过
    headers参数直接构造，也可以通过调用请求实例的add_header()方法添加。
    添加请求头最常用的用法就是通过修改User-Agent来伪装浏览器，默认的User-Agent是Python-urllib，
    我们可以通过修改它来伪装浏览器。比如要伪装火狐浏览器，你可以把它设置为：
    Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11
第四个参数origin_req_host指的是请求方的host名称或者IP地址。
第五个参数unverifiable表示这个请求是否是无法验证的，默认是False，
    意思就是说用户没有足够权限来选择接收这个请求的结果。
    例如，我们请求一个HTML文档中的图片，但是我们没有自动抓取图像的权限，
    这时unverifiable的值就是True`。
第六个参数method是一个字符串，用来指示请求使用的方法，比如GET、POST和PUT等。
'''
# url = 'http://httpbin.org/post'
# headers = {
#     'User-Agent':'Mozilla/4.0(compatible;MSIE 5.5; Windows NT)',
#     'Host':'httpbin.org'
# }
# dict = {
#     'name':'Germey'
# }
# data = bytes(par.urlencode(dict), encoding='utf8')
# requ = req.Request(url=url, data=data, method='POST')
# requ.add_header( 'User-Agent','Mozilla/4.0(compatible;MSIE 5.5; Windows NT)')
# response = req.urlopen(requ)
# print(response.read().decode('utf-8'))

# 高级用法


# 代理
# Opener可以使用open()方法，返回的类型和urlopen()如出一辙。
# 那么，它和Handler有什么关系呢？简而言之，就是利用Handler来构建Opener。
# proxy_handler = ProxyHandler({
#     'http': 'http://127.0.0.1:9743',
#     'https': 'https://127.0.0.1:9743'
# })
#
# opener = build_opener(proxy_handler)
# try:
#     response = opener.open('https://www.baidu.com')
#     print(response.read().decode('utf-8'))
# except URLError as e:
#     print(e.reason)

# Cookies
# 1：得到cookie
# 2：使用cookie来构建handler
# 3：使用build_opener，加入handler构建opener
# 4：使用opener.open，加入url得到response
import http.cookiejar as cok

# cookie = cok.CookieJar()
# handler = req.HTTPCookieProcessor(cookie)
# opener = build_opener(handler)
#
# response = opener.open('http://www.baidu.com')
# for item in cookie:
#     print(item.name + "=" + item.value)
# print(response.read().decode('utf-8'))

# Cookies实际上也是以文本形式保存的,斯普哦Cookie可以输出为文件格式
'''
LWPCookieJar同样可以读取和保存Cookies，但是保存的格式和MozillaCookieJar不一样，
它会保存成libwww-perl(LWP)格式的Cookies文件。

要保存成LWP格式的Cookies文件，可以在声明时就改为：
cookie = http.cookiejar.LWPCookieJar(filename)

两者Cookies格式不同
MozillaCookieJar:文件格式的cookies
LWPCookieJar:LWP文件格式的cookies

'''
# filename = 'cookies.txt'
# # cookie = cok.MozillaCookieJar(filename)
# cookie = cok.LWPCookieJar(filename)
# cookie.save(ignore_discard=True, ignore_expires=True)
# handler = req.HTTPCookieProcessor(cookie)
# opener = build_opener(handler)
# 保存文件
# response = opener.open('http://www.baidu.com')

# 从文件读取
'''
调用load()方法来读取本地的Cookies文件，获取到了Cookies的
内容。不过前提是我们首先生成了LWPCookieJar格式的Cookies，
并保存成文件，然后读取Cookies之后使用同样的方法构建Handler
和Opener即可完成操作。
'''
# cookie = cok.LWPCookieJar()
# cookie.load(filename, ignore_discard=True, ignore_expires=True)
# handler = req.HTTPCookieProcessor(cookie)
# opener = build_opener(handler)
# response = opener.open('http://www.baidu.com')
# print(response.read().decode('utf-8'))


# ################
# 异常处理
# ################

# 1. URLError
# try:
#     response = req.urlopen('http://cuiqingcai.com/index.htm')
# except URLError as e:
#     print(e.reason)

# HTTPError
# 它是URLError的子类，专门用来处理HTTP请求错误，比如认证请求失败等。它有如下3个属性。
#
# code：返回HTTP状态码，比如404表示网页不存在，500表示服务器内部错误等。
# reason：同父类一样，用于返回错误的原因。
# headers：返回请求头。
# -----------------------------------------
# try:
#     response = req.urlopen('http://cuiqingcai.com/index.htm')
# except err.HTTPError as e:
#     print(e.reason, e.code, e.headers, sep='\n')
# # 因为URLError是HTTPError的父类，所以可以先选择捕获子类的错误，再去捕获父类的错误
# except err.URLError as e:
#     print(e.reason)
# else:
#     print('成功请求')

'''
这样就可以做到先捕获HTTPError，获取它的错误状态码、原因、headers等信息。如果不是
HTTPError异常，就会捕获URLError异常，输出错误原因。最后，用else来处理正常的逻辑。
这是一个较好的异常处理写法。
'''
# reason属性返回的不一定是字符串，也可能是一个对象。
# 可以用isinstance()方法来判断它的类型，作出更详细的异常判断。
# -----------------------------------------------------------
# try:
#     response = req.urlopen('http://www.baidu.com',timeout=0.1)
# except URLError as e:
#     print(type(e.reason))
#     if isinstance(e.reason, socket.error):
#         print("TIME_OUT")

# ################
# 解析链接
# ################

# 1.urlparse(),实现URL识别和分段

# result = par.urlparse('http://www.baidu.com/index.html;user?id=5#comment')
# print(type(result), result)
# 返回结果是一个ParseResult类型的对象，它包含6部分，分别是scheme、netloc、path、params、query和fragment

'''
http://www.baidu.com/index.html;user?id=5#comment
://前面的就是scheme，代表协议；第一个/前面便是netloc，即域名；分号;hou面是params，代表参数
====> scheme://netloc/path;parameters?query#fragment
'''

'''
API用法：
urllib.parse.urlparse(urlstring, scheme='', allow_fragments=True)
==========>ParseResult
可以看到，它有3个参数。

urlstring：这是必填项，即待解析的URL。
scheme：1. 它是默认的协议（比如http或https等）。假如这个链接没有带协议信息，会将这个作为默认的协议。
        eg:result = urlparse('www.baidu.com/index.html;user?id=5#comment', scheme='https')
        2. scheme参数只有在URL中不包含scheme信息时才生效。如果URL中有scheme信息，就会返回解析出的scheme
        eg:result = urlparse('http://www.baidu.com/index.html;user?id=5#comment', scheme='https')

allow_fragments：即是否忽略fragment。如果它被设置为False，fragment部分就会被忽略，
        它会被解析为path、parameters或者query的一部分，而fragment部分为空

        from urllib.parse import urlparse
         
        result = urlparse('http://www.baidu.com/index.html#comment', allow_fragments=False)
        print(result)
    运行结果如下：

        ParseResult(scheme='http', netloc='www.baidu.com', path='/index.html#comment', params='', query='', fragment='')
        可以发现，当URL中不包含params和query时，fragment便会被解析为path的一部分。
'''

# 2.urlunparse()
'''
有了urlparse()，相应地就有了它的对立方法urlunparse()。它接受的参数是一个可迭代对
象，但是它的长度必须是 6，否则会抛出参数数量不足或者过多的问题。
'''
# data = ['http', 'www.baidu.com', 'index.xml', 'user', 'a=6', 'comment']
# print(par.urlunparse(data))

# 3.urlsplit()
# parse的函数
'''
不再单独解析params这一部分，只返回5个结果。上面例子中的params会合并到path中
=======>SplitResult
'''
# result = req.urlsplit('http://www.baidu.com/index.xml:user?id=5#comment')
# print(result.scheme,result[0])

# 4.urlunsplit()
'''
parse的函数
与urlunparse()类似，它也是将链接各个部分组合成完整链接的方法，传入的参数也是
一个可迭代对象，例如列表、元组等，唯一的区别是长度必须为 5。
'''

# 5.urlencode()
'''
序列化
urlencode()方法将其他类型的输入参数其序列化为GET请求参数
'''
# params = {
#     'name':'germey',
#     'age':22
# }
# base_url = 'http://www.baidu.com?'
# url = base_url + par.urlencode(params)
# print(url)

# 6.parse_qs()
'''
反序列化,将url转化为字典
'''
# query = 'name=germey&age=22'
# print(par.parse_qs(query))

# 7.parse_qsl()
'''
parse_qsl()方法，它用于将参数转化为元组组成的列表

'''
# query = 'name=germey&age=22'
# print(par.parse_qsl(query))

# 8.quote()
'''
将内容转化为URL编码的格式。URL中带有中文参数时，
有时可能会导致乱码的问题，此时用这个方法可以将中文字符转化为URL编码

quote()方法对中文进行URL编码，防止乱码
'''

# keyword = '壁纸'
# url = 'https://www.baidu.com/s?wd='+ par.quote(keyword)
# print(url)

# 9.unquote()
'''
得到的URL编码后的结果，这里利用unquote()方法还原,相当于解码
'''
# url = 'https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
# print(par.unquote(url))

# ################
# Robots协议
# ################

# 网络爬虫排除标准（Robots Exclusion Protocol）

'''
urllib.robotparser.RobotFileParser(url='')
当然，也可以在声明时不传入，默认为空，最后再使用set_url()方法设置一下也可。

下面列出了这个类常用的几个方法。

set_url()：用来设置robots.txt文件的链接。如果在创建RobotFileParser对象时传入了链
接，那么就不需要再使用这个方法设置了。
read()：读取robots.txt文件并进行分析。注意，这个方法执行一个读取和分析操作，如果
不调用这个方法，接下来的判断都会为False，所以一定记得调用这个方法。这个方法不会返回
任何内容，但是执行了读取操作。
parse()：用来解析robots.txt文件，传入的参数是robots.txt某些行的内容，它会按照
robots.txt的语法规则来分析这些内容。
can_fetch()：该方法传入两个参数，第一个是User-agent，第二个是要抓取的URL。
返回的内容是该搜索引擎是否可以抓取这个URL，返回结果是True或False。
mtime()：返回的是上次抓取和分析robots.txt的时间，这对于长时间分析和抓取的搜索爬虫
是很有必要的，你可能需要定期检查来抓取最新的robots.txt。
modified()：它同样对长时间分析和抓取的搜索爬虫很有帮助，将当前时间设置为上次抓取
和分析robots.txt的时间。
'''
# from urllib.robotparser import RobotFileParser
# rp = RobotFileParser()
# rp.set_url('http://www.jianshu.com/robots.txt')
# rp.read()
#
# print(rp.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d'))
# print(rp.can_fetch('*', "http://www.jianshu.com/search?q=python&page=1&type=collections"))


# ################
# Request
# ################

# 使用requests的get（）函数，实现与urlopen()相同的操作，得到一个Response对象，然后分别
# 输出了Response的类型、状态码、响应体的类型、内容以及Cookies
import requests
import re

# r = requests.get('http://www.baidu.com/')
# print(type(r))
# print(r.status_code)
# print(type(r.text))
# print(r.text)
# print(r.cookies)

'''
r = requests.post('http://httpbin.org/post')
r = requests.put('http://httpbin.org/put')
r = requests.delete('http://httpbin.org/delete')
r = requests.head('http://httpbin.org/get')
r = requests.options('http://httpbin.org/get')
这里分别用post()、put()、delete()等方法实现了POST、PUT、DELETE等请求
'''

# 1.GET请求
# 可以在后面加入参数?name=germey&age=22
# 如果是字典型参数，则使用
# r = requests.get("http://httpbin.org/get")
# print(r.text)
#
# r = requests.get("http://httpbin.org/get?name=germey&age=22")
# print(r.text)
#
# data = {
#     'name':'germey',
#     'age':22
# }
# r = requests.get("http://httpbin.org/get",params=data)
# print(r.text)
# print(type(r.text))
# print(r.json())
# print(type(r.json()))
'''
调用json()方法，就可以将返回结果是JSON格式的字符串转化为字典。

但需要注意的书，如果返回结果不是JSON格式，便会出现解析错误，
抛出json.decoder.JSONDecodeError异常。
'''

# 2.抓取网页
'''
加入headers信息，其中包含了User-Agent字段信息，
也就是浏览器标识信息。如果不加这个，知乎会禁止抓取
'''
# headers = {
#     'User-Agent':'Mozilla/5.0(Macintosh;Intel Max OS X 10_11_4)
# AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
# }
# r = requests.get('https://www.zhihu.com/explore',headers=headers)
# pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
# titles = re.findall(pattern, r.text)
# print(titles)


# 3.爬取二进制文件
'''
前者出现了乱码，后者结果前带有一个b，这代表是bytes类型的数据。由于图片是二进制数据，
所以前者在打印时转化为str类型，也就是图片直接转化为字符串，这理所当然会出现乱码。
当然，对于音频和视频文件，同样可以用此方法获取
'''
# r = requests.get("https://github.com/favicon.ico")
# print(r.text)
# print(r.content)
# with open("./image/favicon.ico",'wb') as f:
#     f.write(r.content)
# 4.POST请求
# data = {'name':'germey','age':'22'}
#
# r = requests.post("http://httpbin.org/post", data=data)
# print(r.text)
# 注意输出信息,post添加表单参数是通过data=data, get添加参数是通过params=data

# 5.响应
'''
text得到响应的内容,
content得到相应的内容,
status_code,
headers,
cookies,
url,
history
'''
# r = requests.get('https://www.jianshu.com')
# exit() if not r.status_code == requests.codes.ok else print('Request Successfully')
# print(type(r.status_code), r.status_code)
# print(type(r.headers), r.headers)
# print(type(r.cookies), r.cookies)
# print(type(r.url), r.url)
# print(type(r.history), r.history)
# requests还提供了一个内置的状态码查询对象,提供判断请求的状态
'''
# 信息性状态码
100: ('continue',),
101: ('switching_protocols',),
102: ('processing',),
103: ('checkpoint',),
122: ('uri_too_long', 'request_uri_too_long'),
 
# 成功状态码
200: ('ok', 'okay', 'all_ok', 'all_okay', 'all_good', '\\o/', '✓'),
201: ('created',),
202: ('accepted',),
203: ('non_authoritative_info', 'non_authoritative_information'),
204: ('no_content',),
205: ('reset_content', 'reset'),
206: ('partial_content', 'partial'),
207: ('multi_status', 'multiple_status', 'multi_stati', 'multiple_stati'),
208: ('already_reported',),
226: ('im_used',),
 
# 重定向状态码
300: ('multiple_choices',),
301: ('moved_permanently', 'moved', '\\o-'),
302: ('found',),
303: ('see_other', 'other'),
304: ('not_modified',),
305: ('use_proxy',),
306: ('switch_proxy',),
307: ('temporary_redirect', 'temporary_moved', 'temporary'),
308: ('permanent_redirect',
      'resume_incomplete', 'resume',), # These 2 to be removed in 3.0
 
# 客户端错误状态码
400: ('bad_request', 'bad'),
401: ('unauthorized',),
402: ('payment_required', 'payment'),
403: ('forbidden',),
404: ('not_found', '-o-'),
405: ('method_not_allowed', 'not_allowed'),
406: ('not_acceptable',),
407: ('proxy_authentication_required', 'proxy_auth', 'proxy_authentication'),
408: ('request_timeout', 'timeout'),
409: ('conflict',),
410: ('gone',),
411: ('length_required',),
412: ('precondition_failed', 'precondition'),
413: ('request_entity_too_large',),
414: ('request_uri_too_large',),
415: ('unsupported_media_type', 'unsupported_media', 'media_type'),
416: ('requested_range_not_satisfiable', 'requested_range', 'range_not_satisfiable'),
417: ('expectation_failed',),
418: ('im_a_teapot', 'teapot', 'i_am_a_teapot'),
421: ('misdirected_request',),
422: ('unprocessable_entity', 'unprocessable'),
423: ('locked',),
424: ('failed_dependency', 'dependency'),
425: ('unordered_collection', 'unordered'),
426: ('upgrade_required', 'upgrade'),
428: ('precondition_required', 'precondition'),
429: ('too_many_requests', 'too_many'),
431: ('header_fields_too_large', 'fields_too_large'),
444: ('no_response', 'none'),
449: ('retry_with', 'retry'),
450: ('blocked_by_windows_parental_controls', 'parental_controls'),
451: ('unavailable_for_legal_reasons', 'legal_reasons'),
499: ('client_closed_request',),
 
# 服务端错误状态码
500: ('internal_server_error', 'server_error', '/o\\', '✗'),
501: ('not_implemented',),
502: ('bad_gateway',),
503: ('service_unavailable', 'unavailable'),
504: ('gateway_timeout',),
505: ('http_version_not_supported', 'http_version'),
506: ('variant_also_negotiates',),
507: ('insufficient_storage',),
509: ('bandwidth_limit_exceeded', 'bandwidth'),
510: ('not_extended',),
511: ('network_authentication_required', 'network_auth', 'network_authentication')
'''

# 6.文件上传
# files = {'file': open('./image/favicon.ico', 'rb')}
# r = requests.post("http://httpbin.org/post",files=files)
# print(r.text)
'''
首先调用cookies属性即可成功得到Cookies，可以发现它是RequestCookieJar类型。
然后用items()方法将其转化为元组组成的列表，遍历输出每一个Cookie的名称和值，实现Cookie的遍历解析。
'''
# r = requests.get("https://www.baidu.com")
# print(r.cookies)
# for key, item in r.cookies.items():
#     print(key+"="+item)

# 7.Cookies
# 直接用Cookie来维持登录状态
# a.在headers里面加入cookie参数
# headers = {
#     'cookie':'_zap=a44af815-d92f-46d6-8d20-7d8e120d8155; __DAYU_PP=eB7IrRr7b7EiYJ7vuIIm367ec76002ec; d_c0="AFCgV6F3ig2PTkfiAxyEOwk1YaUDVu7XXbU=|1525410682"; __utma=51854390.1816230924.1525540206.1525540206.1525540206.1; __utmz=51854390.1525540206.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=51854390.000--|3=entry_date=20180506=1; q_c1=25530ca3647b442fb32b708a3476b54f|1526878693000|1520604026000; l_cap_id="NzFhYTk0YTVkYjU4NDg3MmFjMTdmN2I3YjgxOWU5MTQ=|1527056136|c18edf6d3b4a4f7199759e06a92eff3cf865ffdd"; r_cap_id="Y2FiZjdlNjVjZWZlNDA3M2I5ZDJiMTM3YjA4OTNjNTc=|1527056136|b8c5a31f857db1af7c0fb74f36d0388f01313a4d"; cap_id="MmNlY2E4Yjg2YTExNDllZmI4YjM5ZGNkMzllNDg4OTY=|1527056136|ace0aa4b60fb62da575152ed890931b662f8ecc0"; tgw_l7_route=931b604f0432b1e60014973b6cd4c7bc; _xsrf=11012134-b754-47d2-9f97-c5fa3029fe6d; capsion_ticket="2|1:0|10:1529140637|14:capsion_ticket|44:MGYzYjRjMGIwZTQ1NDFlY2JkMDAyYzYxZTYzYzA3Yjc=|de8ebd51a0c41d996cb9a2aaaa4929746eab550c74af653b18d4a44182688b76"; z_c0="2|1:0|10:1529140653|4:z_c0|92:Mi4xUjZ0bEFnQUFBQUFBVUtCWG9YZUtEU1lBQUFCZ0FsVk5yU01TWEFDZGFUd3pYckRiang3WVotMHJCN1NscHE4Snl3|7ce3ca013451914b049f2e9156609778dbabbe7ebd2415bd6274e45e42e4b991',
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
# }
# r = requests.get('https://www.zhihu.com', headers=headers)
# print(r.text)

# b.可以通过cookies参数来设置，不过这样就需要构造RequestsCookieJar对象，而且需要分割一下cookies。
#   这相对烦琐，不过效果是相同的

# cookies = ' zap=a44af815-d92f-46d6-8d20-7d8e120d8155; __DAYU_PP=eB7IrRr7b7EiYJ7vuIIm367ec76002ec; d_c0="AFCgV6F3ig2PTkfiAxyEOwk1YaUDVu7XXbU=|1525410682"; __utma=51854390.1816230924.1525540206.1525540206.1525540206.1; __utmz=51854390.1525540206.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=51854390.000--|3=entry_date=20180506=1; q_c1=25530ca3647b442fb32b708a3476b54f|1526878693000|1520604026000; l_cap_id="NzFhYTk0YTVkYjU4NDg3MmFjMTdmN2I3YjgxOWU5MTQ=|1527056136|c18edf6d3b4a4f7199759e06a92eff3cf865ffdd"; r_cap_id="Y2FiZjdlNjVjZWZlNDA3M2I5ZDJiMTM3YjA4OTNjNTc=|1527056136|b8c5a31f857db1af7c0fb74f36d0388f01313a4d"; cap_id="MmNlY2E4Yjg2YTExNDllZmI4YjM5ZGNkMzllNDg4OTY=|1527056136|ace0aa4b60fb62da575152ed890931b662f8ecc0"; tgw_l7_route=931b604f0432b1e60014973b6cd4c7bc; _xsrf=11012134-b754-47d2-9f97-c5fa3029fe6d; capsion_ticket="2|1:0|10:1529140637|14:capsion_ticket|44:MGYzYjRjMGIwZTQ1NDFlY2JkMDAyYzYxZTYzYzA3Yjc=|de8ebd51a0c41d996cb9a2aaaa4929746eab550c74af653b18d4a44182688b76"; z_c0="2|1:0|10:1529140653|4:z_c0|92:Mi4xUjZ0bEFnQUFBQUFBVUtCWG9YZUtEU1lBQUFCZ0FsVk5yU01TWEFDZGFUd3pYckRiang3WVotMHJCN1NscHE4Snl3|7ce3ca013451914b049f2e9156609778dbabbe7ebd2415bd6274e45e42e4b991'
# jar = requests.cookies.RequestsCookieJar()
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
# }
# for cookie in cookies.split(';'):     #利用;作为分割标准
#     key, value = cookie.split('=', 1)  #cookie字符串切割出key和value
#     jar.set(key,value)
#
# r = requests.get('http://www.baidu.com', cookies=jar, headers=headers)
# print(r.text)

# 会话维持
# 8.Session对象

# requests.get('http://httpbin.org/cookies/set/number/123456789')
# r = requests.get('http://httpbin.org/cookies')
# print(r.text)
'''
利用Session，可以做到模拟同一个会话而不用担心Cookies的问题。
它通常用于模拟登录成功之后再进行下一步的操作。
'''
# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/number/123456789')
# r = s.get('http://httpbin.org/cookies')
# print(r.text)
# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/number/12349')
# print(s.get('http://httpbin.org/cookies').text)

# 9. SSL证书验证
'''
如果请求一个HTTPS站点，但是证书验证错误的页面时，就会报这样
的错误，那么如何避免这个错误呢？很简单，把verify参数设置为False即可。
'''
# try:
#     response = requests.get('https://www.12306.cn')
#     print(response.status_code)
# except URLError as e:
#     print(e.reason)
'''
跑出来有一个warning，
    a.可以通过设置忽略警告的方式来屏蔽这个警告
    from requests.packages import urllib3
    urllib3.disable_warnings()
    b.通过捕获警告到日志的方式忽略警告
    import logging
    logging.captureWarnings(True)
'''
# from requests.packages import urllib3
# urllib3.disable_warnings()
# import logging
# logging.captureWarnings(True)
# try:
#     response = requests.get('https://www.12306.cn', verify=False)
#     print(response.status_code)
# except URLError as e:
#     print(e.reason)

# 10. 代理设置
'''
对于某些网站，在测试的时候请求几次，能正常获取内容。但是一旦开始大规模爬取，
对于大规模且频繁的请求，网站可能会弹出验证码，或者跳转到登录认证页面，更甚者
可能会直接封禁客户端的IP，导致一定时间段内无法访问。
为了防止这种情况出现，需要设置代理来解决这个问题，这就需要用到proxies参数
'''
# 代理
# proxies = {
#     "http": "http://user:password@115.218.123.168：9000",
#     "http": "http://user:password@115.223.205.138：9000",
# }
# 未尝试成功
# proxies = {
#     "http": "socks5://user:password@host:port",
#     "https": "socks5://user:password@host:port",
# }
#
# response = requests.get("https://www.taobao.com", proxies=proxies)
# print(response.text)
# 若代理需要使用HTTP Basic Auth，可以使用类似http://user:password@host:port这样的语法来设置代理
# 除了基本的HTTP代理外，requests还支持SOCKS协议的代理

'''
实际上，请求分为两个阶段，即连接（connect）和读取（read）。

上面设置的timeout将用作连接和读取这二者的timeout总和。

如果要分别指定，就可以传入一个元组：

r = requests.get('https://www.taobao.com', timeout=(5,11, 30))
如果想永久等待，可以直接将timeout设置为None，或者不设置直接留空，因为默认是None。这样的话，如果服务器还在运行，但是响应特别慢，那就慢慢等吧，它永远不会返回超时错误的。其用法如下：

r = requests.get('https://www.taobao.com', timeout=None)
或直接不加参数：
r = requests.get('https://www.taobao.com')

'''

# 11.身份认证
'''
auth=HTTPBasicAuth('username', 'password')
auth=('username', 'password')

'''
# from requests.auth import HTTPBasicAuth
# r = requests.get('http://localhost:5000', auth=HTTPBasicAuth('username', 'password'))
# print(r.status_code)

'''
requests还提供了其他认证方式，如OAuth认证，不过此时需要安装oauth包
'''
# from requests_oauthlib import OAuth1
# url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
# auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET',
#               'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
#
# requests.get(url, auth=auth)

# 12.Prepared Request

# from requests import Request, Session
# url = 'http://httpbin.org/post'
#
# data = {
#     'name':'germey'
# }
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
# }
#
# s = Session()
# req = Request('POST', url, data=data, headers=headers)
#
# prepared = s.prepare_request(req)
# res = s.send(prepared)
# print(res.text)
'''
有了Request这个对象，就可以将请求当作独立的对象来看待，这样在进行队列调度时会非常方便。
后面我们会用它来构造一个Request队列。
'''


# #############################
# Python 的正则表达式
# #############################
# re库
import re

# 1.match()
'''
match()，向它传入要匹配的字符串以及正则表达式，就可以检测这个正则表达式是否匹配字符串。

match()方法会尝试从字符串的起始位置匹配正则表达式，如果匹配，就返回匹配成功的结果；
                如果不匹配，就返回None
match()方法中，第一个参数传入了正则表达式，第二个参数传入了要匹配的字符串

可以使用()括号将想提取的子字符串括起来。()实际上标记了一个子表达式的开始和结束位置，
被标记的每个子表达式会依次对应每一个分组，调用group()方法传入分组的索引即可获取提取的结果

'''
# 匹配目标

# content = 'Hello 123 4567 World_This is a Regex Demo'
# print(len(content))
# result = re.match('^Hello\s\d{3}\s\d{4}\s\w{10}', content)
# print(result)
# print(result.group())
# print(result.group(1))  #123
# print(result.span())

# 通用匹配
# 我们可以使用.*简化正则表达式的书写

# 贪婪策略：
# .*(\d+)
# 非贪婪策略
# .*?(\d+)
# 在做匹配的时候，字符串中间尽量使用非贪婪匹配，也就是用.*?来代替.*，以免出现匹配结果缺失的情况。

# 如果匹配的结果在字符串结尾，.*?就有可能匹配不到任何内容了，因为它会匹配尽可能少的字符
# content = 'htt/p://weibo.com/comment/kEraCN'
# result1 = re.match('http.*?comment/(.*?)', content)
# result2 = re.match('http.*?comment/(.*)', content)
# print('result1', result1.group(1))
# print('result2', result2.group(1))

# 3.修饰符
'''
加了一个换行符，就匹配不到了呢？这是因为\.匹配的是除换行符之外的任意字符，
当遇到换行符时，.*?就不能匹配了，所以导致匹配失败。这里只需加一个修饰符re.S，即可修正这个错误：

result = re.match('^He.*?(\d+).*?Demo$', content, re.S)

ps:re.S在网页匹配中经常用到。因为HTML节点经常会有换行，加上它，就可以匹配节点与节点之间的换行了。
'''

# content = '''Hello 1234567 World_This
# is a Regex Demo
# '''
# result = re.match('^He.*?(\d+).*?Demo$', content, re.S)
# print(result.group(0))

'''
修饰符

描述

re.I 使匹配对大小写不敏感

re.L

做本地化识别（locale-aware）匹配

re.M

多行匹配，影响^和$

re.S

使.匹配包括换行在内的所有字符

re.U

根据Unicode字符集解析字符。这个标志影响\w、\W、 \b和\B

re.X

该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解
'''

# 爬去猫眼电影排行

# yield使用方法
# yield可以用来为一个函数返回值塞数据
#
# import re
# import requests
# import json
# import time
# def get_ont_graph(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.text
#     return None
#
# def parse_one_page(html):
#     pattern = re.compile(
#         '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',
#         re.S
#     )
#     items = re.findall(pattern, html)
#     for item in items:
#         yield {
#             'index': item[0],
#             'image': item[1],
#             'title': item[2].strip(),
#             'actor': item[3].strip()[3:] if len(item[3]) > 3 else '',
#             'time': item[4].strip()[5:] if len(item[4]) > 5 else '',
#             'score': item[5].strip()+item[6].strip()
#         }
#
# def write_to_json(content):
#     with open('result.txt', 'ab+') as f:
#         print(type(json.dumps((content))))
#         f.write(json.dumps(content,ensure_ascii=False,).encode('utf-8'))
#
#
#
# def main(offset=0):
#     url = 'http://maoyan.com/board/4?offset='+str(offset)
#     html = get_ont_graph(url)
#     res = parse_one_page(html)
#     for i in res:
#         print(i, '\n')
#         write_to_json(i)
#
# if __name__ == "__main__":
#     for i in range(10):
#         main(offset=i*10)
# #         增加延时时间，防止速度过快无响应
#         time.sleep(1)

# 使用正则表达式取解析爬取下来的html页面，难度大，容易出错，因此应该首先选择其他方式

########################################################################################################################

############################################## xpath ###################################################################

########################################################################################################################

# from lxml import etree
# text = '''
# <div>
#     <ul>
#          <li class="item-0"><a href="link1.html">first item</a></li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-inactive"><a href="link3.html">third item</a></li>
#          <li class="item-1"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a>
#      </ul>
#  </div>
# '''

# html = etree.HTML(text)

# # 须以//开头
# # 记住      /用于获取直接子节点，//用于获取子孙节点。
# # 记住      .表示当前节点，..用来查找父节点
# 使用parent::获取父节点，parent::*父层所有节点
# result = html.xpath("//ul/a")
# print(result)

# html = etree.HTML(text)
# result = html.xpath("//a[@href='link4.html']/parent::*/@class")
# print(result)


# 属性匹配
# 在[]之内使用@进行属性过滤
# 文本获取
# 文本获取使用text()
# 属性获取
# 直接使用@
# html = etree.HTML(text)
# result = html.xpath('//li[@class="item-1"]//text()')
# print(len(result))

# html = etree.HTML(text)
# result = html.xpath('//li[@class="item-1"]//@href')
# print(result)


# 属性多值匹配，不能只使用@添加匹配某个值,
# 要么@然后加上所有的属性来匹配
# 要么使用contains()函数

"""
text()  contains()

"""

import re
import requests
from lxml import etree
# text2 = '''
# <li class="li li-first"><a href="link.html">first item</a></li>
# '''
#
# html = etree.HTML(text=text2)
# result = html.xpath('//li[contains(@class,"li")]/a/text()')
# print(result)


# 多属性匹配
# 使用and来连接，并列在同一个[]之中
'''

运算符             描述                  实例                  返回值

or                  或               age=19 or age=20        如果age是19，则返回true。如果age是21，则返回false

and                 与               age>19 and age<21       如果age是20，则返回true。如果age是18，则返回false

mod             计算除法的余数             5 mod 2                 1

|               计算两个节点集            //book | //cd        返回所有拥有book和cd元素的节点集

+                   加法                  6 + 4                   10

-                   减法                  6 - 4                   2

*                   乘法                  6 * 4                   24

div                 除法                  8 div 4                 2

=                   等于                  age=19                  如果age是19，则返回true。如果age是20，则返回false

!=                  不等于                 age!=19                 如果age是18，则返回true。如果age是19，则返回false

<                   小于                  age<19                  如果age是18，则返回true。如果age是19，则返回false

<=                  小于或等于             age<=19                如果age是19，则返回true。如果age是20，则返回false

>                   大于                  age>19                  如果age是20，则返回true。如果age是19，则返回false

>=                  大于或等于             age>=19                如果age是19，则返回true。如果age是18，则返回false
'''

# text3 = '''
# <li class="li li-first" name="item1"><a href="link.html">first item</a></li>
# <li class="li-first" name="item2"><a href="link.html">second item</a></li>
# '''
# html3 = etree.HTML(text=text3)
# result3 = html3.xpath("//li[contains(@class,'li') and @name='item1']/a/text()")
# print(result3)

# text4 = '''
# <div>
#     <ul>
#          <li class="item-0" name="item0"><a href="link1.html"><span>first item</span></a></li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-inactive"><a href="link3.html">third item</a></li>
#          <li class="item-1"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a></li>
#     </ul>
# </div>
# '''
# 按序选择
# 与代码不同，序号是从1开始，不是0开始，     1,2,3,4,5

# html4 = etree.HTML(text=text4)

# result4 = html4.xpath('//li[1]/a/text()')
# print(result4)
# result4 = html4.xpath('//li[last()]/a/text()')
# print(result4)
# result4 = html4.xpath('//li[position()<3]/a/text()')
# print(result4)
# result4 = html4.xpath('//li[last()-2]/a/text()')
# print(result4)

# 节点轴选择
# XPath提供了很多节点轴选择方法，包括获取子元素、兄弟元素、父元素、祖先元素等

# result5 = html4.xpath('//li[1]/ancestor::*')
# print(result5)
# result5 = html4.xpath('//li[1]/ancestor::html')
# print(result5)
# result5 = html4.xpath('//li[1]/attribute::class')
# print(result5)
# result5 = html4.xpath('//li[1]/child::a[@href="link1.html"]')
# print(result5)
# result5 = html4.xpath('//li[1]/descendant::span')
# print(result5)
# result5 = html4.xpath('//li[1]/following::*[2]')
# print(result5)
# result5 = html4.xpath('//li[1]/following-sibling::*')
# print(result5)
#

# ###############################################################################################


########################################################################################################################

############################################ BeautifulSoup #############################################################

########################################################################################################################


# from bs4 import BeautifulSoup
# soup = BeautifulSoup('<div>Hello!</div>','lxml')
# print(soup.div.string)
#

# html = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
# <p class="story">...</p>
# """
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# print(soup.prettify())
# print(soup.title.string)

'''
直接调用节点的名称就可以选择节点元素，再调用string属性就可以得到节点内的文本了,如果单个节点结构层次非常清晰，可以选用这种方式来解析。
                                                    当有多个节点时，这种选择方式只会选择到第一个匹配的节点，其他的后面节点都会忽略。


'''
# # .name获取名称
# print(soup.title.name)
# # .attrs获取属性,
# print(soup.p.attrs)
# print(soup.p.attrs['name'])
# print(soup.p.attrs['class'])
# # .string获取内容
# # 嵌套选择
# print(soup.head.title)
# print(type(soup.head.title))
# print(soup.head.title.string)

# 关联选择
'''
子节点
contents获取直接子节点, 返回的是子节点列表，可能包含'\n'字符
children，获取直接子节点，，返回结果是生成器类型
descendants,获取所有子孙节点

父节点
parent属性，获取某个元素的直接父节点
parents属性，获取元素的所有祖先节点,返回的是geerator类型，list(enumerate(   ))

兄弟节点
next_sibling  下一个兄弟节点
previous_sibling 上一个兄弟节点
next_siblings  接下来的所有兄弟节点   返回的是生成器类型，需用list(enumerate())进行转化
previous_siblings  以上所有的兄弟节点



'''
# from bs4 import BeautifulSoup

# html = """
# <html>
#     <head>
#         <title>The Dormouse's story</title>
#     </head>
#     <body>
#         <p class="story">
#             Once upon a time there were three little sisters; and their names were
#             <a href="http://example.com/elsie" class="sister" id="link1">
#                 <span>Elsie</span>
#             </a>
#             <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
#             and
#             <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
#             and they lived at the bottom of a well.
#         </p>
#         <p class="story">...</p>
# """
#
# soup = BeautifulSoup(html, 'lxml')
# print(soup.body.contents)
# for i, des in enumerate(soup.body.contents):
#     print(i, des)
# print(soup.p.contents)
# print('\n')
# print(soup.p.children)
# print('\n')
# for i, child in enumerate(soup.p.children):
#     print(i, child)

# print(soup.p.descendants)
# for i, child in enumerate(soup.p.descendants):
#     print(i, child)
#
# print(soup.a.parent)

# print(type(soup.a.parents))
# print(soup.a.parents)
# print(list(enumerate(soup.a.parents)))


from bs4 import BeautifulSoup

html = """
<html>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            Hello
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
    </body>
</html>
"""

soup = BeautifulSoup(html,"lxml")
# print('Next Sibling', soup.a.next_sibling)
# print('Prev Sibling', soup.a.previous_sibling)
# print('Next Siblings',soup.a.next_siblings)
# print('Prev Siblings', soup.a.previous_siblings)
# print('Next Siblings', list(enumerate(soup.a.next_siblings)))
# print('Prev Siblings', list(enumerate(soup.a.previous_siblings)))

# 提取信息
# .name
# .string
# .attrs

# print('Next Siblings')
# print(soup.a.next_sibling.string)
# print(list(soup.a.parents)[0].attrs)
# print(list(soup.a.parents)[0].attrs['class'])


############################################## 方法选择器 ###############################################################

'''
1.find_all()查询符合所有条件的元素    find_all(name , attrs , recursive , text , **kwargs)
            name参数
            attrs参数  参数的类型是字典类型。比如，要查询id为list-1的节点，可以传入attrs={'id': 'list-1'}的查询条件，得到的结果是列表形式，包含的内容就是符合id为list-1的所有节点
            text参数   可用来匹配节点的文本，传入的形式可以是字符串，可以是正则表达式对象           

2.find()返回的是翻个元素，即是第一个匹配的·元素，而find_all()反蝴蝶所有匹配正则表达式的节点文本组成·的·1列表

3.find_parents()和find_parent()：前者返回所有祖先节点，后者返回直接父节点。
4.find_next_siblings()和find_next_sibling()：前者返回后面所有的兄弟节点，后者返回后面第一个兄弟节点。
5.find_previous_siblings()和find_previous_sibling()：前者返回前面所有的兄弟节点，后者返回前面第一个兄弟节点。
6.find_all_next()和find_next()：前者返回节点后所有符合条件的节点，后者返回第一个符合条件的节点。
7.find_all_previous()和find_previous()：前者返回节点后所有符合条件的节点，后者返回第一个符合条件的节点。

     
'''

# html = '''
# <div class="panel">
#     <div class="panel-heading">
#         <h4>Hello</h4>
#     </div>
#     <div class="panel-body">
#         <ul class="list" id="list-1" name='elements'>
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#             <li class="element">Jay</li>
#         </ul>
#         <ul class="list list-small" id="list-2">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#         </ul>
#     </div>
# </div>
# '''
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# print(type(soup.find_all(name='ul')))
# print(soup.find_all(name='ul'))
# print(type(soup.find_all(name='ul')[0]))

'''
因为都是Tag类型，所以依然可以进行嵌套查询。还是同样的文本，这里查询出所有ul节点后，再继续查询其内部的li节点
'''

# for ul in soup.find_all(name='ul'):
#     # print(ul.find_all(name='li'))
#     for li in ul.find_all(name='li'):
#         print(li.string)
#         print(li.attrs['class'])

# print(soup.find_all(attrs={'id': 'list-1'}))
# print(soup.find_all(attrs={'name': 'elements'}))

# print(soup.find_all(id='list-1'))
# print(soup.find_all(class_='element'))

# import re
# html='''
# <div class="panel">
#     <div class="panel-body">
#         <a>Hello, this is a link</a>
#         <a>Hello, this is a link, too</a>
#     </div>
# </div>
# '''
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# print(soup.find_all(text=re.compile('link')))

# print(soup.find(name='ul'))
# print(type(soup.find(name='ul')))
# print(soup.find(class_='list'))

# 要使用find_parents等，需要定位到某一个Tag元素
# print(soup.find_all(class_='list')[0].find_parents(class_='panel-body'))

############################################# CSS选择器 ###############################################

html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''

# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# print(soup.select('.panel .panel-heading'))
# print(soup.select('ul li'))
# print(soup.select('#list-2 .element'))
# print(type(soup.select('li')[0]))

# 嵌套选择
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# # for ul in soup.select('ul'):
# #     for li in ul.select('li'):
# #         print(li.name)
# #         print(li.string)
#
# # 获取属性
# # 获取属性还可以用原来的方法[],      .attrs[]
#
# # 获取文本
# # 使用string，  以及另一种方式get_text()

# for li in soup.select('#list-1 .element'):
#     print('Get_text', li.get_text())
#     print('string', li.string)



########################################################################################################################

############################################ pyquery使用 ###############################################################

########################################################################################################################

# html = '''
# <div>
#     <ul>
#          <li class="item-0">first item</li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#          <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a></li>
#      </ul>
#  </div>
# '''
# from pyquery import PyQuery as pq
# res = pq(html)
# print(res('li'))

# 初始化pyquery对象
# 传入字符串， URL 或者  文件进行初始化
#       -     url=    filename=
# from pyquery import PyQuery as pq
#
# res = pq(url='http://cuiqingcai.com')
# print(res('title'))

# html = '''
# <div id="container">
#     <ul class="list">
#          <li class="item-0">first item</li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#          <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a></li>
#      </ul>
#  </div>
# '''


# 查找节点
# 1. 查找子孙节点 ，使用find()方法，参数为css选择器
# 2. 查找直接子节点， 使用children()方法, 传入的参数为css选择器
# 3. 查找某节点的父节点， 使用parent()方法
# 4. 查找某节点的所有祖先节点， 使用parents()方法
# 5. 获取某节点的兄弟节点, 使用siblings()方法



# from pyquery import PyQuery as pq
# res = pq(html)
# items = res('#container .list')
# print(res('#container .list'))
#
# # lis = items.find('li')
# # print(type(lis))
# # print(lis)
#
# lis = items.children('.active')
# print(type(lis))
# print(lis)

# html = '''
# <div class="wrap">
#     <div id="container">
#         <ul class="list">
#              <li class="item-0">first item</li>
#              <li class="item-1"><a href="link2.html">second item</a></li>
#              <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#              <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#              <li class="item-0"><a href="link5.html">fifth item</a></li>
#          </ul>
#      </div>
#  </div>
# '''

from pyquery import PyQuery as pq

# res = pq(html)
# items = res('.list')
# # container = items.parent()
# # print(type(container))
# # print(container)
# parents = items.parents()
# print(parents)
#
# parent = items.parents('.wrap')
# print(parent)

# 注意次数，一个属性多值时，比如class有两个值1，2. 如何要进行csS筛选时,应该注意 .1.2 中间不能加入空格， 加入空格则表示了嵌套关系

# doc = pq(html)
# li = doc('.list .item-0.active')
# print(li.siblings())

# 遍历
'''
pyquery的选择结果可能是多个节点，也可能是单个节点，类型都是PyQuery类型，并没有返回像Beautiful Soup那样的列表
'''
# 对于单个节点来说，可以直接打印输出，也可以直接转成字符串
# 对于多节点的结果，则需要通过遍历来获取
# 通过.items()来得到生成器，从而进行遍历

# from pyquery import PyQuery as pq
# doc = pq(html)
# items = doc('li').items()
# print(type(items))
#
# for i in items:
#     print(i, type(i))

# 获取信息·
# 1. 获取属性
#   .attr('href')
#   .attr.href
'''
照理来说，我们选中的a节点应该有4个，而且打印结果也应该是4个，
但是当我们调用attr()方法时，返回结果却只是第一个。这是因为，当返回结果包含多个节点时，调用attr()方法，只会得到第一个节点的属性。
'''


# 2. 获取文本
# 调用text()方法

# from pyquery import PyQuery as pq
# doc = pq(html)
# a = doc('a')
# print(a)
# print(a.attr.href)
# print(a.attr('href'))
#
# print('\n')
# print('\n')
# for item in a.items():
#     print(item.attr.href)
#     print(item.text())

# 使用text()，它会忽略掉节点内部包含的所有HTML，只返回纯文字内容。
# 如果想要获取这个节点内部的HTML文本，就要用html()方法

# html()方法返回的是第一个li节点的内部HTML文本，
# 而text()则返回了所有的li节点内部的纯文本，中间用一个空格分割开，即返回结果是一个字符串。
# 要遍历每个节点的内部html时，需要hi用.items()进行轮询

html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
#
# from pyquery import PyQuery as pq
#
# doc = pq(html)
# li = doc("li")
# print(li.html())
# print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
# print(li.text())
# print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
# print(type(li.html()))
# print(type(li.text()))
# print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
# print(li.items())
# print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
# for item in li.items():
#     print(item.html())
#     print(item.text())


# 节点操作

# 对节点进行动态修改，比如为某个节点添加一个class，移除某个节点等，这些操作有时候会为提取信息带来极大的便利。
# 由于节点操作的方法太多，下面举几个典型的例子来说明它的用法。
# addClass和removeClass ， 参数是CSS选择器

# attr、text和html
# 当然，除了操作class这个属性外，也可以用attr()方法对属性进行操作。此外，还可以用text()和html()方法来改变节点内部的内容。

# remove()方法就是移除，它有时会为信息的提取带来非常大的便利
# html = '''
# <div class="wrap">
#     Hello, World
#     <p>This is a paragraph.</p>
#  </div>
# '''
# from pyquery import PyQuery as pq
# doc = pq(html)
# wrap = doc('.wrap')
# print(wrap.text())
# 现在想提取Hello, World这个字符串，而不要p节点内部的字符串

#   wrap.find('p').remove()
#   print(wrap.text())

'''
存储
'''

#########################################################################################################

############################################## 文件存储 #################################################

#########################################################################################################
#  txt存储

# import requests
# from pyquery import PyQuery as pq
#
# url = 'https://www.zhihu.com/explore'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
# }
#
# html = requests.get(url=url, headers=headers).text
# doc = pq(html)
# items = doc(".explore-tab .feed-item").items()
# i = 0
# for item in items:
#     question = item.find("h2").text()
#     author = item.find('.author-link-line').text()
#     answer = pq(item.find('.content').html()).text()
#     # print(question)
#     # print("@@@@@")
#     # print(author)
#     # print("@@@@@")
#     # print(answer)
#     with open('explore.txt', 'a', encoding='utf-8') as f:
#         f.write('\n'.join([question,author,answer]))
#         f.write('\n'+'='*50+'\n')


#       文件打开方式
# r：以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
# rb：以二进制只读方式打开一个文件。文件指针将会放在文件的开头。
# r+：以读写方式打开一个文件。文件指针将会放在文件的开头。
# rb+：以二进制读写方式打开一个文件。文件指针将会放在文件的开头。
# w：以写入方式打开一个文件。如果该文件已存在，则将其覆盖。如果该文件不存在，则创建新文件。
# wb：以二进制写入方式打开一个文件。如果该文件已存在，则将其覆盖。如果该文件不存在，则创建新文件。
# w+：以读写方式打开一个文件。如果该文件已存在，则将其覆盖。如果该文件不存在，则创建新文件。
# wb+：以二进制读写格式打开一个文件。如果该文件已存在，则将其覆盖。如果该文件不存在，则创建新文件。
# a：以追加方式打开一个文件。如果该文件已存在，文件指针将会放在文件结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，则创建新文件来写入。
# ab：以二进制追加方式打开一个文件。如果该文件已存在，则文件指针将会放在文件结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，则创建新文件来写入。
# a+：以读写方式打开一个文件。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，则创建新文件来读写。
# ab+：以二进制追加方式打开一个文件。如果该文件已存在，则文件指针将会放在文件结尾。如果该文件不存在，则创建新文件用于读写。

# 清空文件内容
#
# f.truncate()
#
# 注意：仅当以 "r+"   "rb+"    "w"   "wb" "wb+"等以可写模式打开的文件才可以执行该功能。

# 、删除文件
#
# import os
#
# os.remove(file)

# 2.json文件存储
'''
1. 对象和数组
在JavaScript语言中，一切都是对象。因此，任何支持的类型都可以通过JSON来表示，例如字符串、数字、对象、数组等，但是对象和数组是比较特殊且常用的两种类型，下面简要介绍一下它们。

对象：它在JavaScript中是使用花括号{}包裹起来的内容，数据结构为{key1：value1, key2：value2, ...}的键值对结构。在面向对象的语言中，key为对象的属性，value为对应的值。键名可以使用整数和字符串来表示。值的类型可以是任意类型。
数组：数组在JavaScript中是方括号[]包裹起来的内容，数据结构为["java", "javascript", "vb", ...]的索引结构。在JavaScript中，数组是一种比较特殊的数据类型，它也可以像对象那样使用键值对，但还是索引用得多。同样，值的类型可以是任意类型。
所以，一个JSON对象可以写为如下形式：
[{
    "name": "Bob",
    "gender": "male",
    "birthday": "1992-10-18"
}, {
     "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
}]

'''

'''
 读取JSON
Python为我们提供了简单易用的库来实现JSON文件的读写操作，
                        我们可以调用库的loads()方法将JSON文本字符串转为JSON对象，
                        可以通过dumps()方法将JSON对象转为文本字符串。
'''
# import json
# str= '''
# [{
#     "name":"Bob",
#     "gender":"male",
#     "birthday":"1992-02-18"
# },{
#     "name":"加",
#     "gender":"男",
#     "birthday":"1995-02-18"
# }]
# '''
#
# print(str)
# print(type(str))
#
# data = json.loads(str)
# print(data)
# print(type(data))
# str1 = json.dumps(data)

# 使用数组的方式(中括号)调用
# print(data[0])
# print(data[0]["name"])
# print(data[0]['birthday'])
# 也可以使用.get()方式来调用
# print(data[0].get("gender"))

############ 值得注意的是，JSON的数据需要用双引号来包围，不能使用单引号

# 为了输出中文，还需要指定参数ensure_ascii为False，另外还要规定文件输出的编码
# import json
# with open("data.json", "w", encoding='utf-8') as file:
#     file.write(json.dumps(str, indent=2,ensure_ascii=False))  # 加入indent表示缩进
#
# with open("data.json", "r", encoding='utf-8') as file:
#     data1 = file.read()
#     print(data1)
#     print(type(data1))
#     data = json.loads(data1)
#     print(data)
#     print(type(data))

#  3.csv文件保存
# import csv
#
# with open("data.csv", "w") as file:
#     # 调用csv库的writer()方法初始化写入对象，传入该句柄，然后调用writerow()方法传入每行的数据即可完成写入。
#     # writedowns()一次写入多行
#     # 如果想修改列与列之间的分隔符，可以传入delimiter参数
#     # writer = csv.writer(file, delimiter=' ')
#     # writer.writerow(['id', 'name', 'age'])
#     # # writer.writerow(['10001', 'Mike', '20'])
#     # # writer.writerow(['10002', 'Bob', '22'])
#     # # writer.writerow(['10003', 'Jordan', '18'])
#     # writer.writerows([['10004', 'Mik', '20'], ['10005', 'ike', '20'],['10006', 'Mke', '21']])
#     filednames = ['id', 'name', 'age']
#     writer = csv.DictWriter(file, fieldnames=filednames)
#     writer.writeheader()
#     writer.writerow({'id':'10003', 'name':'Jordan', 'age':'18'})
#     writer.writerow({'id': '10004', 'name': 'Jordan', 'age': '18'})

# 用fieldnames表示，然后将其传给DictWriter来初始化一个字典写入对象，接着可以调用writeheader()方法先写入头信息，
# 然后再调用writerow()方法传入相应字典即可。最终写入的结果与直接writer.writerow()完全相同的

# import csv
# with open("data.csv", 'r', encoding='utf-8') as file:
#     render = csv.reader(file)
#     for i in render:
#         if i == []:
#             continue
#         print(i)

#########################################################################################################

############################################## 数据库存储 #################################################

#########################################################################################################
# mysql
# 1. 创建数据库
import pymysql
# 还没有创建数据库前，不需要指定db
# db = pymysql.connect(host='localhost', user='root', port=3306)
# cursor = db.cursor()
# # 获取数据库游标
# cursor.execute('SELECT VERSION()')
# 调用游标的execute()函数进行数据库sql语言的操作
# data = cursor.fetchone()
#
# print("version", data)
# cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")
# db.close()

# # 2. 创建表
# db = pymysql.connect(host='localhost', user='root', port=3306, db="spiders")
# cursor = db.cursor()
# sql = "create table if not exists students(id varchar(255) not null, name varchar(255) not null, age int not null, primary key (id))"
# cursor.execute(sql)
# db.close()
#
# # 3. 插入数据
# 对于数据插入、更新、删除操作，都需要调用db的commit()方法才能生效
# commit和rollback保证数据库更改事务的ACID
# data =[["20120001", "Bob", 20],
#         ["20120002", "Mike", 21],
#         ["20120003", "Tom", 22],
#         ["20120004", "Amy", 23]
#        ]
# db = pymysql.connect(host='localhost', user='root', port=3306, db="spiders")
# cursor = db.cursor()
# sql = "insert into students(id,name,age) values(%s,%s,%s)"
# try:
#     for item in data:
#         cursor.execute(sql, (item[0], item[1], item[2]))
#     db.commit()
# except:
#     db.rollback()
# db.close()

#
import pymysql
# data =[{'id':"20120001", 'name':"Bob", 'age':20},
#        {'id': "20120002", 'name': "Bob", 'age': 21},
#        {'id': "20120003", 'name': "Bob", 'age': 22},
#        {'id': "20120004", 'name': "Bob", 'age': 23}]
#
# db = pymysql.connect(host='localhost', user="root", port=3306, db="spiders")
# cursor = db.cursor()
# table = "student"
# sql1 = "create table if not exists {table} (id varchar(255) not null, name varchar(255) not null, age int not null, primary key (id))".format(table=table)
# cursor.execute(sql1)
# print(tuple(data[0].values()))
# keys = ', '.join(data[0].keys())
# values = ", ".join(["%s"]*len(data[0]))
#### 动态构造sql语句，实现通用的插入方法
# sql = "insert into {table}({keys}) values({values})".format(table=table,keys=keys,values=values)
#
# print(sql)
# try:
#     for item in data:
#         print(item.values())
#         cursor.execute(sql, tuple(item.values()))
#
#     print("successfully")
#     db.commit()
# except :
#     print("Failed")
#     db.rollback()
# db.close()

# 更新数据
# sql_update = 'update student set age=%s where name=%s'
# db = pymysql.connect(host='localhost', user="root", port=3306, db="spiders")
# cursor = db.cursor()
# try:
#     cursor.execute(sql_update, (30, "Bob"))
#     db.commit()
# except:
#     db.rollback()
# db.close()

### 实现主键不存在便插入数据，存在则更新数据的功能了

# 删除数据

# 查询数据
# 使用数据库游标执行完查询语句，通过游标的fetch方法来获取sql语句执行之后的数据
# db = pymysql.connect(host='localhost', user="root", port=3306, db="spiders")
# cursor = db.cursor()
# sql_query = "select * from student where age > %s"
# try:
#     cursor.execute(sql_query, (20))
#     print('Count:', cursor.rowcount)
#     data = cursor.fetchone()
#     print("one" , data)
#     data = cursor.fetchall()
#     print("all", data)
#     print("type", type(data))
#     for item in data:
#         print(item)
#
# except:
#     db.rollback()
# db.close()


'''
查询tips:
此外，我们还可以用while循环加fetchone()方法来获取所有数据，而不是用fetchall()全部一起获取出来。
fetchall()会将结果以元组形式全部返回，如果数据量很大，那么占用的开销会非常高。因此，推荐使用如下方法来逐条取数据：

sql = 'SELECT * FROM students WHERE age >= 20'
try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)
    row = cursor.fetchone()
    while row:
        print('Row:', row)
        row = cursor.fetchone()
except:
    print('Error')
这样每循环一次，指针就会偏移一条数据，随用随取，简单高效。
'''
# MongoDB
# import pymongo
# 1.连接MongoDB
# client = pymongo.MongoClient(host='localhost', port=27017)

# 2.指定数据库
# db = client.dbname
# db = client['spiders']

# 3.指定集合
# collection = db.students
# collection = db['students']

# 4.插入数据
# insert插入数据，不限定条数
# insert_one插入一条数据， insert_many插入多条数据
# data = [{
#     'id': '20170101',
#     'name': 'Jordan',
#     'age': 20,
#     'gender': 'male'
# }, {
#     'id': '20170202',
#     'name': 'Mike',
#     'age': 21,
#     'gender': 'male'
# }]
# result = collection.insert(data)
# print(result)

# student = {
#     'id': '20170101',
#     'name': 'Jordan',
#     'age': 20,
#     'gender': 'male'
# }
# res = collection.insert_one(student)
# print(res)
# print(res.inserted_id)

# 5.查询数据
# find_one({查询条件}), 返回结果是dict
# find(), 返回结果是Cursor类型生成器，

# result = collection.find({'age': {'$lt': 30}})
# print(result)
# print(type(result))
# for item in result:
#     print(item)

'''
比较符号
符号                  含义                      示例

$lt                   小于                    {'age': {'$lt': 20}}

$gt                   大于                    {'age': {'$gt': 20}}

$lte                 小于等于                 {'age': {'$lte': 20}}

$gte                 大于等于                 {'age': {'$gte': 20}}

$ne                  不等于                   {'age': {'$ne': 20}}

$in                  在范围内                 {'age': {'$in': [20, 23]}}

$nin                不在范围内                {'age': {'$nin': [20, 23]}}

功能符号

符号             含义                   示例                                       示例含义

$regex      匹配正则表达式         {'name': {'$regex': '^M.*'}}                   name以M开头

$exists     属性是否存在           {'name': {'$exists': True}}                    name属性存在

$type          类型判断             {'age': {'$type': 'int'}}                     age的类型为int

$mod          数字模操作            {'age': {'$mod': [5, 0]}}                        年龄模5余0

$text           文本查询           {'$text': {'$search': 'Mike'}}                   text类型的属性中包含Mike字符串

$where       高级条件查询      {'$where': 'obj.fans_count == obj.follows_count'}      自身粉丝数等于关注数

'''
# result = collection.find({'name':{'$regex': '^M.*'}})
# for item in result:
#     print(item)

# 6. 计数
#  .count()进行统计计数
# count = collection.find().count()
# print(count)

# 7.排序
# results = collection.find().sort('age', pymongo.DESCENDING)
# # print(result['name'] for result in results)
# for result in results:
#     print(result)

# 8.偏移
# 利用skip()方法偏移几个位置，比如偏移2，就忽略前两个元素，得到第三个及以后的元素
# 使用.limit()方法指定返回的结果的个数
# results =collection.find().skip(2).limit(1)
# for result in results:
#     print(result)

# 7.更新
# 使用update()方法, 第二个参数可以直接修改，写
# 使用update_one()方法，第二个参数需要使用$类型操作符作为字典的键名
# 使用update_many()方法

# 分别调用matched_count和modified_count属性，可以获得匹配的数据条数和影响的数据条数。

# condition = {'name': 'Jordan'}
# student = collection.find_one(condition)
#
# result = collection.update_one(condition, {'$set': {'id': '20170103'}})
# print(result)
#
# res = collection.find()
# for i in res:
#     print(i)

'''
{'$set':{  :  }}
{'$inc':{  :  }}
'''

# 10. 删除
# remove()
# delete_one()
# delete_many()


# result = collection.remove({'name': 'Tom'})
# res = collection.find()
# for i in res:
#     print(i)


'''
另外，PyMongo还提供了一些组合方法，如find_one_and_delete()、find_one_and_replace()和find_one_and_update()，
                                                它们是查找后删除、替换和更新操作，其用法与上述方法基本一致。

另外，还可以对索引进行操作，相关方法有create_index()、create_indexes()和drop_index()等。
'''

import requests
from pyquery import PyQuery as pq
import csv
import json
import pymysql
import pymongo

# url = 'https://www.zhihu.com/explore'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
# }
#
# html = requests.get(url=url, headers=headers).text
# doc = pq(html)
#
# items = doc("#js-explore-tab .explore-feed").items()

# 文件保存
# flag = 1

# with open("zhizhu.csv", "a+", encoding="utf-8") as file:
#     fieldname = ['question', 'author', 'content', 'comment']
#     writer = csv.DictWriter(file, fieldnames=fieldname)
#     writer.writeheader()
#     for item in items:
#
#         question = item.find("h2 a").text()
#         author = item.find(".author-link-line").text()
#         content = pq(item.find(".content").html()).text()
#         comment = item.find(".meta-item.toggle-comment").text()
#
#         # question = "问题:"+question
#         # author = "作者:"+author
#         # content = "内容:"+content
#         # comment = "评论数:"+comment
#         # # text保存
#         # with open("zhihu.txt", "a+", encoding="utf-8") as file:
#         #     file.write("\n"+ str(flag) + "==>" * 50 + "\n")
#         #     file.write("\n".join([question, author, content, comment]))
#
#         # #json保存
#         # data = [{
#         #     "question":question,
#         #     "author":question,
#         #     "content":content,
#         #     "comment":comment
#         # }]
#         # file.write(json.dumps(data, ensure_ascii=False))
#
#         # # csv保存
#         data = {
#             'question':question,
#             'author':question,
#             'content':content,
#             'comment':comment
#         }
#         writer.writerow(data)
#
#         flag +=1

# 数据库保存
# mysql创建
# db = pymysql.connect(host="localhost", user="root", port=3306)
# cursor = db.cursor()
# sql_create = "create database zhihu default character set utf8"
# cursor.execute(sql_create)
# db.close()
# db = pymysql.connect(host="localhost", user="root", port=3306, db="zhihu")
# cursor =db.cursor()

# sql_drop = "drop table hots"
# cursor.execute(sql_drop)
# db.commit()

# sql_create_table = "create table if not exists hots(id varchar(255) not null, question varchar(255) not null, author varchar(255) not null, answer mediumtext not null , comment varchar(255) not null, primary key(id) ) "
# cursor.execute(sql_create_table)
# try:
#
#     tables = "hots"
#     keys = ", ".join(['id', 'question', 'author', 'answer', 'comment'])
#     values = ", ".join(['%s']*5)
#     flag = 1
#     for item in items:
#         question = item.find("h2 a").text()
#         author = item.find(".author-link-line").text()
#         content = pq(item.find(".content").html()).text()
#         comment = item.find(".meta-item.toggle-comment").text()
#
#         sql_insert = "insert into {tables}({keys}) values({values})".format(tables=tables, keys=keys, values=values)
#         id = str(flag).rjust(4, '0')
#
#         cursor.execute(sql_insert, (id, question, author, content, comment))
#         flag += 1
#     db.commit()
# except:
#     db.rollback()

# 查询
# tables = "hots"
# sql_query = "select * from {tables}".format(tables=tables)
# try:
#     cursor.execute(sql_query)
#     print("counts", cursor.rowcount)
#     row = cursor.fetchone()
#     while row:
#         print("Row", row)
#         row = cursor.fetchone()
# except:
#     db.rollback()
#
# db.close()

# mongoDB

# client = pymongo.MongoClient(host="localhost", port=27017)
#
# # 创建
# zhihu = client['zhihu']
# hots = zhihu['hots']
#
# result = hots.delete_many({"id": {'$regex': '^00.*'}})
#
# flag = 1
# for item in items:
#     id = str(flag).rjust(4, '0')
#     question = item.find("h2 a").text()
#     author = item.find(".author-link-line").text()
#     content = pq(item.find(".content").html()).text()
#     comment = item.find(".meta-item.toggle-comment").text()
#
#     one_piece = {
#         'id':id,
#         'question':question,
#         'author':author,
#         'answer':content,
#         'comment':comment
#     }
#     result = hots.insert_one(one_piece)
#     flag += 1
#
# result = hots.find()
# for re in result:
#     print(re)

########################################################################################################################

################################################### Ajax ###############################################################

########################################################################################################################

# ######################################################################################################################
# from urllib.parse import urlencode
# import requests
# from pyquery import PyQuery as pq
# import pymongo
#
# base_url = "https://m.weibo.cn/api/container/getIndex?"
# headers = {
#     'Host': 'm.weibo.cn',
#     'Referer': 'https://m.weibo.cn/u/2830678474',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
#     'X-Requested-With': 'XMLHttpRequest',
# }
#
# def get_page(page):
#     params = {
#         'type': 'uid',
#         'value': '2830678474',
#         'containerid': '1076032830678474',
#         'page': page
#     }
#     url = base_url + urlencode(params)
#     try:
#         response = requests.get(url, headers=headers)
#         if response.status_code == 200:
#             return response.json()
#     except requests.ConnectionError as e:
#         print('Error', e.args)
#
# def parse_page(json):
#     if json:
#         items = json.get('data').get('cards')
#         for item in items:
#             item = item.get('mblog')
#             if item != None:
#                 weibo = {}
#                 weibo['id'] = item.get('id')
#                 # pyquery将正文的html标签去掉
#                 weibo['text'] = pq(item.get('text')).text()
#                 weibo['attitudes'] = item.get('attitudes_count')
#                 weibo['comments'] = item.get('comments_count')
#                 weibo['reposts'] = item.get('reposts_count')
#                 yield weibo
#
# if __name__ == '__main__':
#
#     # 保存到mongoDB数据库之中
#     client = pymongo.MongoClient(host='localhost', port=27017)
#     db = client['spiders']
#     table = db['tiezis']
#
#     for page in range(1, 11):
#         json = get_page(page)
#         parse_page(json)
#         results = parse_page(json)
#
#         for result in results:
#             # print(result)
#             result = table.insert_one(result)
#
#     query_result = table.find()
#     for res in query_result:
#         print(res)

#########################################################################################################################
# Ajax爬取今日头条街拍美图
# 通过直接分析Ajax, 借助requests或urllib来实现数据爬取

# import requests
# from urllib.parse import urlencode
# from pyquery import PyQuery as pq
# import os
# from hashlib import md5
# from multiprocessing.pool import Pool
#
# def get_page(offset):
#     params = {
#         'offset': offset,
#         'format': 'json',
#         'keyword':'街拍',
#         'autoload':'true',
#         'count':'20',
#         'cur_tab':'1',
#         'from':'search_tab'
#     }
#     base_url = 'https://www.toutiao.com/search_content/?'
#     url = base_url + urlencode(params)
#
#     try:
#         response = requests.get(url)
#         if response.status_code == 200:
#             return response.json()
#     except requests.ConnectionError as e:
#         print(e)
#         return None
#
# def get_image(json):
#     if json.get('data'):
#         for item in json.get('data'):
#             title = item.get('title')
#             if title == None:
#                 continue
#             images = item.get('image_list')
#             for image in images:
#                 yield{
#                     'image': image.get('url'),
#                     'title': title
#                 }
#
# def save_image(item):
#     mkdir_path = item.get('title')
#     mkdir_path = "jiepai_image//"+mkdir_path
#     if not os.path.exists(mkdir_path):
#         os.mkdir(mkdir_path)
#     try:
#         image_path = "http:{path}".format(path=item.get('image'))
#         response = requests.get(image_path)
#         if response.status_code == 200:
#             file_path = "{0}/{1}.{2}".format(mkdir_path, md5(response.content).hexdigest(), 'jpg')
#             if not os.path.exists(file_path):
#                 with open(file_path, 'wb') as file:
#                     file.write(response.content)
#             else:
#                 print('Already Download', file_path)
#
#     except requests.ConnectionError as e:
#         print(e)
#
# def main(offset):
#     json = get_page(offset=offset)
#     base_dir = "jiepai_image"
#     os.mkdir(base_dir)
#     for item in get_image(json):
#         print(item)
#         save_image(item)
#
# GROUP_START = 1
# GROUP_END = 20
#
# if __name__ == '__main__':
#     # pool = Pool()
#     # groups = ([x * 20 for x in range(GROUP_START, GROUP_END+1)])
#     # pool.map(main, groups)
#     # pool.close()
#     # pool.join()
#
#     for i in range(0,1):
#         main(i)

########################################################################################################################












