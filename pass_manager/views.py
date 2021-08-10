from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, View, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomLoginForm, CustomSignUpForm, PassCardForm
from .models import Folder, PassCard
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalReadView


class MainPage(LoginRequiredMixin, View):

    def get(self, request):
        folders = Folder.objects.all()
        return render(request, 'index.html', {'folders': folders})


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = CustomLoginForm


class CustomLogoutView(LogoutView):
    template_name = 'registration/login.html'


class CustomSignUpView(CreateView):
    template_name = 'registration/register.html'
    form_class = CustomSignUpForm

    def get_success_url(self):
        return reverse('login')


class PassCardCreateView(LoginRequiredMixin, CreateView):
    template_name = 'edit-card.html'
    form_class = PassCardForm

    def get_success_url(self):
        return reverse('mainpage')

    def form_valid(self, form):
        new_pass_card = form.save(commit=False)
        folder_name = form.cleaned_data['folder']
        try:
            new_pass_card.folder = Folder.objects.get(name=folder_name)
        except Folder.DoesNotExist:
            Folder.objects.create(name=folder_name)
            new_pass_card.folder = Folder.objects.get(name=folder_name)
        form.save()
        return super(PassCardCreateView, self).form_valid(form)


class CardView(LoginRequiredMixin, BSModalReadView):
    model = PassCard
    template_name = 'card-info.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class EditCardView(LoginRequiredMixin, UpdateView):
    model = PassCard
    form_class = PassCardForm
    template_name = 'edit-card.html'

    def get_success_url(self):
        return reverse('mainpage')


class DeleteCardView(LoginRequiredMixin, DeleteView):
    model = PassCard
    success_url = reverse_lazy('mainpage')
    template_name = 'delete-card.html'
