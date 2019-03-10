from django.shortcuts import render

from .models import Zadacha
# Create your views here.

def post_list(request):
	n = Zadacha.objects.all()
	return render(request, 'todo/index.html', context={'Zadacha': n})