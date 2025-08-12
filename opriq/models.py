from django.db import models
from django import template

register = template.Library()


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, unique=True, null=False, blank=False)
    base_sensitivity = models.FloatField()

    def __str__(self):
        return f"[{self.id:04}] {self.name} (s={self.base_sensitivity})"

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(base_sensitivity__gte=0), name="sensitivity_gte_0"),
            models.CheckConstraint(check=models.Q(base_sensitivity__lte=1), name="sensitivity_lte_1"),
        ]


class Inference(models.Model):
    id = models.AutoField(primary_key=True)
    from_items = models.ManyToManyField(Item, related_name='inferences_coming_from')
    to_item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='inferences_pointing_to')
    probability = models.FloatField()

    def __str__(self):
        from_names = ", ".join([i.name for i in self.from_items.all()])
        return f"[{self.id:04}] {from_names} -> {self.to_item.name} (p={self.probability})"


    @register.filter
    def from_items_ids(self):
        return [i.id for i in self.from_items.all()]


    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(probability__gte=0), name="probability_gte_0"),
            models.CheckConstraint(check=models.Q(probability__lte=1), name="probability_lte_1"),
        ]


class Modifier(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    value = models.CharField(max_length=128, null=False, blank=False)
    multiplier = models.FloatField()

    def __str__(self):
        return f"[{self.id:04}] {self.item.name} == {self.value} (×{self.multiplier})"


class FAQ(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128, null=False, blank=False)
    content = models.TextField(null=False, blank=False)