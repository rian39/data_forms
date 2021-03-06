# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

%load_ext autoreload
%autoreload 2

# <codecell>

import ml_lit_anal as ml
import re
import nltk
import pickle
import operator
import google_scholar_parser as gs
import pandas as pd
import networkx as nx
import itertools
import matplotlib.pyplot as plt
import numpy as np
import graph_tool.all as gt

# <codecell>

df = ml.load_records('data/machine_learning_WOS/')
df = ml.clean_topics(df)
df = ml.clean_fields(df)
df.shape

# <codecell>

# loads my handcurated list of techniques
techniques_domains = pickle.load(open('technique_classification.pyd', 'r'))

# <markdowncell>

# # Analysis of decision tree, random forest, neural network and support vector machine 
# 
# The 'motivating intuition' here is that every major technique entails a manner of movement, handling and shaping of data _and_ this manner of movement affects how the technique itself travels or moves around. 

# <markdowncell>

# ## Decision tree analysis
# 
# Hopefully I can do the analysis for decision trees, then just automate it for all the other techniques.
# 
# First of all, just check how they fit with related terms:

# <codecell>

# get the records that keyword decision tree
dt = ml.keyword_years(df, 'decision tree')
print('decision tree: %d'%dt.shape[0])
## get the records that keyword CART
cart = ml.keyword_years(df, 'cart|classification and regression tree|classification tree')
print('CART: %d'%cart.shape[0])
# get the records that keyword C4.5
c45 = ml.keyword_years(df, 'C4.5')
print('C4.5: %d'%c45.shape[0])
rf = ml.keyword_years(df, 'random(.?)forest.?')
print('Random forests: %d'%rf.shape[0])

# <codecell>

#the intersection between these?
indexes = set(dt.index)
indexes.intersection(cart.index)
# very little intersection it seems

# <markdowncell>

# Seems like only a few records overlap.
# 
# ## How do decision tree topics appear over time?
# 

# <codecell>

fig=plt.figure(figsize=(10,4))
plt.subplot(121)
years = (1990, 2012)
plt.hist(dt.PY, bins=20, alpha=0.2, range=years, label='decision tree')
plt.hist(cart.PY, bins=20, range=years, label='cart')
plt.hist(c45.PY, bins=20, range=years, label='C4.5')
plt.hist(rf.PY, bins=20,alpha=0.6, range=years,label='random forest' )
plt.title('Decision tree papers in machine learning literature')
plt.legend()
plt.subplot(122)
plt.hist(df.PY, bins=20, alpha=0.2)
plt.title('Machine learning overall')
plt.show()

# <markdowncell>

# This doesn't mean that there were no decision tree papers before 1990. They have been around longer, but were not presented as part of machine learning until then. And indeed the machine learning literature in general does not take shape until around then. (See the second plot).
# 
# So, did a WoS search just on decision trees and save the 3000 top-cited references. There were around 10,000 returned.  The problem with this search is that it is hard to know whether the decision tree is actually a software or algorithmic decision tree. That is, it might be a medical decision tree. 

# <codecell>

dec_tree_df = ml.load_records('data/decision_tree_WOS/')
dec_tree_df = ml.clean_topics(dec_tree_df)

# <codecell>

plt.figure(figsize=(12,4))
plt.title('Decision tree literature')
x = plt.hist(dec_tree_df.PY, bins=dec_tree_df.PY.max()-dec_tree_df.PY.min())

# <markdowncell>

# OK, this gives a different picture. Now the decision trees are much more numerous, and they span 1965 onwards. They were not developing only in the machine learning literature. They were going elsewhere. Nothing much was happening in them during 1960-1970s. But in the years after 1985, things really become much more active. 

# <codecell>

dec_tree_df[['TI','PY', 'AF', 'TC']][(dec_tree_df.PY<1986) & (dec_tree_df.PY>=1977)]

# <markdowncell>

# Still problems here. Important people like Friedman and Breiman don't appear here. Why not? How are they keyworded? Not by decision tree it seems.
# 
# Might be worth tracking in by different routes. 
# 
# 1. The Morgan-Sonquist citations -- who cited them?
# 2. The Cover-Hart nearest neighbour work -- how does it allow the technique to be renovated?

# <codecell>

morgan_df = ml.load_records('data/morgan_sonquist_WOS/')
figure = plt.figure(figsize=(12,4))
plt.subplot(121)
plt.hist(morgan_df.PY, bins=morgan_df.PY.max()-morgan_df.PY.min())
plt.title('Citations of Morgan and Sonquist 1963')
cover_df = ml.load_records('data/cover_hart_WOS/')
plt.subplot(122)
plt.hist(cover_df.PY, color = 'g', bins=cover_df.PY.max()-cover_df.PY.min())
plt.title('Citations of Cover-Hart, 1967')
figure.remove

# <markdowncell>

# Both Morgan-Sonquist and Cover-Hart show a huge increase in the last decade or so, although on different scales. It would be interesting to see how they intersect.

# <codecell>

set(cover_df.UT).intersection(set(morgan_df.UT))

# <markdowncell>

# ## Decision trees 1985-2000
# 
# I'd like to see what was happening with the topics and applications of decision trees between 1980s-2012. Maybe this is already too late, given that the work on decision trees had been done much earlier. But it is a starting point.

# <codecell>

dec_tree_df[['TI','PY', 'AF', 'TC']][(dec_tree_df.PY<2000) & (dec_tree_df.PY>=1986)].head(10)

# <markdowncell>

# Also, it might be worth looking at the intersection between machine learning decision trees and decision trees in general. How much do they overlap?

# <codecell>

# using WoS ids to do this: df.UT
ml_dt = set(df.UT.unique())
dt_dt = set(dec_tree_df.UT.unique())
print("""there are %d references to decision tree articles in the machine learning literature;
even though there are at least %d articles in the machine learning set on decision trees"""
      %(len(dt_dt.intersection(ml_dt)), dt.shape[0]))

# <markdowncell>

# This difference -- 309 vs 513 -- could be because the decision tree dataset is not complete. In any case, it supports the conclusion that much of the decision tree has not been labelled as 'machine learning.'

# <markdowncell>

# # Analysis of techniques in the decision tree literature

# <codecell>

# get all the techniques from my list of techniques 
techniques = [key for key, value in techniques_domains.iteritems() if value == 'y']

# find all the domains/topics in the list of decision tree topics that are not techniques
dt_topics = df.topics.ix[dt.index]

def remove_techniques(x):
    return [top for top in x if top not in techniques]
dt_topics = dt_topics.apply(remove_techniques)
dt_df = df.ix[dt_topics.index].groupby(df['PY'])
dt_df


# <codecell>

ml.term_year_network(dt, 'decision tree', 1980, 2000, (18,18), plot=True)

# <codecell>

dt_nx_2004 = ml.term_year_network(dt, 'decision tree', 2000, 2004, (19,10))

# <codecell>

dt_all_g = ml.coword_network_fast(dt, 1990, 2000)

# <markdowncell>

# ## Random forest
# 
# How do they get taken up?

# <codecell>

rf_df = ml.keyword_years(df, 'random forest.?|randomForest.?')
rf_df.head()

# <codecell>

plt.figure(figsize=(12,3))
plt.hist(rf_df.PY, bins=11)
plt.title('Random forests in machine learning')

# <codecell>

ml.term_year_network(rf_df, 'random forest', 2007, 2008)

# <codecell>

ml.term_year_network(rf_df, 'random forest', 2011, 2012, (18, 20))

# <markdowncell>

# # Support vector machine
# 
# Trying to see how this literature takes shape

# <codecell>

svm_df = ml.keyword_years(df, 'support vector|support vector machine.?|svm|support vector network.?')
svm_df.shape

# <markdowncell>

# SVMs contribute a substantial portion of the growth in SVM during the last decade. They dwarf random forests. 

# <codecell>

plt.figure(figsize=(12,5))
plt.subplot(121)
plt.title('Support vector machine publications')
x,y,z = plt.hist(svm_df.PY, color='g',bins  = svm_df.PY.max() - svm_df.PY.min(), 
                 label= 'SVM', alpha=0.65, hold='on')
x,y,z = hist(rf_df.PY, color='r', label='random forest')
plt.plot(y[:-1],x, linewidth=2)

plt.subplot(122)
bins = 2013-1998
plt.hist(svm_df.PY,color='g', bins = bins, hold='on', label='SVM', range=(1998,2013))
plt.hist(df.PY, alpha=0.5, color='y', label='all', bins = bins,  range=(1998,2013))
plt.xlim(1998, 2013)
plt.legend()
plt.title('SVM against all machine learning publications')

# <markdowncell>

# Cortes is meant to be one of the most highly cited papers in the literature. Some sign of that. 

# <codecell>

cortes_cit = ml.find_citation(df, 'Cortes 1995')
cortes_cit.shape

# <codecell>

cortes = gs.ScholarQuerier(author = 'Corinna Cortes', count=50)
res = cortes.query('')

# <codecell>

type(cortes) ## not working

# <codecell>

cortes_df = ml.find_author(df, '(Cortes)|(Vapnik)')
cortes_df.shape

# <codecell>

cortes_topics = ml.keyword_counts(cortes_df).keys()

# <codecell>

c1 = ml.coword_network(cortes_df, 1995, 2013, 200)

# <codecell>

plt.figure(figsize=(15,15))
plt.title('Corinna Cortes topics')
nx.draw_graphviz(c1, with_labels=True, 
                 alpha = 0.7,
                 node_color = 'y',
                 width=0.3,
                 font_size=11,
                 labels = nx.get_node_attributes(c1, 'topic'))

# <codecell>

cortes_nx = ml.coword_network(cortes_df, 1995, 2012, 500)

# <codecell>

plt.figure(figsize=(12,10))
plt.title('Corinna Cortes topics')
nx.draw_graphviz(cortes_nx, with_labels=True, 
                 alpha = 0.7,
                 node_color = 'y',
                 width=0.3,
                 font_size=11,
                 labels = nx.get_node_attributes(cortes_nx, 'topic'))

# <markdowncell>

# But I don't see Cortes and Vapnik, 1995 here. That is the important paper, published in the journal _Machine Learning_. What happened to it?

# <markdowncell>

# ## Network analysis of SVM literature
# 
# 
# There are around 4000 keywords in the literature. 

# <codecell>

svm_df_lim = svm_df.ix[svm_df.PY <2006]
svm_df_lim.shape

# <codecell>

def term_year_network(svm_df, topic, start, end, size = (18,18)):
    svm_nx = ml.coword_network(svm_df, start, end)

    svm_cow = nx.to_numpy_matrix(svm_nx)
    topics = nx.get_node_attributes(svm_nx, 'topic')
    eigen = nx.eigenvector_centrality(svm_nx)
    #[(i[0], svm_nx_2004.node[i[0]].values()) for i in ml.sorted_map(eigen_2004)[:20]]
    class_nx = nx.ego_graph(svm_nx, nxkey_for_topic(topic, topics), undirected=True, radius=20)

    ml.plot_co_x(class_nx, start, end, size)
    return class_nx

# <codecell>

def nxkey_for_topic(topic, topics):
    return [k[0] for k in topics.items() if k[1] == topic][0]

# <markdowncell>

# ## SVM: pre-2000

# <codecell>

svm_nx_2000 = ml.coword_network(svm_df, 1995, 2000)
svm_2000_cow = nx.to_numpy_matrix(svm_nx_2000)

# <codecell>

topics_2000 = nx.get_node_attributes(svm_nx_2000, 'topic')
eigen_2000 = nx.eigenvector_centrality(svm_nx_2000)
[(i[0], svm_nx_2000.node[i[0]].values()) for i in ml.sorted_map(eigen_2000)[:20]]

# <codecell>

key_for_topic('support vector machine', topics_2000)

# <codecell>

# plot ego graph for svm
term_year_network(svm_df, 'support vector machine', 1995, 2000, (5,5))

# <markdowncell>

# ## SVM: year by year

# <markdowncell>

# ## SVM: 2000-2

# <codecell>


svm_nx_2002 = term_year_network(svm_df, 'support vector machine', 2000, 2001, (10,10))

# <codecell>

svm_nx_2002 = term_year_network(svm_df, 'support vector machine', 2001, 2002)

# <codecell>

term_year_network(svm_df, 2001, 2002, (12,12))

# <codecell>

svm_year_plot(svm_df, 2002,2003)

# <codecell>

svm_year_plot(svm_df, 2003, 2004)

# <codecell>

svm_nx_2013 = term_year_network(svm_df, 'support vector machine', 2012, 2013)

# <codecell>

term_year_network(svm_df, 'support vector machine', 2004, 2005)

# <codecell>

svm_year_plot(svm_df, 2005,2006)

# <markdowncell>

# ## SVM: 2004-6

# <codecell>

#looking at 2000 top topics for the moment
svm_nx_2006 = ml.coword_network(svm_df, 2004, 2006, 2000)

svm_2006_cow = nx.to_numpy_matrix(svm_nx_2006)

# <codecell>

topics_2006 = nx.get_node_attributes(svm_nx_2006, 'topic')
eigen_2006 = nx.eigenvector_centrality(svm_nx_2006)
[(i[0], svm_nx_2006.node[i[0]].values()) for i in ml.sorted_map(eigen_2006)[:20]]

# <codecell>

# ego network for svm
class_nx = nx.ego_graph(svm_nx_2006, n=0, center=True)
ml.plot_co_x(class_nx, 2004, 2006, (20,20))

# <codecell>

svm_nx_2006_trim = ml.trim_degrees(svm_nx_2006, 1)
len(svm_nx_2006_trim.nodes())

# <codecell>

svm_nx_2006_trim = ml.trim_edges(svm_nx_2006_trim,2)
svm_nx_2006_trim = ml.trim_degrees(svm_nx_2006_trim, 2)

# <codecell>


ml.plot_co_x(svm_nx_2006_trim, 1995, 2006, (18,18))

# <codecell>

ml.sorted_map(nx.betweenness_centrality(svm_nx))

# <markdowncell>

# ## SVM: 2007-8

# <codecell>

svm_nx_2008 = ml.coword_network(svm_df, 2007, 2008)

# <codecell>

svm_nx_2008.number_of_nodes()

# <codecell>

topics_2008 = nx.get_node_attributes(svm_nx_2008, 'topic')
eigen_2008 = nx.eigenvector_centrality(svm_nx_2008)
[(i[0], svm_nx_2008.node[i[0]].values()) for i in ml.sorted_map(eigen_2008)[:20]]

# <codecell>

class_nx = nx.ego_graph(svm_nx_2008, 532)
#class_nx = nx.ego_graph(svm_nx, 1449)
ml.plot_co_x(class_nx, 2006, 2008, (15,15))

# <markdowncell>

# # Experiments with inclusion, proximity and equivalence scores

# <codecell>

## try inclusion matrix
svm_2006_cow_inc = ml.inclusion_matrix(svm_2006_cow)

# <codecell>

#svm_2006_cow_inc[np.isnan(svm_2006_cow_inc)]=0

# <codecell>

#set diagonal to zero 
np.fill_diagonal(svm_2006_cow_inc,0)

# <codecell>

inc_edges = ml.inclusion_matrix_to_edge_weights(svm_2006_cow_inc)
nx.set_edge_attributes(svm_nx_2006, 'inclusion', inc_edges)

# <codecell>

inc_edges_sorted = ml.sorted_map(inc_edges)

# <codecell>

{(topics_2006[x[0]], topics_2006[x[1]]):v for x,v in inc_edges_sorted[:30]}

# <codecell>

# draw graph of most inclusive nodes

elarge=[(u,v) for (u,v,d) in svm_nx_2006.edges(data=True) if d['inclusion'] ==1]

# <codecell>

svm_2006_nx_inc = nx.Graph(elarge)

# <codecell>

svm_2006_nx_inc.number_of_edges()

# <codecell>

svm_2006_nx_inc.number_of_nodes()

# <codecell>

labels_inc = {n: topics_2006[n] for n in svm_2006_nx_inc.nodes()}

# <codecell>

plt.figure(figsize=(15,15))
nx.draw_graphviz(svm_2006_nx_inc, 
                 with_labels = True,
                 labels = labels_inc,
                 node_size = [s for s in nx.betweenness_centrality(svm_2006_nx_inc)],
                 width=0.3,
                 alpha=0.4)

# <codecell>

np.unravel_index(svm_2006_cow_inc.argmax(), svm_2006_cow_inc.shape)

# <codecell>

np.where(svm_2006_cow_inc == 1.0)[0].shape

# <codecell>

most_inclusive_node = nx.ego_graph(svm_nx_2006,11,5)

# <codecell>

topics[845]

# <codecell>

plt.figure(figsize=(15,15))
nx.draw_graphviz(most_inclusive_node, with_labels = True, labels = nx.get_node_attributes(most_inclusive_node, 'topic'))

# <codecell>


