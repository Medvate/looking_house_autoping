# Looking house autoping

## Example of result

```
{'138.124.180.32': (' USA, NJ, Secaucus', -1.0),
 '146.19.170.34': (' Poland, Warsaw', 174.23),
 '146.19.75.7': (' Romania, Bucharest', 15.0),
 '146.19.80.3': (' Bulgaria, Sofia', 21.31),
 '77.91.72.6': (' Hungary, Budapest', 166.14),
 '80.92.204.122': (' Germany, Frankfurt am Main', 103.36)}
```

If the ping is -1, then the ip is unavailable.

## How to use

```
$ pip3 install requests==2.27.1 beautifulsoup4==4.11.1 ping3==4.0.3
```

Change URL const in main.py

```
$ python3 main.py
```

