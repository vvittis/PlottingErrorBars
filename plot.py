# vasilis vittis

# Reference Article: https://www.geeksforgeeks.org/errorbar-graph-in-python-using-matplotlib/
import matplotlib.pyplot as plt

NUMBER_OF_TESTS = 4


def plot(file, experiment_name, y_axis_label, initial_size, dataset_size, batch_size, y_direct, y_package, y_acc, y_direct_error, y_package_error, y_acc_error, query_ids):
    fig, axes = plt.subplots(1, NUMBER_OF_TESTS, figsize=(20, 5))
    """
    Parameters:
    
    file (string): the name of the file you want to save the plot as
    experiment_name (string): the name of the file you want to save the plot as
    y_axis_label (string): the name of the label in y axis. 
                        (You may want to call the function for different functionalities)
    initial_size (int): the size of the first iteration of your algorithm. 
                        (In my case the experiments don't start from zero, but from a value defined by each experiment e.g. 1000)
    dataset_size (int): the size of your dataset
    batch_size (int): the "step" size
    y_direct, y_package, y_acc (arrays): 2-D arrays containing all the information for NUMBER_OF_TESTS y-values
                                        (if you have 3 queries y_direct will be of the stype [ [0] , [1], [2] ], where each respective value contains an array)
    y_direct_error,y_package_error,y_acc_error (arrays): 2-D arrays containing all the information fro NUMBER_OF_TESTS error values
    query_ids (array): the names of the queries [ 'Query 1' , 'Query 2', 'Query 3'] ln.55
    """

    fig.suptitle('Comparison between Naive Direct, Greedy IPM', fontname="serif", size=20, fontweight="bold")

    i = 0
    for ax in axes:
        x = []
        for value in range(initial_size, dataset_size + 1, batch_size):
            x.append(value)

        plt.rc('font', family='serif')

        range_size = round(dataset_size - initial_size, -2)
        parts = round(range_size / 4, -2)
        checkpoint1_pos = round((initial_size + 1 * parts) / dataset_size, 2) * 100
        checkpoint2_pos = round((initial_size + 2 * parts) / dataset_size, 2) * 100
        checkpoint3_pos = round((initial_size + 3 * parts) / dataset_size, 2) * 100

        checkpoint1 = initial_size + 1 * parts
        checkpoint2 = initial_size + 2 * parts
        checkpoint3 = initial_size + 3 * parts
        ax.errorbar(x, y_direct[i], yerr=y_direct_error[i], markersize=4, fmt='o', ls='dotted', color='red', capsize=5)
        ax.errorbar(x, y_package[i], yerr=y_package_error[i], markersize=5, fmt='x', ls='dotted', color='blue', capsize=5)
        ax.errorbar(x, y_acc[i], yerr=y_acc_error[i], markersize=4, fmt='o', ls='dotted', color='green', capsize=5)

        ax.set_yscale("log")
        ax.set_xticks([initial_size, checkpoint1, checkpoint2, checkpoint3, dataset_size])

        ax.set_xticklabels([str(initial_size / 10) + "%", str(checkpoint1_pos) + "%", str(checkpoint2_pos) + "%", str(checkpoint3_pos) + "%", '100%'])
        ax.tick_params(axis="x", direction="in")
        ax.tick_params(axis="y", direction="in")
        ax.grid(axis="x", alpha=1, linestyle=":")
        ax.set_title(str(query_ids[i]), fontname="serif", size=20, fontweight="bold")
        ax.set_ylabel(y_axis_label)
        ax.set_xlabel('Dataset Size')
        plt.tight_layout()
        i += 1
    fig.legend(["Naive Direct", "Greedy IPM", "Acc. IPM"], loc='center right')
    plt.savefig('figures/plots/' + str(experiment_name) + str(file) + '_all_3_obj_val.pdf', bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    plot()
