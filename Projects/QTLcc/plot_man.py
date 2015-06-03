# Copyright(c) 2014, The LIMIX developers (Christoph Lippert, Paolo Francesco Casale, Oliver Stegle)
#
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.

import matplotlib
matplotlib.use('Agg')
import limix.io.genotype_reader as gr
import limix.io.phenotype_reader as phr
import limix.io.data as data
import scipy as sp
import pylab as pl
import pandas as pd
import limix.io.data_util as data_util
from limix.utils.plot import *
import limix.utils.preprocess as preprocess
import limix.modules.qtl as qtl
import limix.stats.fdr as fdr


geno_reader = gr.genotype_reader_tables('Yeast-Genotype.hdf5')
pheno_reader = phr.pheno_reader_tables('Yeast-Phenotype.hdf5')
dataset = data.QTLData(geno_reader=geno_reader,pheno_reader=pheno_reader)
geno = dataset.getGenotypes()
position = dataset.getPos()
pos,chromBounds = data_util.estCumPos(position=position,offset=0)


import sys
import scipy as sp 
import numpy as np
import pdb
import pylab as pl 
import matplotlib.pylab as plt
import scipy.stats as st
import copy
import os

def plot_manhattan(posCum,pv,chromBounds=None,
					thr=None,qv=None,lim=None,xticklabels=True,
					alphaNS=0.1,alphaS=0.5,colorNS='DarkBlue',colorS='Orange',plt=None,thr_plotting=None,labelS=None,labelNS=None):
	"""
	This script makes a manhattan plot
	-------------------------------------------
	posCum			cumulative position
	pv				pvalues
	chromBounds		chrom boundaries (optionally). If not supplied, everything will be plotted into a single chromosome
	qv				qvalues
					if provided, threshold for significance is set on qvalues but pvalues are plotted
	thr				threshold for significance
					default: 0.01 bonferroni correceted significance levels if qvs are not specified,
					or 0.01 on qvs if qvs specified
	lim				top limit on y-axis
					if not provided, -1.2*log(pv.min()) is taken
	xticklabels		if true, xtick labels are printed
	alphaNS			transparency of non-significant SNPs
	alphaS			transparency of significant SNPs
	plt				matplotlib.axes.AxesSubplot, the target handle for this figure (otherwise current axes)
	thr_plotting	plot only P-values that are smaller than thr_plotting to speed up plotting
    labelS           optional plotting label (significant loci)
    labelNS          optional plotting label (non significnat loci)
	"""
	if plt is None:
		plt = pl.gca()

	if thr==None:
		thr = 0.01/float(posCum.shape[0])

	if lim==None:
		lim=-1.2*sp.log10(sp.minimum(pv.min(),thr))

	if chromBounds is None:
		chromBounds = sp.array([[0,posCum.max()]])
	else:
		chromBounds = sp.concatenate([chromBounds,sp.array([posCum.max()])])

	
	n_chroms = chromBounds.shape[0]
	for chrom_i in range(0,n_chroms-1,2):
		pl.fill_between(posCum,0,lim,where=(posCum>chromBounds[chrom_i]) & (posCum<chromBounds[chrom_i+1]),facecolor='LightGray',linewidth=0,alpha=0.5)

	if thr_plotting is not None:
		if pv is not None:
			i_small = pv<thr_plotting
		elif qv is not None:
			i_small = qv<thr_plotting
		
		if qv is not None:
			qv = qv[i_small]
		if pv is not None:
			pv = pv[i_small]
		if posCum is not None:
			posCum=posCum[i_small]

	if qv==None:
		Isign = pv<thr
	else:
		Isign = qv<thr

	pl.plot(posCum[~Isign],-sp.log10(pv[~Isign]),'.',color=colorNS,ms=5,alpha=alphaNS,label=labelNS)
	pl.plot(posCum[Isign], -sp.log10(pv[Isign]), '.',color=colorS,ms=5,alpha=alphaS,label=labelS)

	if qv is not None:
		pl.plot([0,posCum.max()],[-sp.log10(thr),-sp.log10(thr)],'--',color='Gray')

	pl.ylim(0,lim)

	pl.ylabel('-log$_{10}$pv')
	pl.xlim(0,posCum.max())
	xticks = sp.array([chromBounds[i:i+2].mean() for i in range(chromBounds.shape[0]-1)])
	plt.set_xticks(xticks)
	pl.xticks(fontsize=6)

	if xticklabels:
		plt.set_xticklabels(sp.arange(1,n_chroms+1))
		pl.xlabel('genetic position')
	else:
		plt.set_xticklabels([])

	plt.spines["right"].set_visible(False)
	plt.spines["top"].set_visible(False)
	plt.xaxis.set_ticks_position('bottom')
	plt.yaxis.set_ticks_position('left')
