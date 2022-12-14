# Deep Reinforcement Learning vs Deep Learning <br> Retail Recommendation Engines <img width=90 align="right" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Duke_University_logo.svg/1024px-Duke_University_logo.svg.png">

## 💡 Introduction
Recommendation engines are present in every aspect of our digital lifes today. The retail industry in particular heavily depends on efficient algorithms to push the products to relevant customers.
In this project, we implement and benchmark the performance of two Deep Reinforcement Learning (DRL) models and one Deep Learning (DL) model on two separate datasets in order to better understand the nuances of each system.

### Deep Reinforcement Models
#### *Supervised Negative Q-learning (SNQN)*
Sequential transactional data can be leveraged to recommend relevant products with reinforcement learning (RL) algorithms. One limitation to this vanilla approach is the lack of negative reward signals. Xin Xin, et al. proposed the SNQN method to address this positive signal bias by integrating a negative sampling training strategy for the RL algorithms with a supervised sequential learning algorithm [1].

#### *Supervised Advantage Actor-Critic (SA2C)*
Taking one step further from the SNQN model is the SA2C framework proposed by Xin Xin, et al. in the same publication [1]. The authors propose calculating the "advantage" of a positive action over the average case to normalize weights and reduce positive bias.

#### *Bayesian Personalized Ranking (BPR)*
The BPR model takes non-sequential user-item iteraction data as input. Instead of taking one item, item pairs will be considered as training data. Optimization would be performed based on the rank of these user-item pairs instead of scoring just on the user-item interaction. If user *u* views item *i* but not item *j*, then the algorithm ascribes positive feedback to this interaction and infers that *u* prefers *i* over *j* [2].

## 🔢 Data
In both our datasets, there is a lack of explicit negative feedback. 

### Diginetica
> Download [here](https://competitions.codalab.org/competitions/11161)

This dataset is released as part of the *CIKM Cup 2016 Track 2: Personalized E-Commerce Search Challenge*. The dataset features anonymized search, browsing, and purchase logs, product data, and product images. For the purpose of our project, we primarily leverage the view and purchase logs. 


### RetailRocket
> Download [here](https://www.kaggle.com/datasets/retailrocket/ecommerce-dataset)

The dataset is released as part of a Kaggle competition. This raw data set contains data on user-item interactions and item properties. For the purpose of this project we leverage the user-item interactions like clicks, add to carts, transactions.

## 🛠️ Methodology
### Deep Reinforcement Models
Both SNQN and SA2C models require click (or view), purchase (or add to cart) data. While both are positive interactions, we treat clicks as negative signals and purchases as positive, where only positive signals affect the user state as part of the model. We leverage the open-sourced implementation [code](https://drive.google.com/file/d/185KB520pBLgwmiuEe7JO78kUwUL_F45t/view) provided Xin Xin, et al. and we proceed to preprocess our datasets to assign `is_buy` flags and drop users with less than 3 interactions.


### Deep Learning Model
The BPR model requires explicit negative feedback, so we pre-process our datasets to assign negative flags to when an existing user did not interact with an item. The limitation to this approach is that it exponetially increases the data size. Due to the larger number of unique users and items in the RetailRocket dataset, we were able to run the model only on a sample of 0.5% of the data.

## 🔎 Results

We compare NDCG@10 across all models and HR@10 across the DRL models. To keep the results directly comparable, between DRL models, we report results at the maximum number of epochs of training we could manage (around 15epochs).

Overall, we can observe that **SA2C-GRU achieves the best performance** out of our three models while BPR achieves performs the worst performance. The significant drop in performance from the BPR is likely because the model is unable to leverage session data like the DRL models and the preprocessing of building negative feedback comes with too heavy of assumptions. Also in the RetailRocket case, we were only able to leverage 0.5% of the total data.


### Diginetica

| **Models**  | **NDCG** |  **HR**  | **MAP**  |
| :---------: | :------: | :------: | :------: |
| SNQN-SASRec | 0.180273 | 0.267916 |   N/A    |
|  SA2C-GRU   | 0.215147 | 0.299065 |   N/A    |
|     BPR     | 0.104363 |   N/A    | 0.000246 |

> We are reporting NDCG, HR and MAP @ 10 for all models.

### RetailRocket

| **Models**  | **NDCG** | **HR** | **MAP**  |
| :---------: | :------: | :----: | :------: |
| SNQN-SASRec | 0.475768 | 0.613615 |   N/A    |
|  SA2C-GRU   | 0.491089 | 0.593839 |   N/A    |
|     BPR     | 0.207392 |    N/A   | 0.000268 |



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

### **4. Run our Notebooks or Scripts in your Command Line** 

#### Command Line for DRL Models

To reproduce the results for the DRL models on Diginetica, download the datasets and save it in the ```/data``` folder. We will only need ```data/train-purchases.csv``` and ```data/train-item-views.csv``` as our input. To get the pre-processed data for Diginetica, where we combine the view and purchase dataframe with a is_purchase flag, run the the following command:
```
python src/preprocessing_dg.py
```
For RetailRocket, we only need the file ```data/events.csv```. We also need to clean up the dataframe and create a is_purchase indicator for the data. Run the following command to get the pre-processed data. 
```
python src/preprocessing_rr.py
```

After getting the output file, the processes are similar between RetailRocket and Diginetica. Run the split file to get training and validation data:
```
python src/split_train.py
```
Then use the training set to create replay buffer for the model:
```
python src/gen_replay_buffer.py
```
We'll also calculate item popularity:
```
python src/pop.py
```
The steps above will generate all the files we need to run the DRL python scripts. 

#### Locate our Notebooks
Navigate to the folder of the model and dataset you are interested to run. Locate the **notebook** in the folder, download the data as instructed in the notebook and run it to reproduce our results. Auxilary files in each folder are used in each notebook.


```
├── README.md
├── BPR
│   ├── Diginetica
│   │   └── Diginetica_BPR_recommender.ipynb
│   └── RetailRocket
│       └── RetailRocket_BPR_recommender_0p5pct.ipynb
├── SNQN
│   ├── Diginetica
│   │   └── SNQN_SASRec_Diginetica.ipynb
│   └── RetailRocket
│       └── SNQN_SASRec_RetailRocket.ipynb
└── SA2C
    ├── Diginetica
    │   └── SA2C_GRU_Diginetica.ipynb
    └── RetailRocket
        └── SA2C_GRU_Retail_Rocket.ipynb
```

## 👯 Contributors

| **Name**      | **Reference**                                          | **Primary Technical Contributions**                                         |
| ------------- | ------------------------------------------------------ | --------------------------------------------------------------------------- |
| Cindy Chiu    | [GitHub Profile](https://github.com/cindy-yuting-chiu) | SA2C model implementation, preprocessing, and initial exploration           |
| Anna Dai      | [GitHub Profile](https://github.com/dai-anna)          | SNQN model implementation, preprocessing and edits for BPR on Retail Rocket |
| Preet Khowaja | [GitHub Profile](https://github.com/preetkhowaja)      | BPR model implementation and preprocessing, and initial exploration         |

## 📚 References
[1] Xin, Xin, et al. "Supervised Advantage Actor-Critic for Recommender Systems." Proceedings of the Fifteenth ACM International Conference on Web Search and Data Mining. 2022.

[2] Rendle, Steffen, et al. "BPR: Bayesian Personalized Ranking from Implicit Feedback". Machine Learning Lab, University of Hildesheim. 2009.

