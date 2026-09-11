# Chapter 54 Solutions

1. A learned kernel slides across local patches and produces a spatial response map.
2. Each activation connects only to a local region.
3. The same kernel weights are used at every spatial location.
4. `3*3*3*16+16=448`.
5. `(32+2-3)/1+1=32`.
6. Stride controls movement and downsampling; padding adds border values.
7. The spatial responses produced by one filter.
8. The original input region capable of affecting an activation.
9. One retains the maximum; the other retains the mean.
10. It discards exact spatial detail.
11. They output an image class, object locations and classes, or pixel labels.
12. It averages each final feature map before the output layer.
13. Frames from one package in different splits are near duplicates.
14. Mirroring when text orientation matters.
15. Blur, compression, occlusion, exposure, and camera replacement.
16. Use package-grouped future-like splits, compare baselines, report defect and subgroup metrics, calibration, cost, capacity, robustness, and latency.
