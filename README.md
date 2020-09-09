# Python_Examples


Example Python projects are in the Python_Examples repository.


Optimization_s1_s2_q_Partial_Data.py is an optimization script that was used for validation of the optimization routine in Excel used in my dissertation project. This script is titled, "Partial_Data" because this particular upload to github provides a sample of the experimental data as an example. The script finds parameter values s1, s2, and q by matching the amplitude (A), period (P) and normalized center of mass (ZCOM) in our inverted pendulum model to experimental values from cats walking on split-belt treadmills in different speed conditions. 

We optimize using the following pdf function:

pdf ~ exp(-1.2)*( (A-A(s1,s2,q))^2/(deltaA)^2 + (P-P(s1,s2,q))^2/(deltaP)^2 + (Zcom-Zcom(s1,s2,q))^2/(deltaZcom)^2 )

where delta is the standard error of A, P, and Zcom respectively.

When A=A(s1,s2,q) , P=P(s1,s2,q), and ZCOM=ZCOM(s1,s2,q), then the inside of the function is about equal to zero and the pdf is about equal to 1.

The script accesses values for A, P, and ZCOM for a speed condition from an Excel sheet called Variable_Values_Partial_Data.xlsx. The control condition is shown as an example in the Excel file and is called "S_0404." In the control condition left and right belts of the split-belt treadmill are equal. In other conditions (not shown in Excel sheet), the right belt was faster than the left belt. It is possible to vary the speed of left and right belts individually in a split-belt treadmill. 