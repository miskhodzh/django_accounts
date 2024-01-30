from django.shortcuts import render
from . forms import PostCreationForm
from . models import Post

def post_create(request):
    template = 'posts/posts.html'
    if request.method == 'POST':
        form = PostCreationForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            post = Post(
                title=title,
                text=text,
                author=request.user
            )
            post.save()
    else:
        form = PostCreationForm()
    context = {
        'form': form,
        'posts': Post.objects.all(),
        'user_groups': str(request.user.groups.all()),
    }
    return render(request, template, context)
