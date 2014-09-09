#Directed-Reading
Repo for Directed Reading and Research course.  Fall 2014

##Related Articles
###Big Data's Effect on Organ Transplants
http://mashable.com/2014/07/23/big-data-organ-transplants/
Article on big data and organ transplants but in regards to donor matching.  Interesting article but more related to living donor matching than exploratory data analysis.

###Big Data for All: Privacy and User Control in the Age ofAnalytics
Omer Tene andJules PolonetskyBigDataforAll: Privacy and User Control in the Age ofAnalytics, 11 Nw.J. TECH. & INTELL. PROP.  239 (2013).  http://scholarlycommons.1aw.northwestern.edu/njtip/voll 1/iss5/1
Article reviews the "date deluge" which leads to privacy concerns and the need for a balance between beneficial uses of data and individual privacy.  Protecting privacy becomes difficult as information is multiplied and shared among multiple parties around the world.  Predictive analysis can become problematic when based on sensitive categories like health, race, or sexuality.  Predictive analysis may have a stifling effect on individuals and society, perpetuating old prejudices.  

###Lung Transplant Outcome Prediction using UNOS Data
http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=6691751
Analysis of lung transplant data from UNOS to develop risk prediction models for mortality within 1 year of lung transplant using data mining.  Dataset has 5319 patient instances.  Data mining techniques were used to build predictive models for the outcome.  Results were evaluates using the c-statistic.  Feature selection was also used in the model to find a smaller subset of attributes that can potentially achieve similar prediction performance but can result in a simpler model.  Sixteen different classification schemes were used in the study including support vector machines, artificial neural networks, decision tables, KStar, bayesian network, and logistic regression.

Two feature selection techniques were also used for the study: Correlation Feature Selection (CFS) and Information Gain. CFS was used to find a smaller subset of attributed and then information gain was used on the reduced set of attributes to find a ranking of the attributes.

The UNOS SAR file contained data on all transplant candidates and recipients in the US since 1987.  Data entry is mandated by the 1984 National Transplantation Act.  There is one record per waiting list registration/transplant event.  Each record includes the most recent follow-up data including patient/graft survival.  The dataset has about 500 fields used to characterize the candidate/recipient.  

The WEKA (http://www.cs.waikato.ac.nz/ml/weka/) toolkit was used for the implementation of data mining techniques. 

###2011 U.S. Organ and Tissue Transplant Cost Estimates and Discussion
http://publications.milliman.com/research/health-rr/pdfs/2011-us-organ-tissue.pdf
Report on the costs of organ transplants in the US.  Average costs per member per month (PMPM) of the billed charges and utilization related to the 30 days before and 180 days folowing a transplant.  Interesting report given with estimated costs for everything.  
