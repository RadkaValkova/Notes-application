from django.shortcuts import render, redirect

from notes.notes_app.models import Note
from notes.profile_app.forms import ProfileForm
from notes.profile_app.models import Profile


def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProfileForm()
    context = {
        'form': form,
    }
    return render(request, 'home-no-profile.html', context)


def profile_info(request):
    profile = Profile.objects.first()
    notes = Note.objects.all()
    notes_count = notes.count()

    context = {
        'profile': profile,
        'notes_count': notes_count,
    }
    return render(request, 'profile.html', context)


def delete_profile(request):
    profile = Profile.objects.first()

    profile.delete()
    Note.objects.all().delete()
    return redirect('index')

