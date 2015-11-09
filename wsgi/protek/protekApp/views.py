from django.shortcuts import render


def main_page(request):
    return render(request, 'core/home.html')