from operator import itemgetter
dic={'tabla1':{2:{'color':'rojo','estatura':170},1:{'color':'verde','estatura':270},3:{'color':'azul','estatura':40}},'tabla2':{1:{'color':'amarillo','estatura':70},2:{'color':'violeta','estatura':210}}}
##lista=[{'color':'carmelita','estatura':170},{'color':'verde','estatura':240},{'color':'carmesi','estatura':440}]
table_name='tabla1'
   
        
for table in dic.keys():
        lista=[]
        for fila in sorted(dic[table].keys()):  ####ordenar las filas al ingresarlas a la lista
                lista.append(dic[table][fila])
        dic[table]=lista
print(dic)
