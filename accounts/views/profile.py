from django.shortcuts import render, redirect

from accounts.forms import ProfileEditForm


def settings_view(request):
    return render(request, "accounts/settings.html")


def profile_view(request):
    return render(request, "accounts/profile.html")


def profile_edit(request):
    form = ProfileEditForm(instance=request.user)

    if request.method == "POST":
        form = ProfileEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("accounts:profile_view")

    return render(request, "accounts/profile_edit.html", {"form": form})
