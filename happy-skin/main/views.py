from django.shortcuts import render

def show_main(request):
    context = {
        'app name': 'Happy Ecommerce',
        'name': 'Nur Khoirunnisa Salsabila',
        'npm' : '2306165534',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)