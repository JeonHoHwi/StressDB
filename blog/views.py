from django.shortcuts import render
from .models import Description, tpm_list, short_name, annotation, df_root, df_shoot, df_leaf
from django import forms
import pandas as pd
import numpy as np
from operator import itemgetter, attrgetter
from django.http import HttpResponse

# Create your views here.

def study(request):

	return render(request, 'blog/study.html', {})

def rf(request):

	rf_root = df_root.objects.all()
	rf_shoot = df_shoot.objects.all()
	rf_leaf = df_leaf.objects.all()

	return render(request, 'blog/rf.html', {'rf_root': rf_root, 'rf_shoot' : rf_shoot, 'rf_leaf' : rf_leaf})

def post_list(request):

	treat_list, ix, tpm_values, tpm_set, tpm_set_fix, data, = [],[],[],[], [], []
	locus_name, object_name,TAIR_accession, relationship_type, GO_term, GO_ID, TAIR_Keyword_ID, Aspect, Goslim_term, Evidence_code, Evidence_description, Reference, Annotator, Date_annotated = [], [], [], [], [], [], [], [], [], [], [], [], [], []
	Name, FullName, Description_1 = [], [], []
	dic_tissue 			= {'rosette leaf':'R_leaf', 'aerial shoot':'A_shoot','mature leaf':'M_leaf','leaf':'leaf','root':'root'}


# tissue select -> push treat_list

	tissue = request.GET.get('tissueSelect')

	if str(tissue) == 'None':
		tissue = 'root'
	tissue_selected 	= Description.objects.filter(Tissue=tissue)
	treat_list			= [x.Treat for x in tissue_selected]
	ix					+= [int(x.id) for x in tissue_selected]

	tissue_list = Description.objects.all()
	tissue_list_set = set([x.Tissue for x in tissue_list])


# gene select -> push tpm_output
	query 				= request.GET.get("gene")

	if str(query)		== 'None':
		query 			= 'AT1G01010.1'

	gene_selected 		= tpm_list.objects.filter(target_id=query)
	tpm_values 			+= [x.Tpm for x in gene_selected]
	tpm_set				+= [np.array(x.split(','))[ix] for x in tpm_values]
	tpm_set_fix			+= [list(map(float,x.tolist())) for x in tpm_set]
	tpm_output			=  sum(tpm_set_fix,[])

	annotation_1         = annotation.objects.filter(object_name=query)

	short_name_selected = short_name.objects.filter(Tissue=tissue)
	Name          += [x.Name for x in short_name_selected]
	Name1 		   = Name[0]
	Name2 		   = Name[1]
	Name3 		   = Name[2]
	Name4 		   = Name[3]
	FullName      += [x.FullName for x in short_name_selected]
	FullName1 = FullName[0]
	FullName2 = FullName[1]
	FullName3 = FullName[2]
	FullName4 = FullName[3]
	Description_1 += [x.Description_1 for x in short_name_selected]
	Description1 = Description_1[0]
	Description2 = Description_1[1]
	Description3 = Description_1[2]
	Description4 = Description_1[3]



# csv file
	data				+= [[x,y] for x, y in zip(tpm_output, treat_list)]
	data_sort   		= sorted(data,  key=lambda x: x[1]=='Con', reverse=True)
	DB_output			= [(np.array(data_sort))]
	csv_file			= '/static/%s/output.csv'%dic_tissue[tissue]

	np.savetxt('./blog/static/%s/output.csv'%dic_tissue[tissue], np.column_stack((DB_output)), delimiter = ',', fmt = '%s', header = 'tpm,treatment',comments="")

	return_source 		= {
	'csv_file':csv_file, 'query':query, 'tissue':tissue, 'tissue_list_set':tissue_list_set,
	'Name1':Name1, 'Name2':Name2, 'Name3':Name3,'Name4':Name4,
	'FullName1':FullName1, 'FullName2':FullName2, 'FullName3':FullName3,'FullName4':FullName4,
	'Description1':Description1, 'Description2':Description2, 'Description3':Description3,'Description4':Description4, 'annotation_1' : annotation_1,
	}

	return render(request, 'blog/post_list.html', return_source)