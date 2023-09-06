from django.db import models
from treebeard.mp_tree import MP_Node

from tcap.models import TerroristGroup

class Content(models.Model):
    some_stuff = models.CharField(max_length=30)
    def __str__(self):
        return f"{self.some_stuff}"

# terrorist group with heirachal properties in archive
# must foreign key to terrorist groups in tcap
class TaxonomyTerroristGroup(MP_Node):
    tcap_terrorist_group = models.ForeignKey(to=TerroristGroup, on_delete=models.deletion.CASCADE)

    def __str__(self):
        return f"TaxonomyTerroristGroup: {self.tcap_terrorist_group.name}"


# Taxonomy which foreign keys to archive (heirachal) terrorist group
class Taxonomy(models.Model):
    content = models.ForeignKey(to=Content, on_delete=models.deletion.CASCADE)
    terrorist_group = models.ForeignKey(to=TaxonomyTerroristGroup, on_delete=models.deletion.CASCADE)
    other_stuff = models.CharField(max_length=30, default="some other taxonomy stuff")

    def __str__(self):
        return f"taxonomy on content{self.content.pk}"



