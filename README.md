# Django 설정
1. 가상환경 설정
```shell script
$ pip3 install virtualenv
$ virtualenv [root-name]
$ source [root-name]/bin/activate
```

2. django 설정
```shell script
$ pip3 install django
$ django-admin startproject [project-name]
$ cd [project-name]
$ django-admin startapp [app-name]
```

3. app 등록 - 프로젝트 앱폴더 settings.py
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'board',
    'izuser'
]
```