import json
import os

 
def step7(servicio):
    utilizacion_fut = {}
    '''Formula:
    Utilizaciónfutura=Utilizaciónactual*Usuariosfuturos/Usuariosactuales*β
    '''
    with open('{}.json'.format(os.path.join(os.getcwd(),'step6',servicio))) as f:
        utilizacion = json.load(f)
    with open('step1.json') as f:
        user_dic = json.load(f)
    users_act = user_dic['current_users']
    users_fut = user_dic['future_users']
    for item in utilizacion.keys():
        util_act = utilizacion[item]['Percentil_max']
        util_fut = float(util_act)*float(users_fut)/float(users_act)
        utilizacion_fut[item] = util_fut
    with open('step7.json','w') as f:
        json.dump(utilizacion_fut, f)
    return utilizacion_fut

