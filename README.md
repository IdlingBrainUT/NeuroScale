# NeuroScale
NeuroScale performs background noise removal, binning, scaling to standard normal distribution and addition of null cells of calcium imaging data.

## params
-f : filename

-ss: session size 

syntax -> (number of sessions) (size of session 1) (size of session 2) ...

-sn: session name

syntax -> (number of sessions) (name of session 1) (name of session 2) ...

-hp: threshold of highpass filter (default: 0.1Hz)

-bs: bin size (default: 1)

-sf: suffix mode (default: False)

-nu: number of null cells (default: 100)

[example]

-f filename.csv -sn 2 A B

-> A.csv, B.csv are output.

-f filename.csv -sn 2 A B -sf

-> filename_A.csv, filename_B.csv are output.

## usage
```bash
python neuroscale.py -f filename.csv -ss 4 1000 500 1000 2000 -sn 4 A B C D -hp 0.1 -bs 1 -sf
```