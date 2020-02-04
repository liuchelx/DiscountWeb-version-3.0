from django.contrib import admin
from .models import Profile
from .models import Product


admin.site.register(Profile)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    #all the info show to user
    #to do change the Tag to a selectable list
    list_display =('Product_ID','ProductName','PubTime','EndTime','Tag','click','isExpired')

    ordering = ('PubTime',)

    list_editable = ['ProductName','Tag','EndTime']

    date_hierarchy = 'PubTime'

    search_fields = ['Tag','EndTime','isExpired']
