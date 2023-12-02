# -*- encoding: utf-8 -*-

from django.db import transaction
from django.db.models import Q, Sum
from django.db.models import Count
from django.db.models.functions import ExtractWeekDay
from django.db.models.query import QuerySet


from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, JsonResponse, QueryDict

from django import template
from django.template.loader import render_to_string
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required

from rest_framework.views import APIView
from rest_framework.response import Response


from app.forms import AppForm, OrderForm
from app.forms import ItemFormSet
from app.models import App, Order, Item

from app.utils import set_pagination
from django.forms import inlineformset_factory

import datetime 
from .decorators import  unauthenticated_user, allowed_users, admin_only


from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

@login_required(login_url="/login/")
@admin_only

def index(request):

    date = datetime.datetime.now()
    month = date.month
    year = date.year
    labels = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 
    'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    month_label = labels[month-1]
   
    anual = Order.objects.filter(criado__year=date.year).aggregate(Sum('total')).get('total__sum')
    if not anual:
        anual = 0
    mensal = Order.objects.filter(criado__month=date.month).aggregate(Sum('total')).get('total__sum')
    if not mensal:
        mensal = 0

    

    orders = Order.objects.all().order_by('-id')[:5]
    #orders= reversed(orders)
    
    totalyear = (
            Order.objects
            .all()
            #.filter(criado__month='09')
            .values_list('criado__year')
            .annotate(Sum('total'))
            .order_by('criado__year')
        )
    
    divlist =[]
    divisao = Order.objects.values('tipo').annotate(total=Sum('total'))
    for item in divisao:
            divlist.append(item['tipo'])


    if 'Outros' not in divlist:
        outros = 0
    else:
        outros = (divisao.filter(tipo='Outros')[0].get('total')/totalyear[0][1])*100
    if 'Pizza' not in divlist:
        pizza = 0
    else:
        pizza = (divisao.filter(tipo='Pizza')[0].get('total')/totalyear[0][1])*100
    if 'Sanduiche' not in divlist:
        sanduiche = 0
    else:
        sanduiche = (divisao.filter(tipo='Sanduiche')[0].get('total')/totalyear[0][1])*100
    if 'Sushi' not in divlist:
        sushi = 0
    else:
        sushi = (divisao.filter(tipo='Sushi')[0].get('total')/totalyear[0][1])*100
   

    
    totalresto = Order.objects.all().count()
    divlist2 =[]
    count = Order.objects.values('tipo').annotate(total=Count('tipo'))
    for item in divisao:
            divlist2.append(item['tipo'])

    if 'Outros' not in divlist:
        outros2 = 0
    else:
        outros2 = (count.filter(tipo='Outros')[0].get('total')/totalresto)*100
    if 'Pizza' not in divlist:
        pizza2 = 0
    else:
        pizza2 = (count.filter(tipo='Pizza')[0].get('total')/totalresto)*100
    if 'Sanduiche' not in divlist:
        sanduiche2 = 0
    else:
        sanduiche2 = (count.filter(tipo='Sanduiche')[0].get('total')/totalresto)*100
    if 'Sushi' not in divlist:
        sushi2 = 0
    else:
        sushi2 = (count.filter(tipo='Sushi')[0].get('total')/totalresto)*100
    
    

    context = {'segment': 'index','anual':anual, 'mensal':mensal, 'orders':orders, 
    'outros':outros, "pizza":pizza, 'sanduiche':sanduiche, 'sushi':sushi, 'outros2':outros2, 
    "pizza2":pizza2, 'sanduiche2':sanduiche2, 'sushi2':sushi2, 'month_label':month_label,
    "year":year}
    
    html_template = loader.get_template('index.html')
    
    return HttpResponse(html_template.render(context, request))



@login_required(login_url="/login/")
@allowed_users(allowed_roles=['cliente'])
def userPage(request):

    obj_user = request.user.cliente.order_set
    date = datetime.datetime.now()
    month = date.month
    year = date.year
    labels = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 
    'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    month_label = labels[month-1]
    anual = obj_user.filter(criado__year=date.year).aggregate(Sum('total')).get('total__sum')
    if not anual:
        anual = 0
    mensal = obj_user.filter(criado__month=date.month).aggregate(Sum('total')).get('total__sum')
    if not mensal:
        mensal = 0

    orders = request.user.cliente.order_set.all()
    
    totalyear = (
            obj_user
            .all()
            #.filter(criado__month='09')
            .values_list('criado__year')
            .annotate(Sum('total'))
            .order_by('criado__year')
        )
    
    divlist =[]
    divisao = obj_user.values('tipo').annotate(total=Sum('total'))
    for item in divisao:
            divlist.append(item['tipo'])

   
    if 'Outros' not in divlist:
        outros = 0
    else:
        outros = (divisao.filter(tipo='Outros')[0].get('total')/totalyear[0][1])*100
    if 'Pizza' not in divlist:
        pizza = 0
    else:
        pizza = (divisao.filter(tipo='Pizza')[0].get('total')/totalyear[0][1])*100
    if 'Sanduiche' not in divlist:
        sanduiche = 0
    else:
        sanduiche = (divisao.filter(tipo='Sanduiche')[0].get('total')/totalyear[0][1])*100
    if 'Sushi' not in divlist:
        sushi = 0
    else:
        sushi = (divisao.filter(tipo='Sushi')[0].get('total')/totalyear[0][1])*100
   
    
    totalresto = obj_user.all().count()
    divlist2 =[]
    count = obj_user.values('tipo').annotate(total=Count('tipo'))
    
    for item in divisao:
            divlist2.append(item['tipo'])

    
    if 'Outros' not in divlist:
        outros2 = 0
    else:
        outros2 = (count.filter(tipo='Outros')[0].get('total')/totalresto)*100
    if 'Pizza' not in divlist:
        pizza2 = 0
    else:
        pizza2 = (count.filter(tipo='Pizza')[0].get('total')/totalresto)*100
    if 'Sanduiche' not in divlist:
        sanduiche2 = 0
    else:
        sanduiche2 = (count.filter(tipo='Sanduiche')[0].get('total')/totalresto)*100
    if 'Sushi' not in divlist:
        sushi2 = 0
    else:
        sushi2 = (count.filter(tipo='Sushi')[0].get('total')/totalresto)*100


    context = {'segment': 'index','anual':anual, 'mensal':mensal, 'orders':orders, 
    'outros':outros, "pizza":pizza, 'sanduiche':sanduiche, 'sushi':sushi, 'outros2':outros2, 
    "pizza2":pizza2, 'sanduiche2':sanduiche2, 'sushi2':sushi2, 'month_label':month_label,
    "year":year}
    
    html_template = loader.get_template('index_user.html')
    
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        context['segment'] = load_template

        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))


class ChartData(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    
    def get(self, request,  format=None):
        
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'cliente':
            obj_user = request.user.cliente.order_set

        if group == 'admin':
            obj_user = Order.objects
        

        count = obj_user.all().values('tipo').annotate(total=Count('tipo'))

        weeklist = [0,0,0,0,0,0,0]       
        
        resultpizza = [0,0,0,0,0,0,0,0,0,0,0,0]
        resultsanduiche = [0,0,0,0,0,0,0,0,0,0,0,0]
        resultoutros = [0,0,0,0,0,0,0,0,0,0,0,0]
        resultsushi = [0,0,0,0,0,0,0,0,0,0,0,0]
        resultall = [0,0,0,0,0,0,0,0,0,0,0,0]
        divlist = []

        week = (obj_user
        .annotate(weekday=ExtractWeekDay('criado')) 
        .values('weekday')                          
        .annotate(count=Count('id'))                  
        .values('weekday', 'count')
        .order_by('weekday')
        )
        print(week)

        for day in week:
            p = day['weekday'] - 1 
            weeklist.insert(p, day['count'])

        results = (
            obj_user
            .all()
            #.filter(criado__month='09')
            .values_list('criado__year', 'criado__month','tipo')
            .annotate(Sum('total'))
            .order_by('criado__year', 'criado__month')
        )
        
        results2 = (
            obj_user
            .all()
            #.filter(criado__month='09')
            .values_list('criado__year', 'criado__month')
            .annotate(Sum('total'))
            .order_by('criado__year', 'criado__month')
        )
       
        
        for result in results:
            if result[2] == 'Pizza':
                p = result[1]-1
                resultpizza.insert(p,result[3])
            elif result[2] == 'Sanduiche':
                p = result[1]-1
                resultsanduiche.insert(p,result[3])
            elif result[2] == 'Sushi':
                p = result[1]-1
                resultsushi.insert(p,result[3])
            else: 
                p = result[1]-1
                resultoutros.insert(p,result[3])

        for result in results2:
            p = result[1]-1
            resultall.insert(p,result[2])



        for item in count:
            divlist.append(item['tipo'])

        divisao = obj_user.values('tipo').annotate(total=Sum('total'))

        if 'Outros' not in divlist:
            Outros = 0
        else:
            Outros = divisao.filter(tipo='Outros')[0].get('total')
        if 'Pizza' not in divlist:
            Pizza = 0
        else:
            Pizza = divisao.filter(tipo='Pizza')[0].get('total')
        if 'Sanduiche' not in divlist:
            Sanduiche = 0
        else:
            Sanduiche = divisao.filter(tipo='Sanduiche')[0].get('total')
        if 'Sushi' not in divlist:
            Sushi = 0
        else:
            Sushi = divisao.filter(tipo='Sushi')[0].get('total')

        

        if 'Outros' not in divlist:
            outros2 = 0
        else:
            outros2 = count.filter(tipo='Outros')[0].get('total')
        if 'Pizza' not in divlist:
            pizza2 = 0
        else:
            pizza2 = count.filter(tipo='Pizza')[0].get('total')
        if 'Sanduiche' not in divlist:
            sanduiche2 = 0
        else:
            sanduiche2 = count.filter(tipo='Sanduiche')[0].get('total')
        if 'Sushi' not in divlist:
            sushi2 = 0
        else:
            sushi2 = count.filter(tipo='Sushi')[0].get('total')

        pielist= [Outros,Pizza,Sanduiche,Sushi]
        pielist2 = [outros2,pizza2,sanduiche2,sushi2]    
        
        labels = ['Jan', 'Fev', 'Mar', 'Abr', 'Maio', 'Jun', 'Jul', 'Ago', 
        'Set', 'Out', 'Nov', 'Dez']
        labels2 = ['Dom','Seg','Ter','Qua','Qui','Sexta','Sab']
        data = {
                "labels": labels,
                "labels2": labels2,
                "default": resultsanduiche,
                "default2": resultpizza,
                "default3": resultoutros,
                "default4": resultall,
                "default5": resultsushi,
                "pielist": pielist,
                "pielist2": pielist2,
                "weeklist":weeklist,  
                "divlist": divlist,  
        }
        return Response(data)


def newapp(request):
        form = AppForm()
        if request.method == 'POST':
            form = AppForm(request.POST, request.FILES)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.cliente = request.user.cliente
                obj.user = request.user
                obj.save()
                return redirect('apps')
                      
        context = {'form':form}
        return render(request, 'app/apps/new_app.html', context)


# App!! ------------------------------------------------------------------------
class AppView(View):
    context = {'segment': 'apps'}

    def get(self, request, pk=None, action=None):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest': 
            if pk and action == 'edit':
                edit_row = self.edit_row(pk)
                return JsonResponse({'edit_row': edit_row})
            elif pk and not action:
                edit_row = self.get_row_item(pk)
                return JsonResponse({'edit_row': edit_row})

        if pk and action == 'edit':
            context, template = self.edit(request, pk)
        else:
            context, template = self.list(request)

        if not context:
            html_template = loader.get_template('page-500.html')
            return HttpResponse(html_template.render(self.context, request))

        return render(request, template, context)

    def post(self, request, pk=None, action=None):
        self.update_instance(request, pk)
        return redirect('apps')

    def put(self, request, pk, action=None):
        is_done, message = self.update_instance(request, pk, True)
        edit_row = self.get_row_item(pk)
        return JsonResponse({'valid': 'success' if is_done else 'warning', 
        'message': message, 'edit_row': edit_row})

    def delete(self, request, pk, action=None):
        app = self.get_object(pk)
        app.delete()

        redirect_url = None
        if action == 'single':
            messages.success(request, 'Item deleted successfully')
            redirect_url = reverse('apps')

        response = {'valid': 'success', 'message': 'Item deleted successfully', 
        'redirect_url': redirect_url}
        return JsonResponse(response)

    """ Get pages """
    
    def list(self,request):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'cliente':
            obj_user = request.user.cliente.app_set

        if group == 'admin':
            obj_user = App.objects

        
        apps = obj_user.all()

        self.context['apps'] = apps
    
        return self.context, 'app/apps/apps.html'

        
    def edit(self, request, pk):
        app = self.get_object(pk)

        self.context['app'] = app
        self.context['form'] = AppForm(instance=app)

        return self.context, 'app/apps/edit_app.html'

    """ Get Ajax pages """

    def edit_row(self, pk):
        app = self.get_object(pk)
        form = AppForm(instance=app)
        context = {'instance': app, 'form': form}
        return render_to_string('app/apps/edit_app_row.html', context)

    """ Common methods """

    def get_object(self, pk):
        app = get_object_or_404(App, id=pk)
        return app

    def get_row_item(self, pk):
        app = self.get_object(pk)
        edit_row = render_to_string('app/apps/edit_app_row.html', {'instance': app})
        return edit_row

    def update_instance(self, request, pk, is_urlencode=False):
        app= self.get_object(pk)
        form_data = QueryDict(request.body) if is_urlencode else request.POST
        form = AppForm(form_data, instance=app)
        if form.is_valid():
            form.save()
            if not is_urlencode:
                messages.success(request, 'App salvo com sucesso')

            return True, 'App salvo com sucesso'

        if not is_urlencode:
            messages.warning(request, 'Erro Ocorrido. Por favor, tente de novo.')
        return False, 'Erro Ocorrido. Por favor, tente de novo.'


    
# Orders!! ------------------------------------------------------------------------------------------
class OrderItemCreate(CreateView):
    model = Order
    form_class = OrderForm
    
    template_name = 'app/orders/orders_edit.html'
    #fields= '__all__'
    success_url = reverse_lazy('orders')
    
    def get_form_kwargs(self):
        kwargs = super(OrderItemCreate, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['items'] = ItemFormSet(self.request.POST)
        else:
            data['items'] = ItemFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        items = context['items']
        with transaction.atomic():
            obj = form.save(commit=False)
            obj.cliente = self.request.user.cliente
            obj.user = self.request.user
            obj.save()
            #self.object = form.save()
    
            if items.is_valid():
                items.instance = self.object
                items.save()
        #return super(ProfileItemCreate, self).form_valid(form)
        return super().form_valid(form)


class OrderItemUpdate(UpdateView):
    model = Order
    form_class = OrderForm
    #fields = ['nome', 'nota']
    template_name = 'app/orders/orders_edit.html'
    success_url = reverse_lazy('orders')

   
    def get_form_kwargs(self):
        kwargs = super(OrderItemUpdate, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        data = super(OrderItemUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['items'] = ItemFormSet(self.request.POST, instance=self.object)
        else:
            data['items'] = ItemFormSet(instance=self.object)
            #print(data)
            #print( data['items'])
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        items = context['items']
       
        with transaction.atomic():
            self.object = form.save()
    
            if items.is_valid():
                obj = form.save(commit=False)
                obj.cliente = self.request.user.cliente
                obj.user = self.request.user
                obj.save()
                # items.instance = self.object
                # items.save()   
                

        return super(OrderItemUpdate, self).form_valid(form)


# class ProfileDelete(DeleteView):
#     model = Profile
#     success_url = reverse_lazy('profilelist')

class OrderView(View):
    context = {'segment': 'orders'}

    def get(self, request, pk=None, action=None):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest': 
            if pk and action == 'edit':
                edit_row = self.edit_row(pk)
                return JsonResponse({'edit_row': edit_row})
            else:
                edit_row = self.get_row_item(pk)
                return JsonResponse({'edit_row': edit_row})

        
        else:
            context, template = self.list(request)

        if not context:
            html_template = loader.get_template('page-500.html')
            return HttpResponse(html_template.render(self.context, request))

        return render(request, template, context)

    def post(self, request, pk=None, action=None):
        self.update_instance(request, pk)
        return redirect('orders')
        

    def put(self, request, pk, action=None):
        is_done, message = self.update_instance(request, pk, True)
       
        edit_row = self.get_row_item(pk)
    
        return JsonResponse({'valid': 'success' if is_done else 'warning', 
        'message': message, 'edit_row': edit_row})

    def delete(self, request, pk, action=None):
        order = self.get_object(pk)
        order.delete()

        redirect_url = None
        if action == 'single':
            messages.success(request, 'Item deletado com sucesso')
            redirect_url = reverse('orders')

        response = {'valid': 'success', 'message': 'Item deletado com sucesso', 
        'redirect_url': redirect_url}
        return JsonResponse(response)

    """ Get pages """
    
    def list(self,request):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'cliente':
            obj_user = request.user.cliente.order_set

        if group == 'admin':
            obj_user = Order.objects

        orders = obj_user.all()
        #orders= reversed(orders)

        self.context['orders'] = orders
    
        return self.context, 'app/orders/orders.html'
        

    """ Get Ajax pages """

    def edit_row(self, pk):
        user = self.request.user
        print(user)
        order = self.get_object(pk)
        form = OrderForm(self.request.user,instance=order)
        context = {'instance': order, 'form': form, 'user':user}
        return render_to_string('app/orders/orders_edit_row.html', context, request=self.request)
        

    """ Common methods """

    def get_object(self, pk):
        order = get_object_or_404(Order, id=pk)
        return order

    def get_row_item(self, pk):
        order = self.get_object(pk)
        edit_row = render_to_string('app/orders/orders_edit_row.html', {'instance': order},
        request=self.request)
        return edit_row

    def update_instance(self, request, pk, is_urlencode=False):
        order= self.get_object(pk)
        form_data = QueryDict(request.body) if is_urlencode else request.POST
        form = OrderForm(self.request.user.id,form_data, instance=order)
        if form.is_valid():
            form.save()
            if not is_urlencode:
                messages.success(request, 'Pedido salvo com sucesso')

            return True, 'Pedido salvo com sucesso'

        if not is_urlencode:
            messages.warning(request, 'Erro Ocorrido. Por favor, tente de novo.')
        return False, 'Erro Ocorrido. Por favor, tente de novo.'





