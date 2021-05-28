import matplotlib.pyplot as plt

history = dict()
history['acc'] = list()
history['val_acc'] = list()
history['loss'] = list()
history['val_loss'] = list()
with open("./raw/guonihe.txt", "r") as f:
    line = f.readline()
    while line:
        line = line.split()
        if len(line) == 12:
            pass
        if len(line) == 6:
            history['loss'].append(line[2].split(",")[0])
            history['acc'] .append(line[5])
            history['val_acc'].append(line[5])
            history['val_loss'].append(line[2].split(",")[0])
        line = f.readline()
    pass
# 创建一个绘图窗口
plt.figure()

acc = history['acc']
val_acc = history['val_acc']
loss = history['loss']
val_loss = history['val_loss']

epochs = range(len(acc))

plt.plot(epochs, acc, 'b', label='Training acc')  # 'bo'为画蓝色圆点，不连线
# plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.legend()  # 绘制图例，默认在右上角

plt.figure()

plt.plot(epochs, loss, 'b', label='Training loss')
# plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.legend()

plt.show()
