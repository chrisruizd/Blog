from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)   #instantiates a user form
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created successfully!')
            return redirect('login')
    else:
        form = UserRegisterForm()   #creating a blank form
    return render(request, 'accounts/register.html', {'form': form})

#user must be logged in to view this page
@login_required
def profile(request):
    return render(request, 'accounts/profile.html')




#messages
"""
message.debug
message.info
message.success
message.warning
message.error
"""