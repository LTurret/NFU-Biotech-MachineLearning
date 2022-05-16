# MachineLearning Practices

![anna](./image/Anna.jpg)
Biotechnology class one of first grade, 41047320

## Language

[繁體中文](README.zh-TW.md) | English

## Content

1. Frequently operations  
   - pandas
   - numpy
2. Types of learning method
   1. Supervised learning
      1. Linear Regression
      2. Logistic Regression
3. Troubleshooting
   1. General
      1. File name issue
   2. Technical
      1. DataFrame length issue
      2. DataFrame reshape issue
      3. Linear regression value errors
   3. haha
      1. LaTex issue
4. Documentations
   1. Relative coefficient
   2. 相關程度
   3. 書面資料

## Frequently operations

- **pandas**
   1. [Create `Series` object](./src/1.pandas/PRACTICE_1_pandas_01.py)
   2. [Series indexing](./src/1.pandas/PRACTICE_1_pandas_02.py)
   3. [Create `Series` object with `Dictionary`](./src/1.pandas/PRACTICE_1_pandas_03.py)
   4. [Replace element](./src/1.pandas/PRACTICE_1_pandas_04.py)
   5. [`drop()`](./src/1.pandas/PRACTICE_1_pandas_05.py)
   6. [`append()`](./src/1.pandas/PRACTICE_1_pandas_06.py)
   7. [Using `Series` functions to data statistics](./src/1.pandas/PRACTICE_1_pandas_07.py)
   8. [Filter data with `Series` syntax](./src/1.pandas/PRACTICE_1_pandas_08.py)
   9. [Sort data with `Series` functions](./src/1.pandas/PRACTICE_1_pandas_09.py)
   10. [Create `DataFrame` object with `Dictionary`](./src/1.pandas/PRACTICE_1_pandas_10.py)
   11. [Reshape `DataFrame` spaces](./src/1.pandas/PRACTICE_1_pandas_11.py)
- **numpy**
    1. [Create a m*n matrix using `np.random()`](./src/2.numpy/PRACTICE_2_numpy_01.ipynb)
    2. [Create `DataFrame` and create with custom index indent](./src/2.numpy/PRACTICE_2_numpy_02.ipynb)
    3. [`DataFrame` exhibition manipulations-1, DF's details](./src/2.numpy/PRACTICE_2_numpy_03.ipynb)
    4. [Create `DataFrame` with `Dictionary` then indexing with `head()` and `tail()`](./src/2.numpy/PRACTICE_2_numpy_04.ipynb)  

## Types of learning method

- **Supervised learning**
  - **Linear Regression**
      1. [Linear Regression practice](./src/3.LinearRegression/PRACTICE_3_LR_01.ipynb)
      2. [Linear Regression implement](./src/3.LinearRegression/PRACTICE_3_LR_02.ipynb)
  - **Logistic Regression**
      1. [Logistic Regression practice](./src/4.LogisticRegression/PRACTICE_4_LR_01.ipynb)

## Troubleshooting

### General

#### File name issue

> Don't ever name your file to `pandas.py`  
> `pandas` will raise some unexpected exceptions.

---

### Technical

#### DataFrame length issue

> When creating `DataFrame` with `Dictionary`, All arrays must be of the same length.  

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

The best solution here is make sure every element has the same legth, change the element whom doesn't meet the requirement, Changing `dic[1]` to `list("bird")` to make compile successfully, Due to `list("bird")` has the same length:4 with other elements.

---

#### DataFrame reshape issue

> `pd.reshape()` makes user specific DataFrame size.

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

---

#### Linear regression value errors

> When plotting graph with `test_x` versus `pred`, the graph should plot line with the three dots:
> [1.70, 65.15], [1.75, 68.30], [1.47, 50.63]
>> But it is probably due to there are different data type, `DataFrame` seems like does not match well with `ndarray`

##### defining the variables

```py
pred = model.predict(test_x)
score = mean_squared_error(pred, test_y)
print(f"{test_x}\n{pred}")
```

```console
    Height
9     1.70
11    1.75
0     1.47
[65.14531356 68.30189952 50.62501816]
```

##### plotting the line

```py
plt.plot(test_x, pred, color="r")
```

- ValueError:

```console
ValueError: x and y must have same first dimension, but have shapes (3,) and (1,)
```

- InvalidIndexError:

```console
InvalidIndexError: (slice(None, None, None), None)
```

---

### haha

#### LaTex issue

> Github doesn't support latex, haha  

[check this](https://gist.github.com/a-rodin/fef3f543412d6e1ec5b6cf55bf197d7b)

## Documentations

- Relative coefficient
  - [相關程度](http://amebse.nchu.edu.tw/new_page_517.htm)
  - [書面資料](./docs/Relative%20coefficient)

- Some sort of distance methods
  - E
  - a
  - M
