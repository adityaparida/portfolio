from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.

def home(request):
	context = locals()
	template = 'home.html'
	return render(request,template,context)
def portfolio(request):
	context = locals()
	template = 'portfolio.html'
	return render(request,template,context)
def contact(request):
	context = locals()
	template = 'contact.html'
	return render(request,template,context)
def about(request):
	context = locals()
	template = 'about.html'
	return render(request,template,context)
def interests(request):
	context = locals()
	template = 'interests.html'
	return render(request,template,context)	
def projects(request):
	context = locals()
	template = 'projects.html'
	return render(request,template,context)

# def pdf_download(request, filename):
# 	path = os.expanduser('../static/document/')
# 	f = open(path+filename, "r")
# 	response = HttpResponse(FileWrapper(f), content_type='application/pdf')
# 	response['Content-Disposition'] = 'attachment; filename=Resume1.pdf'
# 	f.close()
# 	return response