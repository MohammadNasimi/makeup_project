from datetime import datetime

from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView
from booking.models import Booking
from booking import forms


# class BookingCreateView(CreateView):
#     model = Booking
#     fields = ['service', 'count_adult', 'count_child', 'start_time', 'agent', 'customer']
#     # fields ="__all__"
#     template_name = 'Booking/create_booking.html'
#     success_url = reverse_lazy('booking:create_booking')


class BookingView(View):

    def post(self, request):
        form = forms.BookingForm(request.POST)
        if form.is_valid():
            service = form.cleaned_data['service']
            count_adult = form.cleaned_data['count_adult']
            count_child = form.cleaned_data['count_child']
            start = form.cleaned_data['start_time']
            start_time = datetime(start.year, start.month, start.day)
            end_time = form.cleaned_data['start_time']
            print(12)
            # agent = form.cleaned_data['agent']
            # customer = form.cleaned_data['customer']

            def list_time():
                return [i for i in range(8, 17, service.time * (count_child + count_adult))]

            print(list_time())
            print(start_time.year)
            print(service.cost)
            # m=Booking.objects.create(service=service, count_adult=count_adult, count_child=count_child, start_time=start_time,
            #                    end_time=end_time, cost_final=cost_final, agent=agent, customer=customer)
        context = {
            'form': form,
        }
        return render(request=self.request, template_name='Booking/bo.html', context=context)

    def get(self, request):
        form = forms.BookingForm()
        context = {
            'form': form,
        }
        return render(request=self.request, template_name='Booking/bo.html', context=context)


class BookingListView(ListView):
    model = Booking
    fields = ['service', 'count_adult', 'count_child', 'start_time', 'agent', 'customer']
    template_name = 'Booking/list_book.html'
