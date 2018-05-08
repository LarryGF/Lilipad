import json

def step_1(users_dic):
	f=open('step_1.json','w')
	json.dump(users_dic,f)
	f.close()

dic={'current_users': 34, 'new_users': 55, 'future_users': 79}
step_1(dic)
