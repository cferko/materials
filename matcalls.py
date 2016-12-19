def materialsStudy(fiber_resolution,printing_resolution,annealing_time):

	import numpy as np 
	import matplotlib.pyplot as plt

	strength =  max(0,(10.*fiber_resolution) + 75000*printing_resolution*(3-printing_resolution) - 90.*annealing_time)
	max_speed2 =  max(0,1.0 - (printing_resolution/4.) - (50000.-fiber_resolution)/80000. + .00008*annealing_time )
	max_speed = min(1.0, max_speed2)
	cost = max(0,1500. + 1000.*(3.-printing_resolution) + 0.075*(fiber_resolution) + (0.5*annealing_time))


	fig = plt.figure(figsize=(18,8))

	ax1 = fig.add_subplot(131)
	ax1.plot( [1,1], [0,strength/1000.], lw = 50 ) 
	plt.ylabel('STRENGTH (Meganewtons per square meter)')
	plt.grid()
	plt.ylim([0,550])

	ax2 = fig.add_subplot(132)
	ax2.plot([1,1], [0,max_speed],  lw = 50 )
	plt.ylabel('MAX. SAFE SPEED (fraction of speed of light)')
	plt.ylim([0,1])
	plt.grid()


	ax3 = fig.add_subplot(133)
	ax3.plot([1,1], [0,cost], lw = 50 )
	plt.ylabel('COST (Andromeda Credits)')
	plt.ylim([0,12000])
	plt.grid()

	plt.show()

	return