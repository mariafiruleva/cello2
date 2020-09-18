import matplotlib.pyplot as plt
import numpy as np

num_plots = 4

fig, ax = plt.subplots(num_plots, 1, sharex=True, sharey=True)
fig.set_size_inches(4, 1*num_plots)

fig.suptitle("$2 / P1_PhlF")

for a in ax:
    a.set_xscale('log')
    a.set_yscale('log')
    a.set_xlim(1,000000e-03, 1,000000e+02)

ax[0].plot([1,000000e-03,1,056818e-03,1,116863e-03,1,180321e-03,1,247384e-03,1,318257e-03,1,393157e-03,1,472313e-03,1,555966e-03,1,644372e-03,1,737801e-03,1,836538e-03,1,940886e-03,2,051162e-03,2,167704e-03,2,290868e-03,2,421029e-03,2,558586e-03,2,703958e-03,2,857591e-03,3,019952e-03,3,191538e-03,3,372873e-03,3,564511e-03,3,767038e-03,3,981072e-03,4,207266e-03,4,446313e-03,4,698941e-03,4,965923e-03,5,248075e-03,5,546257e-03,5,861382e-03,6,194411e-03,6,546362e-03,6,918310e-03,7,311391e-03,7,726806e-03,8,165824e-03,8,629785e-03,9,120108e-03,9,638290e-03,1,018591e-02,1,076465e-02,1,137627e-02,1,202264e-02,1,270574e-02,1,342765e-02,1,419058e-02,1,499685e-02,1,584893e-02,1,674943e-02,1,770109e-02,1,870682e-02,1,976970e-02,2,089296e-02,2,208005e-02,2,333458e-02,2,466039e-02,2,606154e-02,2,754229e-02,2,910717e-02,3,076097e-02,3,250873e-02,3,435579e-02,3,630781e-02,3,837072e-02,4,055085e-02,4,285485e-02,4,528976e-02,4,786301e-02,5,058247e-02,5,345644e-02,5,649370e-02,5,970353e-02,6,309573e-02,6,668068e-02,7,046931e-02,7,447320e-02,7,870458e-02,8,317638e-02,8,790225e-02,9,289664e-02,9,817479e-02,1,037528e-01,1,096478e-01,1,158777e-01,1,224616e-01,1,294196e-01,1,367729e-01,1,445440e-01,1,527566e-01,1,614359e-01,1,706082e-01,1,803018e-01,1,905461e-01,2,013724e-01,2,128139e-01,2,249055e-01,2,376840e-01,2,511886e-01,2,654606e-01,2,805434e-01,2,964831e-01,3,133286e-01,3,311311e-01,3,499452e-01,3,698282e-01,3,908409e-01,4,130475e-01,4,365158e-01,4,613176e-01,4,875285e-01,5,152286e-01,5,445027e-01,5,754399e-01,6,081350e-01,6,426877e-01,6,792036e-01,7,177943e-01,7,585776e-01,8,016781e-01,8,472274e-01,8,953648e-01,9,462372e-01,1,000000e+00,1,056818e+00,1,116863e+00,1,180321e+00,1,247384e+00,1,318257e+00,1,393157e+00,1,472313e+00,1,555966e+00,1,644372e+00,1,737801e+00,1,836538e+00,1,940886e+00,2,051162e+00,2,167704e+00,2,290868e+00,2,421029e+00,2,558586e+00,2,703958e+00,2,857591e+00,3,019952e+00,3,191538e+00,3,372873e+00,3,564511e+00,3,767038e+00,3,981072e+00,4,207266e+00,4,446313e+00,4,698941e+00,4,965923e+00,5,248075e+00,5,546257e+00,5,861382e+00,6,194411e+00,6,546362e+00,6,918310e+00,7,311391e+00,7,726806e+00,8,165824e+00,8,629785e+00,9,120108e+00,9,638290e+00,1,018591e+01,1,076465e+01,1,137627e+01,1,202264e+01,1,270574e+01,1,342765e+01,1,419058e+01,1,499685e+01,1,584893e+01,1,674943e+01,1,770109e+01,1,870682e+01,1,976970e+01,2,089296e+01,2,208005e+01,2,333458e+01,2,466039e+01,2,606154e+01,2,754229e+01,2,910717e+01,3,076097e+01,3,250873e+01,3,435579e+01,3,630781e+01,3,837072e+01,4,055085e+01,4,285485e+01,4,528976e+01,4,786301e+01,5,058247e+01,5,345644e+01,5,649370e+01,5,970353e+01,6,309573e+01,6,668068e+01,7,046931e+01,7,447320e+01,7,870458e+01,8,317638e+01,8,790225e+01,9,289664e+01,9,817479e+01,1,037528e+02,1,096478e+02,1,158777e+02,1,224616e+02,1,294196e+02,1,367729e+02,1,445440e+02,1,527566e+02,1,614359e+02,1,706082e+02,1,803018e+02,1,905461e+02,2,013724e+02,2,128139e+02,2,249055e+02,2,376840e+02,2,511886e+02,2,654606e+02,2,805434e+02,2,964831e+02,3,133286e+02,3,311311e+02,3,499452e+02,3,698282e+02,3,908409e+02,4,130475e+02,4,365158e+02,4,613176e+02,4,875285e+02,5,152286e+02,5,445027e+02,5,754399e+02,6,081350e+02,6,426877e+02,6,792036e+02,7,177943e+02,7,585776e+02,8,016781e+02,8,472274e+02,8,953648e+02,9,462372e+02,], [0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,1,427959e-04,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,1,427959e-04,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,1,427959e-04,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,1,427959e-04,0,000000e+00,0,000000e+00,1,427959e-04,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,1,427959e-04,0,000000e+00,1,427959e-04,5,711838e-04,1,427959e-04,0,000000e+00,0,000000e+00,0,000000e+00,1,427959e-04,1,427959e-04,4,283878e-04,1,427959e-04,1,427959e-04,2,855919e-04,1,427959e-04,1,427959e-04,0,000000e+00,4,283878e-04,0,000000e+00,1,427959e-04,9,995716e-04,2,855919e-04,2,855919e-04,7,139797e-04,9,995716e-04,4,283878e-04,7,139797e-04,1,427959e-04,5,711838e-04,1,285164e-03,7,139797e-04,5,711838e-04,1,142368e-03,1,285164e-03,5,711838e-04,1,713551e-03,4,283878e-04,5,711838e-04,7,139797e-04,4,283878e-04,5,711838e-04,5,711838e-04,1,427959e-04,2,855919e-04,5,711838e-04,0,000000e+00,2,855919e-04,2,855919e-04,2,855919e-04,2,855919e-04,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,1,427959e-04,1,427959e-04,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,1,427959e-04,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,2,855919e-04,1,427959e-04,1,427959e-04,4,283878e-04,9,995716e-04,9,995716e-04,1,142368e-03,1,856347e-03,3,712695e-03,4,569470e-03,5,426246e-03,8,139369e-03,1,070970e-02,1,470798e-02,1,656433e-02,2,356133e-02,2,755962e-02,3,284307e-02,3,627017e-02,3,969727e-02,4,755105e-02,5,197772e-02,6,154505e-02,6,468656e-02,6,354420e-02,7,011281e-02,6,468656e-02,6,140226e-02,5,254891e-02,5,012138e-02,4,098244e-02,3,084392e-02,2,241896e-02,2,141939e-02,1,385121e-02,8,710553e-03,7,425389e-03,5,283450e-03,3,284307e-03,2,284735e-03,1,427959e-03,7,139797e-04,4,283878e-04,2,855919e-04,4,283878e-04,0,000000e+00,1,427959e-04,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,])
ax[1].plot([1,000000e-03,1,056818e-03,1,116863e-03,1,180321e-03,1,247384e-03,1,318257e-03,1,393157e-03,1,472313e-03,1,555966e-03,1,644372e-03,1,737801e-03,1,836538e-03,1,940886e-03,2,051162e-03,2,167704e-03,2,290868e-03,2,421029e-03,2,558586e-03,2,703958e-03,2,857591e-03,3,019952e-03,3,191538e-03,3,372873e-03,3,564511e-03,3,767038e-03,3,981072e-03,4,207266e-03,4,446313e-03,4,698941e-03,4,965923e-03,5,248075e-03,5,546257e-03,5,861382e-03,6,194411e-03,6,546362e-03,6,918310e-03,7,311391e-03,7,726806e-03,8,165824e-03,8,629785e-03,9,120108e-03,9,638290e-03,1,018591e-02,1,076465e-02,1,137627e-02,1,202264e-02,1,270574e-02,1,342765e-02,1,419058e-02,1,499685e-02,1,584893e-02,1,674943e-02,1,770109e-02,1,870682e-02,1,976970e-02,2,089296e-02,2,208005e-02,2,333458e-02,2,466039e-02,2,606154e-02,2,754229e-02,2,910717e-02,3,076097e-02,3,250873e-02,3,435579e-02,3,630781e-02,3,837072e-02,4,055085e-02,4,285485e-02,4,528976e-02,4,786301e-02,5,058247e-02,5,345644e-02,5,649370e-02,5,970353e-02,6,309573e-02,6,668068e-02,7,046931e-02,7,447320e-02,7,870458e-02,8,317638e-02,8,790225e-02,9,289664e-02,9,817479e-02,1,037528e-01,1,096478e-01,1,158777e-01,1,224616e-01,1,294196e-01,1,367729e-01,1,445440e-01,1,527566e-01,1,614359e-01,1,706082e-01,1,803018e-01,1,905461e-01,2,013724e-01,2,128139e-01,2,249055e-01,2,376840e-01,2,511886e-01,2,654606e-01,2,805434e-01,2,964831e-01,3,133286e-01,3,311311e-01,3,499452e-01,3,698282e-01,3,908409e-01,4,130475e-01,4,365158e-01,4,613176e-01,4,875285e-01,5,152286e-01,5,445027e-01,5,754399e-01,6,081350e-01,6,426877e-01,6,792036e-01,7,177943e-01,7,585776e-01,8,016781e-01,8,472274e-01,8,953648e-01,9,462372e-01,1,000000e+00,1,056818e+00,1,116863e+00,1,180321e+00,1,247384e+00,1,318257e+00,1,393157e+00,1,472313e+00,1,555966e+00,1,644372e+00,1,737801e+00,1,836538e+00,1,940886e+00,2,051162e+00,2,167704e+00,2,290868e+00,2,421029e+00,2,558586e+00,2,703958e+00,2,857591e+00,3,019952e+00,3,191538e+00,3,372873e+00,3,564511e+00,3,767038e+00,3,981072e+00,4,207266e+00,4,446313e+00,4,698941e+00,4,965923e+00,5,248075e+00,5,546257e+00,5,861382e+00,6,194411e+00,6,546362e+00,6,918310e+00,7,311391e+00,7,726806e+00,8,165824e+00,8,629785e+00,9,120108e+00,9,638290e+00,1,018591e+01,1,076465e+01,1,137627e+01,1,202264e+01,1,270574e+01,1,342765e+01,1,419058e+01,1,499685e+01,1,584893e+01,1,674943e+01,1,770109e+01,1,870682e+01,1,976970e+01,2,089296e+01,2,208005e+01,2,333458e+01,2,466039e+01,2,606154e+01,2,754229e+01,2,910717e+01,3,076097e+01,3,250873e+01,3,435579e+01,3,630781e+01,3,837072e+01,4,055085e+01,4,285485e+01,4,528976e+01,4,786301e+01,5,058247e+01,5,345644e+01,5,649370e+01,5,970353e+01,6,309573e+01,6,668068e+01,7,046931e+01,7,447320e+01,7,870458e+01,8,317638e+01,8,790225e+01,9,289664e+01,9,817479e+01,1,037528e+02,1,096478e+02,1,158777e+02,1,224616e+02,1,294196e+02,1,367729e+02,1,445440e+02,1,527566e+02,1,614359e+02,1,706082e+02,1,803018e+02,1,905461e+02,2,013724e+02,2,128139e+02,2,249055e+02,2,376840e+02,2,511886e+02,2,654606e+02,2,805434e+02,2,964831e+02,3,133286e+02,3,311311e+02,3,499452e+02,3,698282e+02,3,908409e+02,4,130475e+02,4,365158e+02,4,613176e+02,4,875285e+02,5,152286e+02,5,445027e+02,5,754399e+02,6,081350e+02,6,426877e+02,6,792036e+02,7,177943e+02,7,585776e+02,8,016781e+02,8,472274e+02,8,953648e+02,9,462372e+02,], [0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,1,427959e-04,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,1,427959e-04,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,1,427959e-04,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,1,427959e-04,0,000000e+00,0,000000e+00,1,427959e-04,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,1,427959e-04,0,000000e+00,1,427959e-04,5,711838e-04,1,427959e-04,0,000000e+00,0,000000e+00,0,000000e+00,1,427959e-04,1,427959e-04,4,283878e-04,1,427959e-04,1,427959e-04,2,855919e-04,1,427959e-04,1,427959e-04,0,000000e+00,4,283878e-04,0,000000e+00,1,427959e-04,9,995716e-04,2,855919e-04,2,855919e-04,7,139797e-04,9,995716e-04,4,283878e-04,7,139797e-04,1,427959e-04,5,711838e-04,1,285164e-03,7,139797e-04,5,711838e-04,1,142368e-03,1,285164e-03,5,711838e-04,1,713551e-03,4,283878e-04,5,711838e-04,7,139797e-04,4,283878e-04,5,711838e-04,5,711838e-04,1,427959e-04,2,855919e-04,5,711838e-04,0,000000e+00,2,855919e-04,2,855919e-04,2,855919e-04,2,855919e-04,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,1,427959e-04,1,427959e-04,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,1,427959e-04,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,2,855919e-04,1,427959e-04,1,427959e-04,4,283878e-04,9,995716e-04,9,995716e-04,1,142368e-03,1,856347e-03,3,712695e-03,4,569470e-03,5,426246e-03,8,139369e-03,1,070970e-02,1,470798e-02,1,656433e-02,2,356133e-02,2,755962e-02,3,284307e-02,3,627017e-02,3,969727e-02,4,755105e-02,5,197772e-02,6,154505e-02,6,468656e-02,6,354420e-02,7,011281e-02,6,468656e-02,6,140226e-02,5,254891e-02,5,012138e-02,4,098244e-02,3,084392e-02,2,241896e-02,2,141939e-02,1,385121e-02,8,710553e-03,7,425389e-03,5,283450e-03,3,284307e-03,2,284735e-03,1,427959e-03,7,139797e-04,4,283878e-04,2,855919e-04,4,283878e-04,0,000000e+00,1,427959e-04,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,])
ax[2].plot([1,000000e-03,1,056818e-03,1,116863e-03,1,180321e-03,1,247384e-03,1,318257e-03,1,393157e-03,1,472313e-03,1,555966e-03,1,644372e-03,1,737801e-03,1,836538e-03,1,940886e-03,2,051162e-03,2,167704e-03,2,290868e-03,2,421029e-03,2,558586e-03,2,703958e-03,2,857591e-03,3,019952e-03,3,191538e-03,3,372873e-03,3,564511e-03,3,767038e-03,3,981072e-03,4,207266e-03,4,446313e-03,4,698941e-03,4,965923e-03,5,248075e-03,5,546257e-03,5,861382e-03,6,194411e-03,6,546362e-03,6,918310e-03,7,311391e-03,7,726806e-03,8,165824e-03,8,629785e-03,9,120108e-03,9,638290e-03,1,018591e-02,1,076465e-02,1,137627e-02,1,202264e-02,1,270574e-02,1,342765e-02,1,419058e-02,1,499685e-02,1,584893e-02,1,674943e-02,1,770109e-02,1,870682e-02,1,976970e-02,2,089296e-02,2,208005e-02,2,333458e-02,2,466039e-02,2,606154e-02,2,754229e-02,2,910717e-02,3,076097e-02,3,250873e-02,3,435579e-02,3,630781e-02,3,837072e-02,4,055085e-02,4,285485e-02,4,528976e-02,4,786301e-02,5,058247e-02,5,345644e-02,5,649370e-02,5,970353e-02,6,309573e-02,6,668068e-02,7,046931e-02,7,447320e-02,7,870458e-02,8,317638e-02,8,790225e-02,9,289664e-02,9,817479e-02,1,037528e-01,1,096478e-01,1,158777e-01,1,224616e-01,1,294196e-01,1,367729e-01,1,445440e-01,1,527566e-01,1,614359e-01,1,706082e-01,1,803018e-01,1,905461e-01,2,013724e-01,2,128139e-01,2,249055e-01,2,376840e-01,2,511886e-01,2,654606e-01,2,805434e-01,2,964831e-01,3,133286e-01,3,311311e-01,3,499452e-01,3,698282e-01,3,908409e-01,4,130475e-01,4,365158e-01,4,613176e-01,4,875285e-01,5,152286e-01,5,445027e-01,5,754399e-01,6,081350e-01,6,426877e-01,6,792036e-01,7,177943e-01,7,585776e-01,8,016781e-01,8,472274e-01,8,953648e-01,9,462372e-01,1,000000e+00,1,056818e+00,1,116863e+00,1,180321e+00,1,247384e+00,1,318257e+00,1,393157e+00,1,472313e+00,1,555966e+00,1,644372e+00,1,737801e+00,1,836538e+00,1,940886e+00,2,051162e+00,2,167704e+00,2,290868e+00,2,421029e+00,2,558586e+00,2,703958e+00,2,857591e+00,3,019952e+00,3,191538e+00,3,372873e+00,3,564511e+00,3,767038e+00,3,981072e+00,4,207266e+00,4,446313e+00,4,698941e+00,4,965923e+00,5,248075e+00,5,546257e+00,5,861382e+00,6,194411e+00,6,546362e+00,6,918310e+00,7,311391e+00,7,726806e+00,8,165824e+00,8,629785e+00,9,120108e+00,9,638290e+00,1,018591e+01,1,076465e+01,1,137627e+01,1,202264e+01,1,270574e+01,1,342765e+01,1,419058e+01,1,499685e+01,1,584893e+01,1,674943e+01,1,770109e+01,1,870682e+01,1,976970e+01,2,089296e+01,2,208005e+01,2,333458e+01,2,466039e+01,2,606154e+01,2,754229e+01,2,910717e+01,3,076097e+01,3,250873e+01,3,435579e+01,3,630781e+01,3,837072e+01,4,055085e+01,4,285485e+01,4,528976e+01,4,786301e+01,5,058247e+01,5,345644e+01,5,649370e+01,5,970353e+01,6,309573e+01,6,668068e+01,7,046931e+01,7,447320e+01,7,870458e+01,8,317638e+01,8,790225e+01,9,289664e+01,9,817479e+01,1,037528e+02,1,096478e+02,1,158777e+02,1,224616e+02,1,294196e+02,1,367729e+02,1,445440e+02,1,527566e+02,1,614359e+02,1,706082e+02,1,803018e+02,1,905461e+02,2,013724e+02,2,128139e+02,2,249055e+02,2,376840e+02,2,511886e+02,2,654606e+02,2,805434e+02,2,964831e+02,3,133286e+02,3,311311e+02,3,499452e+02,3,698282e+02,3,908409e+02,4,130475e+02,4,365158e+02,4,613176e+02,4,875285e+02,5,152286e+02,5,445027e+02,5,754399e+02,6,081350e+02,6,426877e+02,6,792036e+02,7,177943e+02,7,585776e+02,8,016781e+02,8,472274e+02,8,953648e+02,9,462372e+02,], [2,898201e-03,5,192610e-03,3,139717e-03,4,951093e-03,4,468059e-03,0,000000e+00,4,347301e-03,5,796401e-03,4,709576e-03,1,123053e-02,5,192610e-03,7,245502e-03,5,675643e-03,1,449100e-02,6,158676e-03,1,545707e-02,1,304190e-02,6,883227e-03,1,581935e-02,1,557783e-02,1,726845e-02,1,545707e-02,2,777442e-02,1,763072e-02,3,018959e-02,3,683130e-02,2,886125e-02,2,861973e-02,3,103490e-02,3,188021e-02,4,528439e-02,4,045405e-02,3,985026e-02,4,129936e-02,3,997102e-02,3,755585e-02,4,178239e-02,4,685424e-02,3,345007e-02,3,477841e-02,3,731433e-02,2,451395e-02,2,584229e-02,2,294409e-02,1,763072e-02,1,159280e-02,1,123053e-02,5,313368e-03,6,037918e-03,4,709576e-03,3,622751e-03,1,811375e-03,1,086825e-03,9,660669e-04,7,245502e-04,7,245502e-04,8,453085e-04,7,245502e-04,4,830335e-04,7,245502e-04,3,622751e-04,3,622751e-04,1,207584e-04,2,415167e-04,0,000000e+00,2,415167e-04,1,207584e-04,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,1,207584e-04,0,000000e+00,1,207584e-04,1,207584e-04,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,1,207584e-04,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,1,207584e-04,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,])
ax[3].plot([1,000000e-03,1,056818e-03,1,116863e-03,1,180321e-03,1,247384e-03,1,318257e-03,1,393157e-03,1,472313e-03,1,555966e-03,1,644372e-03,1,737801e-03,1,836538e-03,1,940886e-03,2,051162e-03,2,167704e-03,2,290868e-03,2,421029e-03,2,558586e-03,2,703958e-03,2,857591e-03,3,019952e-03,3,191538e-03,3,372873e-03,3,564511e-03,3,767038e-03,3,981072e-03,4,207266e-03,4,446313e-03,4,698941e-03,4,965923e-03,5,248075e-03,5,546257e-03,5,861382e-03,6,194411e-03,6,546362e-03,6,918310e-03,7,311391e-03,7,726806e-03,8,165824e-03,8,629785e-03,9,120108e-03,9,638290e-03,1,018591e-02,1,076465e-02,1,137627e-02,1,202264e-02,1,270574e-02,1,342765e-02,1,419058e-02,1,499685e-02,1,584893e-02,1,674943e-02,1,770109e-02,1,870682e-02,1,976970e-02,2,089296e-02,2,208005e-02,2,333458e-02,2,466039e-02,2,606154e-02,2,754229e-02,2,910717e-02,3,076097e-02,3,250873e-02,3,435579e-02,3,630781e-02,3,837072e-02,4,055085e-02,4,285485e-02,4,528976e-02,4,786301e-02,5,058247e-02,5,345644e-02,5,649370e-02,5,970353e-02,6,309573e-02,6,668068e-02,7,046931e-02,7,447320e-02,7,870458e-02,8,317638e-02,8,790225e-02,9,289664e-02,9,817479e-02,1,037528e-01,1,096478e-01,1,158777e-01,1,224616e-01,1,294196e-01,1,367729e-01,1,445440e-01,1,527566e-01,1,614359e-01,1,706082e-01,1,803018e-01,1,905461e-01,2,013724e-01,2,128139e-01,2,249055e-01,2,376840e-01,2,511886e-01,2,654606e-01,2,805434e-01,2,964831e-01,3,133286e-01,3,311311e-01,3,499452e-01,3,698282e-01,3,908409e-01,4,130475e-01,4,365158e-01,4,613176e-01,4,875285e-01,5,152286e-01,5,445027e-01,5,754399e-01,6,081350e-01,6,426877e-01,6,792036e-01,7,177943e-01,7,585776e-01,8,016781e-01,8,472274e-01,8,953648e-01,9,462372e-01,1,000000e+00,1,056818e+00,1,116863e+00,1,180321e+00,1,247384e+00,1,318257e+00,1,393157e+00,1,472313e+00,1,555966e+00,1,644372e+00,1,737801e+00,1,836538e+00,1,940886e+00,2,051162e+00,2,167704e+00,2,290868e+00,2,421029e+00,2,558586e+00,2,703958e+00,2,857591e+00,3,019952e+00,3,191538e+00,3,372873e+00,3,564511e+00,3,767038e+00,3,981072e+00,4,207266e+00,4,446313e+00,4,698941e+00,4,965923e+00,5,248075e+00,5,546257e+00,5,861382e+00,6,194411e+00,6,546362e+00,6,918310e+00,7,311391e+00,7,726806e+00,8,165824e+00,8,629785e+00,9,120108e+00,9,638290e+00,1,018591e+01,1,076465e+01,1,137627e+01,1,202264e+01,1,270574e+01,1,342765e+01,1,419058e+01,1,499685e+01,1,584893e+01,1,674943e+01,1,770109e+01,1,870682e+01,1,976970e+01,2,089296e+01,2,208005e+01,2,333458e+01,2,466039e+01,2,606154e+01,2,754229e+01,2,910717e+01,3,076097e+01,3,250873e+01,3,435579e+01,3,630781e+01,3,837072e+01,4,055085e+01,4,285485e+01,4,528976e+01,4,786301e+01,5,058247e+01,5,345644e+01,5,649370e+01,5,970353e+01,6,309573e+01,6,668068e+01,7,046931e+01,7,447320e+01,7,870458e+01,8,317638e+01,8,790225e+01,9,289664e+01,9,817479e+01,1,037528e+02,1,096478e+02,1,158777e+02,1,224616e+02,1,294196e+02,1,367729e+02,1,445440e+02,1,527566e+02,1,614359e+02,1,706082e+02,1,803018e+02,1,905461e+02,2,013724e+02,2,128139e+02,2,249055e+02,2,376840e+02,2,511886e+02,2,654606e+02,2,805434e+02,2,964831e+02,3,133286e+02,3,311311e+02,3,499452e+02,3,698282e+02,3,908409e+02,4,130475e+02,4,365158e+02,4,613176e+02,4,875285e+02,5,152286e+02,5,445027e+02,5,754399e+02,6,081350e+02,6,426877e+02,6,792036e+02,7,177943e+02,7,585776e+02,8,016781e+02,8,472274e+02,8,953648e+02,9,462372e+02,], [2,898201e-03,5,192610e-03,3,139717e-03,4,951093e-03,4,468059e-03,0,000000e+00,4,347301e-03,5,796401e-03,4,709576e-03,1,123053e-02,5,192610e-03,7,245502e-03,5,675643e-03,1,449100e-02,6,158676e-03,1,545707e-02,1,304190e-02,6,883227e-03,1,581935e-02,1,557783e-02,1,726845e-02,1,545707e-02,2,777442e-02,1,763072e-02,3,018959e-02,3,683130e-02,2,886125e-02,2,861973e-02,3,103490e-02,3,188021e-02,4,528439e-02,4,045405e-02,3,985026e-02,4,129936e-02,3,997102e-02,3,755585e-02,4,178239e-02,4,685424e-02,3,345007e-02,3,477841e-02,3,731433e-02,2,451395e-02,2,584229e-02,2,294409e-02,1,763072e-02,1,159280e-02,1,123053e-02,5,313368e-03,6,037918e-03,4,709576e-03,3,622751e-03,1,811375e-03,1,086825e-03,9,660669e-04,7,245502e-04,7,245502e-04,8,453085e-04,7,245502e-04,4,830335e-04,7,245502e-04,3,622751e-04,3,622751e-04,1,207584e-04,2,415167e-04,0,000000e+00,2,415167e-04,1,207584e-04,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,1,207584e-04,0,000000e+00,1,207584e-04,1,207584e-04,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,1,207584e-04,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,1,207584e-04,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,0,000000e+00,])


plt.savefig("SC1C1G1T1/and.v/cytometry_plot_$2_P1_PhlF.png", bbox_inches='tight')
