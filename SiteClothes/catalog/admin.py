from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import clothes, newss, Topic, Comment


@admin.register(clothes)
class ClothesAdmin(admin.ModelAdmin):
    list_display = ('title', 'summ', 'catt', 'genderr', 'display_size', 'statuss', 'image_show')
    list_filter = ('catt', 'genderr')
    fieldsets = (('Общая информация', {'fields': ('title', 'summ', 'catt', 'genderr', 'imgg', 'statuss')}),
                 ('Характеристика', {'fields': ('materiall', 'colorr', 'brendd', 'sizee')}))

    def image_show(self, obj):
        if obj.imgg:
            return mark_safe("<img src='{}' width='60' />".format(obj.imgg.url))
        return "None"

    image_show.__name__ = "Фото"

admin.site.register(newss)
admin.site.register(Topic)
admin.site.register(Comment)



