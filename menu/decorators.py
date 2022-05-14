from django.shortcuts import render, redirect


def unauthenticated_user(view_funct):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('menu')
        else:
            return view_funct(request, *args, **kwargs)

    return wrapper_func



