import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats


weight = [0.3, 0.5, 0.2]
mean = [1.2, 4.3, 7.7]
std_dev = [0.34, 0.69, 1.4]

start = min(mean) - 3 * max(std_dev)
end = max(mean) + 3 * max(std_dev)
x = np.linspace(start, end, 500)

y0 = stats.norm.pdf(x, mean[0], std_dev[0])
y1 = stats.norm.pdf(x, mean[1], std_dev[1])
y2 = stats.norm.pdf(x, mean[2], std_dev[2])
y = y0 + y1 + y2

plt.plot(x, y0, x, y1, x, y2)
plt.plot(x, y)
# plt.show()


def generate_data(mixture_proportions, mean, std_dev):
    data = []
    for _ in range(200):
        num = np.random.choice([0, 1, 2], p=weight)
        data.append(stats.norm(loc=mean[num], scale=std_dev[num]).rvs())
    return np.array(data)


def Expectation(data, mean, std_dev, weight):
    n1 = np.array(stats.norm.pdf(data, mean[0], std_dev[0])) * weight[0]
    n2 = np.array(stats.norm.pdf(data, mean[1], std_dev[1])) * weight[1]
    n3 = np.array(stats.norm.pdf(data, mean[2], std_dev[2])) * weight[2]
    n = np.array([n1, n2, n3])
    n = n.transpose()
    for i in range(len(n)):
        n[i] = n[i] / sum(n[i])
    return n


def Maximisation(data, posteriori):
    sum_prob = posteriori.sum(axis=0)
    mean = data.dot(posteriori) / sum_prob
    std_dev = []
    for i in range(3):
        temp = (data - mean[i]) ** 2
        var = temp.dot(posteriori[:, i]) / sum_prob[i]
        std_dev.append(var ** 0.5)
    weight = sum_prob / len(data)
    return mean, std_dev, weight


def get_likelihood(data, mean, std_dev, weight):
    likelihood = 0
    for i in range(3):
        likelihood += sum(stats.norm.pdf(data, mean[i], std_dev[i]) * weight[i])
    return likelihood


data = generate_data(weight, mean, std_dev)

random_mean = np.array([5, 7, 10])
random_std_dev = np.array([1, 1, 1])
random_weight = np.array([0.2, 0.6, 0.2])
previous_likelihood = get_likelihood(data, random_mean, random_std_dev, random_weight)

while True:
    posteriori = Expectation(data, random_mean, random_std_dev, random_weight)
    random_mean, random_std_dev, random_weight = Maximisation(data, posteriori)
    likelihood = get_likelihood(data, random_mean, random_std_dev, random_weight)
    print('likelihood', likelihood)
    if likelihood - previous_likelihood < 0.00000000001:
        break
    else:
        previous_likelihood = likelihood

print(random_weight)
print(random_mean)
print(random_std_dev)
print(sum(random_weight))
