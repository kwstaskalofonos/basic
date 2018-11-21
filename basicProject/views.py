from django.shortcuts import redirect, render

def home_page(request):
    context={
        "title":"welcome"
    }
    return render(request,"home.html",context)