from django.contrib.auth import login,authenticate
from django.shortcuts import render
from .models import Profile
from .form import SignUpForm
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
    pass