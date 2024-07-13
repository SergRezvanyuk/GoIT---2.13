from django.forms import ModelForm, CharField, TextInput, ModelChoiceField, Textarea, ChoiceField
from .models import Author, Quote


class AuthorForm(ModelForm):

    fullname = CharField(
        min_length=3, max_length=50, required=True, widget=TextInput()
    )

    born_date = CharField(max_length=50,  widget=TextInput())
    born_location = CharField(max_length=50,  widget=Textarea())
    description = CharField(min_length=10, max_length=150, required=True, widget=Textarea())


    class Meta:
        model = Author
        fields = ['fullname','born_date', 'born_location', 'description']


class AuthorChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.fullname

class QuoteForm(ModelForm):
    author = AuthorChoiceField(queryset=Author.objects.all(), required=True)
    quote = CharField(min_length=10, max_length=150, required=True, widget=Textarea())

    class Meta:
        model = Quote
        fields = ['quote', 'author']
