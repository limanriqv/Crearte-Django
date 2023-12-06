from django.views.generic import TemplateView

class Cerveceria(TemplateView):
    template_name = "index.html"
    
class Productos(TemplateView):
    template_name = "productos.html"
    


