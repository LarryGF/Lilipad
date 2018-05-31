import json
import os

 
def step7(servicio):
    utilizacion_fut = {}
    row = {}
    dic_to_save = {}

    '''Formula:
    Utilizaciónfutura=Utilizaciónactual*Usuariosfuturos/Usuariosactuales*β
    '''
    with open('{}.json'.format(os.path.join(os.getcwd(),'step6',servicio))) as f:
        utilizacion = json.load(f)
    with open('step_1.json') as f:
        user_dic = json.load(f)
        print(user_dic)
    users_act = user_dic['usract']
    users_fut = user_dic['usrfutr']
    for item in utilizacion.keys():
        util_act = utilizacion[item]['Percentil_max']
        util_fut = float(util_act)*float(users_fut)/float(users_act)
        utilizacion_fut[item] = util_fut
    
    row['service'] = servicio

    for key in utilizacion_fut:
        if key == 'read.sda':
            row['read'] = utilizacion_fut[key]

        elif key == 'Incoming network traffic on $1':
            row['in'] = utilizacion_fut[key]

        elif key == 'Used disk space on $1':
            row['disk_usage'] = utilizacion_fut[key]

        elif key == 'RAM-used':
            row['ram'] = utilizacion_fut[key]

        elif key == 'Outgoing network traffic on $1':
            row['out'] = utilizacion_fut[key]

        elif key == 'CPU Usage':
            row['cpu'] = utilizacion_fut[key]

        elif key == 'write.sda':
            row['write'] = utilizacion_fut[key]

        elif key == 'iostat.sda':
            row['iops'] = utilizacion_fut[key]

    dic_to_save[servicio] = row

    with open('step_7.json','w') as f:
        json.dump(dic_to_save, f)
    
step7('navegacion')