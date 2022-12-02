
BEGIN SCULPT

  cell_size = 30.0
  xmin = 0
  ymin = 0
  zmin = 0
  xmax = 150
  ymax = 150
  zmax = 150
  nelx = 5
  nely = 5
  nelz = 5
  
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
