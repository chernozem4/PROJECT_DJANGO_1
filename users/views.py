from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import CreateView, ListView
from django.contrib.auth.views import LoginView, LogoutView
from . import forms, models

class RegistrationView(CreateView):
    form_class = forms.CustomRegistrationForm
    template_name = 'users/register.html'
    success_url = '/login/'

    def form_valid(self, form):
        response = super().form_valid(form)
        # Assign the developer level during registration
        level = form.cleaned_data['level']
        if level == 'junior':
            self.object.salary = 500
        elif level == 'middle':
            self.object.salary = 1000
        elif level == 'senior':
            self.object.salary = 3000
        self.object.save()
        return response

class AuthLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse('users:user_list')

class AuthLogoutView(LogoutView):
    next_page = reverse_lazy('users:login')

class UserListView(ListView):
    template_name = 'users/user_list.html'
    model = models.CustomUser

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Show salary info in the employee list
        context['employees'] = self.model.objects.all().values('username', 'level', 'salary')
        return context

