from django.contrib import admin
from .models import Description, tpm_list, short_name, annotation, df_root, df_shoot, df_leaf
# Register your models here.
admin.site.register(Description)