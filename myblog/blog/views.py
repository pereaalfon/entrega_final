# blog/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserSignupForm, ProfileForm, PageForm, MessageForm
from .models import Page, Message, Profile

def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')

def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro exitoso. Por favor inicia sesión.')
            return redirect('login')
    else:
        form = UserSignupForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuario o contraseña inválidos')
    return render(request, 'login.html')

@login_required
def profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Perfil actualizado exitosamente')
            return redirect('profile')
    else:
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {'profile_form': profile_form})

@login_required
def create_page(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            page = form.save(commit=False)
            page.author = request.user
            page.save()
            messages.success(request, 'Página creada exitosamente')
            return redirect('pages')
    else:
        form = PageForm()
    return render(request, 'create_page.html', {'form': form})

@login_required
def get_pages(request):
    pages = Page.objects.all()
    return render(request, 'pages.html', {'pages': pages})

@login_required
def delete_page(request, page_id):
    page = get_object_or_404(Page, id=page_id)
    if request.user == page.author or request.user.is_staff:
        page.delete()
        messages.success(request, 'Página eliminada exitosamente')
    return redirect('pages')

@login_required
def messages_view(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            messages.success(request, 'Mensaje enviado exitosamente')
    messages_list = Message.objects.filter(
        sender=request.user
    ).select_related('recipient')
    form = MessageForm()
    return render(request, 'messages.html', {'messages': messages_list, 'form': form})
