# Generated by Django 3.2.4 on 2021-07-05 18:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('imagen', models.ImageField(null=True, upload_to='productos')),
                ('descripcion', models.TextField()),
                ('precio', models.IntegerField()),
                ('destacado', models.BooleanField(default='False')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField(default=0)),
                ('productos', models.ManyToManyField(blank=True, to='core.producto')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]