# imports are always needed
import torch

n_gpus = torch.cuda.device_count()

# get number of GPUs available
print(f"GPUs available: {n_gpus}") # returns 1 in my case

for i in range(n_gpus):
	# get index and name of the device
	print(f"{i}: {torch.cuda.get_device_name(i)}")

print("You can also try 'nvidia-smi' from the command line.")
