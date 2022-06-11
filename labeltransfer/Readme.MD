This directory contains the code for label transfer cases.

# Step 1

download the Neuron cells by ECAUGT

`python download.py`

# Step 2

download the query dataset from http://resource.psychencode.org/Datasets/Derived/SC_Decomp/DER-22_Single_cell_expression_raw_UMI.tsv and use the *GeneSymbolUniform_Rtoolkit*(https://github.com/XuegongLab/hECA_GeneSymbolUniform_Rtoolkit) to uniform the gene symbols.

After running the *GeneSymbolUniform_Rtoolkit*, you will get a file 'UniformedExpression.csv' 

# Step 3

follow the `ECAUGT_label_transfer.ipynb` . Notice that some paths need to be changed according to your directory setting.
