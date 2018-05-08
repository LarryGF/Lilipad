import eel
from step_1 import step_1,step_1_load




eel.init('web')


@eel.expose
def handler(step,table,dictio):
    print(step)
    print(table)
    print(dictio)
    if step == 1:
        step_1(dictio)
    
@eel.expose
def load(step,table,dictio):
    if step == 1:
        values = step_1_load()
        return values

eel.start('lilipad.html')