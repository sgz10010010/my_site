# Generated by Django 2.2.1 on 2019-07-02 18:35

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20190625_1826'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='内容')),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='article',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='article',
            name='is_deleted',
            field=models.NullBooleanField(default=False, verbose_name='删除状态'),
        ),
        migrations.AlterField(
            model_name='article',
            name='read_count',
            field=models.IntegerField(default=0, verbose_name='阅读数'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=50, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='article',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='articletype',
            name='type_name',
            field=models.CharField(max_length=20, verbose_name='文章类型'),
        ),
    ]
