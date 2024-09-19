from django.shortcuts import render
from . import models


def product_filter_view(request):
    if request.method == 'GET':
        product_cloth_men = models.Cloth.objects.filter(tags__name='Одежда мужская').order_by('-id')
        product_cloth_women = models.Cloth.objects.filter(tags__name='Одеждая женская').order_by('-id')
        product_cloth_kids = models.Cloth.objects.filter(tags__name='Одеждая детская').order_by('-id')

        return render(
            request,
            template_name='filter_list.html',
            context={
                'product_cloth_men': product_cloth_men,
                'product_cloth_women': product_cloth_women,
                'product_cloth_kids': product_cloth_kids
            }
        )
