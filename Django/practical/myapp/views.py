from django.shortcuts import render
from .forms import RegisterForm

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Process the form data (e.g., save to database)
            return render(request, "success.html", {"form": form})
        else:
            # If the form is invalid, re-render the form with error messages
            return render(request, "register.html", {"form": form})
    else:
        form = RegisterForm()
        return render(request, "register.html", {"form": form})
