from django.shortcuts import render, get_object_or_404
from . import  models

def my_book_list_view(request):
    if request.method == "GET":
        # query запрос
        post_object = models.MyBook.objects.all()
        return render(
            request,
            template_name='my_book_list.html',
            context={
                'post_object': post_object
            }
        )



def my_book_detail_view(request, id):
    if request.method == 'GET':
        post_id = get_object_or_404(models.MyBook, id=id)
        return render(
            request,
            template_name='my_book_detail.html',
            context={
                'post_id': post_id
            }
        )


# Create your views here.
