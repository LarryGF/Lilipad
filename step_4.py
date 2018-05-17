
def step_4(dic):		###diccionario con servicio y argumentos
	if dic['servicio']=='correo':
		import correo
		##el orden de los argumentos es:ruta,mes/dia
		correo.main(dic['ruta'],dic['fecha'])		
	elif dic['servicio']=='navegacion':
		import QoE
		##el orden de los argumentos es: ruta,lista de usuarios,start_time,end_time
		QoE.main(dic['ruta'],dic['users_list'],dic['start_time'],dic['end_time'])
lista=['ftomar.hd','abdcasamayorf','abmarcosqq','abfelixxd']
##step_4('navegacion','access.log',lista,1522837518,1522852855)
##step_4('correo','mail.log','050
dic = {'servicio':'navegacion','ruta':'access.log','users_list':lista,'start_time':1522324800.0,'end_time':1522339200.0}
step_4(dic)
