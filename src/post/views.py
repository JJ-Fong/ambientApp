from django.http import HttpResponse
from django.shortcuts import render
from .form import PostForm
from .models import Post
# Create your views here.

def posts_create(request):
	form = PostForm(request.POST or None)

	if form.is_valid():
		instance = form.save(commit = False)
		instance.save()
	context = {
		"form" : form 
	} 

	query_set = Post.objects.all()
	for i in range(len(query_set)):
		print query_set[i].title
		print query_set[i].content
		print query_set[i].timestamp
		
		
	return render(request, "post-create.html", context)

def posts_detail(request):
	return HttpResponse("<h1>Detail</h1>")
	
def posts_list(request):
	# if request.user.is_authenticated():
	# 	context_data = {
	# 		"title": "My User List"
	# 	}
	# else:
	# 	context_data = {
	# 		"title": "List"
	# 	}
	context_data = {
 		"title": "List"
 	}
 	
	return render(request, "post-index.html", context_data )
	#return HttpResponse("<h1>List</h1>")
	
def posts_update(request):
	return HttpResponse("<h1>Update</h1>")
	
def posts_delete(request):
	return HttpResponse("<h1>Delete</h1>")
	