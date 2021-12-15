from django import forms
from app.models import App, Order, Item
#from app.lookups import WorkerLookup, RestaurantLookup

from django.forms import inlineformset_factory





class AppForm(forms.ModelForm):

    nome = forms.CharField(label="Nome", widget=forms.TextInput(attrs={'class': 'form-control order'}))
    fone= forms.CharField(label="Telefone", widget=forms.TextInput(attrs={'class': 'form-control order'})) 
    class Meta:
        model = App
        fields = ['nome','fone']


class OrderForm(forms.ModelForm):

    ENTREGA = ( ('Normal', 'Normal'), ('Atrasada','Atrasada'),('Rápida','Rápida'))
    TIPO = (('Pizza', 'Pizza'), ('Sanduiche', 'Sanduiche'), ('Sushi','Sushi'),('Outros', 'Outros'))
    NOTA = ((1,1),(2,2),(3,3),(4,4),(5,5))

    #cliente = forms.CharField(label="Cliente", widget=forms.TextInput(attrs={'class': 'form-control order'}))
    nome = forms.CharField(label="Nome", widget=forms.TextInput(attrs={'class': 'form-control order'}))
    #app = forms.ModelChoiceField(initial='Your name',label="App", queryset=App.objects.all(),widget=forms.Select(attrs={'class': 'form-select order'}))
    nota = forms.IntegerField(label="Nota Geral", widget=forms.Select(choices=NOTA,attrs={'class': 'form-select order'}))
    tipo = forms.CharField(label="Tipo", widget=forms.Select(choices=TIPO,attrs={'class': 'form-select order'}))
    entrega = forms.CharField(label="Entrega", widget=forms.Select(choices=ENTREGA,attrs={'class': 'form-select order'}))
    total = forms.DecimalField(label="Preço", widget=forms.NumberInput(attrs={'class': 'form-control order'}))
    class Meta:
        model = Order
        fields = ['nome','nota','tipo','entrega','app','total']

    def __init__(self,  user=None, *args, **kwargs,):
        # kwargs.update(initial={
        #     # 'field': 'value'
        #     'app': '6'
        # })
        super(OrderForm, self).__init__(*args, **kwargs)

        self.fields['app'] = forms.ModelChoiceField(initial='Your name',label="App", 
        queryset=App.objects.filter(user=user),widget=forms.Select(attrs={'class': 'form-select order'}))
        #self.fields['app'].widget.attrs['class'] = 'form-select'
        
        
        
        
        

       




class ItemForm(forms.ModelForm):

    nome = forms.CharField(required=False, label="Nome", widget=forms.TextInput(attrs={'class': 'form-control'}))
    nota = forms.CharField(required=False,label="Nota", widget=forms.TextInput(attrs={'class': 'form-control'})) 
    comentario = forms.CharField(required=False, label="Comentário", widget=forms.TextInput(attrs={'class': 'form-control'}))   
    class Meta:
        model = Item
        fields = ['nome','nota','comentario']
        #exclude = ()


ItemFormSet = inlineformset_factory(Order, Item,form=ItemForm, extra=1)
        



        
        