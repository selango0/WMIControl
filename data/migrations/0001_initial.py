# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-21 04:48
from __future__ import unicode_literals

import data.models
from django.db import migrations, models
import django.db.models.deletion
import macaddress.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('COAID', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('productKey', models.CharField(max_length=255, unique=True)),
                ('securityCode', models.CharField(blank=True, max_length=255, null=True)),
                ('windowsVer', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CPU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.CharField(blank=True, max_length=255, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CPUModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('manufacturer', models.CharField(max_length=255)),
                ('arch', models.CharField(max_length=255)),
                ('partnum', models.CharField(blank=True, max_length=255, null=True)),
                ('family', models.CharField(blank=True, max_length=255, null=True)),
                ('upgradeMethod', models.CharField(blank=True, max_length=255, null=True)),
                ('cores', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('threads', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('speed', models.PositiveSmallIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GPU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GPUModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('size', models.BigIntegerField(blank=True, null=True)),
                ('refresh', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('arch', models.CharField(blank=True, max_length=255, null=True)),
                ('memoryType', models.CharField(blank=True, max_length=255, null=True)),
            ],
            bases=(models.Model, data.models.CalcSizeMixin),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campus', models.CharField(blank=True, max_length=255)),
                ('room', models.CharField(blank=True, max_length=255)),
                ('address', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='LogicalDisk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('mount', models.CharField(blank=True, max_length=4, null=True)),
                ('filesystem', models.CharField(blank=True, max_length=255, null=True)),
                ('size', models.BigIntegerField()),
                ('freesize', models.BigIntegerField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
            ],
            bases=(models.Model, data.models.CalcSizeMixin),
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('os', models.CharField(blank=True, max_length=255)),
                ('cloudID', models.PositiveSmallIntegerField(blank=True, null=True, unique=True)),
                ('activation', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.Activation')),
            ],
        ),
        migrations.CreateModel(
            name='MachineModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compType', models.PositiveSmallIntegerField(choices=[(0, 'Unknown'), (1, 'Other'), (2, 'Desktop'), (3, 'Laptop'), (4, 'Server')], default=0)),
                ('manufacturer', models.CharField(blank=True, max_length=255)),
                ('name', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mac', macaddress.fields.MACAddressField(integer=True, unique=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Machine')),
            ],
        ),
        migrations.CreateModel(
            name='NetworkModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('manufacturer', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PhysicalDisk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.CharField(blank=True, max_length=255)),
                ('partitions', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Machine')),
            ],
        ),
        migrations.CreateModel(
            name='PhysicalDiskModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('size', models.BigIntegerField()),
                ('interface', models.CharField(blank=True, max_length=5)),
                ('manufacturer', models.CharField(blank=True, max_length=255)),
            ],
            bases=(models.Model, data.models.CalcSizeMixin),
        ),
        migrations.CreateModel(
            name='RAM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.CharField(blank=True, max_length=255, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Machine')),
            ],
        ),
        migrations.CreateModel(
            name='RAMModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.BigIntegerField()),
                ('manufacturer', models.CharField(blank=True, max_length=255, null=True)),
                ('partnum', models.CharField(blank=True, max_length=255, null=True)),
                ('speed', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('formFactor', models.CharField(blank=True, max_length=255, null=True)),
                ('memoryType', models.CharField(blank=True, max_length=255, null=True)),
            ],
            bases=(models.Model, data.models.CalcSizeMixin),
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='WMICodes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Unknown', max_length=255)),
                ('code', models.PositiveSmallIntegerField()),
                ('identifier', models.CharField(max_length=255)),
                ('wmiObject', models.CharField(max_length=255)),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Unknown'), (1, 'Known'), (2, 'Custom')], default=0)),
                ('machines', models.ManyToManyField(blank=True, to='data.Machine')),
            ],
        ),
        migrations.AddField(
            model_name='ram',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.RAMModel'),
        ),
        migrations.AddField(
            model_name='physicaldisk',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.PhysicalDiskModel'),
        ),
        migrations.AddField(
            model_name='network',
            name='model',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.NetworkModel'),
        ),
        migrations.AddField(
            model_name='machine',
            name='model',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.MachineModel'),
        ),
        migrations.AddField(
            model_name='machine',
            name='roles',
            field=models.ManyToManyField(blank=True, to='data.Role'),
        ),
        migrations.AddField(
            model_name='logicaldisk',
            name='disk',
            field=models.ManyToManyField(to='data.PhysicalDisk'),
        ),
        migrations.AddField(
            model_name='location',
            name='computers',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.Machine'),
        ),
        migrations.AddField(
            model_name='gpu',
            name='machine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Machine'),
        ),
        migrations.AddField(
            model_name='gpu',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.GPUModel'),
        ),
        migrations.AddField(
            model_name='cpu',
            name='machine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Machine'),
        ),
        migrations.AddField(
            model_name='cpu',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.CPUModel'),
        ),
    ]
