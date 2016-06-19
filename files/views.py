from django.shortcuts import render

def index(request):
	return render(request, 'files/index.html', {})

# Create your views here.
def upload(request):
	return render(request, 'files/upload.html', {})
