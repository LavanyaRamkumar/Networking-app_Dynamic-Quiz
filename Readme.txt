SETUP:

cd Desktop/faction-master-master/
virtualenv venv --python=python3
source venv/bin/activate
pip install -r requirements.txt
python dbs.py        #creation of db










EXECUTION:


terminal 1: 
redis-server

terminal 2:
cd Desktop/faction-master-master/
source venv/bin/activate
celery -A app.celery purge -f
celery -A app.celery worker --loglevel=info -P eventlet

terminal 3:
python generate.py             # to load the database of questions
python run.py

Client:
go to localhost:8000 in browser to enter the quiz

Server:
go to admin123gh1g2hvh12gvh312us1jsc1j2sj12sf3t2f1stf3y123
Clear the 'Answers' table before clearing the 'Players' (can't delete Players directly due to Answers having a foreign key of Players [Answers dependent on Players])

Make sure the asked column is NULL for all questions.

Create a schedule with current time and number of seconds for video(20).

Go to home of the admin and click on 'Refresh Schedule' to start the scheduling process.




