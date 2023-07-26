def pascal_triangle(n):
  if n <= 0: 
    return []
  
  pascal = [[1]]
  
  for i in range(1, n):
    curr_row = [1]
    prev_row = pascal[-1]
    
    for j in range(1, i):
      curr_row.append(prev_row[j-1] + prev_row[j])
      
    curr_row.append(1)
    pascal.append(curr_row)
    
  return pascal
