from django.shortcuts import render

def  post_list(request):
	n = ['Dauka', 'DDD', 'RRR', 'Wh']
	return render(request, 'blog/index.html', context={'names': n}) 
