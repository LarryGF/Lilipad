#to work with timestamps
import datetime
from readingdbmodif import get_items, get_trends, search_host, percentil, rank, mean,filter_time,db_connect,filter_time_history
# import mysqldb 

##@click.command()
##@click.option('--name', prompt='What host are you searching for?',help='Host to look for.')

trends_items=['CPU Usage'] 
history_items=['iostat.sda','read.sda','write.sda','RAM-used','Used disk space on /','Incoming network traffic on eth0','Outgoing network traffic on eth0']
'''
faltan por anadir los items de RAM,Capacidad, y red(ver problemas relacionados a estos)
'''
# def make_timestamp(date):
#    p = re.compile('[/\-\s]')
#    Time=p.sub(' ',date)
#    t = time.strptime(Time,"%d %m %Y %H:%M")
#    timestamp = time.mktime(t)
#    return timestamp

def hosts(name,start_time,end_time):
    st = start_time.timestamp()
    et = end_time.timestamp()
    # print('hosts')
    trends_item_id=[]
    history_item_id=[]
    host_list = search_host(name)
    
##    while host_list == []:
##        name =click.prompt("The host doesn't exists,select a new one")
##        host_list = search_host(name)
##    	
    hosts_ids = [e[0] for e in host_list]
    # print(hosts_ids)

##    click.echo('Hostid\tHostname')
##    for host in host_list:
##        print('{}\t{}'.format(*host))
##    while not select.isnumeric() or int(select) not in hosts_ids:
    select = hosts_ids[0]   #click.prompt('\nSelect a hostid')#### Ver bien lo que devuelve la funcion search_host
##        if not select.isnumeric() or int(select) not in hosts_ids:
##            click.echo('\nPlease use a number from the list')
##    print(select)
##    click.echo('You selected host: "{}" with hostid: {}'.format([e[1] for e in host_list if e[0] == int(select)].pop(), select))

    items_list = get_items(int(select))
    for i in range(len(trends_items)):
        trends_item_id.append(0)

    for i in range(len(history_items)):
        history_item_id.append(0)

    for i in items_list:
        if i[2] in trends_items:
            index=trends_items.index(i[2])
            trends_item_id[index]=i[1]
        elif i[2] in history_items:
            index=history_items.index(i[2])
            history_item_id[index]=i[1]




    filtered = filter_time(st,et,trends_item_id)
    # hist = generator()



        


    dic={}
    for i,item in zip(filtered,trends_items):
        numbers_max = [sample[3] for sample in i]
        num_max = mean(numbers_max)

        numbers_avg = [sample[2] for sample in i]
        num_avg = mean(numbers_avg)

        numbers_min = [sample[1] for sample in i]
        num_min = mean(numbers_min)

        score_max = [sample[3] for sample in i]
        score_max.sort()
        p_max = percentil(score_max)
        ans_max = rank(score_max, p_max, 0.95)

        score_avg = [sample[2] for sample in i]
        score_avg.sort()
        p_avg = percentil(score_avg)
        ans_avg = rank(score_avg, p_avg, 0.95)

        score_min = [sample[1] for sample in i]
        score_min.sort()
        p_min = percentil(score_min)
        ans_min = rank(score_min, p_min, 0.95)

        '''
        ir incrementando el diccionario dic de la forma dic={item_id:{'Average max':num_max,'Average avg':num_avg,..... }....}
        '''
        dic[item]={'Average_max':num_max,'Average_avg':num_avg}
    # dic.update(dic1)
    return dic
        
        # print('\nAverage max', num_max)
        # print('\n95 percentile max', ans_max)
        # print('\nAverage avg', num_avg)
        # print('\n95 percentile avg', ans_avg)
        # print('\nAverage min', num_min)
        # print('\n95 percentile min', ans_min)
        # print('\n')


