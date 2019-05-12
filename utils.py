from matplotlib import pyplot as plt


def myplot(ys, labels=None, xs=None, figsize=None):
    # check dimension
    if labels is not None:
        assert len(ys) == len(labels)
    if figsize is not None:
        plt.figure(figsize=(20, 10))
    for i, y in enumerate(ys):
        if xs is None:
            x = range(len(y))
        else:
            x = xs[i]
        if labels is None:
            label = i
        else:
            label = labels[i]
        plt.plot(x, y, label=label)
    plt.legend()
