from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.title_uz

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Condition(models.Model):
    title = models.CharField(max_length=256)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="conditions")

    def __str__(self) -> str:
        return self.title_uz


class Question(models.Model):
    title = models.CharField(max_length=256)
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE, related_name="questions")

    def __str__(self) -> str:
        return self.title_uz


class Answer(models.Model):
    title = models.CharField(max_length=256)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")

    def __str__(self) -> str:
        return self.title_uz
