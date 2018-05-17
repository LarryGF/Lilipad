 import os
 import json
 

 def load_step6(servicio):
    '''
    Cargar dict = {VM_name:Indice}, donde indice es un dict con los valores por item
    '''
    vm_values = {}
    list_to_send = []
    for root,dirnames,files in os.walk(os.path.join(os.getcwd(),'step5',servicio)):
        for file in files:
            # if file == str(servicio)+'.json':
            #     path = os.path.join(root,file)
            path = os.path.join(root,file)
            with open(path) as f:
                dic = json.load(f)
                indice =dic.get('Index')
            vm_values[file.strip('.json')]=indice
    # print(os.path.join(os.getcwd(),'step6',servicio))
    with open ('{}.json'.format(os.path.join(os.getcwd(),'step6',servicio)),'r') as f:
        sumatoria = json.load(f)
    vm_values.update(sumatoria) 
    # print('Values:',vm_values)
    return vm_values
