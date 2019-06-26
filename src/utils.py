import matplotlib


"""
Utils file storing parameters
"""

# maximum and minimum number of clusters
min_cl = 3
max_cl = 15

# number of iterations for clustering
n_iter = 100
# percentage subsampling for clustering
subsampl = 0.8

# glove parameters
n_epoch = 1
batch_size = 5

# dimension of SVD and word embeddings
n_dim = 10

# vocabulary and behavioral ehr file names
file_names = {'vocab': 'cohort-vocab.csv',
              'behr': 'cohort-behr.csv'}

# models to validate
model_vect = {'0': ['tfidf', 'glove'],
              '1': ['tfidf', 'glove'],
              '2': ['tfidf', 'glove'],
              '3': ['tfidf', 'glove'],
              '4': ['tfidf', 'glove', 'feat']}

# colors for visualization
col_dict = matplotlib.colors.CSS4_COLORS
c_out = ['bisque', 'mintcream', 'cornsilk', 'lavenderblush', 'aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'azure',
         'beige', 'powderblue', 'floralwhite', 'ghostwhite', 'lightcoral', 'lightcyan', 'lightgoldenrodyellow',
         'lightgray', 'lightgreen', 'lightgrey', 'lightpink', 'lightsalmon', 'lightseagreen', 'lightskyblue',
         'lightslategray', 'lightslategrey', 'lightsteelblue', 'lightyellow', 'linen', 'palegoldenrod', 'palegreen',
         'paleturquoise', 'palevioletred', 'papayawhip', 'peachpuff', 'mistyrose', 'lemonchiffon', 'lightblue',
         'seashell', 'white', 'blanchedalmond', 'oldlace', 'moccasin', 'snow', 'darkgray', 'ivory', 'whitesmoke']

