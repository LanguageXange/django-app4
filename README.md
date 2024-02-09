# LinkTree Clone

A link-in-bio tool like Linktree that allows you to create a webpage that has all your links in one place. You'll be able to create, edit, and delete links and create a landing page that displays all your links to share with the world!

## MyLink -> Profile: Many To One Relationship with `models.ForeignKey`

https://docs.djangoproject.com/en/5.0/topics/db/examples/many_to_one/#

```python
# models.py
class Profile(models.Model):
   BG_CHOICES = (
       ('blue', 'Blue'), # stored value , displayed valued
       ('orange', 'Orange'),
       ('purple', 'Purple'),
       ('green', 'Green'),
       ('black', 'Black'),
   )
   # name, slug, bg_color
   name = models.CharField(max_length = 50)
   slug = models.SlugField(max_length = 100)
   bg_color = models.CharField(max_length =50, choices = BG_CHOICES)

   def __str__(self):
       return self.name.upper()


class MyLink(models.Model):
   text = models.CharField(max_length =100)
   url = models.URLField(max_length = 100)
   profile = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name="mylinks")

```

## Class Based Views

`from django.views.generic import ListView, CreateView, UpdateView, DeleteView`

- ListView -> `model_list.html`
- CreateView & UpdateView -> `model_form.html`
- DeleteView -> `model_confirm_delete.html`

```python
class LinkListView(ListView):
    model = MyLink
    # by default look for a template called model_list.html -> aka mylink_list.html
class LinkCreateView(CreateView):
    model = MyLink
    fields = "__all__"
    success_url = reverse_lazy('link-list')
    # by default look for a template model_form.html => aka mylink_form.html
class LinkUpdateView(UpdateView):
    model = MyLink
    fields = ['text','url']
    success_url = reverse_lazy('link-list')
    # by default look for a template model_form.html => aka mylink_form.html
class LinkDeleteView(DeleteView):
    model = MyLink
    success_url = reverse_lazy('link-list')
    # by default look for a template called model_confirm_delete.html -> aka mylink_confirm_delete.html

```
