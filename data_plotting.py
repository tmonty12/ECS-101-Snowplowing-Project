import matplotlib.pyplot as plt
from snowplowProgram import snowplow_program
import numpy as np

sample_edges = [(0,1),(1,2),(1,3),(1,4),(2,3),(3,4),(2,5),(3,5),(4,5)]

syracuse_edges = [(0,1),(0,2),(0,3),(1,6),(1,2),(2,4),(2,5),(2,7),(3,4),(4,5),(4,8),(5,7),(5,8),(6,11),(7,10),(8,9),(9,10),(10,11)]

total_minutes = []
back_tracks = []

for i in range(0,10000):
    result = snowplow_program(12,18,syracuse_edges)
    total_minutes.append(result[0])
    back_tracks.append(result[1])

fig, ax = plt.subplots()

counts, bins, patches = plt.hist(total_minutes, density=False, bins = 20)
plt.ylabel('Occurences')
plt.xlabel('Total Minutes')
plt.title('Snowplow robot average time')
ax.set_xticks(bins)
plt.show()
plt.close()

fig, ax = plt.subplots()

counts, bins, patches = plt.hist(back_tracks, density=False, bins = 20)
plt.ylabel('Occurences')
plt.xlabel('Back Tracks')
plt.title('Snowplow robot average backtracks')
ax.set_xticks(bins)
plt.show()
plt.close()



