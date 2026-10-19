from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm
from accounts.models import Courses
from django.shortcuts import render

class BlogListView(ListView):
    model = Post
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tas"] = get_user_model().objects.filter(is_ta=True)
        return context

class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

#you have to be logged in to be able to create times
class TimeCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "time_add.html"
    form_class = PostForm

    def form_valid(self, form):
        form.instance.TA = self.request.user
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["Class"].choices = [
            (value, label) for value, label in Courses.choices
            if value in self.request.user.courses
        ]
        return form

class BlogUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    form_class = PostForm

class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

class TutorsPageView(DetailView):
    model = get_user_model()
    template_name = "tutors.html"
    context_object_name = "ta"


# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, "post_detail.html", {"post": post})