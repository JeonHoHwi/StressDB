from django.db import models
from django.utils import timezone
# Create your models here.

class Description(models.Model):
	class Meta:
		db_table = 'Description'
	id = models.AutoField(primary_key=True)

	SRP_ID				= models.CharField(max_length=200 ,blank=True)
	SRR_ID				= models.CharField(max_length=200 ,blank=True)
	Assay_Type			= models.CharField(max_length=200 ,blank=True)
	Cultivar			= models.CharField(max_length=200 ,blank=True)
	Treatment			= models.CharField(max_length=200 ,blank=True)
	Stage				= models.CharField(max_length=200 ,blank=True)
	Tissue				= models.CharField(max_length=200 ,blank=True)
	Layout				= models.CharField(max_length=200, blank=True)
	Treat				= models.CharField(max_length=200, blank=True)




class tpm_list(models.Model):
	class Meta:
		db_table = 'tpm_list'
	id = models.AutoField(primary_key=True)

	target_id			= models.CharField(max_length=200 ,blank=True)
	Tpm 				= models.CharField(max_length=500 ,blank=True)


class short_name(models.Model):
    class Meta:
    	db_table = 'short_name'
    id = models.AutoField(primary_key=True)

    Tissue  	= models.CharField(max_length=200, blank=True)
    Name     	= models.CharField(max_length=200, blank=True)
    FullName 	= models.CharField(max_length=200, blank=True)
    Description_1 = models.CharField(max_length=200, blank=True)

class annotation(models.Model):
	class Meta:
		db_table = 'annotation'
	id = models.AutoField(primary_key=True)

	locus_name           = models.CharField(max_length=200, blank=True)
	TAIR_accession       = models.CharField(max_length=200, blank=True)
	object_name          = models.CharField(max_length=200, blank=True)
	relationship_type    = models.CharField(max_length=200, blank=True)
	GO_term              = models.CharField(max_length=200, blank=True)
	GO_ID                = models.CharField(max_length=200, blank=True)
	TAIR_Keyword_ID      = models.CharField(max_length=200, blank=True)
	Aspect               = models.CharField(max_length=200, blank=True)
	Goslim_term          = models.CharField(max_length=200, blank=True)
	Evidence_code        = models.CharField(max_length=200, blank=True)
	Evidence_description = models.CharField(max_length=200, blank=True)
	Evidence_with        = models.CharField(max_length=200, blank=True)
	Reference            = models.CharField(max_length=200, blank=True)
	Annotator            = models.CharField(max_length=200, blank=True)
	Date_annotated       = models.CharField(max_length=200, blank=True)

class df_leaf(models.Model):
    class Meta:
    	db_table = 'df_leaf'
    id = models.AutoField(primary_key=True)

    Sym_Description  	= models.CharField(max_length=200, blank=True)
    target_id           = models.CharField(max_length=200, blank=True)

class df_root(models.Model):
    class Meta:
    	db_table = 'df_root'
    id = models.AutoField(primary_key=True)

    Sym_Description  	= models.CharField(max_length=200, blank=True)
    target_id           = models.CharField(max_length=200, blank=True)

class df_shoot(models.Model):
    class Meta:
    	db_table = 'df_shoot'
    id = models.AutoField(primary_key=True)

    Sym_Description  	= models.CharField(max_length=200, blank=True)
    target_id           = models.CharField(max_length=200, blank=True)