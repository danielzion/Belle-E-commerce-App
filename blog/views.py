from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Blog, Comment, Preference, BlogCategory
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Count
from .forms import NewCommentForm
from django.contrib.auth.decorators import login_required

def is_users(post_user, logged_user):
    return post_user == logged_user

PAGINATION_COUNT = 3

# Create your views here.
@login_required(login_url='/accounts/login')
def BlogView(request):
    posts = Blog.objects.all().order_by('date_posted')
    recent_posts = posts[0:5]
    post_categories = BlogCategory.objects.all()

    return render(request, 'blog/home.html', {'posts':posts, 'post_categories': post_categories, 'recent_posts' : recent_posts})

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        posts = Blog.objects.all().order_by('date_posted')
        data = super().get_context_data(**kwargs)
        comments_connected = Comment.objects.filter(post_connected=self.get_object()).order_by('-date_posted')
        post_categories = BlogCategory.objects.all()
        data['comments'] = comments_connected
        data['form'] = NewCommentForm(instance=self.request.user)
        data['post_categories'] = post_categories
        data['recent_posts'] = posts[0:5]
        return data

    def post(self, request, *args, **kwargs):
        new_comment = Comment(content=request.POST.get('content'),
                              author=self.request.user,
                              post_connected=self.get_object())
        new_comment.save()

        return self.get(self, request, *args, **kwargs)


class BlogListView(LoginRequiredMixin, ListView):
    model = Blog
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = PAGINATION_COUNT

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['preference'] = Preference.objects.all()
        return data


    def get_queryset(self):
        category = get_object_or_404(BlogCategory, name=self.kwargs.get('name'))
        return Blog.objects.filter(category=category)



class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    template_name = 'blog/post_delete.html'
    context_object_name = 'post'
    success_url = '/blog'

    def test_func(self):
        return is_users(self.get_object().author, self.request.user)


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ['title','description','code_snippet','github','download','images']
    template_name = 'blog/post_new.html'
    success_url = '/blog'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['tag_line'] = 'Add a new post'
        return data


class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    fields = ['title','description','code_snippet','github','download','images']
    template_name = 'blog/post_new.html'
    success_url = '/blog'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return is_users(self.get_object().author, self.request.user)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['tag_line'] = 'Edit a post'
        return data

# Like Functionality====================================================================================

@login_required
def postpreference(request, postid, userpreference):
        
        if request.method == "POST":
                eachpost= get_object_or_404(Blog, id=postid)

                obj=''

                valueobj=''

                try:
                        obj= Preference.objects.get(user= request.user, post= eachpost)

                        valueobj= obj.value #value of userpreference


                        valueobj= int(valueobj)

                        userpreference= int(userpreference)
                
                        if valueobj != userpreference:
                                obj.delete()


                                upref= Preference()
                                upref.user= request.user

                                upref.post= eachpost

                                upref.value= userpreference


                                if userpreference == 1 and valueobj != 1:
                                        eachpost.likes += 1
                                        eachpost.dislikes -=1
                                elif userpreference == 2 and valueobj != 2:
                                        eachpost.dislikes += 1
                                        eachpost.likes -= 1
                                

                                upref.save()

                                eachpost.save()
                        
                        
                                context= {'eachpost': eachpost,
                                  'postid': postid}

                                return HttpResponseRedirect(request.META.get('HTTP_REFERER',  '/'))

                        elif valueobj == userpreference:
                                obj.delete()
                        
                                if userpreference == 1:
                                        eachpost.likes -= 1
                                elif userpreference == 2:
                                        eachpost.dislikes -= 1

                                eachpost.save()

                                context= {'eachpost': eachpost,
                                  'postid': postid}

                                return HttpResponseRedirect(request.META.get('HTTP_REFERER',  '/'))
                                
                        
        
                
                except Preference.DoesNotExist:
                        upref= Preference()

                        upref.user= request.user

                        upref.post= eachpost

                        upref.value= userpreference

                        userpreference= int(userpreference)

                        if userpreference == 1:
                                eachpost.likes += 1
                        elif userpreference == 2:
                                eachpost.dislikes +=1

                        upref.save()

                        eachpost.save()                            


                        context= {'eachpost': eachpost,
                          'postid': postid}

                        return HttpResponseRedirect(request.META.get('HTTP_REFERER',  '/'))


        else:
                eachpost= get_object_or_404(Blog, id=postid)
                context= {'eachpost': eachpost,
                          'postid': postid}

                return HttpResponseRedirect(request.META.get('HTTP_REFERER',  '/'))