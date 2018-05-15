import re,subprocess
##MEMORY
##SIZE
def onevm(vm_name):
	dic = {}
	with subprocess.Popen(['sshpass','-p','opennebula_manager*','ssh','root@10.8.9.189','onevm','show',vm_name,'--all'],stdout = subprocess.PIPE) as p:
		print('dasdasd')
		output = p.stdout.read().decode()
		# print(output)
	patt1 = re.compile('VCPU="(.+)"')
	patt2 = re.compile('MEMORY="(.+)"')
	patt3 = re.compile(r'\s+(SIZE="(.+)")')
	VCPU = patt1.search(output)
	MEMORY = patt2.search(output)
	SIZE = patt3.search(output)
	# print(VCPU.group(1))
	# print(MEMORY.group(1))
	# print(SIZE.group(2))
	dic={'asignacion vCPU': float(VCPU.group(1)),'asignacion RAM':float(MEMORY.group(1)),'asignacion disco':float(SIZE.group(2)),'asignacion IOPS':'no limitado','asignacion throughput':'no limitado','asignacion red TX':'no limitado','asignacion red RX':'no limitado'}
	return dic
dic = onevm('SQUID01')
print(dic)