# trivial-map-reduce

Gave up to implement string processing for map & reduce scripts in C++ and went with Haskell. Hope it's not much of a bother.

Compile scripts:
```
ghc word_count/wc_map.hs
ghc word_count/wc_reduce.hs
```
Run examples (using stdin & stdout here):
```
./mapreduce.py map word_count/wc_map word_count/example1.txt /dev/fd/1 | \
./mapreduce.py reduce hs/wc_reduce /dev/fd/0 /dev/fd/1
```
