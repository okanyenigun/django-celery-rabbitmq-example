from django.views.generic.edit import FormView
from django.http import HttpResponse
from myapp2.forms import MessageForm

class MessageView(FormView):
    template_name = 'message.html'
    form_class = MessageForm

    def form_valid(self, form):
        form.create_json()
        msg = 'Your message has been posted.'
        return HttpResponse(msg)