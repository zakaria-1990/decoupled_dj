from django.urls import path
from .views import Index
from .api.views import InvoiceCreate, ClientList

app_name = 'billing'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('api/clients/', ClientList.as_view(), name='client_list'),
    path('api/invoice', InvoiceCreate.as_view(), name='invoice_create'),
]