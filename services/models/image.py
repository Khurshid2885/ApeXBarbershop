from django.db import models

from services.models.base import BaseModel
from services.models.service import Service


class HaircutImage(BaseModel):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="haircuts")
    img_file = models.FileField(upload_to='haircuts/', default="haircuts/crew_cut.png", blank=True, null=True)

    class Meta:
        db_table = 'haircutImage'