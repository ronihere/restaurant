from django.contrib import admin
from . models import contactform,booktable,menu,specials,Gallery,subscription
# Register your models here.
admin.site.register(contactform)
admin.site.register(booktable)
admin.site.register(menu)
admin.site.register(specials)
admin.site.register(Gallery)
admin.site.register(subscription)