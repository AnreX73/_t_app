from .models import AdditionalMaterials

def get_logo(request):
   logo = AdditionalMaterials.objects.filter(title="логотип").first()   
   return {"logo": logo}