"""
Text Files
Mashrur
Woodlands
Open text file
"""

marks = open('marks.txt')                                                    
lines = marks.readlines()      
marks.close()

awards = open('awards.txt', 'a+')

for i in range(len(lines)): 
  if len(lines[i])==7:
    student_num = lines[i]
    num_courses = int(lines[i+1])
    midterm_sum=0
    final_sum=0
    improved=0
    for m in range(2,num_courses+2):
      marks = lines[i+m].split("$")
      midterm = marks[0]
      final=marks[1][0:2]
      midterm_sum+=int(midterm)
      final_sum+=int(final)
      if final>midterm:improved+=1

      with open("awards.txt", "a+") as text_file:
        text_file.write("\n"+"Student #: "+student_num)
        midterm=round(midterm_sum/num_courses,1)
        final=round(final_sum/num_courses,1)
        text_file.write("Midterm Avg: "+str(midterm)+"\n")
        text_file.write("Final Avg: "+str(final)+"\n")
        if improved/num_courses>=0.5:text_file.write("Award "+"("+str(improved)+"/"+str(num_courses)+" courses improved)\n")
        else: text_file.write("No Award "+ "("+str(improved)+"/"+str(num_courses)+" courses improved)\n")
    

    
