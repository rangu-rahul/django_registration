from django.shortcuts import render
from .forms import UserRegister 
from .models import User

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            form.save()
            form = UserRegister()
    else:
        form = UserRegister()
    users = User.objects.all()
    return render(request, "Register.html",
    {
        "form": form,
        "users": users
    })