from django.contrib import admin


# Make poll app modifiable in admin
from django.contrib import admin
from .models import Question

admin.site.register(Question)

# Register your models here.
