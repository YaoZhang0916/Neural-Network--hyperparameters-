



import matplotlib.pyplot as plt
 
name_list = ['sigmoid','linear','tanh','relu']
num_list = [0.9509,0.9161,0.9782,0.9789]
plt.bar(range(len(num_list)), num_list,color='rgb',tick_label=name_list)
plt.show()

