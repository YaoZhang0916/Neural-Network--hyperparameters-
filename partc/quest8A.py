



import matplotlib.pyplot as plt
 
name_list = ['Logcosh','categorical_hinge','categorical-crossentropy']
num_list = [0.9372,0.9756,0.9789]
plt.bar(range(len(num_list)), num_list,color='rgb',tick_label=name_list)
plt.show()

