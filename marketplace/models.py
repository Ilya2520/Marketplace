# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import UniqueConstraint



class Client(models.Model):
    id_client = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    locate = models.CharField(max_length=255)
    birthday = models.DateField()
    USERNAME_FIELD = 'email'

    class Meta:
        managed = False
        db_table = 'client'


class User(AbstractUser):
    id_client = models.ForeignKey('Client', models.DO_NOTHING, db_column='id_client', blank=True, null=True)


class Delivery(models.Model):
    id_delivery = models.AutoField(primary_key=True)
    id_storage = models.ForeignKey('Storage', models.DO_NOTHING, db_column='id_storage', blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)
    delivery_time = models.CharField(max_length=255, blank=True, null=True)
    id_order = models.ForeignKey('Order1', models.DO_NOTHING, db_column='id_order', blank=True, null=True)
    id_delivery_stat = models.ForeignKey('DeliveryStat', models.DO_NOTHING, db_column='id_delivery_stat', blank=True,
                                         null=True)

    class Meta:
        managed = False
        db_table = 'delivery'


class DeliveryStat(models.Model):
    id_delivery_stat = models.AutoField(primary_key=True)
    delivery_stat = models.IntegerField(blank=True, null=True)
    state_desc = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'delivery_stat'


class Goods(models.Model):
    id_good = models.AutoField(primary_key=True)
    good_price = models.IntegerField(blank=True, null=True)
    short_info = models.CharField(max_length=255, blank=True, null=True)
    good_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'goods'


#
# class HasOrderStruct(models.Model):
#     order = models.OneToOneField('Order1', models.DO_NOTHING)  # The composite primary key (order_id, order_struct_id) found, that is not supported. The first column is selected.
#     order_struct = models.ForeignKey('OrderStruct', models.DO_NOTHING)
#     UniqueConstraint(fields=['order', 'order_struct'], name='id')
#
#     class Meta:
#         managed = False
#         db_table = 'has_order_struct'
#
#
# class HasOrderStruct1(models.Model):
#     order = models.OneToOneField('Order1', models.DO_NOTHING)  # The composite primary key (order_id, order_struct_id) found, that is not supported. The first column is selected.
#     order_struct = models.ForeignKey('OrderStruct', models.DO_NOTHING)
#     UniqueConstraint(fields=['order', 'order_struct'], name='id')
#
#     class Meta:
#         managed = True
#         db_table = 'has_order_struct2'


class Order1(models.Model):
    id_order = models.AutoField(primary_key=True)
    payment = models.IntegerField()
    order_price = models.IntegerField(blank=True, null=True)
    order_info = models.CharField(max_length=255, blank=True, null=True)
    order_date = models.DateField(blank=True, null=True)
    id_client = models.ForeignKey(Client, models.DO_NOTHING, db_column='id_client', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order1'


class OrderStruct(models.Model):
    id_order_struct = models.AutoField(primary_key=True)
    count_of_prod = models.IntegerField(blank=True, null=True)
    id_good = models.ForeignKey(Goods, models.DO_NOTHING, db_column='id_good', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_struct'


class Storage(models.Model):
    id_storage = models.AutoField(primary_key=True)
    locate = models.CharField(max_length=255, blank=True, null=True)
    worktime = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'storage'


class HasOrderStruct(models.Model):
    order_id = models.OneToOneField('Order1',
                                 models.DO_NOTHING, primary_key=True)  # The composite primary key (order_id, order_struct_id) found, that is not supported. The first column is selected.
    order_struct_id = models.ForeignKey('OrderStruct', models.DO_NOTHING)

    class Meta:
        db_table = 'has_order_struct'
        unique_together = (('order_id','order_struct_id'),)
