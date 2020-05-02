from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login

from .models import User
from .forms import UserCreationForm


class UserViewSet(generic.View):
    def get(self, request, *args, **kwargs):
        template = "registration/auth.html"
        # form = UserForm()
        context = {} # "form": form}
        return render(request, template, context)

    def post(self, request):
        # import pdb; pdb.set_trace()
        email = request.POST.get("email")
        password = request.POST.get("password1")
        user = authenticate(email=email, password=password)

        if user:
            login(request, user)
            return redirect("home")
        else:
            import pdb; pdb.set_trace()
            return redirect("accounts")


def UserRegister(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        # import pdb; pdb.set_trace()
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            import pdb; pdb.set_trace()

