import click
#to work with timestamps
import datetime,time,re
from readingdbmodif import get_items, get_trends, search_host, percentil, rank, mean,filter_time,db_connect,filter_time_history

##@click.command()
##@click.option('--name', prompt='What host are you searching for?',help='Host to look for.')

trends_items=['CPU Usage'] 
history_items=['iostat.sda','read.sda','write.sda'] 
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
    print('hosts')
    trends_item_id=[]
    history_item_id=[]
    host_list = search_host(name)
    
##    while host_list == []:
##        name =click.prompt("The host doesn't exists,select a new one")
##        host_list = search_host(name)
##    	
    hosts_ids = [e[0] for e in host_list]
    print(hosts_ids)

##    click.echo('Hostid\tHostname')
##    for host in host_list:
##        print('{}\t{}'.format(*host))
##    while not select.isnumeric() or int(select) not in hosts_ids:
    select = hosts_ids[0]   #click.prompt('\nSelect a hostid')#### Ver bien lo que devuelve la funcion search_host
##        if not select.isnumeric() or int(select) not in hosts_ids:
##            click.echo('\nPlease use a number from the list')
    print(select)
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



##    click.echo('Hostid\tItemid\tItemName')
##    for item in items_list:
##        click.echo('{}\t{}\t{}'.format(*item))
##    select = ''
##    items_ids = [e[1] for e in items_list]
##    while not select.isnumeric() or int(select) not in items_ids:
##    select = 

##        if not select.isnumeric() or int(select) not in items_ids:
##            click.echo('\nPlease use a number from the list')
##            print(items_ids)

##    item = [e for e in items_list if e[1] == int(select)].pop()
##    select = int(select)
##    itemid = select
##    click.echo('You have selected the item: {}'.format(item[2]))

    # (trends.itemid, trends.value_min, trends.value_avg, trends.value_max)
##    trends = get_trends(lista_item_id)
    # print(select, type(select))
##    if trends == []:
##        click.echo('No trends in database for that item')
##        exit()

##    if click.confirm('Do you want to see it?'):
##        for trend in trends:
##            #to convert the timestamp into a human readable format
##            clock = trend[4]
##            date=datetime.datetime.fromtimestamp(int(clock)).strftime('%Y-%m-%d %H:%M:%S')
##            click.echo('{}\t{}\t\t{}\t\t{}\t\t{}'.format(trend[0],trend[1],trend[2],trend[3],date))

    #Tells the rest of the program if the results will be filtered or not (is needed later)
##    isfiltered=False

##    if click.confirm('Do you want to filter by date and time?'):
    date = start_time#click.prompt('Insert the date and time to start with\nIt must be in the format YYYYMMDDHHMMSS (all together for now)')
        #fetchs the date from the 'date' string, so it can generate a Unix timestamp from it
##        datetuple = (int(date[0:4]),int(date[4:6]),int(date[6:8]),int(date[8:10]),int(date[10:12]),int(date[12:14]),0,0,0)
    # timestamp1 = make_timestamp(date)
    date = end_time#click.prompt('\nInsert the date and time to finish the search\nIt must be in the format YYYYMMDDHHMMSS (all together for now)')        
##        datetuple = (int(date[0:4]),int(date[4:6]),int(date[6:8]),int(date[8:10]),int(date[10:12]),int(date[12:14]),0,0,0)
    # timestamp2 = make_timestamp(date)
    filtered = filter_time(1524441600,1524614400,trends_item_id)
    hist= filter_time_history(1524441600,1524614400,history_item_id)
        #Sets the variable to True so the rest of the programs knows that it's working with filtered values
##isfiltered = True

##        if click.confirm('Do you want to see it?'):
##            for sample in filtered:
##                clock = sample[4]
##                date=datetime.datetime.fromtimestamp(int(clock)).strftime('%Y-%m-%d %H:%M:%S')
##                click.echo('{}\t{}\t\t{}\t\t{}\t\t{}'.format(sample[0],sample[1],sample[2],sample[3],date))

    
##    if click.confirm('Do you want to export it to a .csv file? \nThe file if exist will be deleted'):
##        file = ''
##        while file == '':
##            userinput = click.prompt('Name the file')
##            file = str(userinput + '.csv')
##            try:
##                fd = open(file, 'w')
##
##            except Exception as e:
##                click.echo('Error opening the file')
##                print(e)
##                print('try again')
##                file = ''
##            pass
##
##        click.echo('Itemid;Min;Avg;Max', file=fd)
##        if isfiltered == False:
##            for trend in trends:
##                click.echo('{};{};{};{}'.format(*trend), file=fd)
##
##        else:
##            for sample in filtered:
##                clock = sample[4]
##                date=datetime.datetime.fromtimestamp(int(clock)).strftime('%Y-%m-%d %H:%M:%S')
##                click.echo('{}\t{}\t\t{}\t\t{}\t\t{}'.format(sample[0],sample[1],sample[2],sample[3],date), file=fd)
##
##    if isfiltered == False:
##        numbers_max = [e[3] for e in trends]
##        num_max = mean(numbers_max)
##
##        numbers_avg = [e[2] for e in trends]
##        num_avg = mean(numbers_avg)
##
##        numbers_min = [e[1] for e in trends]
##        num_min = mean(numbers_min)
##
##        score_max = [e[3] for e in trends]
##        score_max.sort()
##        p_max = percentil(score_max)
##        ans_max = rank(score_max, p_max, 0.95)
##
##        score_avg = [e[2] for e in trends]
##        score_avg.sort()
##        p_avg = percentil(score_avg)
##        ans_avg = rank(score_avg, p_avg, 0.95)
##
##        score_min = [e[1] for e in trends]
##        score_min.sort()
##        p_min = percentil(score_min)
##        ans_min = rank(score_min, p_min, 0.95)
##
##    else:


    dic1={}
    for value_list,l in zip(hist,history_items):
        values = [sample[1] for sample in value_list]
        max_value = sorted(values,reverse = True)[0]
        avg_val = mean(values) 
        dic1[l]={'Max_value':max_value,'Avg_value':avg_val}
        


    dic={}
    for i,l in zip(filtered,trends_items):
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
        dic[l]={'Average max':num_max,'Average avg':num_avg,'95 percentile max':ans_max}
    dic.update(dic1)
    return dic
        
        # print('\nAverage max', num_max)
        # print('\n95 percentile max', ans_max)
        # print('\nAverage avg', num_avg)
        # print('\n95 percentile avg', ans_avg)
        # print('\nAverage min', num_min)
        # print('\n95 percentile min', ans_min)
        # print('\n')


