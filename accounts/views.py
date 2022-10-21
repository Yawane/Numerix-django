from django.contrib.auth import get_user_model, login, logout, authenticate
from django.shortcuts import render, redirect

User = get_user_model()


def signup(request):
    if request.method == 'POST':
        # Traiter le formulaire
        username = request.POST.get('username')
        password = request.POST.get('password')
        if authenticate(username=username, password=password):
            login(request, authenticate(username=username, password=password))
            return redirect('home')
        else:
            user = User.objects.create_user(username=username,
                                            password=password)
            login(request, user)
            return redirect('home')
        return render(request, 'signup.html', context={'error': True})

    return render(request, 'signup.html')


def logout_user(request):
    logout(request)
    return redirect('home')


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,
                            password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', context={'error': True})
    return render(request, 'login.html')
