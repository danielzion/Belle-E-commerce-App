from django.shortcuts import render, redirect


# Create your views here.
def login_view(request):

    return render(request,'accounts/login.html', {'form':form})


def signup_view(request):

    return render(request, 'accounts/signup.html', {'form': form})