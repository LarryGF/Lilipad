import json,os,datetime
import zabixmaster as zb
import opennebula 
from readingdbmodif import percentil,rank,mean

def load(table_name):
    for root,dirs,files in os.walk(os.getcwd()):
        for file in files:
            if file == str(table_name)+'.json':
                path = os.join(root,file)
                
            # try:
                with open(path) as f:
                    dic = json.load(f)
                    lista=[]
                for fila in sorted(dic.keys()):  ####ordenar las filas al ingresarlas a la lista
                    lista.append(dic[fila])
        ##        dic[table_name] = lista
                return lista #####retornarle diccionario con todas las tablas,llave-nombre da tabla,valor-lista con filas

            # except FileNotFoundError:
            #     dic={}
            #     with open('{}.json'.format(table_name),'w') as f:
            #         json.dump(dic,f)

def write(table_name,lista):###nos devuelve nombre da tabla y lista con filas
    with root,dirs,files in os.walk(os.getcwd()):
        for file in files:
            if file == str(table_name)+'.json':
                path = os.join(root,file)
                break
    dic = {}
    for num,fila in enumerate(lista):
        dic[num+1]=fila##Primer elemento de la fila no necesariamente es primera fila a menos lista ordenada
    with open(path,'w') as f:
        json.dump(dic,f)


    
            
##            
##def step6(servcicio,item_names):
##    l = []
##    for root,dirnames,files in os.walk(os.join(os.getcwd,'step6',servicio)):
##        for file in files:
##            with open(file) as f:
##                dic = json.load(f)
##            index = dic['Index']
##            l.append(index)


    

# start_time = datetime.datetime(2018,4,2)
# # print('Start:',start_time)
# end_time = datetime.datetime(2018,5,4)
# # print('End:',end_time)
# step5('navegacion','zabbixinfo','1234','127.0.0.1',start_time,end_time)
# # v = load_step6('navegacion')
