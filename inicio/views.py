from django.http import HttpResponse


def index(request):
    return HttpResponse("Soy un anillo de polinomios")
