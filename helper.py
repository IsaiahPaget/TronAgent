import matplotlib.pyplot as plt
from IPython import display

plt.ion()

def plot(results_to_plot):
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()
    plt.title('Training...')
    plt.xlabel('number of games')
    plt.ylabel('score')
    plt.ylim(ymin=0)

    for results in results_to_plot:
        scores = results.scores
        mean_scores = results.mean_scores
        plt.plot(scores)
        plt.plot(mean_scores)
        plt.text(len(scores) - 1, scores[-1], str(scores[-1]))
        plt.text(len(mean_scores) - 1, mean_scores[-1], str(mean_scores[-1]))
    plt.show(block=False)
    plt.pause(.1)
