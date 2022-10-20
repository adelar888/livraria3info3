# Generated by Django 4.1 on 2022-10-20 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_autor_editora_livro"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="editora",
            name="site",
        ),
        migrations.AddField(
            model_name="livro",
            name="autores",
            field=models.ManyToManyField(related_name="livros", to="core.autor"),
        ),
        migrations.AlterField(
            model_name="categoria",
            name="descricao",
            field=models.CharField(max_length=255),
        ),
    ]
