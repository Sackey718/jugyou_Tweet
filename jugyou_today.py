#coding:utf-8
def tweet(data):
	from requests_oauthlib import OAuth1Session

	CK = 'Your consumer key'
	CS = 'Your consumer secret'
	AT = 'Your access token'
	AS = 'Your access secret'
	url = "https://api.twitter.com/1.1/statuses/update.json"

	params = {"status":data}
	twitter = OAuth1Session(CK, CS, AT, AS)
	req = twitter.post(url, params = params)

	if req.status_code == 200:
	        print ("Tweet Success!")
	else:
	        print ("Error: %d" %req.status_code)

#-----------------------------------------------------------------------------

import urllib2
import zenhan
import datetime

res = urllib2.urlopen("http://jyugyou.tomakomai-ct.ac.jp/jyugyou.php")
html = res.read()
html = html.replace("\t",'')
html = html.upper()
html = html.split('HEIGHT="35"')
del html[0]
html = "".join(html)
html = html.split('>')
tmp = []
print html
for count in html:
	if not count.startswith("<"):
		count = count[:count.find('<')]
		tmp.append(count.decode('utf-8'))
del tmp[0]
honka = ""
senkoka = ""
flag = 0
hs = 0
gyo = 0

for count in tmp:
	if count.startswith("AE"):
		gyo = 0
		hs = 1
		senkoka += zenhan.z2h(count)
	elif count.startswith("AP"):
		gyo = 0
		hs = 1
		senkoka += zenhan.z2h(count)
	elif count.encode('utf-8').startswith("１年"):
		gyo = 0
		hs = 0
		honka += zenhan.z2h(count)
	elif count.encode('utf-8').startswith("２年"):
		gyo = 0
		hs = 0
		honka += zenhan.z2h(count)
	elif count.encode('utf-8').startswith("３年"):
		gyo = 0
		hs = 0
		honka += zenhan.z2h(count)
	elif count.encode('utf-8').startswith("４年"):
		gyo = 0
		hs = 0
		honka += zenhan.z2h(count)
	elif count.encode('utf-8').startswith("５年"):
		gyo = 0
		hs = 0
		honka += zenhan.z2h(count)
	elif count.encode('utf-8').startswith("専１年"):
		gyo = 0
		hs = 1
		senkoka += zenhan.z2h(count)
	elif count.encode('utf-8').startswith("専２年"):
		gyo = 0
		hs = 1
		senkoka += zenhan.z2h(count)
	elif count.startswith("M"):
		gyo = 0
		hs = 0
		honka += zenhan.z2h(count)
	elif count.startswith("A"):
		gyo = 0
		hs = 0
		honka += zenhan.z2h(count)
	elif count.startswith("J"):
		hs = 0
		gyo = 0
		honka += zenhan.z2h(count)
	elif count.startswith("S"):
		hs = 0
		gyo = 0
		honka += zenhan.z2h(count)
	elif count.startswith("K"):
		hs = 0
		gyo = 0
		honka += zenhan.z2h(count)
	else:
		if flag == 1:
			if hs == 0:
				honka += zenhan.z2h(count)+'\n'
			else:
				senkoka += zenhan.z2h(count)+'\n'
			flag = 0
			continue

		if hs == 0:
			if gyo == 0:
				honka += zenhan.z2h(count)
				gyo = gyo+1
			else:
				honka += "  "+zenhan.z2h(count)
			flag = 1
		elif hs == 1:
			if gyo == 0:
				senkoka += zenhan.z2h(count)
				gyo = gyo+1
			else:
				senkoka += "   "+zenhan.z2h(count)
			flag = 1
today = datetime.datetime.today()
data = "本日"+today.strftime('%m月%d日') + "の授業変更(本科)\n"
if len(honka) > 0:
	data += honka.encode('utf-8')
else:
	data += "授業変更はありません"
print data
tweet(data)

data = "本日"+today.strftime('%m月%d日') + "の授業変更(専攻科)\n"
if len(senkoka) > 0:
	data += senkoka.encode('utf-8')
else:
	data += "授業変更はありません"
print data
tweet(data)
