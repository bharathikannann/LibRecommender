import time
import numpy as np
import tensorflow as tf
from libreco.dataset.DatasetPure import DatasetPure
from libreco.dataset.DatasetFeat import DatasetFeat
from libreco.algorithms import user_KNN, item_KNN, SVD, SVDpp, NCF, wide_deep, FM, DeepFM, BPR
from libreco.evaluate import rmse_knn, rmse_svd, rmse_tf, MAP_at_k, AP_at_k
from libreco.utils.baseline_estimates import baseline_als, baseline_sgd
from libreco.utils.sampling import NegativeSampling
from pprint import pprint


if __name__ == "__main__":
#    loaded_data = Dataset.load_dataset(data_path="ml-1m/ratings.dat")
    t0 = time.time()
#    dataset = DatasetPure()
#    dataset.build_dataset(data_path="ml-1m/ratings.dat", sep="::", length="all", shuffle=True,
#                          convert_implicit=True, build_negative=True, num_neg=1, batch_size=256)
#    dataset.leave_k_out_split(4, data_path="ml-1m/ratings.dat", length=100000, sep="::",
#                              convert_implicit=True, build_negative=True, batch_size=256, num_neg=1)
#    print("data size: ", len(dataset.train_user_implicit) + len(dataset.test_user_implicit))
#    print("data processing time: {:.2f}".format(time.time() - t0))

#    print(dataset.train_item_indices.max(), len(dataset.train_item), len(dataset.train_user),
#          len(np.unique(dataset.train_item_indices)), len(np.unique(dataset.train_user_indices)))
#    print("data size: ", len(dataset.train_user_implicit) + len(dataset.test_user_implicit), "\n")

    dataset = DatasetFeat(include_features=True)
    dataset.build_dataset("ml-1m/merged_data.csv", length=100000, user_col=0, item_col=1, label_col=2,
                          numerical_col=None, categorical_col=[3, 4, 5], merged_categorical_col=[[6, 7, 8]],
                          convert_implicit=True, build_negative=True, num_neg=1, batch_size=256)
#                         numerical_col=None, categorical_col=[3, 4, 5, 6, 7, 8], merged_categorical_col=None)
#    dataset.leave_k_out_split(4, data_path="ml-1m/merged_data.csv", length="all", sep=",", shuffle=True,
#                              user_col=0, item_col=1, label_col=2, numerical_col=None, categorical_col=[3, 4, 5],
#                              merged_categorical_col=[[6, 7, 8]])
    print("data size: ", len(dataset.train_indices_implicit) + len(dataset.test_indices_implicit))
#    print("data processing time: {:.2f}".format(time.time() - t0))
    print()
#    dataset.build_trainset_implicit(4)
#    dataset.build_testset_implicit(4)

#    print(dataset.train_user_implicit[:10])
#    print(dataset.train_item_implicit[:10])
#    print(dataset.train_label_implict[:10])
#    print(dataset.test_user_implicit[:10])
#    print(dataset.test_item_implicit[:10])
#    print(dataset.test_label_implict[:10])

#    neg = negative_sampling(dataset, 4, 8)
#    pprint(neg.next_batch())
#    pprint(neg.next_batch())
#    pprint(neg.next_batch())

#    with tf.Session() as sess:
#    dataset.load_tf_trainset(batch_size=2048)

#    user_knn = user_KNN.userKNN(sim_option="pearson", k=40, min_support=5, baseline=True)
#    user_knn.fit(dataset)
#    print(rmse_knn(user_knn, dataset, mode="train"))
#    print(rmse_knn(user_knn, dataset, mode="test"))
#    print(user_knn.topN(1, 10, 5, random_rec=False))
#    print(user_knn.topN(1, 10, 5, random_rec=True))

#    svd = SVD.SVD(n_factors=10, n_epochs=200, reg=10.0)
#    svd.fit(dataset)
#    print(rmse_svd(svd, dataset, mode="train"))
#    print(rmse_svd(svd, dataset, mode="test"))
#    print(svd.topN(1, 5, random_rec=False))
#    print(svd.topN(1, 5, random_rec=True))

#    svd = SVD.SVD_tf(n_factors=100, n_epochs=10, lr=0.01, reg=0.1,
#                     batch_size=1280, batch_training=True)
#    svd.fit(dataset, data_mode="structure")
#    print(svd.predict(1,2))
#    print(rmse_svd(svd, dataset, mode="train"))
#    print(rmse_svd(svd, dataset, mode="test"))

#    svd = SVD.SVDBaseline(n_factors=30, n_epochs=20000, lr=0.001, reg=0.1,
#                          batch_size=256, batch_training=True)
#    svd.fit(dataset)
#    print(rmse_svd(svd, dataset, mode="train"))
#    print(rmse_svd(svd, dataset, mode="test"))

#    svdpp = SVDpp.SVDpp(n_factors=30, n_epochs=20000, lr=0.001, reg=0.1,
#                        batch_size=256, batch_training=True)
#    svdpp.fit(dataset)
#    print(rmse_svd(svdpp, dataset, mode="train"))
#    print(rmse_svd(svdpp, dataset, mode="test"))

#    svdpp = SVDpp.SVDpp_tf(n_factors=100, n_epochs=10, lr=0.001, reg=0.1,
#                            batch_size=256, batch_training=True)  # 0.8579
#    svdpp.fit(dataset)
#    print(svdpp.predict(1,2))
#    print(rmse_svd(svdpp, dataset, mode="train"))
#    print(rmse_svd(svdpp, dataset, mode="test"))

#    superSVD = superSVD.superSVD(n_factors=200, n_epochs=10000, lr=0.001, reg=0.001,
#                                 batch_training=True, sim_option="cosine",
#                                 k=40, min_support=5)  # lr1, lr2 reg1, reg2
#    superSVD.fit(dataset)
#    print(superSVD.predict(1,2))
#    print(rmse_svd(superSVD, dataset, mode="train"))
#    print(rmse_svd(superSVD, dataset, mode="test"))

#    ncf = NCF.NCF(embed_size=32, lr=0.0007, batch_size=256, n_epochs=500)
#    ncf = NCF.NCF(embed_size=16, lr=0.001, batch_size=256, n_epochs=500)
#    ncf.fit(dataset)
#    print(ncf.predict(1,2))
#    print(AP_at_k(ncf, dataset, 1, 10))
#    print(MAP_at_k(ncf, dataset, 10))
#    print(rmse_tf(ncf, dataset, mode="train"))
#    print(rmse_tf(ncf, dataset, mode="test"))

#    wd = wide_deep.WideDeep(embed_size=16, n_epochs=1, batch_size=256, task="ranking")
#    wd.fit(dataset)
#    print(wd.predict(1, 2, "2001-1-8"))
#    print(wd.predict_user(1))

#    wdc = wide_deep.WideDeepCustom(embed_size=16, n_epochs=1, batch_size=256, task="ranking")
#    wdc.fit(dataset)
#    print(wdc.predict_ui(1, 2, "2001-1-8"))
#    print(wdc.predict_user(1))

    # reg=0.001, n_factors=32 reg=0.0001   0.8586  0.8515  0.8511
    # reg=0.0003, n_factors=64, 0.8488    0.8471 0.8453
#    fm = FM.FmPure(lr=0.001, n_epochs=20000, reg=0.0, n_factors=16, batch_size=256, task="ranking")  # orig 0.8650  0.8634 0.8591
    fm = FM.FmFeat(lr=0.0001, n_epochs=20000, reg=0.0, n_factors=16, batch_size=256, task="ranking")
    fm.fit(dataset)
#    print(fm.predict(1, 2))

#    dfm = DeepFM.DeepFM(lr=0.0001, n_epochs=20000, reg=0.0, embed_size=8,
#                        batch_size=1024, dropout=0.0, task="ranking")
#    dfm.fit(dataset)
#    print(dfm.predict(1, 2))
#    print(dfm.predict_user(1))

#    iteration = len(dataset.train_user_indices) * 10000
#    bpr = BPR.BPR(lr=0.01, iteration=iteration)  # reg
#    bpr.fit(dataset, sampling_mode="bootstrap")
#    print(bpr.predict(1, 2))

#    bpr = BPR.BPR(lr=0.03, n_epochs=2, reg=0.0, n_factors=16, batch_size=64)
#    bpr.fit(dataset, sampling_mode="sgd")
#    print(bpr.predict(1, 2))

#    bpr = BPR.BPR_tf(lr=0.001, n_epochs=20, reg=0.0, n_factors=16, batch_size=64)
#    bpr.fit(dataset)
#    print(bpr.predict(1, 2))

#    bpr = BPR.BPR(lr=0.01, n_epochs=2000, reg=0.0, k=100)
#    bpr.fit(dataset, method="knn")
#    print(bpr.predict(1, 2, method="knn"))

    print("train + test time: {:.4f}".format(time.time() - t0))



