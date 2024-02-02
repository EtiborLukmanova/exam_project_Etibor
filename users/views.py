from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.views import View
from .forms import CustomUserCreateForm, UpdateProfileForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUser


class HomepageView(View):
    def get(self, request):
        return render(request, 'home.html')


class ProfileView(LoginRequiredMixin, View):
    template_name = 'users/profile.html'
    def get(self, request):
        user = CustomUser.objects.get(id=request.user.id)
        context = {
            'user': user
        }
        return render(request, self.template_name, context=context)


class UpdateProfileView(LoginRequiredMixin, View):
    template_name = 'users/profile_update.html'

    def get(self, request):
        form = UpdateProfileForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UpdateProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request, self.template_name, {'form': form})


class UserRegisterView(View):
    template_name = 'users/register.html'

    def get(self, request):
        create_form = CustomUserCreateForm()
        context = {
            'form': create_form
        }
        return render(request, self.template_name, context=context)

    def post(self, request):
        create_form = CustomUserCreateForm(request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect('login')
        context = {
            'form': create_form
        }
        return render(request, self.template_name, context=context)


class CustomUserLogin(View):
    template_name = 'users/login.html'

    def get(self, request):
        login_form = AuthenticationForm()
        context = {
            'form': login_form
        }
        return render(request, self.template_name, context=context)

    def post(self, request):
        data = AuthenticationForm(data=request.POST)
        if data.is_valid():
            user = data.get_user()
            login(request, user)
            return redirect('home')
        else:
            return render(request,self.template_name,{'data':data})


class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
