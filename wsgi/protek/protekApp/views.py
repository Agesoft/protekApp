from django.shortcuts import render


def home(request):
    return render(request, 'core/home.html')
	
def conact(request):
	return render(request, 'core/contact.html')