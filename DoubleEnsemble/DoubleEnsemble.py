class DoubleEnsemble():
    def init(params):
        pass

    def DE(self, X, y, K):
        weights = K*[1]
        features = X
        for k in range(K):
            M_k = train_sub_model(X, y, w, f)
            C, L = evaluate(M_k)
            w = SR(C, L, k)
            f = FS(M_k_bar, X, y)





    # returns selected features f
    def FS(self, M_k, X, y):
        L = loss(M_k_bar(X), y)
        for f in F:
            X[i] = X[i].shuffle()
            L_f = loss(M_k_bar(X_f), y)
            d_f = mean(L_f - L) / std(L_f - L)

            #g-val measures contribution of this feature to current ensemble (feature importance)







    def SR(self, C, L, i):
        alpha1 = 1
        alpha2 = 1
        gamma = 0.02

        h_val = ?
        sample_bins = ...?


    def calc_h(self, C, L):
        """
        The normalization function norm : R^ N×d → [0, 1]N×d
    replaces each element in the matrix with its rank
    across other elements in the column, i.e., norm(X)ij = 0.9 if
    Xij is larger than 90% of the elements in the j-th column of
    X.
        """
        C_norm = rank_norm(C)
        neg_L_norm = rank_norm(-L)
    