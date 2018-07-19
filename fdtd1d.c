/* Bare-bones 1D FDTD simulation with a hard source. */
#include <stdio.h>
#include <math.h>

#define SIZE 400
int main()
{

double ez[SIZE] = {0.}, hy[SIZE] = {0.}, imp0 = 377.0, epsR[SIZE];
int qTime, maxTime = 400, mm;
double sourcePeakTime = 30, sourceSdv = 7, sourceSigma;
int sensorLocation = 250;

sourceSigma = 2 * sourceSdv * sourceSdv;

for (mm = 0; mm < SIZE; mm++) epsR[mm] = 1.0;

/* uncomment next line to insert glass slab */
// for (mm = 150; mm < 200; mm++) epsR[mm] = 4.7;

/* do time stepping */
for (qTime = 0; qTime < maxTime; qTime++) {

  /* update magnetic field */
  for (mm = 0; mm < SIZE - 1; mm++)
    hy[mm] = hy[mm] + (ez[mm + 1] - ez[mm]) / imp0;

  /* update electric field */
  for (mm = 1; mm < SIZE; mm++)
    ez[mm] = ez[mm] + (hy[mm] - hy[mm - 1]) * imp0 / epsR[mm];

  /* hardwire a source node */
  if (qTime < sourceSigma)
    ez[0] = exp(-(qTime - sourcePeakTime)*(qTime - sourcePeakTime) / sourceSigma);
  else
    ez[0] = 0.0;

  printf("%g\n", ez[sensorLocation]);

  } /* end of time-stepping */

return 0;
}
