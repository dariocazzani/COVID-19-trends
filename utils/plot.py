import matplotlib.pyplot as plt
import numpy as np

def plot(confirmed, align_indexes, align_around, title):
    # Simple graph
    plt.subplot(2, 3, 1)
    for c, v in confirmed.items():
        if c == "Italy" or c == "VA":
            linewidth = 2.5
        else:
            linewidth = 1.4
        plt.plot(v, label=c, linewidth=linewidth)

    plt.legend(loc="upper left")
    plt.title(f"Number of {title}", fontsize=14, fontweight='bold')
    plt.xlabel(f"Days since February 22 2020")
    plt.grid()

    # Simple aligned
    plt.subplot(2, 3, 2)
    for c, v in confirmed.items():
        if c == "Italy" or c == "VA":
            linewidth = 2.5
        else:
            linewidth = 1.4
        plt.plot(v[align_indexes[c]:], label=c, linewidth=linewidth)
        
    plt.legend(loc="upper left")
    plt.title(f"Number of {title}", fontsize=14, fontweight='bold')
    plt.xlabel(f"Days since cases are around {align_around}")
    plt.grid()

    # Logarithm Gradient
    plt.subplot(2, 3, 3)
    for c, v in confirmed.items():
        if c == "Italy" or c == "VA":
            linewidth = 2.5
        else:
            linewidth = 1.4
        array = np.array(v)
        log_array = np.log10(array+1)
        array = np.gradient(log_array)
        plt.plot(array, label=c, linewidth=linewidth)

    plt.legend(loc="upper left")
    plt.title(f"Gradient of number of {title} in log scale", fontsize=14, fontweight='bold')
    plt.xlabel(f"Days since February 22 2020")
    plt.grid()

    # Logarithm
    plt.subplot(2, 3, 4)
    for c, v in confirmed.items():
        if c == "Italy" or c == "VA":
            linewidth = 2.5
        else:
            linewidth = 1.4
        array = np.array(v)
        plt.plot(np.log10(array+1), label=c, linewidth=linewidth)

    plt.legend(loc="upper left")
    plt.title(f"Number of {title} in log scale", fontsize=14, fontweight='bold')
    plt.xlabel(f"Days since February 22 2020")
    plt.grid()

    # Logarithm aligned
    plt.subplot(2, 3, 5)
    for c, v in confirmed.items():
        if c == "Italy" or c == "VA":
            linewidth = 2.5
        else:
            linewidth = 1.4
        array = np.array(v)
        plt.plot(np.log10(array[align_indexes[c]:]+1), label=c, linewidth=linewidth)

    plt.legend(loc="upper left")
    plt.title(f"Number of {title} in log scale", fontsize=14, fontweight='bold')
    plt.xlabel(f"Days since cases are around {align_around}")
    plt.grid()

    # Logarithm aligned Gradient
    plt.subplot(2, 3, 6)
    for c, v in confirmed.items():
        if c == "Italy" or c == "VA":
            linewidth = 2.5
        else:
            linewidth = 1.4
        array = np.array(v)
        alinged_array = array[align_indexes[c]:]
        log_array = np.log10(alinged_array+1)
        array = np.gradient(log_array)
        plt.plot(array, label=c, linewidth=linewidth)

    plt.legend(loc="upper left")
    plt.title(f"Gradient of number of {title} in log scale", fontsize=14, fontweight='bold')
    plt.xlabel(f"Days since cases are around {align_around}")
    plt.grid()

    plt.show()
