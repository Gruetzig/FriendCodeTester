# FriendCodeTester
bruteforces through nintendo 3ds friend codes 

### Usage

```python3 friendcode.py <friendcode>```

Example:
```python3 friendcode.py 461423505```

* Note that it only accepts 1-12 characters, no '-'

Output:

amount of cycles, in this case
```
999
```
log.txt with all possible combinations, in this case
```
461423505092
461423505148
461423505258
461423505329
461423505356
461423505390
461423505447
461423505453
461423505513
461423505656
461423505682
461423505750
```

log.txt will be reset when launching


### Explanation

friend code has some check that makes it cool https://3dbrew.org/wiki/FRDU:IsValidFriendCode
possible use cases: broken screen, want to find possible solutions

