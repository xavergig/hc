from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView
from django.utils.decorators import method_decorator
from .forms import CustomAuthenticationForm


class LoginView(View):
    template_name = 'authentication/login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('authentication:dashboard')

        form = CustomAuthenticationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CustomAuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('authentication:dashboard')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')

        return render(request, self.template_name, {'form': form})


@login_required
def logout_view(request):
    username = request.user.username
    logout(request)
    messages.info(request, f'Goodbye, {username}!')
    return redirect('authentication:login')


@method_decorator(login_required, name='dispatch')
class DashboardView(TemplateView):
    template_name = 'authentication/dashboard.html'
