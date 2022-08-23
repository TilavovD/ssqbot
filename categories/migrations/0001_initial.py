# Generated by Django 4.0.7 on 2022-08-22 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uz', models.CharField(max_length=256)),
                ('title_ru', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uz', models.CharField(max_length=256)),
                ('title_ru', models.CharField(max_length=256)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conditions', to='categories.category')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uz', models.CharField(max_length=256)),
                ('title_ru', models.CharField(max_length=256)),
                ('condition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='categories.condition')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uz', models.CharField(max_length=256)),
                ('title_ru', models.CharField(max_length=256)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='categories.question')),
            ],
        ),
    ]