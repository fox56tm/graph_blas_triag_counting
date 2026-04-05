import pandas as pds
import scipy as sp

def from_txt_to_mtx(txt_file, mtx_file):

    cr = pds.read_csv(txt_file, sep = '\s+', comment = '#', header = None)

    rows = cr[0].values
    cols = cr[1].values

    vals= [1] * len(cr)

    n = max(rows.max(), cols.max()) + 1

    coom = sp.sparse.coo_matrix((vals, (rows, cols)), shape=(n, n))

    sp.io.mmwrite(mtx_file, coom)

from_txt_to_mtx("data/web-Google.txt","data/web-Google.mtx")

