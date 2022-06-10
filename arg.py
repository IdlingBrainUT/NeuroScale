import sys

def read_argv():
    arg = {"highpass":0.1, "bin_size":1, "suffix":0, "n_null":100, "fmt":5, "zth":0.0}
    i = 1
    n = len(sys.argv)
    while i < n:
        if sys.argv[i] == "-f":
            arg["filename"] = sys.argv[i+1]
            i += 2
            continue
        elif sys.argv[i] == "-ss":
            n_ss = int(sys.argv[i+1])
            i += 2
            arg["session_sizes"] = [int(s) for s in sys.argv[i:i+n_ss]]
            i += n_ss
            continue
        elif sys.argv[i] == "-sn":
            n_sn = int(sys.argv[i+1])
            i += 2
            arg["session_names"] = [n for n in sys.argv[i:i+n_sn]]
            i += n_sn
            continue
        elif sys.argv[i] == "-hp":
            arg["highpass"] = float(sys.argv[i+1])
            i += 2
            continue
        elif sys.argv[i] == "-bs":
            arg["bin_size"] = int(sys.argv[i+1])
            i += 2
        elif sys.argv[i] == "-sf":
            arg["suffix"] = 1
            i += 1
        elif sys.argv[i] == "-nu":
            arg["n_null"] = int(sys.argv[i+1])
            i += 2
        elif sys.argv[i] == "-fmt":
            arg["fmt"] = int(sys.argv[i+1])
            i += 2
        elif sys.argv[i] == "-zth":
            arg["zth"] = float(sys.argv[i+1])
            i += 2
        else:
            raise ValueError("Unknown argv!")
    return arg
