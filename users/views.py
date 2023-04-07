from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
# Create your views here.


def main(request, name):
    # template = loader.get_template('index.html')
    # return HttpResponse(template.render())
    data = {
        "dinosaurs": [
            "Tyrannosaurus",
            "Stegosaurus",
            "Raptor",
            "Triceratops",
        ],
        "title": name[0].upper() + name[1:] + " Page"
    }
    return render(request, name + ".html", data)
