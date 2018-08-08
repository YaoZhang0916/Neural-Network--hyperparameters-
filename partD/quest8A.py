



import matplotlib.pyplot as plt
 
name_list = ['256','650','1024']
num_list = [0.9780,0.9790,0.9784]
plt.bar(range(len(num_list)), num_list,color='rgb',tick_label=name_list)
plt.show()

