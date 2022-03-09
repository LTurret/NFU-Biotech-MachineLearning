# 千萬不要

把檔名取作pandas.py  
不然會出問題  

## Content

1. **pandas**
   1. Create `Series` object
   2. Indexing
   3. Create with `Dictionary`
   4. Replace element
   5. `drop()`
   6. `append()`
   7. Using `Series` functions to statistics
   8. Filter with `Series` syntax
   9. Sort with `Series` functions
   10. Create DataFrame with Dictionary
   11. Reshape DataFrame

## DataFrame length issue

When creating DataFrame with Dictionary, All arrays must be of the same length.  

For example:

```py
dic = {
    1: list("quote"),
    2: [2,4,6,8],
    3: True,
    4: 3.141
}
```

```console
$ python ./PRACTICE_1_pandas_10.py

Traceback (most recent call last):
   ValueError: All arrays must be of the same length
```

Change element `dic[1]` to `list("bird")` makes compile successfully due to list("bird") has the same length to other element.

## DataFrame reshape issue

`pd.reshape()` makes user specific DataFrame size.

For example:

```py
df = pd.DataFrame(np.random.randint(0, 100, 5).reshape(3, 4))
```

Notice here that `np.random.randint()` is creating a list which length is 5, but `.reshape()` is assign it to reshape a irrational space which lenth is $3\times 4=12$

```console
$ python ./PRACTICE_1_pandas_11.py

Traceback (most recent call last):
   ValueError: cannot reshape array of size 5 into shape (3,4)
```

## LaTex issue

Github doesn't support latex haha  
[check this](https://gist.github.com/a-rodin/fef3f543412d6e1ec5b6cf55bf197d7b)
