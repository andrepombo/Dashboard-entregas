# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User,Group
from django.conf import settings



class Cliente(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    fone = models.CharField(max_length=50, null=True)
    nome = models.CharField(max_length=50, null=True)
    criado = models.DateTimeField(auto_now_add=True, null=True)
   
    profile_pic = models.ImageField(default='tie.jpg',null=True, blank=True)
    class Meta:
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'

    def __str__(self):
        return self.nome



class App(models.Model):
   
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, null=True, on_delete=models.SET_NULL)
    fone = models.CharField(max_length=50, null=True)
    nome = models.CharField(max_length=50, null=True)
    criado = models.DateTimeField(auto_now_add=True, null=True)
   
    class Meta:
        verbose_name = 'app'
        verbose_name_plural = 'apps'

    def __str__(self):
        return self.nome

class Order(models.Model):

    ENTREGA = ( ('Normal', 'Normal'), ('Atrasada','Atrasada'),('Rápida','Rápida'))
    TIPO = (('Pizza', 'Pizza'), ('Sanduiche', 'Sanduiche'), ('Sushi','Sushi'),('Outros', 'Outros'))
    NOTA = ((1,1),(2,2),(3,3),(4,4),(5,5))

    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, null=True, on_delete=models.SET_NULL)
    app = models.ForeignKey(App, null=True, on_delete=models.SET_NULL)
    nome = models.CharField(max_length=50, null=True)
    nota = models.PositiveSmallIntegerField(null=True,choices=NOTA)
    total = models.DecimalField(null=True, max_digits=9, decimal_places=2)
    tipo = models.CharField(max_length=50, null=True)
    entrega = models.CharField(max_length=50, null=True,choices=ENTREGA)
    criado = models.DateTimeField(auto_now_add=True, null=True)
    
    
    
   
   
    @property
    def status_info(self):
        res = {'class': None}

        if self.entrega == "Normal":
            res['class'] = 'text-success'
        elif self.entrega == 'Atrasada':
            res['class'] = 'text-danger'
        return res

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'

    def __str__(self):
        return self.nome

   

class Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100, null=True, blank=True)
    nota = models.CharField(max_length=100, null=True, blank=True)
    comentario = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'item'
        verbose_name_plural = 'items'
    
    
    def __str__(self):
        return self.nome















 
   
