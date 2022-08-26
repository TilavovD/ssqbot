from django.db import models

# Create your models here.


class Category(models.Model):
    """
    Category is a model to enter the available categories in the bot.
    The examples are psychology, urology, genecology, etc.
    """
    title = models.CharField(max_length=1024)

    def __str__(self) -> str:
        return self.title_uz

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Condition(models.Model):
    """
    Condition is a model for the categories given.
    In the category field, there will be a connection between 
    the condition and the appropriate category
    """
    title = models.CharField(max_length=1024)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="conditions")

    def __str__(self) -> str:
        return self.title_uz
    
    class Meta:
        verbose_name = "Condition"
        verbose_name_plural = "Conditions"


class Question(models.Model):
    """
    Question model serves for the model of conditions given in the 
    condition field of the model and its title field gets the question 
    which should be asked.
    """
    title = models.CharField(max_length=1024)
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE, related_name="questions")

    def __str__(self) -> str:
        return self.title_uz
    
    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions" 


class Answer(models.Model):
    """
    Answer model is a model which serves as an answer for the questions
    given in the question field of the model.
    """
    title = models.CharField(max_length=1024)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    score = models.IntegerField()

    def __str__(self) -> str:
        return self.title_uz

    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers" 


class Result(models.Model):
    """
    Result model to publish the results. In the title field
    is entered the result. In the min_score field, the minimum score whereas
    in the max_score, obviously the maximum score for this result output.
    
    """
    title = models.CharField(max_length=2048)
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE, related_name="results")
    min_score = models.IntegerField()
    max_score = models.IntegerField()

    def __str__(self) -> str:
        return self.title_uz
    
    class Meta:
        verbose_name = "Result"
        verbose_name_plural = "Results" 
