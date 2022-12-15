# Deep Reinforcement Learning vs Deep Learning <br> Retail Recommendation Engines <img width=90 align="right" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Duke_University_logo.svg/1024px-Duke_University_logo.svg.png">

## 💡 Introduction
Recommendation engines are present in every aspect of our digital lifes today. The retail industry in particular heavily depends on efficient algorithms to push the products to relevant customers.
In this project, we implement and benchmark the performance of two Deep Reinforcement Learning models and one Deep Learning model on two separate datasets in order to better understand the nuances of each system.

### Deep Reinforcement Models
#### *Supervised Negative Q-learning (SNQN)*
Sequential transactional data can be leveraged to recommend relevant products with reinforcement learning algorithms. One limitation to this vanilla approach is the lack of negative reward signals. Xin Xin, et al. proposed the SNQN method to address this positive signal bias by using negative action items 

#### *Supervised Advantage Actor-Critic (SA2C)*

#### Bayesian Personalized Ranking

## Data
### Diginetica

### Retailrocket


## 🛠️ Methodology
### Deep Reinforcement Models
Preprocess data..
Modify code as needed

### Deep Learning Model
Preprocess data...

## 🔬 Results

### Diginetica

| **Models**  | **NG...** | **HR** | **MAP** |
| :---------: | :-----: | :-----: | :-----: |
| SASRec-SNQN |   0.0   |   0.0   |  0.0   |
|  GRU-SA2C   |   0.0   |   0.0   |  0.0   |
|     BPR     |   0.0   |   0.0   |  0.0.  |


### Retailrocket

| **Models**  | **NG...** | **HR** | **MAP** |
| :---------: | :-----: | :-----: | :-----: |
| SASRec-SNQN |   0.0   |   0.0   |  0.0   |
|  GRU-SA2C   |   0.0   |   0.0   |  0.0   |
|     BPR     |   0.0   |   0.0   |  0.0.  |

## Reproduce our Study
> Note: CUDA will be required for the code to work! Some of the models are memory and compute intensive.

**1. Clone & Navigate to our Repo**
```
git clone https://github.com/dai-anna/DRLvsDLrecommenders.git && 
cd DRLvsDLrecommenders
```

**2. Setup your Virtual Environment**
```
python -m venv env
source env/bin/activate
```

**3. Install all Dependencies**
```
pip install -r requirements.txt
```

**4. Run our Notebooks**
Navigate to the folder of the model and dataset you are interested to run. Locate the **notebook** in the folder, download the data as instructed in the notebook and run it to reproduce our results. Auxilary files in each folder are used in each notebook.

### Locate our notebooks 
```
├── README.md
├── BPR
│   ├── Diginetica
│   │   └── xxx.ipynb
│   └── Retailrocket.ipynb
│       └── xxx.ipynb
├── SQNQ
│   ├── Diginetica
│   │   └── xxx.ipynb
│   └── Retailrocket.ipynb
│       └── xxx.ipynb
└── SA2C
    ├── Diginetica
    │   └── xxx.ipynb
    └── Retailrocket.ipynb
        └── xxx.ipynb

## Contributors

| Name | Reference |
|---- | ----|
|Cindy Chiu | [GitHub Profile](https://github.com/cindy-yuting-chiu)|
|Anna Dai | [GitHub Profile](https://github.com/dai-anna)|
|Preet Khowaja |[GitHub Profile](https://github.com/preetkhowaja)|

