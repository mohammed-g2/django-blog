from django.core.paginator import Paginator
from django.db.models.functions import Left
from .models import Post

def paginate_posts(current_page, posts_per_page, user=None):
    if user:
        posts = user.post_set.annotate(partial_content=Left('content', 120)).order_by('-date').all()
    else:
        posts = Post.objects.annotate(partial_content=Left('content', 120)).order_by('-date').all()
    pagination = Paginator(posts, posts_per_page)
    page = pagination.get_page(current_page)

    return {
        'pages': pagination.page_range,
        'posts': page.object_list,
        'page_obj': page
    }