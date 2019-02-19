from django.http import HttpResponse
from django.template import loader


# Create your views here.
def index(request):
    template = loader.get_template("index.html")
    human = {
        "name": "Permpoon",
        "age": 25,
        "food": ["water", "soda", "cocktail"]
    }
    return HttpResponse(template.render(human, request))
