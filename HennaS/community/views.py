from django.shortcuts import render


def view_posts(request):
    """ View to return index page """
    template = 'community/view_posts.html'
    context = {
    }
    return render(request, template, context)
