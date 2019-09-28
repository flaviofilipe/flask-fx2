**This is an example of a Flask Project.**
> Note: All the comands have been tested on Ubuntu.

## Install dependencies

This example uses mysql. So it is necessary to install the libmysqlclient

MySQL
 `sudo apt-get install python3-dev libmysqlclient-dev`

Install and activate virtualenv

    pip3 install virtualenv
    virtualenv venv
    source venv/bin/activate

Install dependencies

    pip install -r requirements.txt

Configurations
- 
- Create file **.env**. Uses the code from env-example file and edit database configuration.

UPDATE DATABASE
**[Flask Migrate](https://flask-migrate.readthedocs.io/en/latest/)**
- `flask db init`
- `flask db migrate`
- `flask db upgrade`

Run Project
-

    flask run

Endpoints Test
-
host = http://127.0.0.1:5000/
Category
- Create = [POST] host/category
	- Params = { "name":"category 01" }
- Update = [PUT] host/category/1
	- Params = { "name":"category 01" }
- View = [GET] host/category/1
- Delete = [DELETE] host/category/1


Posts
- New = [POST] host
	- Params = { "title":"Post 03", "text":"texto do post", "category_id":1 }
- Update = [PUT] host/1
	- Params = { "title":"Post 03", "text":"texto do post", "category_id":1 }
- View = [GET] host/1
- Delete = [DELETE] host/1
