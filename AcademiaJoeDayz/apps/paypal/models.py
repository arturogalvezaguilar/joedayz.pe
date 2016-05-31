from django.db import models

# Create your models here.

class Dolar(models.Model):
    dolar_a_soles = models.DecimalField(max_digits=10, decimal_places=2)
    create_to = models.DateField(auto_now_add=True)
    update_to = models.DateField(auto_now=True)
    estado = models.IntegerField()

class ModeloPaypal:
    cmd = '_xclick'
    business = 'jamdiazdiaz@gmail.com'
    item_name = str()
    #item_name = 'Core Spring 3.0 y 4.0 Presencial'
    item_number = int()
    #item_number = 7
    quantity = 1
    discount_amount = 0
    amount = float()
    #amount = 400
    page_style = 'primary'
    no_shipping = 1
    rm = 2
    no_note = 1
    currency_code = 'USD'
    cn = 'PP-BuyNowBF'
    lc = 'es'
    url = 'https://www.paypal.com/cgi-bin/webscr'