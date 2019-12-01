import matplotlib.pyplot as plt

x = [14, 16, 18, 20, 22]
y = [0.3871217407990079,
    0.41440194222220283,
    0.40019949354954604,
    0.39122271849797563,
    0.36811389976741304]

plt.plot(x, y)
plt.suptitle('20 Newsgroups', fontsize=20)
plt.xlabel('Number of Topics')
plt.ylabel('Coherence Score')
plt.show()