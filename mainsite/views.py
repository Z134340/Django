from django.template.loader import get_template
from django.http import HttpResponse
from datetime import datetime
from .models import Post

# Create your views here.


def homepage(request):
    # posts = Post.objects.all()
    # post_lists = list()
    # for count, post in enumerate(posts):
    #     post_lists.append("<h3>No.{}:".format(
    #         str(count)) + str(post)+"</h3>")
    #     post_lists.append("<small>"+str(post.body)+"</small><br><br>")
    # return HttpResponse(post_lists)

    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)

