#Exercise: Star printing
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0],
]
def draw_arrow():
  for img in picture:
    for pixel in img:
      if pixel==0:
        print('*',end='')
      else:
        print(' ',end='')
    print()
draw_arrow()
draw_arrow()
draw_arrow()
