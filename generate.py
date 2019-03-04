from app import db
from app.models import Question, Option, Weight, Faction

Question.query.delete()
Option.query.delete()
Weight.query.delete()
#############################################################
from random import randint
lists={}
op=[]
ques=''
with open('questions.txt','r') as file:
	c=0
	for line in file:
		if(c%5==0):
			op=[]
			ques=line.split('\n')[0]
		elif(c%5==4):
			op.append(line.split('\n')[0])
			lists[ques]=op
		else:
			op.append(line.split('\n')[0])
		c=c+1
##############################################################

factions = Faction.query.all()
for faction in factions:
	c = 0
	for i in range(5):
		q = Question(
		 	text='%s q.no. %d' % (faction.name, (c + 1)),
			for_first_round=False, duration=15,
			faction_id=faction.id
		)
		db.session.add(q)
		c += 1
db.session.commit()

questions = Question.query.all()
for question in questions:
	c = 0
	for i in range(4):
		o = Option(question=question, text='option no. %d' % c)
		db.session.add(o)
		c += 1
db.session.commit()
#########################################################
for k,v in lists.items():
	q = Question(text=k, for_first_round=True, duration=15)
	db.session.add(q)
db.session.commit()
for k,v in lists.items():
	q=Question.query.filter(Question.text==k).first()
	for i in range(4):
		o = Option(question=q, text=v[i])
		db.session.add(o)
db.session.commit()
#########################################################
options = Option.query.join(Question).filter(Question.for_first_round == True)
c = 0
for option in options:
	if c % 4 == 0:
		w = Weight(option=option, f1=60, f2=20, f3=10, f4=0, f5=0)
	elif c % 4 == 1:
		w = Weight(option=option, f1=0, f2=70, f3=0, f4=50, f5=20)
	elif c % 4 == 2:
		w = Weight(option=option, f1=20, f2=10, f3=70, f4=20, f5=40)
	elif c % 4 == 3:
		w = Weight(option=option, f1=20, f2=0, f3=20, f4=30, f5=60)
	db.session.add(w)
	c += 1
db.session.commit()
###############################
for faction in Faction.query.all():
	question=Question.query.filter(Question.faction_id==faction.id).all()
	for ques in question:
		options=Option.query.filter(Option.question==ques).all()
		for option in options:
			wts = {}
			for i in range(5):
				wts['f%d' % (i+1)] = 0
			c=randint(0, 4)
			wts['f%d' % (c+1)] = 1
			wts['option_id'] = option.id
			w = Weight(**wts)
			db.session.add(w)
db.session.commit()
##################################
