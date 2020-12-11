import numpy as np
import pandas as pd
import sys
from arg import read_argv
from binning import binning_data_sessions
from denoise import remove_bg_noise
from output import save_sessions
from null import add_null
from plot import plot_single_cell, plot_activity_hist
from scale import scale_data

print("Reading params...")
params = read_argv()
filename = params["filename"]
filecore = filename.split(".")[0]
session_sizes = params["session_sizes"]
session_names = params["session_names"]
highpass = params["highpass"]
bin_size = params["bin_size"]
suffix = params["suffix"]
n_null = params["n_null"]
if suffix == 1:
    session_names = [filecore + "_" + sn for sn in session_names]

print("Reading Ca imaging file...")
data = pd.read_csv(filename, header=None).values
plot_single_cell(data, filecore+"_before_filter.png", "before filter")

print("Denoising Ca activity...")
data_denoise = remove_bg_noise(data, highpass)
plot_single_cell(data_denoise, filecore+"_after_filter.png", "after filter")

_ = plot_activity_hist(data_denoise, filecore+"_dist.png", "Distribution of ΔF/F", positive=True)

global data_bin
if bin_size > 1:
    print("Binning Ca activity...")
    data_bin = binning_data_sessions(data_denoise, bin_size, session_sizes)
    plot_activity_hist(data_bin, filecore+"_dist_bin.png", "Distribution of ΔF/F (Binned)", positive=True)
    session_sizes = [int(np.ceil(i/bin_size)) for i in session_sizes]
else:
    data_bin = data_denoise

print("Scaling Ca activity...")
data_scale = scale_data(data_bin)
b = plot_activity_hist(data_scale, filecore+"_dist_scale.png", "Distribution of ΔF/F (Scaled)", positive=True)

print("Adding null cells...")
data_null = add_null(data_scale, n_null)
plot_activity_hist(data_null, filecore+"_dist_null.png", "Distribution of ΔF/F (Null)", positive=True, bins=b, num_cells=-4)

print("Making save files...")
save_sessions(data_null, session_sizes, session_names)