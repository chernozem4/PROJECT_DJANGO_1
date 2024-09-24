from django.shortcuts import render, get_object_or_404
from . import  models, forms
from django.http import HttpResponse
from django.views import View
from django.views import generic

class MyBookListView(View):
    def get(self, request):
        post_object = models.MyBook.objects.all()
        return render(
            request,
            template_name='my_book_list.html',
            context={
                'post_object': post_object
            }
        )

# Detail View for MyBook
class MyBookDetailView(View):
    def get(self, request, id):
        post_id = get_object_or_404(models.MyBook, id=id)
        return render(
            request,
            template_name='my_book_detail.html',
            context={
                'post_id': post_id
            }
        )

# List View for editing MyBook items
class BookListEditView(View):
    def get(self, request):
        post_object = models.MyBook.objects.all()
        return render(
            request,
            template_name='crud/book_list_edit.html',
            context={
                'post_object': post_object
            }
        )

# Update View for a specific MyBook
class UpdateBookView(View):
    def get(self, request, id):
        post_id = get_object_or_404(models.MyBook, id=id)
        form = forms.PostForm(instance=post_id)
        return render(
            request,
            template_name='crud/update_book.html',
            context={
                'form': form,
                'post_id': post_id
            }
        )

    def post(self, request, id):
        post_id = get_object_or_404(models.MyBook, id=id)
        form = forms.PostForm(request.POST, instance=post_id)
        if form.is_valid():
            form.save()
            return HttpResponse('Новость отредактирована!!! <a href = "/post_list/">На список новостей</a>')
        return render(
            request,
            template_name='crud/update_book.html',
            context={
                'form': form,
                'post_id': post_id
            }
        )

# Delete View for listing MyBook items
class MyBookListDeleteView(View):
    def get(self, request):
        post_object = models.MyBook.objects.all()
        return render(
            request,
            template_name='crud/my_book_list_delete.html',
            context={
                'post_object': post_object
            }
        )

# Delete a specific MyBook
class BookDropView(View):
    def post(self, request, id):
        post_id = get_object_or_404(models.MyBook, id=id)
        post_id.delete()
        return HttpResponse('Новость удалена!!! <a href = "/my_book_list/">На список новостей</a>')

# Create a new MyBook item
class CreateBookView(View):
    def get(self, request):
        form = forms.PostForm()
        return render(
            request,
            template_name='crud/create_book.html',
            context={
                'form': form
            }
        )

    def post(self, request):
        form = forms.PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Данные успешно отправлены!!! <a href = "/post_list/">На список новостей</a>')
        return render(
            request,
            template_name='crud/create_book.html',
            context={
                'form': form
            }
        )



class SearchView(generic.ListView):
    template_name = 'my_book_list.html'
    context_object_name = 'post_object'
    paginate_by = 5
    def get_queryset(self):
        return models.MyBook.objects.filter(title__icontains=self.request.GET.get('q')).order_by('-id')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context







class BookDropDeleteView(generic.DeleteView):
    template_name = 'crud/confirm_delete.html'
    success_url = '/my_book_list_delete/'
    def get_object(self, **kwargs):
        post_id = self.kwargs.get('id')
        return get_object_or_404(models.MyBook, id=post_id)
