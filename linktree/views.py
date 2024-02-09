from django.shortcuts import render,get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Profile, MyLink

# Create your views here.

# function based view
# def index(request):
#     links = MyLink.objects.all()
#     context = {'links':links}
#     return render(request, 'linktree/index.html', context)


# class based view inherits from ListView
class LinkListView(ListView):
    model = MyLink
    # by default look for a template called model_list.html -> aka mylink_list.html


class LinkCreateView(CreateView):
    # in function based we will need to
    # create forms.py file and Form
    # check if this was a POST or GET request
    # return an empty form or to save the form data

    model = MyLink
    fields = "__all__"
    success_url = reverse_lazy('link-list')
    # by default look for a template model_form.html => aka mylink_form.html


# update link
class LinkUpdateView(UpdateView):
    # in function based we will need to:
    # create a form
    # check if it's a get or put request
    # render a form or update and save the form in DB

    model = MyLink
    fields = ['text','url']
    success_url = reverse_lazy('link-list')
    # by default look for a template model_form.html => aka mylink_form.html


class LinkDeleteView(DeleteView):
    # in function based we will need to:
    # take in a id/pk of an object
    # query to db for this object
    # check if exists - delete
    # return some template or forward to user to some url

    model = MyLink
    # after successful deletion
    success_url = reverse_lazy('link-list')

    # by default, it gives us a form to submit to delete the item
    # expect a template called model_confirm_delete.html -> aka mylink_confirm_delete.html



# function based view
def profile_view(request, profile_slug):
    profile = get_object_or_404(Profile, slug=profile_slug)
    links = profile.mylinks.all() # in our models.py we set the related_name to mylinks
    context = {
        "links":links,
        "profile":profile
    }

    return render(request,'linktree/profile.html', context)