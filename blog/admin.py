from django.contrib import admin
from blog.models import Article

class ArticleAdmin (admin.ModelAdmin):
	list_display = [field.name for field in Article._meta.fields]
	list_filter = ["title"] # Фильтрация по имени
	search_fields = ["title", "body"]
	# exclude = ["body"] Исключение
	# fields = ["body"] Только показывать
	# inlines = [FieldMappingInline]
	
	class Meta:
		model = Article
			
admin.site.register(Article, ArticleAdmin)
