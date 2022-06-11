#!/usr/bin/env python
# coding: utf-8

# In[1]:
import sys
import pandas as pd
import ECAUGT
import time
import multiprocessing
import numpy as np

# In[12]:


result = pd.read_pickle('sorted_tcells_raw.pk')


# In[13]:


import scanpy as sc
import sys
import pandas as pd
import ECAUGT
import time
import multiprocessing
import numpy as np


# In[22]:


# create scanpy object from the matrices
expr = result.iloc[:,:43878]
meta = result.iloc[:,43878:43878+16]
meta.reset_index(inplace=True)
expr.reset_index(inplace=True)
expr.drop(['cid'],axis=1,inplace=True)
adata = sc.AnnData(X = expr, obs = meta)
adata = adata[adata.obs['seq_tech']=='10X',:]
adata.var_names_make_unique()


# In[23]:



# In[24]:


sc.pp.filter_genes(adata, min_counts=5)
sc.pp.filter_genes(adata, min_cells=3)

# In[26]:


sc.pp.highly_variable_genes(adata, min_mean=0.0125, max_mean=3, min_disp=0.5)

sc.pp.scale(adata, max_value=10)
sc.tl.pca(adata, svd_solver='arpack')


# In[27]:


sc.pp.neighbors(adata, n_neighbors=10, n_pcs=20)
sc.tl.umap(adata)


# In[29]:


sc.pl.umap(adata,color=['CD8A','CD8B','GZMK','CD3E','GZMH','GZMB'],ncols=3)


# In[30]:


# sc.pl.umap(adata,color=['cell_type', 'cl_name', 'donor_age', 'donor_gender', 'donor_id', 'uHAF_name', 'organ', 'original_name', 'region', 'sample_status', 'seq_tech', 'study_id', 'subregion', 'tissue_type']) 


# In[ ]:





# In[ ]:





# In[ ]:




