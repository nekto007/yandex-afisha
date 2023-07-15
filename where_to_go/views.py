from django.http import HttpResponse
from django.template import loader


def start_page(request):
    template = loader.get_template('index.html')
    context = {}
    render_page = template.render(context, request)
    return HttpResponse(render_page)
