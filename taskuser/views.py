from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import SignUpForm, ImageUploadForm
from .models import StudentProfile


def login(request):
    return HttpResponseRedirect("/accounts/login")

@login_required
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        photo_upload_form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.user_type = form.cleaned_data.get('user_type')
            user.profile.address_line1 = form.cleaned_data.get('address_line1')
            user.profile.city = form.cleaned_data.get('city')
            user.profile.state = form.cleaned_data.get('state')
            user.profile.pincode = form.cleaned_data.get('pincode')
            user.save()
            if photo_upload_form.is_valid():
                user = form.save()
                avatar = photo_upload_form.cleaned_data.get("profile_photo")
                new_user_profile = StudentProfile.objects.create(user=user,avatar=avatar)
                new_user_profile.save()
                return redirect('login')

    else:
        form = SignUpForm()
        photo_upload_form = ImageUploadForm()
    return render(request, 'signup.html', {'form': form,'photo_upload_form':photo_upload_form })