from django.contrib.auth import login
from django.shortcuts import redirect, render

from accounts.forms import ResetPasswordForm, VerifyCodeForm, ForgetPasswordForm
from accounts.service import send_verification_email_async
from accounts.models import CustomUser


def forget_password(request):
    form = ForgetPasswordForm()
    if request.method == "POST":
        form = ForgetPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            user = form.cleaned_data.get("user")
            request.session['restore_email'] = email

            send_verification_email_async(to_email=email, user=user)
            return redirect("accounts:verify_code")

    return render(request, "accounts/forget_password.html", {"form": form})


def verify_code(request):
    form = VerifyCodeForm()

    if request.method == "POST":
        form = VerifyCodeForm(request.POST)
        if form.is_valid():
            return redirect("accounts:reset_password")
        return render(request, "accounts/verify_code.html", {"form": form})

    return render(request, "accounts/verify_code.html", {"form": form})


def reset_password(request):
    form = ResetPasswordForm()

    if request.method == "POST":
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            session_email = request.session["restore_email"]
            user_db = CustomUser.objects.get(email=session_email)

            user = form.save(user=user_db)
            login(request, user)
            return redirect("home")

    return render(request, "accounts/reset_password.html", {"form": form})
