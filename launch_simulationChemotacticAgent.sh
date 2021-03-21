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
java -Xms2000m -Xmx2000m -classpath "lib/*:j3dlibs/*" core.SimulationChemotacticAgent -p $1/parameters.xml -o $1 -s 999

python ~/dropbox_usyd/projects/biro/neutroswarm/swarm_metric/bolus_distance_from_position.py -i $1