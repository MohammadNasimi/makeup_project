from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.views import View

from customer.forms import contactusForm
from customer.models import Customer
from django.contrib import messages
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response


class CustomerCreateView(CreateView):
    model = Customer
    fields = ['first_name', 'last_name', 'email', 'Password']
    template_name = 'customer/create_customer.html'
    success_url = reverse_lazy('customer:create')


class CustomerListView(ListView):
    model = Customer
    fields = ['first_name', 'last_name', 'email', 'Password']
    template_name = 'customer/list_customer.html'


class CustomerUpdateView(UpdateView):
    model = Customer
    fields = ['first_name', 'last_name', 'email', 'Password']
    template_name = 'customer/update_customer.html'
    success_url = reverse_lazy('customer:list')


class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customer/delete_customer.html'
    success_url = reverse_lazy('customer:list')


def create_message(request):
    messages.set_level(request, 0)
    messages.add_message(request, messages.ERROR, "create success")
    messages.info(request, "email is not correct")
    return HttpResponse("New messages created!")


@api_view(['GET'])
def view_message(request):
    from customer.serializers import MessageSerializer
    storage = messages.get_messages(request)
    msgs = list(storage)
    MessageSerializer(msgs, many=True)
    return render(request, 'customer/create_customer.html')


class ContactusView(View):
    form_class = contactusForm
    template_name = 'customer/contact-us'

    def get(self, request):
        return render(request, 'customer/contact_us.html', {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            messages.add_message(request, messages.ERROR, "create success")
            return render(request, 'customer/contact_us.html', {'form': self.form_class})
        messages.add_message(request, messages.ERROR, "wrong email use @")
        return render(request, 'customer/contact_us.html', {'form': self.form_class})
