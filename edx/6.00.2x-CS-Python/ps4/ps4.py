# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    delays = (300,)
    addTime = 150
    viruses = [ResistantVirus(0.1, 0.05, {'guttagonol': False}, 0.005) for i in xrange(100)]
    figure = 1
            
    for delay in delays:
        totalOutcomes = []
        for trial in xrange(numTrials):
            patient = TreatedPatient(viruses[:], 1000)
            for ts in xrange(delay):
                patient.update()
            
            patient.addPrescription('guttagonol')
        
            for ts in xrange(addTime):
                patient.update()
    
            totalOutcomes.append(patient.getTotalPop())
            
        pylab.figure(figure)
        pylab.hist(totalOutcomes, 100)
    
    pylab.show()

simulationDelayedTreatment(100)


#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    # TODO
