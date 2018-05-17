import json,os
import zabixmaster as zb
import opennebula 
from readingdbmodif import percetil,rank,mean
from step2 import *
 
def step5 (servicio,user,passw,db_addr,start_time,end_time):
    values_avg = []
    max_values = []
    step6_sum = {}
    os.makedirs(os.path.join(os.getcwd(),'step5',servicio),exist_ok = True)
    os.makedirs(os.path.join(os.getcwd(),'step6'),exist_ok = True)
    dic4={}
    
    dic = l5('topologia_fisica')
    # print(dic)######cambiar esto para llamar a la tabla del paso 2
    for row in dic.keys():
        Index = {}
        if dic[row]['servicio'] == servicio:
            with open('parser.json') as f:
                parse = json.load(f)
                
            zabbix_id = parse[dic[row]['MV']]
            # print(zabbix_id)
            
            now = start_time##Falta por definir
            # print('Now:',now)
            delta = datetime.timedelta(1)
            # print('delta:',delta)
            zb.db_connect(user,passw,db_addr)
            
            while now<=end_time:
                dic2=zb.hosts(zabbix_id,now,now+delta)
                dic4[now.timestamp()]=dic2
                now +=delta
            # print(dic4)
            
            days = dic4.keys()##Lista con dias a iterar
            item_names = [each_dic.keys() for each_dic in dic4.values()][0]##Lista con los item_names a iterar
            # print(item_names,end='\n\n')
            # print(days)
            for item_name in item_names:
                for day in days: 
                    if day!='Index':
                        # print(dic4[day][item_name]['Average_avg'])
                        values_avg.append(dic4[day][item_name]['Average_avg'])
                        # print(values_avg,end='\n\n')
                        max_values.append(dic4[day][item_name]['Average_max'])
                # print(max_values,end='\n\n')
                avg_avg = mean(values_avg)
                perc = percentil(sorted(max_values))
                ans_max = rank(sorted(max_values), perc, 0.95)
                asignacion=opennebula.onevm(dic[row]['MV'])
                # print('Asignacion OPenN:',asignacion)
##                dic2.update(dic3)
                Index[item_name]={'Asignacion':asignacion[item_name],'Avg_avg':avg_avg,'Percentil_max':ans_max}

                if item_name in step6_sum:
                    ##Realizar sumatoria de los valores de cada item de todas las VM pertenecientes a un servicio
                    if 'Avg_avg' and 'Percentil_max' and 'Asignacion' in step6_sum[item_name]:
                        step6_sum[item_name]['Avg_avg'] += avg_avg
                        step6_sum[item_name]['Percentil_max'] += ans_max
                        step6_sum[item_name]['Asignacion'] += asignacion[item_name]
                        # print('2DA VEZ:',step6_sum[item_name]['Avg_avg'],Index[item_name]['Avg_avg'])
                    else:
                        step6_sum[item_name]['Avg_avg'] = avg_avg
                        step6_sum[item_name]['Percentil_max'] = ans_max
                        step6_sum[item_name]['Asignacion'] = asignacion[item_name]
                        
                else:
                    step6_sum = Index
                    # print('1RA VEZ:',step6_sum[item_name]['Avg_avg'],Index[item_name]['Avg_avg'])
            ##Estructura de dic4:
            ## dic4 = {day:{item_name:{'Average max':num_max,'Average avg':num_avg,'95 percentile max':ans_max}},Index:{'Avg_avg':avg_avg,'Percentil_max':ans_max}}
            dic4['Index']=Index
            # print('Index %s:'%dic[row]['MV'],Index)
            # print('Step6_sum:',step6_sum)
            

            with open ('{}.json'.format(os.path.join(os.getcwd(),'step5',servicio,dic[row]['MV'])),'w') as f:
                ##Guardar en dir step5, archivo con nombre de la VM, conteniendo los valores de cada item por dia
                json.dump(dic4,f)
            with open ('{}.json'.format(os.path.join(os.getcwd(),'step6',servicio)),'w') as f:
                ##Guardar en directorio step6, archivo con nombre del servicio conteniendo la sumatoria descrita anteriormente
                json.dump(step6_sum,f)
