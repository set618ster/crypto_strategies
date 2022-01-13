## based on https://arxiv.org/pdf/2010.01265.pdf

Crypto: OKEx

currencies used: ETC/BTC, ETH/BTC, GAS/BTC and LTC/BTC. 

1 sample = 1 market snapshot (~ 0.3 seconds)
training: 10 trading days ~ 3mn datapoints
testing: 5 trading days ~ 1.5mn datapoints

features: 31 (various)
e.g OFI, RSI

30% noise (20 random features and 30% random samples sampling from U[0,1])

Algos:

SR:
FS:

Basic:
- SingleModel
    - equal eights
    - MLP
        - 2 hidden layers, each 64 neurons + dropout layer + batch-norm layer
        - Mish as activation function
        - 200 epochs + early stopping and learning rate
    - GBM
        - LightGBM w/ 200 tress w/ 32leaves max.
- Simple Ensemble
    ?

Baselines
- LDMI
- LCCN
- MentorNet
and others

Performance metrics:
- AUC (ROC)
- F1 bc in finmarket, we care about recall (ability of model to seize trading opportunity)
- PCT: avg return for each trading day