# Generated by Django 4.2.3 on 2023-10-20 05:40

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
            name='Chude',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten_chude', models.CharField(max_length=100)),
                ('lan_capnhat_cuoi', models.DateTimeField(auto_now_add=True)),
                ('luot_xem', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Diendan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten_diendan', models.CharField(max_length=100, unique=True)),
                ('mota', models.CharField(max_length=1000000)),
                ('ngaytao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Thaoluan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nd', models.TextField(max_length=5000)),
                ('ngay_tao', models.DateTimeField(auto_now_add=True)),
                ('ngay_capnhat', models.DateTimeField(null=True)),
                ('chu_de', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cac_thaoluan', to='blog.chude')),
                ('tao_boi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tao_thaoluan', to=settings.AUTH_USER_MODEL)),
                ('thanhvien_capnhat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='capnhat_boi', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='chude',
            name='dien_dan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cac_chude', to='blog.diendan'),
        ),
        migrations.AddField(
            model_name='chude',
            name='tao_boi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tao_chude_moi', to=settings.AUTH_USER_MODEL),
        ),
    ]
