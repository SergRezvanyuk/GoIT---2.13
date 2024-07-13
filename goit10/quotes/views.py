from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Quote, Author, Tag
from django.shortcuts import render, redirect, get_object_or_404
from .forms import AuthorForm, QuoteForm

def main(request, page=1):
    quotes = Quote.objects.all()

    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})



def nauthor(request):

    if request.method == 'POST':
        form = AuthorForm(request.POST)

        if form.is_valid():

            form.save()
            return redirect(to='quotes:root')
        else:
            return render(request, 'quotes/nauthor.html', {'form': form})

    return render(request, 'quotes/nauthor.html', {'form': AuthorForm()})
    # return render(request)

def nquote(request):
    
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes:root')  
    else:
        form = QuoteForm()
    return render(request, 'quotes/nquote.html', {'form': form})
    

def author_page(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'quotes/author_page.html', {"author": author})

def tag_page(request, tag):
    tag = get_object_or_404(Tag, name=tag)
    # print('---------',tag)
    quotes_with_tag = Quote.objects.filter(tags=tag)
    # print('---///---',quotes_with_tag)
    return render(request, 'quotes/tag_page.html', context={'quotes': quotes_with_tag})