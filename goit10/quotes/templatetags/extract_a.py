from django import template

from ..models import Author, Quote, Tag



register = template.Library()

def get_author(author_obj):
    a_id = author_obj.id
    obj = Author.objects.filter(id=a_id)
    name= obj.first().fullname
    return name

def get_tag(quote_id):

    quote_obj = Quote.objects.get(pk=quote_id)
    tags = quote_obj.tags.all()
    tag_names = [tag.name for tag in tags]
    return tag_names




register.filter('author', get_author)
register.filter('qtag', get_tag)
