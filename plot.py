from matplotlib import pyplot as plt
import numpy as np

def plot_single_cell(
        data:np.ndarray, save_name:str="", title:str="", 
        cell_id:int=0, unit:str="x50ms", row_is_cell:bool=True):
    if row_is_cell:
        plt.plot(data[:, cell_id])
    else:
        plt.plot(data[cell_id])
    plt.title(title)
    plt.xlabel("time (" + unit + ")")
    plt.ylabel("ΔF/F")
    if save_name == "":
        plt.show()
    else:
        plt.savefig(save_name)
        plt.close()
    return

def plot_activity_hist(
        data:np.ndarray, save_name:str="", title:str="",
        num_cells:int=4, bins=1000, positive=False, row_is_cell:bool=True):
    if type(bins) == np.ndarray:
        b = bins
    else:
        if row_is_cell:
            if num_cells >= 0:
                b = plt.hist(data[:, :num_cells].reshape(-1), bins=bins)[1]
            else:
                b = plt.hist(data[:, num_cells:].reshape(-1), bins=bins)[1]
        else:
            if num_cells >= 0:
                b = plt.hist(data[:num_cells].reshape(-1), bins=bins)[1]
            else:
                b = plt.hist(data[num_cells:].reshape(-1), bins=bins)[1]
        if positive:
            b = b[b > 0]
    plt.close()
    if num_cells >= 0:
        r = list(range(num_cells))
    else:
        r = [num_cells + i for i in range(-num_cells)]
    for i in r:
        if row_is_cell:
            plt.hist(data[:, i], bins=b, alpha=0.5)
        else:
            plt.hist(data[i], bins=b, alpha=0.5)
    plt.xlabel("ΔF/F")
    plt.ylabel("n")
    plt.title(title)
    if save_name == "":
        plt.show()
    else:
        plt.savefig(save_name)
        plt.close()
    return b