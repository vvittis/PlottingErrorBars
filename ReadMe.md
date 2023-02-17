# Plotting Error bars 

This project plots the objective values with error bars of 3 different Algorithms in 4 different Queries.



## Data Structure 

This project considers that it has 3 time series with the y values to be plotted
(y_direct, y_package, y_acc), along side with their respective standard errors (y_direct_error,y_package_error,y_acc_error)

We have to be careful that all of these time series have the same size.

    For example:
        if we have a dataset if initial size of 100.000 tuples and a step of 100 tuples
            we are expecting all our time series to have a size of 1.000. 
            (we want to show 1.000 points with their respective error bars)


Because we want to plot for example y_direct in 4 different plots. y_direct should be an array of 4 arrays.
Therefore, when we want to plot y_direct for the first query, we will call y_direct[0].

## Plotting Structure

At each subplot (1 out of 4)

```python
    ax.errorbar(x, y_direct[i], yerr=y_direct_error[i], markersize=4, fmt='o', ls='dotted', color='red', capsize=5)
    ax.errorbar(x, y_package[i], yerr=y_package_error[i], markersize=5, fmt='x', ls='dotted', color='blue', capsize=5)
    ax.errorbar(x, y_acc[i], yerr=y_acc_error[i], markersize=4, fmt='o', ls='dotted', color='green', capsize=5)
```
Both x and y values are ARRAYS. We don't call errorbar function for each point but for the whole object we want to plot.


The function errorbar takes 3 main parameters
1. x: which is the set of values in the x-axis
2. y: which is the set of values in y-axis
3. yerr: the standard error in the y-axis.

There is also xerror thad adds an error bar to the x-axis at each point.

The number of test/queries is parameterized.

```python
    fig, axes = plt.subplots(1, NUMBER_OF_TESTS, figsize=(20, 5))
```

Finally, it's up to you if you want to add custom x ticks to the x-axis.
This project splits the x-axis in 3 even spaces, based on the dataset size.

```python
    ax.set_xticks([initial_size, checkpoint1, checkpoint2, checkpoint3, dataset_size])
    ax.tick_params(axis="x", direction="in")
    ax.tick_params(axis="y", direction="in")
    ax.grid(axis="x", alpha=1, linestyle=":")
```

As I have seen, this pattern of choosing some reference points is widely used in research.

The project itself has some description about the nature and use of the parameters.
