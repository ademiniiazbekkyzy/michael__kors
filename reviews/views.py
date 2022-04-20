from django.shortcuts import render, redirect
from rest_framework.generics import get_object_or_404

from product.models import Product
from reviews.forms import CommentForm
from reviews.models import Comments


def new_single(request, pk):
    """Вывод полной статьи
    """
    new = get_object_or_404(Product, id=pk)
    comment = Comments.objects.filter(new=pk, moderation=True) # moderation=True
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.new = new
            form.save()
            return redirect(new_single, pk)
    else:
        form = CommentForm()
    return render(request, "news/new_single.html",
                  {"new": new,
                   "comments": comment,
                   "form": form})
