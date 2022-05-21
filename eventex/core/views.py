from django.views.generic.list import ListView

home = ListView.as_view(template_name='index.html')