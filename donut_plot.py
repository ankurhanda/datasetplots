#
# # Pie chart
# labels = ['Frogs', 'Hogs', 'Dogs', 'Logs']
# sizes = [15, 30, 45, 10]
# # colors
# colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
# # explsion
# explode = (0.05, 0.05, 0.05, 0.05)
#
# fig1, ax1 = plt.subplots()
#
# plt.pie(sizes, colors=colors, labels=labels, autopct='%1.1f%%', startangle=90, pctdistance=0.85, explode=explode)
# # draw circle
# centre_circle = plt.Circle((0, 0), 0.70, fc='white')
# fig = plt.gcf()
# fig.gca().add_artist(centre_circle)
# # Equal aspect ratio ensures that pie is drawn as a circle
# ax1.axis('equal')
# plt.tight_layout()
# plt.show()

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import glob

depth_pngs = sorted(glob.glob('/Users/ankurhanda/workspace/code/plots/nyuv2_test/' +'/new_nyu_class13_*.png'))

total_pixel_area = [0]*14

for i in range(0, len(depth_pngs)):

    I = Image.open(depth_pngs[i])

    I = np.array(I)

    for k in range(0, 14):
        pixel_area = I[I==k]
        total_pixel_area[k] += len(pixel_area)

pct = np.array(total_pixel_area)/(64*48*len(depth_pngs))

# labels = ['Missing Values', 'beds', 'books', 'ceiling', 'chair', 'floor', 'furnniture', 'objects',
#           'picture', 'sofa', 'table', 'tv', 'wall', 'window']
#
#
# colors = [[0.5, 0.5, 0.5],[0, 0, 1],[0.9137,0.3490,0.1882],[0, 0.8549, 0],
# [0.5843,0,0.9412],[0.8706,0.9451,0.0941],[1.0000,0.8078,0.8078],
# [0,0.8784,0.8980],[0.4157,0.5333,0.8000],[0.4588,0.1137,0.1608],
# [0.9412,0.1373,0.9216],[0,0.6549,0.6118],[0.9765,0.5451,0],
# [0.8824,0.8980,0.7608]]
#
# # explsion
# explode = (0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05,
#            0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05)
#
# fig1, ax1 = plt.subplots()
#
# plt.pie(pct, colors=colors, labels=labels, autopct='%1.1f%%', startangle=90, pctdistance=0.85, explode=explode)
# # draw circle
# centre_circle = plt.Circle((0, 0), 0.70, fc='white')
# fig = plt.gcf()
# fig.gca().add_artist(centre_circle)
# # Equal aspect ratio ensures that pie is drawn as a circle
# ax1.axis('equal')
# plt.tight_layout()
# plt.show()

import matplotlib.pyplot as plt

plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('Missing Values', 'beds', 'books', 'ceiling', 'chair', 'floor', 'furnniture', 'objects',
          'picture', 'sofa', 'table', 'tv', 'wall', 'window')
y_pos = np.arange(len(objects))
performance = pct #[10, 8, 6, 4, 2, 1]

data = {objects[i]: pct[i] for i in range(0, 14)}
# for i in range(0, 14):
#     data = {objects[i]: pct[i]}


print(data)

sorted(data,key=data.get, reverse=True)

x_objects = []
i = 0

for w in sorted(data, key=data.get, reverse=True):
  print(w, data[w])
  performance[i] = data[w]
  i += 1
  x_objects.append(w)


plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, x_objects, rotation='vertical')
i = 0
for y_value in performance:

    label = "{:.1f}".format(y_value)

    plt.annotate(
            label,                      # Use `label` as label
            (y_pos[i], y_value),         # Place label at end of the bar
            xytext=(0, 13),          # Vertically shift label by `space`
            textcoords="offset points", # Interpret `xytext` as offset in points
            ha='center',                # Horizontally center label
            va='top')

    i += 1

plt.ylabel('Percentage of pixel area')
plt.title('Pixel Area NYUv2')

plt.show()



