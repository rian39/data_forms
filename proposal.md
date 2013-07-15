
# Book Proposal

## In the data: modes of machine thought

Adrian Mackenzie
Sociology, Lancaster University
Bailrigg, LA14YD, UK

## Overview


>The key question isn't 'How much will be automated?' It's how we'll conceive of whatever _can't_ be automated at a given time. Lanier, _Who Owns the Future_, 2012, 77

In recent years, a really marked trend towards aggregation of data ('big data,' 'data-intensive research') has been easy to see in many different settings. Responding to the many promises about the scientific, commercial, political, and financial uses of data (such as the former _Wired_ editor Chris Andersons 'end of theory' [@anderson_end_2008], a fairly broadly skeptical set of responses coming from scientists, social scientists and humanities scholars point to some of the problems with over-commitment to digital data as the answer to all questions. They also suggest that the opacity of data practices pose significant ethico-political problems. 

This book sets out to develop some ways of thinking about data that neither blithely affirm beliefs in the power of data, nor reject beliefs in data as pure hype. It seeks to do this  on terrain that lies close to the centres of contemporary data practices: *machine learning.* Machine learning is a widely used way of programming computers to find patterns, associations, and correlations, to classify events and make predictions on a large scale. Machine learning, as a set of techniques for classifying and predicting, lies close to centre of calculation in the contemporary data economies. Machine learning is heavily used in search engines, social network media, high-frequency trading, and many scientific fields. Examining  key machine learning techniques and practices drawn from social network media, finance markets, image processing, robotics, and contemporary sciences such as genomics and epidemiology, _In the data_ describes who does machine learning, where and how. 

Importantly, *In the Data* is an experiment in writing for humanities and social science audiences that combines code, data and diagram, text, and number with the goal of imagining doing machine learning differently. In both analysing and re-purposing techniques found at the intersection of contemporary sciences and network media, *In the Data* attempts to both make potent data practices more visible, and to facilitate greater  overlaps and entanglements between various science and political, economic and cultural processes associated with data. 

### Key concerns for the book are:

- The modes of existence of data  (in the forms of 'big data,' 'open data,' the rise of 'data analytics' and 'data science') should be analysed critically by situating them in relation to specific settings, techniques and practices. These settings, techniques and practices have complex genealogies, criss-crossing sciences, industries, military, commercial and governmental domains. Both the provenance and distribution of data practices such as learning algorithms, predictive modelling and classification need critical attention. This book focuses on the role of machine learning (or data-mining, as it is called in some domains).

- Humanities and social science responses to data techniques should be methodologically and conceptually inventive, and include appropriation and re-purposing of the techniques and practices. This is major undertaking for the book. It seeks to a broad-ranging way of thinking about data, and what is 'in data' that both soberly appraises beliefs about data, and offers ways of evaluating what is at stake in data in various settings. 
	
### Approaches used in the book

A broad ethico-political concern underpins *In the Data*. Much contemporary data practice is closely allied to the predictive ambitions of business, the military and states, as well as sciences and media. The recent upswing in data talk continues and intensifies the technoscientific 'Regime of Computation' [@hayles_my_2005]. It is no accident that autonomous mililtary vehicles, large-scale analysis of sentiment social media for commercial or security purposes, or face recognition for national border control are iconic examples of machine learning in action.  A key question for critical humanities and social science researchers, as well as activists, non-government groups and civil society actors of many kinds, is how to make sense of such data practices. They are hard to render visible since they take place largely on platforms that are not publicly accessible. Rendering such practices visible, learning to track their workings, and inventing different ways of working with them: these concerns lie at the core of the analytical and experimental writing practices of *In the Data.* 

Broadly speaking, the writing seeks to respond to the long-standing call for what in a widely cited passage Donna Haraway more than a decade ago termed 'diffraction': 'What we need is to make a difference in material-semiotic apparatuses, to diffract the rays of technoscience so that we get more promising interference patterns on the recording films of our lives and bodies' [@haraway_modest_witnesssecond_millennium_1997, 17]. There are a growing number of  attempts to adapt and reinvent data practices such as machine learning for less overtly biopolitically laded, security-minded or commercially-motivated purposes (see the 'OccupyData' group in New York, N.Y. for one such example [@occupydata_occupy_2013];  many citizen science projects have something of this flavours to them too). Some of these will be discussed in the course of the book. 

In order to bring data, code, images and text together more fluidly, the book relies on some straightforward 'executable paper' formats developed in recent scientific publishing. It mingles code written in  [R](http://cran.r-project.org/), the statistical modelling, data manipulation and visualization programming language, with code written in Python and Javascript, two of the most popular general programming languages in use today. Much of the empirical content of the book has been garnered, ordered, analysed and displayed using R, Python and Javascript. Not all of the code used in this process is printed (to avoid long printouts), although certain key portions of the code form part of the text, and will be the object of commentary and analysis, alongside diagrams and graphs generated by the code. All of the code will be available at a public code repository (github.com). 

The motivation for the executable format of this book is partly ethnographic and partly experimental. A long line of ethnographers have learned to do what they  are observing (as in 'observant participation' [@wacquant_body_2004]). This has include working in factories, going to prison, spending time in isolated, far-flung or ostensible boring places,   learning techniques ranging from weaving and cooking to playing the piano or programming robots. Ethnographic presence in a particular setting is normally documented through text, photographs, diagrams and occasionally film or audio recordings, and aims to make sense of this setting in ways that both resonate with the people who live there and with people who don't. The forms of observant participation in this book include competing in machine learning competitions, reconstructing and implementing algorithms,  building predictive models and  visualization as a way to present machine learning. It treats reading and writing code as an ethnographic practice, and code as part of the ethnographic writing process. Hence forms of data practice used in producing this book are also the objects of its analysis.  Several versions of this recursivity will appear in the chapters.  

The experimental character of this writing entails both practical and theoretical challenges. Practically, the book experiments with a range of code constructs, some key mathematical formulae as well as data tables and data graphics. Such constructs are not typically found in humanities and qualitative social science research, although they are extremely common in many scientific fields. The presence of code, formulae and graphics in *In the Data* is not meant to instruct readers in machine learning algorithms or statistical inference. Accompanied by forms of explication and commentary, they are intended to allow  readers to pay close attention to the forms of thought at work in the manifold data practices of sciences or business analytics, and to begin to borrow, appropriate and re-purpose some of the patterns of thought for different purposes. The theoretical ambition here is to treat the code writing also as a way of constructing concepts, metaphors and ways of speaking about contemporary entanglements of subjectivity and computation.  


## The architecture of the book 

The book is organised around two different axes. 

1. On one axis, the 'technique axis,' the chapters of the book catalogue, document and analyse  some of the most  widely used machine learning techniques of working with data [@hastie_elements_2009]. The techniques analysed on this axis -- linear regression models, decision trees, clustering algorithms, Markov Chain Monte Carlo simulation,  neural networks and support vector machines -- are used across scientific, industrial, biomedical, commercial and military settings. Their extraordinary success in populating these domains cannot be explained in terms of IT or digitisation in general. The case studies explore how these techniques, and their implementation as 'learning algorithms,' rely on widely shared assumptions about the problems of knowing, acting, responding or predicting how things happen. To the extent that a situation can be reshaped to conform to these assumptions, these techniques gain traction. 

2. The other axis of the book is 'recursive reconstruction:' the attempt to show how specific situated entanglements of subjectivity and data practice might open up different ways of thinking about contemporary experience as it is increasingly pervaded and subtly (or not subtly) modulated by data-driven processes. Along this axis, chapters of the book engage with the messiness, complications, and frictions of working with datasets, with predictive models and forms of visualization ranging from standard plots of curves to  network graphics. The diagrams, functions and code constructs arrayed along this axis are drawn from scientific fields, or  from commercial applications where data is made available through APIs (Application Programmer Interfaces). The reconstruction of data practices draws on the pragmatist philosopher John Dewey's notion of philosophy as an empirical reconstruction of experience [@dewey_reconstruction_1957; @dewey_essays_2004]. The kinds of experience reconstructed range from encounters with databases, with stream of numbers of varying kinds, with statistical predictions, with various engines that classify, recommend or in general find patterns. Each chapter seeks to address a facet of this. At various points, these reconstructive moves will be linked to broader debates around politics, ethics, publics, democracy, power, equality and differences.

## Existing academic literature and framing of the book

The existing literature relevant to this monograph come from a variety of disciplines. The critical work on data is largely found in science and technology studies (STS), and some parts of information science. Software studies and anthropological accounts of software cultures are highly relevant in reading machine learning algorithms and data visualization software. A broader theoretical background here includes recent reappraisals of pragmatism (particularly William James, C.S Peirce), feminist and other work on materialities, as well as strands of largely European contemporary philosophy relating to experience, space-time, science, calculation and events. A final reference point comes from recent attempts in social sciences and humanities to reinvent methods of research. 

In STS, work on calculation [@callon_qualculation_2005], data practice [@edwards_science_2011],  databases [@bowker_memory_2005] and digital data more generally [@latour_whole_2012] have extensively discussed how science assembles numbers, observations, instruments, readings and databases. This work forms an important part of the background of this book since machine learning has heavy mathematical underpinnings and institutional dynamics. The STS work  has broadly re-theorised many different aspects of data, ranging across collection, measurement, calculation, archiving, labelling and visualising. Much of this work is based on ethnographic case studies of laboratories, technical devices, standards and controversies. It has notably developed ways of analysing its objects relationally (as in actor-network approaches), and with an eye on entanglements and hybridisation of human and non-human entities. While _In the Data_ is not by any means a standard laboratory ethnography, it does rely on practices of participant observation and  analytical approaches found in STS. 

The history of statistics, number and mathematics also frame important aspects of _In the Data_. Works such as Theodore Porter's _Trust in Numbers_ [@porter_trust_1996], Lorraine Daston's work on probability [@daston_classical_1988],  or Alain Desrosiere's _The Politics of Large Numbers_ [@desrosieres_politics_1998] amongst others not only provide background for many of the statistical techniques used in machine learning, they suggest that numerical data and numbers have had an eventful course of development from the 18th to the 20th century. While much of this historical work leaves just around the time when machine learning approaches are emerging (1960-1970s), it provides an extremely useful way to contextualise key traits in the contemporary data practice, ranging from genres of visualization to underlying concepts of probability, chance or error.

The nascent field of software studies has begun to develop ways of analyzing software and code, ranging from source code files to large assemblages. Coupled with media studies and media archaeology-type approaches, software studies has developed geneaologies, critical framings and methods of reading many different aspects of software. Work in this field ranges from quite high-level analyses such as Wendy Chun's _Programmed Visions_ [@chun_programmed_2011] or Lev Manovich's _Cultural Software_ [@manovich_cultural_2011], or Alex Galloway and Eugene Thacker's work [@galloway_exploit_2007] through to studies of specific code objects (as for instance in many of the entries in the _Software Studies: A Lexicon_ volume [@fuller_software_2007]) or analysis of code as speech [@cox_speaking_2012]. Other work should be included here (along with related work on 'platform studies'), but for present purposes, the key influence of software studies consists in its treatment of software, computer code, algorithms and protocols as first-ranking objects of social and cultural analysis. 

A broader range of theoretical approaches informs this book. These include on events, materiality, experience, and capitalism from scholars that include Brian Massumi on radical empiricism [@massumi_too-blue_2000], Nigel Thrift on time-space signatures of calculation [@thrift_knowing_2005], Celia Lury on topological conceptions of culture [@lury_introduction_2012], Manuel Delanda on simulation in philosophy and social science [@delanda_intensive_2002; @delanda_philosophy_2011], Anna Munster on conjunctive experience in networks [@munster_aesthesia_2013], or Luciana Parisi on the contagiousness of computation [@parisi_contagious_2013]. Many of these authors share an interest in re-thinking notions of experience, body, event, time-space and materiality in the context of ongoing transformations of media and technology. Many of them draw on philosophers such as William James or A.N. Whitehead to question taken-for-granted concepts of nature, life or agency. Again, this loose coalescence of work cannot be adequately summarised or even limned here, but it indicates something of the theoretical registers on which _In the Data_ will work. 

The final framing body of work is even less coherent, but nevertheless quite important: it largely comprises threads of research and debate about methods today in social sciences and humanities. This literature tends to treat the growth of digital data as both posing a problem and an opportunity for research in social sciences and humanities. The problem, as framed by sociologists such as Andrew Abbott [@abbott_time_2001] or Mike Savage [@savage_contemporary_2009],is that existing quantitative methods in social science cannot match the efficacy of quantitative methods in the natural or applied sciences, nor those used in business and marketing (e.g. as in analysis of transaction data). Some social scientists advocate the development of 'computational sociology' [@king_ensuring_2011]. A version of the same crisis can be found in digital humanities, and has prompted developments such as 'cultural analytics' [@manovich_cultural_2009]. Commonly, these responses advocate a pattern-based approach to working with social or cultural data, and in this respect, they mirror some of the commitments in machine learning to finding the function that generates the data. Whilst very sympathetic to and in some ways aligned with these debates, _In the Data_ also aims to offer something other than  a new set of 'better' methods. 


## Market

The market for the book is quite diverse, since data practices and indeed machine learning itself are of  interest to a growing audiences. One set of readers I have in mind for the book come from disciplines such as sociology, anthropology, media and cultural studies, and social geography who are grappling with the promise of data. Another set of readers for the book come from the burgeoning 'data science' courses being offered in North American, UK, SE-Asian/Pacific, and European universities. While these courses are largely focused on techniques of organising, visualising and modelling data, many of them are also open to thinking about the transformations in knowledge and value associated with contemporary data practice. The book is written very much with these kind of readers in mind. It will be relatively lightly-written in relation to social theory in order to facilitate their access. 


## Timetable

Many of the chapter exist in draft form, or as conference papers. Writing an introduction, conclusion, and revising the drafts will take roughly 11 months.
- draft conclusion: 1 month
- draft introduction: 1 month
- draft chapter 2: 2 months
- revise chapter 3,4,5,6,7,8 drafts: 3 months
- revise chapter 2: 1 month
- revise whole manuscript: 3 months
I'd like to deliver the whole manuscript mid-2014.

### Format of the book

The book has a standard chapter format. It will include several dozen code-generated figures, diagrams or plots, as well as a number of tables. The Python and R code, and datasets used to generate these components of the text will be available through the public code repository github.com. The Markdown text of the book will be also part of this code repository. Electronic versions of the book will display colour versions of the plots, and be hyperlinked to both the code-data components on github, and to various relevant URLs. The predicted wordcount is 85,000.

## Chapter outline

### 0. Introduction: into data

#### Key examples: Eulerian motion pulse detection; kittydar and cat detection; DARPA challenges


The introduction will begin with a several relatively straight-forward and accessible  examples drawn from a variety of fields over the last decade or so -- handwriting recognition, face recognition, social media trend 'nowcasting', finance, autonomous robots [@thrun_stanley_2006], and cancer prognosis. It will highlight these examples as symptoms of the wide-ranging investments in knowledge, control, prediction and decision-making associated with data flows, and at the same time, suggest how these tracking some of the transformations might elicit changes in how humanities and social science researchers understand their own work. 

The entry point for the wider questions in the book will come from burgeoning debates about the promise of data. These include the notorious 'end of theory' prediction (Chris Anderson, _Wired_ magazine, 2008), and the many claims and controversies about data analytics, machine learning and the 'power of big data.' In broad terms, the  themes of 'in the data' and  'modes of machine thought' will be characterised, drawing on a range of work drawn from pragmatist philosophers such as C.S. Peirce (abduction and diagrams), William James on experience [@james_essays_1996],  John Dewey on 'reconstruction' [@dewey_reconstruction_1957], Alfred N. Whitehead on 'abstraction' [@whitehead_modes_1958] and from recent social and cultural theory  such as Isabelle Stengers on experiment [@stengers_experimenting_2008]; Gilles Deleuze & Felix Guattari on scientific functions, and [@deleuze_what_1994]; Celia Lury on topology [@lury_introduction_2012]). In order to contextualise forms of data thought, the introduction will also sketch some points of departure drawn from software studies work on algorithms and databases, science studies work on calculation, statistics, number, device, image and diagram, , as well as accounts of subjectivity, experience [@berlant, 2007] or [@murphie, 2010] and materiality cross-cutting all of the above. This spectrum of work from across disciplines provide  scaffolding and departure points for much of the book. 


Finally, the introduction will also provide a preliminary overview of the techniques of machine learning discussed in the book -- clustering, linear modelling, Bayesian inference, etc -- but very much with a view to exemplifying  the   of the book concerning data as a material-semiotic entity: dimensioning, diagrams and mapping, generating and discriminating, convolution and multiples, optimality and predictivity.   

### 1. Associating with data: classifiers and predictions

#### Key examples: Pfizer's 'discovery' of Viagra; R programming language as the 'Magna Carta' of analytic rights; Python scikit-learn & pandas; the Titanic survivors;

#### Key techniques: perceptrons, stochastic gradient descent, decision trees


This chapter is primary a methodological discussion, in the form of a series of vignettes that display some of the ways in which research and writing critical accounts of data cultures and data economies can make use of the tools, techniques, instruments and services of 'data science' to generate textual, diagrammatic and modelised accounts of contemporary culture.  The vignettes come from either the author's own history of working with machine learning or online accounts of machine learning, set against the background a particular software ecology, associated with the statistical programming language R. 

Via a discussion of the development of R, the chapter analyses the  transverse, cross-disciplinary moment of machine learning methods in recent decades. It describes some of the transformations in software, network and scientific cultures that underpin the recent growth in data techniques and methods. These range across transformations in statistical science associated with greater computational capacity; the mutations in network,  database and digital device architectures and infrastructures that yield much greater abundance of data in various forms; and the intermeshing of knowledge economies with the media, communication, transaction, transport and logistics systems. It will trace how the lateral associations and multivalencies of data have developed through key software artefacts such as the widely used R programming language, and in generic programming languages such as Python.

Finally, this chapter is somewhat autoethnographic too, in that it reports on the author's own trajectory through coding competitions, online and face-to-face 'machine learning' courses, as well as more broadly on various forms of database and visualization practices. 


### 2. From straight lines to curved surfaces

#### Key examples: housing price prediction; cancer prognosis; digit recognition
#### Key techniques: logistic regression; _k_-nearest neighbours

-- recursion, movement, evocative objects, partial observers, visualisation, etc; functions and states of things; linear regression

Graphs and plots stand at the centre of vision in contemporary data and knowledge economies, whether in the time series plots of financial markets, the scatter plots of scientific publications or the network graphs of social media. The topography of curves, lines, points and network diagrams present views of data, and they are indispensable to many of the classification, decision and prediction techniques of machine learning. Such visual forms, with all their associate aesthetics (code, line, typography, animation) are themselves convey expectations and predictions about the changes in the data practice, especially in the form of the curves showing growth of data.  


```r
source("animations/grad_desc.R")
grad_desc()
```

<video   controls="controls" loop="loop"><source src="figure/gradient_descent.mp4" type="video/mp4" />video of chunk gradient_descent</video>

```r
# library(animation)
saveLatex(grad.desc())
```


This chapter examines the proliferation of data-supported curves and lines in terms of *functions*, the underlying generating mechanisms of curves. Machine learning is conceptually framed as a form of function-finding. Drawing on statistical machine learning texts [@hastie_elements_2009], and more philosophical accounts of functions (e.g. [@deleuze_what_1994; @whitehead_modes_1958]), the chapter  introduces the key instances of the function in machine learning, shows how functions underpin the generation of curves, and how movement along lines, curves and across planes. While later chapters will range across a variety of mathematical functions and forms, this chapter will focus on two of the most widely used machine-learning technique, linear regression model and its classifier version, logistic regression model, and the _k_ nearest neighbour algorithm. It will discuss these important techniques from the perspective of the forms of relationality, referenciality and indexicality associated with them. 

Connecting aesthetic and mathematical data practices, this chapter suggests that finding the functions that generate lines and surfaces in data is a powerful form of imitation that tends to remake the world in certain ways. This re-making may be inimical to social life, or not. The chapter also suggests that the production of curves through software packages and libraries and through various visualization techniques is worth investigating as a signifying social practice in its own right. The architecture and practices associated with graphics and plotting libraries offer a way to trace some of the processes of imitation and invention associated with forms of data thought. 

### 3. Patterns in the data: dimensional exuberance

#### Key examples: hunch.com; 
#### Key techniques: k-means, neural networks,  support vector machines
:  regularisation - dimensional reduction, dimensional explosion -- infinite dimensional spaces; recommender engine - svd as well; ebay; hunch.com

For the last decade, the best-performing 'off-the-shelf' machine learning algorithm has been a technique known broadly as 'support vector machines' (SVM; see [@vapnik_nature_1999]). The chapter examines the architecture of this widely used algorithm both against the background of a spectrum of other statistical machine learning techniques, and more importantly, in terms of the *forms of movement* it brings to data practice. The key focus in this discussion is the dimensionality of data, and how dimensionality is managed in machine learning.  While curves and functions, as discussed the previous chapter, engender senses of change and movement, the advent of increasingly extended and particularly 'wide' datasets (many variables) implies models that embrace high-dimensional abstract spaces. Since the 1950s, scientists  have been aware of the 'curse of dimensionality' [@bellman, TBA], which arises when the dimensions of the data increase. Algorithms such as SVM, and implicitly other highly successful ML algorithms such as neural networks, manage this dimensionality very differently to the regression models that have been the mainstay of statistical modelling for a century. Rather than trying to reduce the dimensionality of the model to a line, plane or hyperplane that best fits the datasets, SVM expands the dimensionality  of the model massively, sometimes infinitely.


### 4. Cruel optimisation and algorithmic competition

#### Key examples: spam filter; Kaggle facebook retention; Kaggle R recommendation engine; TopCoder; Sage Bionetworks
#### Key techniques: ensembles, RandomForests

 - selfhood in Kaggle and Google compute - random forest; aggression, competition, and optimisation in the algorithmic

The chapter focuses on the forms of subjectivity associated with contemporary data practice, situated within  plural data and knowledge economies. Software developers, hackers, statisticians, 'data scientists,' as well as social scientists, are changed by forms of data thought.  The case study in this chapter is data prediction contests run by the [Kaggle.com](kaggle.com) as well as academic-based competitions. In these competitions, competitors from diverse technical and geographic backgrounds compete to construct predictive models for specific datasets -- the Netflix recommendation competition; the Facebook 'find a friend' competition; or the Titanic survivor problem -- using whatever machine learning techniques they can bring to bear. These competitions, conducted on web-based platforms, are useful ways to track contemporary data practices. Combined with some examples of presentations by academic researchers (for instance, Stanford University's Andrew Ng whose YouTube lectures haved attracted 100,000s of views), industry conferences (for instance, at the annual Predictive Analytics World events), this chapter will track the kinds of technical and affective investment associated with popular data modelling techniques such as Random Forest. It is possible, I will suggest, to read a technique as a partial subjectification, in that it affects how they experience and materially engage with data. In order to apprehend the character and texture of these subjectifications, the chapter links university research, commercial and non-commercial adoption, and flows of technical expertise. Again, this chapter has some auto-ethnographic vignettes, as the author has participated in some of these competitions. 

    
### 5. Belief and desires in data

#### Key examples:  Microsoft TrueSkill; Obama election data team
#### Key techniques: Monte Carlo simulations and MCMC; Bayesian networks; 


 - probability and Bayesian inference - belief and desire in data  - belief chance, Bayes, internal proliferation of numbers; event-belief oscillation

The topic in this chapter is the so-called 'Bayesian revolution' in statistical practice that took shape in the early 1990s, and in particular, the key algorithmic technique used in Bayesian statistics, Markov Chain Monte Carlo simulation (MCMC). The computationally intensive techniques of Bayesian analysis treat all numbers as potentially random variables; that is, as best described by probability distributions. The ensuing popularity of Bayesian inference is a striking example of transverse momentum of methods across fields, and the chapter will trace some of the ramifications of the heavily-used MCMC technique in fields ranging from nuclear physics, image processing to political science and epidemiology. 

The chapter traces two important implications of this technique. First, because it is so computationally intensive, MCMC and Bayesian inference, although statistically powerful, are difficult to apply to many dimensional datasets. So Bayesian computation iconically figures the limits of contemporary data practices, with their ambitions to incorporate all available data into calculation. Second, in certain ways this technique challenges us to re-evaluate how we think about numbers. By following some of the ways numbers circulate through MCMC algorithms, we can discern to a semiotic-material faultline running through contemporary number formations. Numbers semiotically and materially embrace both events and degrees of belief. If numbers are crucial in the data economy, then instabilities in their mode of existence will affect much of what happens to data. While much of the machine learning taking place in commercial and operational settings is decidedly non-Bayesian, the popularity of MCMC and Bayesian approaches in contemporary sciences suggests a tension in what counts as number.

### 6. Contagious number flows

#### Key examples: A/H1N1, Google Flu;
#### Key techniques: transmission models, nested models

  - functions & supply chains; APIs; multiplication & convolution; states and functions of the lived;

A predominant narrative around data in many contemporary settings urges that more data makes all problems solveable. This narrative is usefully accompanied by an 'abundance of data' ('big data', 'data deluge', etc) narrative, in which the advent of data corresponds to a groundswell change in how we make sense of and intervene in events. Versions of these narratives surface in genomics, business analytics, and infrastructure management (e.g. in smart energy grids), as well as crisis-events such as financial collapses or epidemics. Via a case study of different data flows during the 2009 A/H1N1 'swine flu' epidemic, this chapter develops an alternative narrative of data flow in terms of number supply chain logistics. The chapter reconstructs a real-time epidemiological model that combines clinical reports, laboratory test data, web surveys, urban population mixing patterns in order to disentangle biological and social forms of contagion and infection during the 2009 epidemic in London. In reconstructing this model, a model that is typical in complicated engagement with numbers of diverse origins, the chapter will suggest that the largely  homogeneous data flows envisaged and embraced in many forms of data practice largely ignore the problem of the interactions between different agents. It specifically contrasts  the much publicised Google Flu Trends approach to 'flu prediction, which is based on search query volumes, with epidemiological models based on multiple forms of surveillance data. The chapter argues  that data practices during crises or times of great uncertainty, entail hybrid integrations of existing data practice and new forms of data.

### 7. Genomic topologies and the data superfold

#### Key examples: the ENCODE project; METABRIC; 
#### Key techniques: decision trees, random forests, self-organising maps

 - doubling times, the auratic power of the instrument, and metacommunity, the topological turn 

The final chapter of the book concerns data-generating instruments and data archives in contemporary genomics (that is, post-Human Genome Project and after the advent of so-called 'high-throughput' or 'next generation sequencers';, this is roughly 2007 onwards). Genomics is a provocative form of data thought in several respects. First, it relentlessly treats one type of quite flat or mono-dimensional data -- nucleic acid sequences -- as the key to potentially biological processes in all their plasticity and mutability. While it is not at all clear that this treatment will be effective, it has generated ways of generating shape or pattern from data that stand as a limit case for data-driven research more generally.  Second, genomics is a scientific discipline almost overwhelmed by the  effectiveness of its own instruments in generating data. The rate of production of sequence data from next generation sequencers exceeds Moore's Law, the standard 18-24 month doubling time for the number of transistors in an integrated circuits. This sequence data needs to be stored and analysed in rhythms that differ from  many other settings where the growth of data can be managed through more memory and computer processing speed. Third, genomic researchers have been extraordinarily adaptive in positioning their work on the borders of cutting edge infrastructure development, machine learning and data-mining, and the life sciences. The flatness of sequence data has been heavily leveraged by this positioning. This chapter experiments conceptually with the increasing topological character of machine learning (and particularly, the growth of 'topological data analysis' [@carlsson_topology_2009; @singh_topological_2007] as well as the topological turn in culture [@lury_introduction_2012]), and practically, with the rich ecology of programmatically accessible bioinformatics tools and archives that on the one hand permits sequence data to move relatively freely (especially in comparison to much commercial or even social media data), but on the one hand poses question as to who wants or needs the data. 
    
### 8. Conclusion

#### Key examples:
#### Key techniques:



The conclusion draws together the main threads running through the previous chapter, and sets out a series of questions and provocations for thinking with data. Crucially, the conclusion will stand back from the much more hands-on approach to data and data practice adopted in the preceding chapters in order to think more about we -- social scientists, humanities scholars -- might invent or create in the midst of data. While this book has a critical angle to it (so many claims about and beliefs in data plainly deserve critique for their conservative and naive approach to things), it is principally concerned with conceptual invention through doing things with data. The work of learning about machine learning, and learning about it in a way that is deeply embodied or practically embodied, brings with it altered ways of thinking about, questioning and integrating what is happening to data more generally. It highlights the key argument that has run through the book about the plural dimensionality of data as it is aggregated, tabulated, summarised and modelled in contemporary data and signal processes, and as well as the extraordinary mobility or kinetic energy of generic machine learning methods. In discussing the shifting dimensionality of data, and the kinetics of methods, the conclusion will attempt to sketch out how some promising ways of thinking with data might proceed. 


## References


    