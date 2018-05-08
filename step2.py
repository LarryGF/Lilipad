import json
import zabixmaster as zb

def step2_load(table_name):
    with open('step2.json') as f:
        dic = json.load(f)
        for table in dic.keys():
            lista=[]
            for fila in sorted(dic[table].keys()):  ####ordenar las filas al ingresarlas a la lista
                lista.append(dic[table][fila])
    return lista#####retornarle diccionario con todas las tablas,llave-nombre da tabla,valor-lista con filas

def step2_write(table_name,lista):###nos devuelve nombre da tabla y lista con filas
    with open('step2.json') as f:
        d = json.load(f)
    for i in range(len(lista)): ##
        d[table_name][i+1] = lista[i]
    with open('step2.json','w') as f:
        json.dump(d,f)

def step3_load(table_list):####diccionario con los nombres da las tablas
    with open('step3.json') as f:
        dic=json.load(f)
    if 'IaaS' and 'DSaaS' in table_list:
        for table in dic.keys():
            lista=[]
            for fila in dic[table].keys():  ####ordenar las filas al ingresarlas a la lista
                lista.append(dic[table][fila])
            dic[table]=lista
        return dic        
    else:
        lista=[]
        for fila in dic[table_list[0]].keys():  ####ordenar las filas al ingresarlas a la lista
            lista.append(dic[table_list[0]][fila])
        dic[table_list[0]]=lista       
        return [table_list[0]]
### nos va a dar un diccionario con la seleccion,
### hacer un for para ver que tabla enviar 

  
def step3_write(table,dic):###nos devuelve nombre da tabla y lista con filas
    with open('step3.json') as f:
        d = json.load(f)
    d[table] = dic
    with open('step3.json','w') as f:
        json.dump(d,f)

def step5 (servicio,user,passw,db_addr,start_time,end_time):
    dic3={}
    dic= step2_load('tabla')######la funcion cambio,nesecitamos modificar estooooooooo
    for row in dic.keys():
        if dic[row]['servicio'] == servicio:
            with open('parser.json') as f:
                parse = json.load(f)
            zabbix_id = parse[dic[row]['MV']]
            now = start_time
            delta = dt.td(1)
            zb.db_connect(user,passw,db_addr)
            while now!=end_time:
                now +=delta
                dic2=zb.hosts(zabbix_id,now,end_time) ##Numero de items id en zabbix de variables a monitorizar tabla 2.9          
                dic3[now]=dic2    
    
    
        
parse={'SQUID01':'Squid01','SQUID02':'Squid02','SQUID03':'Squid03','SQUID04':'Squid04','SQUID05':'Squid05','SQUID06-RECTORA':'Squid06','SQUID07':'Squid07'
        'SQUID08-228':'Squid08','SQUID09':'Squid09','SQUID10':'Squid10','SQUID11-229':'Squid11','SQUID12-230':'Squid12','SQUID13':'Squid13','SQUID14':'Squid14',
        }    
    
        
