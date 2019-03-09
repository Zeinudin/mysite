from django.shortcuts import render

# Create your views here.

def post_list(request):
	n = ['lirov_z', 'oleg', 'viktor', 'irina']
	return render(request, 'todo/index.html', context={'names': n})