# Python_Examples


Example Python projects are in the Python_Examples repository.



is an optimization script that finds parameter values s1, s2, and q by matching the amplitude (A), period (P) and normalized center of mass (ZCOM) in our inverted pendulum model to those of cats walking on split-belt treadmills in different speed conditions. 

When A=A(s1,s2,q) , P=P(s1,s2,q), and ZCOM=ZCOM(s1,s2,q), then the inside of the function is about equal to zero and the pdf is about equal to 1.
image.png

The script accesses values for A, P, and ZCOM for one speed condition from an Excel sheet - the control called "S_0404" is where left and right belts of the split-belt treadmill are equal. In other conditions (not shown in Excel sheet), the right belt was faster than the left belt. It is possible to vary the speed of left and right belts individually in a split-belt treadmill. 
