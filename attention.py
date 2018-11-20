import torch
import torch.nn as nn


class Attention(nn.Module):
    def __init__(self):
        super(Attention, self).__init__()
        self.U = nn.Linear(512, 512)
        self.W = nn.Linear(512, 512)
        self.v = nn.Linear(512, 1)
        self.tanh = nn.Tanh()
        self.softmax = nn.Softmax()

    def forward(self, img_features, hidden_state):
        U_h = self.U(hidden_state)
        W_s = self.W(img_features)
        att = self.tanh(W_s + U_h)
        e = self.v(att)
        alpha = self.softmax(e)
        context = (img_features * alpha).sum(1)
        return context, alpha
