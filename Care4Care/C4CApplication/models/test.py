#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eboutique.settings")

from django.db import models
from backoffice.models import *

# Cr�ation d'un attribut
product_attribute = ProductAttribute(name="couleur")
product_attribute.save()

# Cr�ation des valeurs des attributs
attribute1 = ProductAttributeValue(value="bleu", product_attribute=product_attribute, position=0)
attribute1.save()

attribute2 = ProductAttributeValue(value="jaune", product_attribute=product_attribute, position=0)
attribute2.save()

attribute2 = ProductAttributeValue(value="brun", product_attribute=product_attribute, position=0)
attribute2.save()

# Cr�ation du produit
product = Product(name="Tshirt", code="54065", price_ht=25, price_ttc=30)
product.save()

# Cr�ation d'une d�clinaison de produit
product_item = ProductItem(product=product, code="5046", code_ean13="a1")
product_item.save()
product_item.attributes.add(attribute1)
product_item.attributes.add(attribute1)
product_item.save()