from django.views.generic import TemplateView


class EventListView(TemplateView):
    template_name = 'event_list.html'