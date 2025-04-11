import torch


x = torch.tensor(1.1, dtype=torch.int, device='mps')
print(x)
print(x.type())
print(type(x))
print(isinstance(x, torch.Tensor) and x.dtype == torch.int)