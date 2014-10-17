#Kidney Transplant Process Model Guide

## Models

-KTPM_GUI.jar - GUI for the model.  Includes an index screen and controls that can be used to manage the model's inputs.
-KTPM.jar - Compiled jar for the model.  Can be run with command line arguments or without using default, built-in values
-src/KTPM/Patients.java - Java script for the model.  Can also be run with or without command line inputs.

## Run Instructions

### Model Inputs
Number of Patents - Number of initial patients on the waiting list in the simulation
Deceased Factor - Percent increase over the current current/standard number of deceased donors by.  For example, a deceased factor of 1.0, makes no change to the number of yearly deceased donor organs available.  A deceased factor of 2.0 corresponds to doubling the number of deceased donor organs available.
Deceased Factor - Percent increase over the current current/standard number of living donors.
Equal Living - Boolean Varaible determining if the living donations should be brought up to the probability that white donors (the highest rate of living organ donations) have.

### KTPM GUI 
Double Click the file to open.
Different items can be adjusted under the CONSOLE tab such as an automatic stop time and the random seed.  Different Displays can eb opened using the DISPLAYs tab including Waiting List Size and Patient Outcomes.  The Model tab allows the user to change the Number of Patients, the Deceased Factor, the Living Factor and the Equal Living variables.  Use the Triangle at the bottom of this window to begin the simulation.

### KTPM JAR
Command Line:
$ java -jar KTPM.jar NumberOfPatients DeceasedFactor LivingFactor EqualLiving
Where EqualLiving is true/false

