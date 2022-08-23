# Spectrum-Based-Fault-Localization

## Abstract  
Spectrum Based Fault Localisation(SBFL), using 64 real-world faults from the Defects4j repository. 

## Features used
Based on Formula ochiai, and used method level aggregation of SBFL scores  

## Project source & Tools  
Defects4j, Project Lang - buggy version 1, 3~65   
Used a coverage tool provided by Defects4j  

## Evaluation Metric
acc@n counts the number of faults that have been localized within top n places of the ranking. If there are multiple faulty methods, I assumed that the fault is localized if any of them are ranked within top n places.

## Results   
total faults: 64   

acc@1: 40  
acc@3: 54  
acc@5: 57  
