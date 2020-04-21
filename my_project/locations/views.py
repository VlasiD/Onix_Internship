from django.http import HttpResponse


def home(request):
    """Displays home page"""
    return HttpResponse("<h1>Home page</h1>")


def display_route(request, route):
    """Displays entered route"""
    text = '<h3>Displaying entered route: {}</h3>'.format(route)
    back = '<p><a style="color:blue" href="http://127.0.0.1:8000/"><< Back</a></p>'
    response = text + back
    return HttpResponse(response)