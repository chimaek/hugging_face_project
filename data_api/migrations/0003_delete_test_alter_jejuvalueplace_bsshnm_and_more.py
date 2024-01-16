# Generated by Django 5.0 on 2024-01-16 08:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("data_api", "0002_jejuvalueplace"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Test",
        ),
        migrations.AlterField(
            model_name="jejuvalueplace",
            name="bsshNm",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="jejuvalueplace",
            name="bsshTelno",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="jejuvalueplace",
            name="dataCd",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="jejuvalueplace",
            name="emdNM",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="jejuvalueplace",
            name="etcCn",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="jejuvalueplace",
            name="indutyNm",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="jejuvalueplace",
            name="laCrdnt",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="jejuvalueplace",
            name="loCrdnt",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="jejuvalueplace",
            name="prdlstCn",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="jejuvalueplace",
            name="regDt",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="jejuvalueplace",
            name="rnAdres",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="jejuvalueplace",
            name="slctnMm",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="jejuvalueplace",
            name="slctnYr",
            field=models.CharField(max_length=200, null=True),
        ),
    ]
