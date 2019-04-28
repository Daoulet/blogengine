from django.shortcuts import render

def posts_list(request):
	n = 'Daulet', 'Franco', 'Arjen'
	return render(request, 'mainApp/index.html', context={'names': n})
