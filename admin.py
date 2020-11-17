from django.contrib import admin
from .models import   Categorys, お菓子A, お菓子B, お菓子C, 半生お菓子



admin.site.register(Categorys)

class お菓子AAdmin(admin.ModelAdmin):
    fieldsets = [('商品名', {'fields': ['商品名']}),
                 ('賞味', {'fields': ['dis_date'],'classes': ['collapse']}),
                 
                 ]
    list_display = ('商品名','category','賞味期限','見切り1','見切り2', '見切り3')
    list_filter = ['dis_date','category']
    list_editable = ['category']
    search_fields = ['商品名']
admin.site.register(お菓子A, お菓子AAdmin)

class お菓子BAdmin(admin.ModelAdmin):
    fieldsets = [('商品名', {'fields': ['商品名']}),
                 ('賞味', {'fields': ['dis_date'],'classes': ['collapse']}),
                 ]
    list_display = ('商品名','category','賞味期限','見切り1','見切り2', '見切り3')
    list_filter = ['dis_date','category']
    search_fields = ['商品名']
    list_editable = ['category']
admin.site.register(お菓子B, お菓子BAdmin)

class お菓子CAdmin(admin.ModelAdmin):
    fieldsets = [('商品名', {'fields': ['商品名']}),
                 ('賞味', {'fields': ['dis_date'],'classes': ['collapse']}),
                 ]
    list_display = ('商品名','category', '賞味期限','見切り1','見切り2', '見切り3')
    list_filter = ['dis_date','category']
    search_fields = ['商品名']
    list_editable = ['category']
admin.site.register(お菓子C, お菓子CAdmin)

class 半生お菓子Admin(admin.ModelAdmin):
    fieldsets = [('商品名', {'fields': ['商品名']}),
                 ('賞味', {'fields': ['dis_date'],'classes': ['collapse']}),
                 ]
    list_display = ('商品名','category','賞味期限','見切り1','見切り2', '見切り3')
    list_filter = ['dis_date','category']
    search_fields = ['商品名']
    list_editable = ['category']
admin.site.register(半生お菓子, 半生お菓子Admin)