from sre_constants import error

from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister

# Create your views here.
def sign_up_by_html(request):
    user = ['max', 'pol', 'saha']
    info = {}
    if request.mathod == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        r_password = request.POST.get('r_password')
        age = request.POST.get('age')
        if name in user:
            info["error"] = 'Логин уже зарегистрирован'
        else:
            if password == r_password:
                if age > 18:
                    user.append(name)
                    info["ok"] = f'Приветствуем, {name}'
                else:
                    info["error"] = 'Вам должно быть больше 18 для регистрации'
            else:
                info["error"] = 'Пароли не совпадают'
    error_type = 'error'
    return render(request, 'registration_page.html'), HttpResponse(f"{info[error_type]}")

def sign_up_by_django(request):
    user = ['max', 'pol', 'saha']
    info = {}

    if request.mathod == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            r_password = form.cleaned_data['r_password']
            age = form.cleaned_data['age']
            if name in user:
                info["error"] = 'Логин уже зарегистрирован'

            else:
                if password == r_password:
                    if age > 18:
                        user.append(name)
                        info["error"] = f'Приветствуем, {name}'
                        info['form'] = form

                    else:
                        info["error"] = 'Вам должно быть больше 18 для регистрации'

                else:
                    info["error"] = 'Пароли не совпадают'

    error_type = 'error'
    return render(request, 'registration_page.html', {"info": info}), HttpResponse(f"{info[error_type]}")

