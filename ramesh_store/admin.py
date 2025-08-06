from django.contrib import admin
from .models import Product, ContactInfo, Category

class ProductInline(admin.StackedInline):
    model = Product
    extra = 1
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'price', 'offer_price', 'image', 'in_stock')
        }),
    )
    show_change_link = True
    classes = ['collapse']  

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [ProductInline]
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'offer_price', 'in_stock')
    list_filter = ('category', 'in_stock', 'created_at')
    search_fields = ('name', 'description')
    ordering = ('-created_at',)
    fieldsets = (
        ('Product Info', {
            'fields': ('name', 'category', 'description', 'in_stock')
        }),
        ('Pricing', {
            'fields': ('price', 'offer_price')
        }),
        ('Image', {
            'fields': ('image',)
        }),
    )

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('store_name', 'phone', 'email', 'updated_at')
    search_fields = ('store_name', 'phone', 'email')
    readonly_fields = ('updated_at',)

admin.site.site_header = "Ramesh Store Admin"
admin.site.site_title = "Ramesh Store Control Panel"
admin.site.index_title = "Welcome to Ramesh Store Dashboard"