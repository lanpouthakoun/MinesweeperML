from transformers import ViTModel, ViTConfig
import torch
import torch.nn as nn
import deque

class TransformerDQN(nn.Module):
    def __init__(self, image_size, patch_size, num_actions):
        super(TransformerDQN, self).__init__()
        config = ViTConfig(image_size=image_size, patch_size=patch_size, num_labels=num_actions)
        self.vit = ViTModel(config)
        self.softmax = nn.Softmax(dim=1)

    def forward(self, x):
        outputs = self.vit(pixel_values=x)
        pooled_output = outputs.last_hidden_state.mean(dim=1)
        return pooled_output
    
class QNetwork(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(QNetwork, self).__init__()
        self.fc1 = nn.Linear(input_dim, 512)
        self.fc2 = nn.Linear(512, 256)
        self.fc3 = nn.Linear(256, output_dim)
    
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x
    
class ReplayMemory():
    def __init__(self, maxlen):
        self.memory = deque([], maxlen=maxlen)

    def append(self, transition):
        self.memory.append(transition)
    
    def __len__(self):
        return len(self.memory)


