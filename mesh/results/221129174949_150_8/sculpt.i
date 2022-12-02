
BEGIN SCULPT

  cell_size = 18.75
  xmin = 0
  ymin = 0
  zmin = 0
  xmax = 150
  ymax = 150
  zmax = 150
  nelx = 8
  nely = 8
  nelz = 8
  
  pillow = 3
  smooth = 2
  csmooth = 5
  defeature = 1
  laplacian_iters = 10
  max_opt_iters = 100

  quality = true
  micro_shave = true
  remove_bad = 0.0
  
  diatom_file = sculpt.diatom
  exodus_file = sculpt

END SCULPT
