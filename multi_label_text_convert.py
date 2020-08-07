#!/usr/bin/env python
# coding: utf-8

import re
import pandas as pd
import csv
import sys
file1 = sys.argv[1]
file2 = sys.argv[2] 
input=pd.read_csv(file1)
input=input[['Driver','Review','Selected']]
output=pd.read_csv(file2)
for i in range(len(input)):
    if input['Selected'][i]=='y':
        if input['Review'][i] not in output.values:
            if input['Driver'][i] in output.columns:
                output_dict={}
                output_dict['Review']=input['Review'][i]
                output_dict[input['Driver'][i]]=1
                output_col_list = list(output.columns)
                output_col_list.remove('Review')
                output_col_list.remove(input['Driver'][i])
                for i in output_col_list:
                    output_dict[i]=0
                output = output.append(output_dict, ignore_index=True)     
            else:
                output_dict={}
                output_dict['Review']=input['Review'][i]
                output_col_list = list(output.columns)
                output_col_list.remove('Review')
                for i in output_col_list:
                    output_dict[i]=0
                output = output.append(output_dict, ignore_index = True)                                                                             
        else:
            dup_rev_index_list = output[output['Review']==input['Review'][i]].index.values
            first_index_dup_val = dup_rev_index_list[0]
            if input['Driver'][i] in output.columns:
                driver_val = input['Driver'][i]
                output[driver_val][first_index_dup_val] = 1
    else:
        if input['Review'][i] not in output.values:
            output_dict={}
            output_dict['Review']=input['Review'][i]
            output_col_list = list(output.columns)
            output_col_list.remove('Review')
            for i in output_col_list:
                output_dict[i]=0
            output = output.append(output_dict, ignore_index = True)
output.to_csv(file2, index=False) 
