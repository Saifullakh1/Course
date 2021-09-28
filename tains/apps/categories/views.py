from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.forms import inlineformset_factory
from apps.categories.models import Category, CategoryImage
from apps.categories.forms import CategoryForm, CategoryImageForm


class CategoryDetailView(generic.DetailView):
    model = Category
    template_name = 'categories/category_detail.html'


def category_create(request):
    form = CategoryForm(request.POST, None)
    CategoryImageFormSet = inlineformset_factory(Category, CategoryImage, form=CategoryImageForm, extra=1)
    if form.is_valid():
        category = form.save()
        formset = CategoryImageFormSet(request.POST, request.FILES, instance=category)
        if formset.is_valid():
            formset.save()
        return redirect('index')
    formset = CategoryImageFormSet()
    return render(request, 'categories/category_create.html', locals())


def category_update(request, slug):
    category = get_object_or_404(Category, slug=slug)
    form = CategoryForm(request.POST, None, instance=category)
    CategoryImageFormSet = inlineformset_factory(Category, CategoryImage, form=CategoryImageForm, extra=1)
    if form.is_valid():
        category = form.save()
        formset = CategoryImageFormSet(request.POST, request.FILES, instance=category)
        if formset.is_valid():
            formset.save()
        return redirect('index')
    formset = CategoryImageFormSet(instance=category)
    return render(request, 'categories/category_update.html', locals())


def category_delete(request, slug):
    if request.method == 'POST':
        category = Category.objects.get(slug=slug)
        category.delete()
        return redirect('index')
    return render(request, 'categories/category_delete.html')








