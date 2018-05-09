from django.contrib import admin
from TestModel.models import Test,Contact,Tag

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','age', 'email')
    search_fields = ('name',)

admin.site.register(Contact, ContactAdmin)
admin.site.register([Test])