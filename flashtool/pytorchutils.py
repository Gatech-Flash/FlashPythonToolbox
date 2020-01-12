
def check_torch_memory(brief=False):
    # prints currently alive Tensors and Variables
    import torch
    import gc
    total_memory = 0
    num_tensors = 0
    for obj in gc.get_objects():
        try:
            if torch.is_tensor(obj) or (hasattr(obj, 'data') and torch.is_tensor(obj.data)):
                if not brief:
                    print("{} \t {} \t Memory: {:.2f} MB".format(type(obj), obj.size(),obj.element_size() * obj.nelement()/1024**2))
                total_memory += obj.element_size() * obj.nelement() /1024**2
                num_tensors += 1
        except:
            pass

    print("Num of tensors: \t {}".format(num_tensors))
    print("Total Memory Cost: \t {:.2f} GB".format(total_memory/1024))
    print("GPU Allocated Memory: \t {:.2f} GB".format(torch.cuda.memory_allocated()/1024**3))
    print("GPU Cached Memory: \t {:.2f} GB".format(torch.cuda.memory_cached()/1024**3))
