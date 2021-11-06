from django.contrib import admin
from .models import User, Category, Unit

class UserAdmin(admin.ModelAdmin):
    fields = [
        'username',
        'password',
        'first_name',
        'last_name',
    ]
    list_display = [
        'id',
        'username',
        'first_name',
        'last_name',
        'date_joined',
        'is_staff',
        'is_superuser'
    ]

    def save_form(self, request, form, change):
        category = form.save(commit=False)
        category.admin = request.user
        category.save()

        return super().save_form(request, form, change)

    class Meta:
        model = User

admin.site.register(User, UserAdmin)


class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = Category

admin.site.register(Category, CategoryAdmin)


class UnitAdmin(admin.ModelAdmin):
    class Meta:
        model = Unit

admin.site.register(Unit, UnitAdmin)
