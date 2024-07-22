from django.contrib import admin

from users.models import User

# registration user in admin panel
admin.site.register(User)
