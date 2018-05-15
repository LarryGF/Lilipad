import click
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_
##Para solucionar el problema de que no acepta nuevamente el nombre y pass lo mejor seria ponerlo
##dentro de una funcion.
def db_connect(user, password, dbaddr):    
    """
    Connects to the DB
    """
    #I know these shouldn't be global variables, but that's the solution I came up with
    global session,hosts,items,trends,history
    try:
        #string='mysql://'+user+':'+password+'@'+dbaddr+'/zabbix' 
        string='mysql://{}:{}@{}/zabbix'.format(user, password, dbaddr)
        #string='mysql://%s:%s@%s/zabbix' % (user, password, dbaddr)
        engine = create_engine(string, echo=False) 
        Base = automap_base()
        Base.prepare(engine, reflect=True)
        Session = sessionmaker(bind=engine, expire_on_commit=False)
        session = Session()
        noError = True
        hosts = Base.classes['hosts']
        items = Base.classes['items']
        trends = Base.classes['trends']
        history = Base.classes['history']
        print('is connected')

    except Exception as e:
        print(e)
        print('error')
        pass



def search_host(hostname: str):
    """
    El método recive un hostname y devuelve

    (hosts.id, hosts.name)

    donde hostname es un substring de hosts.name
    """
    return session.query(hosts.hostid, hosts.name).filter(hosts.name.ilike('%{}%'.format(hostname))).all()


def get_items(hostid: int):
    """
    El método recive un hostid y devuelve

    (items.hostid, items.itemid, items.name)

    donde items.hostid == hostid
    """
    return session.query(items.hostid, items.itemid, items.name).filter(items.hostid == hostid).all()


def get_trends(itemid: int):
    lista =[]
    for e in itemid:
        lista.append(session.query(trends.itemid, trends.value_min, trends.value_avg, trends.value_max, trends.clock).filter(trends.itemid == itemid).all())
    """
    El método recive un itemid y devuelve

    (trends.itemid, trends.value_min, trends.value_avg, trends.value_max)

    donde trends. itemid == hostid
    """
    return lista


def percentil(scores):
    count = 0
    ans = []
    for i, score in enumerate(scores):
        i += 1
        ans.append(i / len(scores))

    return ans


def rank(scores, percentil_rank, value):

    for i, e in enumerate(percentil_rank):
        if e >= value:
            return scores[i]


def mean(numbers):
    mean = float(sum(numbers)) / max(len(numbers), 1)
    return mean

def filter_time(timestamp1,timestamp2,itemid):
    lista =[]
    for e in itemid:
        lista.append(session.query(trends.itemid, trends.value_min, trends.value_avg, trends.value_max, trends.clock).filter(and_(trends.itemid == e,trends.clock >= timestamp1,trends.clock <= timestamp2)).all())
    return lista
##Funcion get_trends la podemos votar no nos sirve solo nos interesa filtrar

def filter_time_history(timestamp1,timestamp2,itemid):
    lista =[]
    for e in itemid:
        lista.append(session.query(history.itemid, history.value,history.clock).filter(and_(history.itemid == e,history.clock >= timestamp1,history.clock <= timestamp2)).all())
    return lista
