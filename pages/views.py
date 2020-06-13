from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request,*args,**kwargs):
	#print(args,kwargs)
	#print(request.user)
	#return HttpResponse("<h1>Hello World</h1>") #string of html code
	return render(request, 'index.html', {})
def contact_view(request,*args,**kwargs):
	#return HttpResponse("<h1>Hello this is my contact</h1>") #string of html code
	return render(request, 'contact.html', {})
def about_view(request,*args,**kwargs):
	#return HttpResponse("<h1>Hello this is my about</h1>") #string of html code
	return render(request, 'about.html', {})
def social_view(request,*args,**kwargs):
	#return HttpResponse("<h1>Hello this is social</h1>") #string of html code
	return render(request, 'social.html', {})
