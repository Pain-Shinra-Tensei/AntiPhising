# buat bikin kapok orang yg suka sebar phising Facebook
import os, sys, mechanize, cookielib, random, time

email = str(raw_input('[-] email : '))
sandi = str(raw_input('[+] password : '))
url = 'http://hotzz.invites-grbsexxindofullz.cf/login.php'
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
    br.form['email'] = email
    br.form['password'] = sandi
    sub = br.submit()
    log = sub.geturl()
    if log != url and 'check.php' not in log:
        print('[-] gagal')
	sys.exit()
    else:
	print('[-] berhasil')
	main()

if __name__ == '__main__':
    main()
