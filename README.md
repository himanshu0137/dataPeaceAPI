Data Peace Backend Assignment

TechStack:-
1. Python 3.7 
2. Flask 1.1
3. MongoDb 4.2.2

Steps to setup Project:-

1. Clone the repo using command `git clone https://github.com/himanshu0137/dataPeaceAPI.git`
2. Go inside folder and create a virtual environment using command `python -m venv <name>`[Optional]
3. Install the python packages using command `pip install -r requirements.txt`
4. Install MongoDb and run it (follow the instruction provided by there site)
5. Once MongoDb is up and running verify the URI used by flask API to connect written in `instance\config.py`
6. Run the API using command `set FLASK_ENV=development && set FLASK_APP=app.py && flask run` (replace set with export) inside the repo folder
7. In the starting DB is not populated so you have to add few users to use other APIs

Note - As stated in the assignment that name search in get user api should 'use substring matching algorithm/pattern to match the name' which is not a good approach as to do that you have to get all data in the API then process it. It will consume memory as well as time so I moved this task to the DB side by creating Compound Text index to search in name in much faster and easier way. 