import torch.nn.functional as F
from torch import nn


class Model(nn.Module):#hidden_size2 = 20
    def __init__(self, num_features, num_targets, hidden_size1 = 10,hidden_size2=24,drop_rate1=0.2,drop_rate2=0.5,drop_rate3=0.5): 
                                                                        #30
        #working good on train hidden_size1 = 40, hidden_size2=80,drop_rate1=0.2,drop_rate2=0.5,drop_rate3=0.5 mid_size = 128
        super(Model, self).__init__()
        #self.batch_norm1 = nn.BatchNorm1d(num_features)
        #self.dropout1 = nn.Dropout(drop_rate1)
        self.dense1 = nn.utils.weight_norm(nn.Linear(num_features, hidden_size1,bias=False))
        
        #self.batch_norm2 = nn.BatchNorm1d(hidden_size1)
        self.dropout2 = nn.Dropout(drop_rate2)
        self.dense2 = nn.utils.weight_norm(nn.Linear(hidden_size1, hidden_size2))
        
       # self.batch_norm3 = nn.BatchNorm1d(hidden_size2)
        self.dropout3 = nn.Dropout(drop_rate3)
        self.dense3 = nn.utils.weight_norm(nn.Linear(hidden_size2,32))  #32
        
        #self.batch_norm4 = nn.BatchNorm1d(64)
        self.dropout4 = nn.Dropout(drop_rate3)
        self.dense4 = nn.utils.weight_norm(nn.Linear(32, hidden_size2))
        
       # self.batch_norm5 = nn.BatchNorm1d(hidden_size2)
        self.dropout5 = nn.Dropout(drop_rate3)
        self.dense5 = nn.utils.weight_norm(nn.Linear(hidden_size2, hidden_size1))
        
        self.batch_norm6 = nn.BatchNorm1d(hidden_size1)
        
        self.dense6 = nn.Linear(hidden_size1, num_targets)
    
    def forward(self, x):
      #  x = self.batch_norm1(x)
      #  x = self.dropout1(x)
        x = F.leaky_relu(self.dense1(x))
        
      #  x = self.batch_norm2(x)
        x = self.dropout2(x)
        x = F.leaky_relu(self.dense2(x))
        
      #  x = self.batch_norm3(x)
        x = self.dropout3(x)
        x = F.leaky_relu(self.dense3(x))
        
      #  x = self.batch_norm4(x)
        x = self.dropout4(x)
        x = F.leaky_relu(self.dense4(x))
        
       # x = self.batch_norm5(x)
        x = self.dropout5(x)
        x = F.leaky_relu(self.dense5(x))
        
       # x = self.batch_norm6(x)
        #x = self.dropout6(x)
        #x = F.relu(self.dense6(x))
        x = self.dense6(x)
       # x = F.relu(x)
        
        return x