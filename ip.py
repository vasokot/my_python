##мониторинг, тестовый скрипт для проверки знаний по питону


import ipaddress
import subprocess
import platform
import cx_Oracle
import os


usr = 'S-------'
pwd = '---------'
hst='--------.ru'
prt='1521'
db='----'

ro_com='---'
sysobj = '.1.3.6.1.2.1.1.2.0'

def ping(ip):
	operating_sys = platform.system()
	if operating_sys == 'Windows':
		ping_command = 'ping ' + ip + ' -n 1 -w 20'
	else: 
		ping_comand= 'ping ' + ip + ' -c 1'
	
	shell_needed = True if operating_sys == 'Windows' else False

	ping_output = subprocess.run(ping_command,shell=shell_needed,stdout=subprocess.PIPE)
	success = ping_output.returncode
	return True if success == 0 else False


def snmpget(ip, mib):
	
	operating_sys = platform.system()
	shell_needed = True if operating_sys == 'Windows' else False
	
	cmd ='snmpwalk -v2c -On -c ' + ro_com + ' ' + ip + ' ' + mib
	p = subprocess.Popen(cmd.split(),shell=shell_needed,stdout=subprocess.PIPE)
	out,err = p.communicate()
	res1 = str(out.strip(), 'utf-8')
	
	res2=res1.split(':')
	
	if len(res1.split('='))>1:
		res=res2[1].strip()
	else:
		res=res2
	
	
	assert 0 == p.wait()
	
	return res
	
	
mydsn=cx_Oracle.makedsn(hst, prt, service_name=db)
mycon = cx_Oracle.connect(user=usr,password=pwd, dsn=mydsn)
mycur = mycon.cursor()
mycur.execute('set role FASTCOM_MAIN identified by --------')
mycur.execute("select ipaddress from tomtel.mn_t_switch WHERE ipaddress like '192.168.%.%'")


myres = mycur.fetchall()

#cnt=len(myres)
#print('All: ' + str(cnt))

for myip in myres :
	ip = str(myip[0])
	
	if ping(ip):
		print('Host ' + ip + ' snmp out: ' + snmpget(ip,sysobj))
	
	
	
	else:
		print('host down: ' + ip)

	
mycur.close()
mycon.close()