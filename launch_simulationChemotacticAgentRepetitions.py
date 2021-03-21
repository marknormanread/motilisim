#!/bin/bash
#
# Launches a simulation T cell experiment
# $> launch_simulationTCell.sh to/directory
#
# Assumes that "to/directory" contains parameters.xml, and this is also where
# data will be written.
#
# Mark N. Read, 2018

# Pull directory from commmand line using $1
import os
import subprocess
import sys

direc = sys.argv[1]

if '-reps' in sys.argv:
    repetitions = list(range(int(sys.argv[sys.argv.index('-reps') + 1])))
else:
    repetitions = [0]

for rep in repetitions:
    os.system('java -Xms2000m -Xmx2000m -classpath "lib/*:j3dlibs/*" core.SimulationChemotacticAgent ' + \
                            '-p {dir:s}/parameters.xml -o {dir:s}/rep{seed:d} -s {seed:d}'.format(dir=direc, seed=rep)
                            )
    os.system('python ~/dropbox_usyd/projects/biro/neutroswarm/swarm_metric/bolus_distance_from_position.py '
              '-i {dir:s}/rep{seed:d}'.format(dir=direc, seed=rep))

