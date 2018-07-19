import math

imp0 = 377.0 # property of free space (vacuum)
SIZE = 400 # dimension of space to model
sensorLocation = 250 # location of output sensor
maxTime = 400 # simulation time

sourcePeakTime = 30 # peak of the Gaussian source
sourceSdv = 7 # standard deviation of the Gaussian source
sourceSigma = 2 * sourceSdv**2

ez = [0.0] * SIZE
hy = [0.0] * SIZE

# do time stepping
for qTime in range(maxTime):

    # update magnetic field
    for mm in range(SIZE-1):
        hy[mm] = hy[mm] + (ez[mm + 1] - ez[mm]) / imp0

    # update electric field
    for mm in range(SIZE):
        ez[mm] = ez[mm] + (hy[mm] - hy[mm - 1]) * imp0

    # hardwire a source node */
    if qTime < sourceSigma:
        ez[0] = math.exp(-(qTime - sourcePeakTime)**2 / sourceSigma)
    else:
        ez[0] = 0.0

    print(ez[sensorLocation])
#done with time stepping loop
