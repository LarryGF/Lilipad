import eel
from step_1 import step_1,step_1_load
from step2 import step2_write,step2_load




eel.init('web')


@eel.expose
def handler(step,table,dictio):
    print(step)
    print(table)
    print(dictio)
    if step == 1:
        step_1(dictio)
    elif step ==2:
        step2_write(table,dictio)
    
@eel.expose
def load(step,table_list):
    if step == 1:
        values = step_1_load()
        return values

    elif step == 2:
        values = step2_load(table_list)
        return values
        
eel.start('lili.html')