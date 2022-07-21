from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)   #instantiates a user form
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserRegisterForm()   #creating a blank form
    return render(request, 'accounts/register.html', {'form': form})


#messages
"""
message.debug
message.info
message.success
message.warning
message.error
"""