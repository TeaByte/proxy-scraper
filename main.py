import re
import requests
import threading


print('''
    ╔═╗┬─┐┌─┐─┐ ┬┬ ┬  ┌─┐┌─┐┬─┐┌─┐┌─┐┌─┐┌─┐┬─┐
    ╠═╝├┬┘│ │┌┴┬┘└┬┘  └─┐│  ├┬┘├─┤├─┘├─┘├┤ ├┬┘
    ╩  ┴└─└─┘┴ └─ ┴   └─┘└─┘┴└─┴ ┴┴  ┴  └─┘┴└─
                                        [ V2 ]
        - Coder: @Tufaah
            
''')


urls = '''
http://globalproxies.blogspot.com/
http://www.cybersyndrome.net/plz.html
http://www.cybersyndrome.net/plr5.html
http://biskutliat.blogspot.com/
http://freeproxylist-daily.blogspot.com/2013/05/usa-proxy-list-2013-05-15-0111-am-gmt8.html
http://freeproxylist-daily.blogspot.com/2013/05/usa-proxy-list-2013-05-13-812-gmt7.html
http://www.cybersyndrome.net/pla5.html
http://vipprox.blogspot.com/2013_06_01_archive.html
http://vipprox.blogspot.com/2013/05/us-proxy-servers-74_24.html
http://vipprox.blogspot.com/p/blog-page_7.html
http://vipprox.blogspot.com/2013/05/us-proxy-servers-199_20.html
http://vipprox.blogspot.com/2013_02_01_archive.html
http://alexa.lr2b.com/proxylist.txt
http://vipprox.blogspot.com/2013_03_01_archive.html
http://browse.feedreader.com/c/Proxy_Server_List-1/449196260
http://browse.feedreader.com/c/Proxy_Server_List-1/449196258
http://sock5us.blogspot.com/2013/06/01-07-13-free-proxy-server-list.html#comment-form
http://browse.feedreader.com/c/Proxy_Server_List-1/449196251
http://free-ssh.blogspot.com/feeds/posts/default
http://browse.feedreader.com/c/Proxy_Server_List-1/449196259
http://sockproxy.blogspot.com/2013/04/11-04-13-socks-45.html
http://proxyfirenet.blogspot.com/
https://www.javatpoint.com/proxy-server-list
https://openproxy.space/list/http
http://proxydb.net/
http://olaf4snow.com/public/proxy.txt
http://westdollar.narod.ru/proxy.htm
https://openproxy.space/list/socks4
https://openproxy.space/list/socks5
http://tomoney.narod.ru/help/proxi.htm
http://sergei-m.narod.ru/proxy.htm
http://rammstein.narod.ru/proxy.html
http://greenrain.bos.ru/R_Stuff/Proxy.htm
http://inav.chat.ru/ftp/proxy.txt
http://johnstudio0.tripod.com/index1.htm
http://atomintersoft.com/transparent_proxy_list
http://atomintersoft.com/anonymous_proxy_list
http://atomintersoft.com/high_anonymity_elite_proxy_list
http://atomintersoft.com/products/alive-proxy/proxy-list/3128
http://atomintersoft.com/products/alive-proxy/proxy-list/com
http://atomintersoft.com/products/alive-proxy/proxy-list/high-anonymity/
http://atomintersoft.com/products/alive-proxy/socks5-list
http://atomintersoft.com/proxy_list_domain_com
http://atomintersoft.com/proxy_list_domain_edu
http://atomintersoft.com/proxy_list_domain_net
https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt
https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt
http://atomintersoft.com/proxy_list_domain_org
http://atomintersoft.com/proxy_list_port_3128
http://atomintersoft.com/proxy_list_port_80
http://atomintersoft.com/proxy_list_port_8000
http://atomintersoft.com/proxy_list_port_81
http://hack-hack.chat.ru/proxy/allproxy.txt
https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt
http://hack-hack.chat.ru/proxy/anon.txt
http://hack-hack.chat.ru/proxy/p1.txt
http://hack-hack.chat.ru/proxy/p2.txt
http://hack-hack.chat.ru/proxy/p3.txt
http://hack-hack.chat.ru/proxy/p4.txt
https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt
https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt
https://free-proxy-list.net/
https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt
https://www.us-proxy.org/
https://free-proxy-list.com/
https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt
https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all
https://api.proxyscrape.com/?request=getproxies&proxytype=socks4&timeout=10000&country=all
https://api.proxyscrape.com/?request=getproxies&proxytype=socks5&timeout=10000&country=all
https://spys.one/
https://api.proxyscrape.com/?request=getproxies&proxytype=https&timeout=10000&country=all&ssl=all&anonymity=all
https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all
https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/proxy.txt
https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all
https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all
'''


file = open('proxies.txt', 'w')
file.write('Proxies:\n')
file.close()
file = open('proxies.txt', 'a')
good_proxies = list()


def pattern_one(url):
    ip_port = re.findall('(\d{,3}\.\d{,3}\.\d{,3}\.\d{,3}:\d{2,5})', url)
    if not ip_port: pattern_two(url)
    else:
        for i in ip_port:
            file.write(str(i) + '\n')
            good_proxies.append(i)


def pattern_two(url):
    ip = re.findall('>(\d{,3}\.\d{,3}\.\d{,3}\.\d{,3})<', url)
    port = re.findall('td>(\d{2,5})<', url)
    if not ip or not port: pattern_three(url)
    else:
        for i in range(len(ip)):
            file.write(str(ip[i]) + ':' + str(port[i]) + '\n')
            good_proxies.append(str(ip[i]) + ':' + str(port[i]))


def pattern_three(url):
    ip = re.findall('>\n[\s]+(\d{,3}\.\d{,3}\.\d{,3}\.\d{,3})', url)
    port = re.findall('>\n[\s]+(\d{2,5})\n', url)
    if not ip or not port: pattern_four(url)
    else:
        for i in range(len(ip)):
            file.write(str(ip[i]) + ':' + str(port[i]) + '\n')
            good_proxies.append(str(ip[i]) + ':' + str(port[i]))


def pattern_four(url):
    ip = re.findall('>(\d{,3}\.\d{,3}\.\d{,3}\.\d{,3})<', url)
    port = re.findall('>(\d{2,5})<', url)
    if not ip or not port: pattern_five(url)
    else:
        for i in range(len(ip)):
            file.write(str(ip[i]) + ':' + str(port[i]) + '\n')
            good_proxies.append(str(ip[i]) + ':' + str(port[i]))


def pattern_five(url):
    ip = re.findall('(\d{,3}\.\d{,3}\.\d{,3}\.\d{,3})', url)
    port = re.findall('(\d{2,5})', url)
    for i in range(len(ip)):
        file.write(str(ip[i]) + ':' + str(port[i]) + '\n')
        good_proxies.append(str(ip[i]) + ':' + str(port[i]))


def start(url):
    try:
        req = requests.get(url, headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}).text
        pattern_one(req)
        print(f' [+] Scrapping from: {url}')
    except requests.exceptions.SSLError: print(str(url) + ' [x] SSL Error')
    except: print(str(url) + ' [x] Random Error')


threads = list()
for url in urls.splitlines():
    if url:
        x = threading.Thread(target=start, args=(url, ))
        x.start()
        threads.append(x)


for th in threads:
    th.join()


input(f' \n\n[/] Total scraped proxies: ({len(good_proxies)}) type and thing to quit! ')
