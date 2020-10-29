from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.shortcuts import render
from .models import IzUser


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)
        user_email = request.POST.get('useremail', None)

        res_data = {}
        if not (username and password and re_password and user_email):
            res_data['error'] = '모든 값을 입력해야 합니다.'
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            izuser = IzUser(
                username=username,
                password=make_password(password),
                useremail=user_email
            )
            izuser.save()

        return render(request, 'register.html', res_data)
