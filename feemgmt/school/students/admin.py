from django.contrib import admin

# Register your models here.
from.models import StudentModel,FeesModel,Generalprofile,ResourceProfile

@admin.register(StudentModel)
class StudentAdmin(admin.ModelAdmin):
	list_display=['name','Class','Std_id','Mobile_no','Gender','Academic_year','Branch']
@admin.register(FeesModel)
class FeesAdmin(admin.ModelAdmin):
	list_display=['Name','Std_id','Receipt_no','Total_fees']

admin.site.register(Generalprofile)
admin.site.register((ResourceProfile))
