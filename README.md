# Bland-Altman Plot
Script to generate a Bland-Altman plot ([Bland & Altman, 1986](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(86)90837-8/fulltext)) which is a method of data plotting used in analyzing the agreement between two different measurements. The plot uses systolic blood pressure measurements from the arm and finger ([Bland & Altman, 1995](https://www.thelancet.com/journals/lancet/article/PIIS0140673695917489/abstract)) for demonstration.

Environment setup:

```bash
conda create -n myenv python=3.11
conda activate myenv
```

Dependencies installation:

```bash
pip install -r requirements.txt
```

Usage:

```bash
python bland_altman_plot.py
```

![example image](figure.png)

Cite As

[Nzakimuena, C. B., Solano, M. M., Marcotte-Collard, R., Lesk, M. R., & Costantino, S. (2025). Spatial and temporal changes in choroid morphology associated with long-duration spaceflight. Investigative Ophthalmology & Visual Science, 66(5), 17-17.](https://doi.org/10.1167/iovs.66.5.17)

### References

1. [Bland, J. M., & Altman, D. (1986). Statistical methods for assessing agreement between two methods of clinical measurement. The lancet, 327(8476), 307-310.](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(86)90837-8/fulltext)
1. [Bland, J. M., & Altman, D. G. (1995). Comparing methods of measurement: why plotting difference against standard method is misleading. The lancet, 346(8982), 1085-1087.](https://www.thelancet.com/journals/lancet/article/PIIS0140673695917489/abstract)
