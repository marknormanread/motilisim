# My project's README

## Java3D adventures

Old java3d libraries don't work on modern Java versions (the last JRE I got them working on was 1.6). This kicks up all manner of javax- and AWT-related errors. If you haven't seen them, be happy. Something to do with Oracle not supporting java3d anymore. 

However, MASON uses it. Thankfully MASON has also provided a work around, see the "3D Libraries" section half way down this page:
https://cs.gmu.edu/~eclab/projects/mason/

The j3dlibs directory contains a copy of the jar files (also download-able from the MASON homepage) needed to get java3D working on JRE 1.8 (at least on Mac, I haven't tested on other OSs). The instructions state "Install these in your system-wide Java library location (on the Mac, it's /Library/Java/Extensions/)". On one machie I was able to add the j3dlibs/*.jar files to the Eclipse project build path, and it worked. On my other machine, running the exact same JRE1.8, I had to put j3dlibs/*.jar files into /Library/Java/Extensions. I have no idea what casued this discrepancy, the project and java configurations in Eclipse were identical. Flakey indeed. This should be fine, either way, you only need these files for visualisation, the simulation should run ok on a cluster (where you do not necessarily have sudo privileges to install these jars at the system level) if you are running the simulation headless.

Best of luck to you, I hope this solves any java3d issues you have, because java3d has been a real pain in recent years. 



