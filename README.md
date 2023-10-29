# Circle Detection

<h2>Problem Statement</h2>
<p>Given a sequence of edge points loosely representing a shape such as Circle, Dumble, Bubblebox etc. The program should report circles each circumscribing minimum of 4 points from the sequence.</p>
<h2>Input Format</h2>
<p>A list of tuples [(x,y)] each representing a 2D point in x-y plane</p>

> python main.py <i>file_path</i> <i>linear_error</i>

linear_error is unity (by default)

<h2>Output Format</h2>
<p>
  Bounding Box Size : float <br>
  Detected Circles : int <br>
  === <br>
  CRP <br>
  === <br>
  center in xy coordinates <br>
  radius <br>
  points belonging to this circle <br>
  ==== <br>
  ...
</p>

<h2>Examples</h2>
<p>
  To create the test cases, the figures were made by plotting equations as in 'dimensions' on desmos.com. <br>
  From the plotting, points were derived which were jotted down to text file.<br>
  Find Test Cases in tc directory for details. <br>
<div style="align-items:center;">  
  
  <u>1. Circle</u>

  ![Screenshot (341)](https://github.com/AT3140/circle_detection/assets/88228233/564df563-301d-46c8-8c45-5a89a495cce0)

  <u>2. Dumble</u>
 
  ![Screenshot (340)](https://github.com/AT3140/circle_detection/assets/88228233/aff14924-1b8b-448a-a72f-72a7b2aea3ab)

</div>
  Dimensions as equations of circles and straight lines have been used to construct the shapes <br>
</p>

<h2>Sample Run</h2>

![Screenshot (338)](https://github.com/AT3140/circle_detection/assets/88228233/73ccda9a-497f-4615-8d60-a2bd5ace9b8e)
