from .models import AdditionalMaterials

def get_logo(request):
   logo = AdditionalMaterials.objects.filter(title="logo").first() 
   favicon = AdditionalMaterials.objects.filter(title="favicon").first()  
   return {"logo": logo, "favicon": favicon}