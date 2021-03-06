# Generated by Django 2.0.4 on 2018-04-03 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=511)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='answers.Category')),
                ('title', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=2047)),
                ('answers', models.ManyToManyField(related_name='sources', to='answers.Answer')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='answers.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='categories',
            field=models.ManyToManyField(related_name='answers', to='answers.Category'),
        ),
    ]
