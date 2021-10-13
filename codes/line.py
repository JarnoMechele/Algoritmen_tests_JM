class line:
  def line_distance(self, x1 , y1, x2, y2):
    result = ((((x2 - x1)**2) + ((y2 - y1) ** 2)) ** 0.5)
    return print(result)

line = line()

line.line_distance(8,3,3,4)