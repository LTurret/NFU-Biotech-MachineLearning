# MachineLearning Practices

![anna](./image/Anna.jpg)
Biotechnology class one of first grade, 41047320

## Content

[繁體中文](README.zh-TW.md) | English

1. **pandas**
   1. [Create `Series` object](./src/1.pandas/PRACTICE_1_pandas_01.py)
   2. [Array indexing](./src/1.pandas/PRACTICE_1_pandas_02.py)
   3. [Create `Series` object with `Dictionary`](./src/1.pandas/PRACTICE_1_pandas_03.py)
   4. [Replace element](./src/1.pandas/PRACTICE_1_pandas_04.py)
   5. [`drop()`](./src/1.pandas/PRACTICE_1_pandas_05.py)
   6. [`append()`](./src/1.pandas/PRACTICE_1_pandas_06.py)
   7. [Using `Series` functions to data statistics](./src/1.pandas/PRACTICE_1_pandas_07.py)
   8. [Filter data with `Series` syntax](./src/1.pandas/PRACTICE_1_pandas_08.py)
   9. [Sort data with `Series` functions](./src/1.pandas/PRACTICE_1_pandas_09.py)
   10. [Create `DataFrame` object with `Dictionary`](./src/1.pandas/PRACTICE_1_pandas_10.py)
   11. [Reshape `DataFrame` spaces](./src/1.pandas/PRACTICE_1_pandas_11.py)
2. **numpy**
    1. [Create `DataFrame` and create with custom index indent](./src/2.numpy/PRACTICE_2_numpy_1.py)
    2. [`DataFrame` exhibition manipulations-1](./src/2.numpy/PRACTICE_2_numpy_2.py)
    3. [`DataFrame` exhibition manipulations-2](./src/2.numpy/PRACTICE_2_numpy_3.py)

## Troubleshooting

   1. File name issue
   2. DataFrame length issue
   3. DataFrame reshape issue
   4. LaTex issue

### File name issue

Don't ever name your file to `pandas.py`  
exception occoured with a mystery faces

### DataFrame length issue

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

Change element `dic[1]` to `list("bird")` makes compile successfully due to `list("bird")` has the same length to other element.

### DataFrame reshape issue

`pd.reshape()` makes user specific DataFrame size.

For example:

```py
df = pd.DataFrame(np.random.randint(0, 100, 5).reshape(3, 4))
```

Notice here that `np.random.randint()` is creating a list which length is 5, but `.reshape()` is reshape it to a irrational space which length is $3\times 4=12$

```console
$ python ./PRACTICE_1_pandas_11.py

Traceback (most recent call last):
   ValueError: cannot reshape array of size 5 into shape (3,4)
```

### LaTex issue

Github doesn't support latex haha  
[check this](https://gist.github.com/a-rodin/fef3f543412d6e1ec5b6cf55bf197d7b)
