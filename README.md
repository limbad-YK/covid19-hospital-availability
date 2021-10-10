# API for Covid-19 bed availability

API created from python3, MongoDB and Flask.

## Work of API
- This api is for searching covid-19 bed availability. api will response 
according to 
- Here are some steps given for using this api on your PC. But python should be installed on your system.
So Python 3.8 will be required for it. you can download it from here.
[Python-3.8](https://www.python.org/ftp/python/3.8.0/python-3.8.0-amd64.exe). You can test 
the api by viewing it's response on POSTMAN. 

## Examples of using it
- ROOT PAGE 'LOCALHOST:/ '
  - Default page of api is root page. Where 2 options will apply. First will be GET method.
  And second will be POST method.
  - If user clicked sign-up option then method:'POST' localhost:/ Response will send.
  - Else Login clicked then method:'GET' localhost:/ Response will send.
  - For testing in Postman for login: method = 'GET',url= localhost:/ , and for sign-up
  : method='POST' url= localhost:/

<p align="center">Login Example</p>
<p align="center">
  <img src="/sample-images/root.png">
</p>

<p align="center">Sign-up Example</p>
<p align="center">
  <img src="/sample-images/root(1).png">
</p>
  
- LOGIN PAGE 'LOCALHOST:/login'
  - At login page user have to enter email and their password if user is there they will 
  be at index page.
  - For Testing in postman, method = GET, url = localhost:/login, form body => 
  email - 'EXAMPLE@gmail.com', pass - 'password'
  
<p align="center">
  <img src="/sample-images/login.png">
</p>
  
- ADD USER PAGE 'LOCALHOST:/add-user'
  - At add-user page user have to enter email and their password, and user will be added to 
  database
  - For testing in postman, method = POST, url = localhost:/add-user, form body =>
  email - 'EXAMPLE@gmail.com', pass - 'password'

<p align="center">
  <img src="/sample-images/sign-up.png">
</p>
  
- INDEX PAGE 'LOCALHOST:/index'
  - At index page we can give user some info about the situation or brief summary about 
  website/webapp
  - For testing in postman, method = GET, url = localhost:/index

<p align="center">
  <img src="/sample-images/index.png">
</p>
  
- AVAILABILITY PAGE 'LOCALHOST:/availability'
  - At this page user will get all details about data.
  - For testing in postman, method = GET, url = localhost:/availability

<p align="center">
  <img src="/sample-images/availability.png">
</p>

- SEARCH PAGE 'LOCALHOST:/availability/search'
  - By entering state and district information of that can be seen.
  - For testing in postman, method = GET, url = localhost:/availability/search

<p align="center">
  <img src="/sample-images/search.png">
</p>

## Steps

### Step-1 
- First create a folder and navigate there. For Example covid-api.

For Windows 
```shell
> mkdir covid-api && cd covid-api
```
For Unix/Linux
```shell
$ mkdir covid-api | cd covid-api
```

### Step-2
- Then download package for Python virtual environment. 

For Windows and Unix/Linux
```shell
$ pip install virtualenv
```

### Step-3
- Create a virtual environment

For Windows and Unix/Linux
```shell
$ python3 -m venv env
```

### Step-4
- Activate that virtual environment

For Windows
```shell
> cd env/bin && activate
> cd ../..
```

For Unix/Linux first goto root mode then activate & run environment otherwise there 
will be issue with port running.
```shell
$ sudo su
$ source env/bin/activate
```

### Step-5
- Install requirements

For Windows and Unix/Linux
```shell
$ pip install -r requirement.txt
```

### Step-6
- Run api and test it by Postman app

For starting api  in Windows
```shell
> python API.py 
```

For linux you have to use the api as in ROOT mode.

For starting api in Unix/Linux
```shell
$ python3 API.py
```

Now your api is running. You can test the api on Postman application as shown above.