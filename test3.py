import datetime
import zabixmaster as zb
now = datetime.datetime(2018,4,20)
end_time=datetime.datetime(2018,4,24)
dic3={}
delta = datetime.timedelta(1)
zb.db_connect('zabbixinfo','1234','localhost')
#while now!=end_time:
     	#now +=delta
dic2=zb.hosts('Squid01',now,end_time)
print(dic2)
#dic3[now]=dic2
