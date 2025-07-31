from .models import AdditionalMaterials

def get_logo(request):
   logo = AdditionalMaterials.objects.filter(title="logo").first()   
   return {"logo": logo}