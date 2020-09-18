import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

fig, ax = plt.subplots(figsize=(2.5,2.5))

plt.xlim(1,000000e-03, 1,000000e+02)
plt.ylim(1,000000e-03, 1,000000e+02)

x = np.array([1,000000e-03,1,122018e-03,1,258925e-03,1,412538e-03,1,584893e-03,1,778279e-03,1,995262e-03,2,238721e-03,2,511886e-03,2,818383e-03,3,162278e-03,3,548134e-03,3,981072e-03,4,466836e-03,5,011872e-03,5,623413e-03,6,309573e-03,7,079458e-03,7,943282e-03,8,912509e-03,1,000000e-02,1,122018e-02,1,258925e-02,1,412538e-02,1,584893e-02,1,778279e-02,1,995262e-02,2,238721e-02,2,511886e-02,2,818383e-02,3,162278e-02,3,548134e-02,3,981072e-02,4,466836e-02,5,011872e-02,5,623413e-02,6,309573e-02,7,079458e-02,7,943282e-02,8,912509e-02,1,000000e-01,1,122018e-01,1,258925e-01,1,412538e-01,1,584893e-01,1,778279e-01,1,995262e-01,2,238721e-01,2,511886e-01,2,818383e-01,3,162278e-01,3,548134e-01,3,981072e-01,4,466836e-01,5,011872e-01,5,623413e-01,6,309573e-01,7,079458e-01,7,943282e-01,8,912509e-01,1,000000e+00,1,122018e+00,1,258925e+00,1,412538e+00,1,584893e+00,1,778279e+00,1,995262e+00,2,238721e+00,2,511886e+00,2,818383e+00,3,162278e+00,3,548134e+00,3,981072e+00,4,466836e+00,5,011872e+00,5,623413e+00,6,309573e+00,7,079458e+00,7,943282e+00,8,912509e+00,1,000000e+01,1,122018e+01,1,258925e+01,1,412538e+01,1,584893e+01,1,778279e+01,1,995262e+01,2,238721e+01,2,511886e+01,2,818383e+01,3,162278e+01,3,548134e+01,3,981072e+01,4,466836e+01,5,011872e+01,5,623413e+01,6,309573e+01,7,079458e+01,7,943282e+01,8,912509e+01,1,000000e+02,])
y = np.array([5,069999e+00,5,069999e+00,5,069998e+00,5,069997e+00,5,069996e+00,5,069994e+00,5,069991e+00,5,069987e+00,5,069982e+00,5,069974e+00,5,069962e+00,5,069945e+00,5,069922e+00,5,069887e+00,5,069838e+00,5,069767e+00,5,069666e+00,5,069519e+00,5,069309e+00,5,069008e+00,5,068574e+00,5,067951e+00,5,067055e+00,5,065769e+00,5,063922e+00,5,061270e+00,5,057463e+00,5,052001e+00,5,044174e+00,5,032966e+00,5,016947e+00,4,994102e+00,4,961634e+00,4,915705e+00,4,851169e+00,4,761338e+00,4,637916e+00,4,471354e+00,4,251919e+00,3,971823e+00,3,628373e+00,3,227392e+00,2,785189e+00,2,327164e+00,1,882552e+00,1,477324e+00,1,128666e+00,8,432425e-01,6,189535e-01,4,483052e-01,3,216322e-01,2,293134e-01,1,629288e-01,1,156520e-01,8,221461e-02,5,868047e-02,4,217336e-02,3,062300e-02,2,255461e-02,1,692516e-02,1,300063e-02,1,026625e-02,8,361855e-03,7,035883e-03,6,112828e-03,5,470345e-03,5,023193e-03,4,712007e-03,4,495453e-03,4,344759e-03,4,239897e-03,4,166929e-03,4,116154e-03,4,080824e-03,4,056239e-03,4,039133e-03,4,027230e-03,4,018947e-03,4,013184e-03,4,009174e-03,4,006383e-03,4,004442e-03,4,003091e-03,4,002151e-03,4,001496e-03,4,001041e-03,4,000725e-03,4,000504e-03,4,000351e-03,4,000244e-03,4,000170e-03,4,000118e-03,4,000082e-03,4,000057e-03,4,000040e-03,4,000028e-03,4,000019e-03,4,000013e-03,4,000009e-03,4,000006e-03,4,000005e-03,])
c = "#9c53a0"

hi_x = np.array([2,884195e-02,])
hi_y = np.array([5,030195e+00,])
lo_x = np.array([7,029983e+00,3,826454e+00,3,232371e+00,])
lo_y = np.array([4,019370e-03,4,131591e-03,4,223890e-03,])

plt.loglog(x,y,lw=3,color=c)
plt.scatter(hi_x,hi_y,marker='o',s=50,color='black',zorder=10)
plt.scatter(lo_x,lo_y,marker='o',s=50,edgecolors='black',color='none',zorder=10)

plt.title("$1 / P1_BM3RI")

ax.xaxis.set_major_locator(ticker.LogLocator(numticks=3))
ax.yaxis.set_major_locator(ticker.LogLocator(numticks=3))

ax.set_aspect('equal')
plt.tight_layout()

plt.savefig("output/SC1C1G1T1/and.v/response_plot_$1_P1_BM3RI.png", bbox_inches='tight')