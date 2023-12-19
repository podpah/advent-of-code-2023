Today was quite straightforward
Part 2 took 11s to run so maybe could look at improving it if I have time. Possibly something like looking until I find the first match, then reversing and looking from the back until I find the last match

On my computer part 2 unoptimized took 4.19s meanwhile the efficient way took 1.12s
```shell
% time python day6/part2.py                                        ✔
36919753
python day6/part2.py  4.19s user 0.02s system 99% cpu 4.220 total
```
```shell
% time python day6/part2_efficient.py                       ✔  4s 
36919753
python day6/part2_efficient.py  1.12s user 0.00s system 99% cpu 1.124 total
```
So my second solution was 3.74x faster
The quadratic solution was also considerably faster, needless to say:
```shell
% time python day6/part2_quadratic.py                                 ✔
36919753
python day6/part2_quadratic.py  0.00s user 0.01s system 46% cpu 0.024 total
```
Which makes it 419x faster than the brute force option, and 112x faster than the backtracking solution