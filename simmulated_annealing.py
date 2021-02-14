import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn')
np.seterr(divide="ignore") # ignore the warning of zero division

# initial solution you'd like to start at
x = 2 # initial x
y = 1 # initial y

# the himmelblau function
# objective function value for x and y
def function(x,y):
    return ((x**2)+y-11)**2+(x+(y**2)-7)**2
z = function(x,y)
print()
print()
print("initial x is: %0.3f" % x)
print("initial y is: %0.3f" % y)
print("initial z is: %0.3f" % z)


# hyperparameters (user inputted parameters)
T0 = 1000 # the temperature (temp.)
temp_for_plot = T0 # for plotting purposes
M = 300 # how many times you will decrease the temp.
N = 15 # how many times you want to search your neighborhood
alpha = 0.85 # by how much do you want to decrease the temp.
k = 0.1 # helps reduce the step-size
           
temp = [] # to plot the temprature
obj_val = [] # to plot the obj val reached at the end of each m (small M)

for i in range(M): # how many times to decrease the temp.

    for j in range(N): # for each m, how many neighborhood searches

        rand_num_x_1 = np.random.rand() # increase or decrease x value?
        rand_num_x_2 = np.random.rand() # by how much?

        if rand_num_x_1 >= 0.5: # greater than 0.5, we increase
            step_size_x = k * rand_num_x_2 # make sure we make a smaller
                                            # step-size
        else:
            step_size_x = -k * rand_num_x_2 # less than 0.5, we decrease

        rand_num_y_1 = np.random.rand() 
        rand_num_y_2 = np.random.rand()
        
        if rand_num_y_1 >= 0.5: # greater than 0.5, we increase
            step_size_y = k * rand_num_y_2 
        else:
            step_size_y = -k * rand_num_y_2 # less than 0.5, we decrease


       
        x_temporary = x + step_size_x 
        y_temporary = y + step_size_y 
        
        obj_val_possible = function(x_temporary,y_temporary)

        # where we are currently
        obj_val_current = function(x,y)

        rand_num = np.random.rand()

        formula = 1/(np.exp((obj_val_possible - obj_val_current)/T0))

        if obj_val_possible <= obj_val_current: 
            x = x_temporary
            y = y_temporary

        elif rand_num <= formula:
            x = x_temporary
            y = y_temporary

        else:
            x = x
            y = y


    temp.append(T0)
    obj_val.append(obj_val_current)

    T0 = alpha*T0

print()
print("x is: %0.3f" % x)
print("y is: %0.3f" % y)
print("obj val is: %0.3f" % obj_val_current)
print()
print("------------------------------")


plt.plot(temp,obj_val)
plt.title("Z at Temperature Values",fontsize=20, fontweight='bold')
plt.xlabel("Temperature",fontsize=18, fontweight='bold')
plt.ylabel("Z",fontsize=18, fontweight='bold')

plt.xlim(temp_for_plot,0)
plt.xticks(np.arange(min(temp),max(temp),100),fontweight='bold')
plt.yticks(fontweight='bold')

plt.show()
