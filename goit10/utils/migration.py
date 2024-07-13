import os
import django
from pymongo.server_api import ServerApi
from pymongo import MongoClient

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'goit10.settings')
django.setup()
from quotes.models import Quote, Tag, Author

uri = "mongodb+srv://rezvaserg:FdhiHDdmAphGFbzg@cluster0.5izpshs.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
db = client["GoIT8"]

authors = db.author.find()

for author in authors:
    Author.objects.get_or_create(
        fullname = author['fullname'],
        born_date = author['born_date'],
        born_location = author['born_location'],
        description = author['description'].strip()
    )
    # print(author['fullname'])

quotes = db.quote.find()

for quote in quotes:
    tags = []
    for tag in quote['tags']:
        t, *_ = Tag.objects.get_or_create(name=tag)
        tags.append(t)

    exist_quote = bool(len(Quote.objects.filter(quote=quote['quote'])))

    if not exist_quote:
        author = db.author.find_one({'_id': quote['author']})
        # print('---------------', author['fullname'])
        a = Author.objects.get(fullname=author['fullname'])
        q = Quote.objects.create(
            quote = quote['quote'],
            author = a
        )
        for tag in tags:
            q.tags.add(tag)

