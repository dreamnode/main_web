from django.shortcuts import render, redirect
from .models import our_work, Post
from django.views.generic import (
    ListView,
    DetailView)
from .forms import ContactFormEmail
from django.core.mail import send_mail
'''
from .models import (Post,
						PostComment)
class PostListView(ListView):
    model = Post
    template_name = 'official/dreamblog.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    queryset = Post.objects.filter(post_class='major')
    ordering = ['-date_posted']
    paginate_by = 3
    '''

def dreamnode (request):
	our_works = our_work.objects.all()
	context = {
	'work1':our_works[0],
	'work2':our_works[1],
	'work3':our_works[2],
	'work4':our_works[3],
	'work5':our_works[4],
	'work6':our_works[5],
	}
	if request.method == 'POST':
		forms = ContactFormEmail(request.POST)
		if forms.is_valid():
			fromemail = forms.cleaned_data['from_email']
			subject = forms.cleaned_data['subject']
			message = forms.cleaned_data['message']
			print(message)
			send_mail(subject,message,fromemail,['attehkayode2@gmail.com'],fail_silently=True)
		return redirect('dreamnode')

	else:
		forms = ContactFormEmail()
		context['forms'] = forms
		return render(request,'dreamnode/dreamnode.html',context)



class PostListView(ListView):
    model = Post
    template_name = 'dreamnode/blog.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3

class BlogDetailView(DetailView):
    model = Post


def social_stereotype(request):

	return render(request, 'dreamnode/social_stereotype.html')

