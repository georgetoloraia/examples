from django.shortcuts import render, redirect

# Create your views here.

# home Page View
def home_view(request):
    return render(request, 'home.html')

# About Page view
def about_view(request):
    return render(request, 'about.html')

# Contact PAge view
def contact_view(request):
    if request.method == 'POST':
        # ---
        return redirect('welcome')
    return render(request, 'contact.html')

# Welcome PAge view
def welcome_view(request):
    return render(request, 'welcome.html')