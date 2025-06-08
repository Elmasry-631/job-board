from django.contrib.auth import login,authenticate
from django.shortcuts import render
from django.urls import reverse
from .models import Profile
from .form import SignUpForm, UserForm, ProfileForm 
from django.shortcuts import redirect
# Create your views here.   
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            usr = authenticate (username=username, password=password)
            login(request, usr)
            return redirect('Profile')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html',{'form': form}) 

def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'accounts/profile.html', {'profile': profile})

def profile_edit(request):
    profile_edit = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        profileform = ProfileForm(request.POST, request.FILES, instance=profile_edit)
        userform = UserForm(request.POST, instance=request.user)
        if profileform.is_valid() and userform.is_valid():
            profileform.save()
            userform.save()     
            return redirect(reverse('accounts:profile'))
    else:
        profileform = ProfileForm(instance=profile_edit)
        userform = UserForm(instance=request.user)

    return render(request, 'accounts/profile_edit.html', {'userform': userform, 'profileform': profileform, 'profile_edit' : profile_edit})