# -*- encoding: utf-8 -*-
from django.contrib import admin
from app.models import App,Order, Item, Cliente
 
from import_export import resources
from import_export.admin import ImportMixin



class ClienteResource(resources.ModelResource):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'fone','criado']

@admin.register(Cliente)
class ClienteAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ['id', 'nome', 'fone','criado']
    resource_class = ClienteResource

class AppResource(resources.ModelResource):
    class Meta:
        model = App
        fields = ['id', 'cliente','nome', 'fone','criado']

@admin.register(App)
class AppAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ['id','cliente', 'nome', 'fone','criado']
    resource_class = AppResource


class OrderResource(resources.ModelResource):
    class Meta:
        model = Order
        fields = ['id','criado','user','cliente', 'nome','nota','entrega','tipo', 'app','total']

@admin.register(Order)
class OrderAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ['id','criado','user','cliente', 'nome','nota','entrega','tipo', 'app','total']
    resource_class = OrderResource



class ItemResource(resources.ModelResource):
    class Meta:
        model = Item
        fields = ['id','order','nome']
@admin.register(Item)
class ItemAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ['id','order','nome']
    resource_class = ItemResource









