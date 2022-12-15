# Deep Reinforcement Learning vs Deep Learning <br> Retail Recommendation Engines <img width=90 align="right" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Duke_University_logo.svg/1024px-Duke_University_logo.svg.png">

## 💡 Introduction
Recommendation engines are present in every aspect of our digital lifes today. The retail industry in particular heavily depends on efficient algorithms to push the products to relevant customers.
In this project, we implement and benchmark the performance of two Deep Reinforcement Learning (DRL) models and one Deep Learning (DL) model on two separate datasets in order to better understand the nuances of each system.

### Deep Reinforcement Models
#### *Supervised Negative Q-learning (SNQN)*
Sequential transactional data can be leveraged to recommend relevant products with reinforcement learning (RL) algorithms. One limitation to this vanilla approach is the lack of negative reward signals. Xin Xin, et al. proposed the SNQN method to address this positive signal bias by integrating a negative sampling training strategy for the RL algorithms with a supervised sequential learning algorithm [1].

#### *Supervised Advantage Actor-Critic (SA2C)*
Taking one step further from the SNQN model is the SA2C framework proposed by Xin Xin, et al. in the same publication [1]. The authors propose calculating the "advatage" of a positive action over the average case to normalize weights and reduce positive bias.

#### Bayesian Personalized Ranking
[TODO]@Preet 

## 🔢 Data
In both our datasets, there is a lack of explicit negative feedback. 

### Diginetica
> Download [here](https://competitions.codalab.org/competitions/11161)

This dataset is released as part of the *CIKM Cup 2016 Track 2: Personalized E-Commerce Search Challenge*. The dataset features anonymized search, browsing, and purchase logs, product data, and product images. For the purpose of our project, we primarily leverage the view and purchase logs. \\
To reproduce the results, download the image and save it in the ```\data``` folder. We will only need ```data\train-purchases.csv``` and ```train-item-views.csv``` as our input. 
To get the pre-processed data, where we combine the view and purchase dataframe with a is_purchase flag, run the the following command:
```
!python preprocessing_dg.py
```
After getting the output file, run the split file to get training and validation data:
```
!python split_train.py
```
Then use the training set to create replay buffer for the model:
```
!python gen_replay_buffer.py
```
We'll also calculate item popularity:
```
!python cal_pop.py
```
The steps above will generate all the files we need to run the DRL python scripts. 


### RetailRocket
> Download [here](https://www.kaggle.com/datasets/retailrocket/ecommerce-dataset)

The dataset is released as part of a Kaggle competition. This raw data set contains data on user-item interactions and item properties. For the purpose of this project we leverage the user-item interactions like clicks, add to carts, transactions.

## 🛠️ Methodology
### Deep Reinforcement Models
Both SNQN and SA2C models require click (or view), purchase (or add to cart) data. While both are positive interactions, we treat clicks as negative signals and purchases as positive, where only positive signals affect the user state as part of the model. We leverage the open-sourced implementation [code](https://drive.google.com/file/d/185KB520pBLgwmiuEe7JO78kUwUL_F45t/view) provided Xin Xin, et al. and we proceed to preprocess our datasets to assign `is_buy` flags and drop users with less than 3 interactions.

### Deep Learning Model
The BPR model requires explicit negative feedback, so we pre-process our datasets to assign negative flags to when an existing user did not interact with an item. The limitation to this approach is that it exponetially increases the data size. Due to the larger number of unique users and items in the RetailRocket dataset, we were able to run the model only on a sample of 0.5% of the data.

## 🔎 Results

### Diginetica

| **Models**  | **NDCG** | **HR** | **MAP** |
| :---------: | :-----: | :-----: | :-----: |
| SNQN-SASRec |   0.142716   |   0.234636   |  N/A   |
|  SA2C-GRU   |   0.226836  |   0.288162   |  N/A   |
|     BPR     |   0.104363   |   N/A  |  0.000246  |

> We are reporting NDCG, HR and MAP @ 10 for all models.

### RetailRocket

| **Models**  | **NDCG** | **HR** | **MAP** |
| :---------: | :-----: | :-----: | :-----: |
| SNQN-SASRec |   0.0   |   0.0   |  N/A   |
|  SA2C-GRU   |   0.0   |   0.0   |  N/A   |
|     BPR     |   0.207392   |   N/A   |  0.000268  |

> We are reporting NDCG, HR and MAP @ 10 for all models.

## ⚙️ Reproduce our Study
> Note: CUDA will be required for the code to work! Some of the models are memory and compute intensive.

### **1. Clone & Navigate to our Repo**
```
git clone https://github.com/dai-anna/DRLvsDLrecommenders.git && 
cd DRLvsDLrecommenders
```

### **2. Setup your Virtual Environment**
```
python -m venv env
source env/bin/activate
```

### **3. Install all Dependencies**
```
pip install -r requirements.txt
```

### **4. Run our Notebooks**

Navigate to the folder of the model and dataset you are interested to run. Locate the **notebook** in the folder, download the data as instructed in the notebook and run it to reproduce our results. Auxilary files in each folder are used in each notebook.

#### Locate our notebooks
```
├── README.md
├── BPR
│   ├── Diginetica
│   │   └── xxx.ipynb
│   └── RetailRocket
│       └── RetailRocket_BPR_recommender_0p5pct.ipynb
├── SQNQ_SASRec
│   ├── Diginetica
│   │   └── SNQN.ipynb
│   └── RetailRocket
│       └── xxx.ipynb
└── SA2C_GRU
    ├── Diginetica
    │   └── SAC_GRU_Diginetica.ipynb
    └── RetailRocket
        └── xxx.ipynb
```

## 👯 Contributors

| **Name** | **Reference** | **Primary Technical Contributions** |
|---- | ----| ----|
|Cindy Chiu | [GitHub Profile](https://github.com/cindy-yuting-chiu)| SA2C model implementation, preprocessing, and initial exploration |
|Anna Dai | [GitHub Profile](https://github.com/dai-anna)| SNQN model implementation, preprocessing and edits for BPR on Retail Rocket |
|Preet Khowaja |[GitHub Profile](https://github.com/preetkhowaja)| BPR model implementation and preprocessing, and initial exploration |

## 📚 References
[1] Xin, Xin, et al. "Supervised Advantage Actor-Critic for Recommender Systems." Proceedings of the Fifteenth ACM International Conference on Web Search and Data Mining. 2022.

