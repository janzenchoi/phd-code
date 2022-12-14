"""
 Title:         Symmetry Matrices
 Description:   For returning symmetry matrices
 Author:        Janzen Choi
"""

# Returns symmetry matrices
def get_symmetry_matrices(type = "cubic"):
    if type == "cubic":
        return get_cubic_symmetry_matrices()
    elif type == "hexagonal":
        return get_hexagonal_symmetry_matrices()
    elif type == "tetrahedral":
        return get_tetrahedral_symmetry_matrices()

# Returns the cubic symmetry matrices
def get_cubic_symmetry_matrices():
    return [
        [[1,0,0], [0,1,0], [0,0,1]],
        [[0,0,1], [1,0,0], [0,1,0]],
        [[0,1,0], [0,0,1], [1,0,0]],
        [[0,-1,0], [0,0,1], [-1,0,0]],
        [[0,-1,0], [0,0,-1], [1,0,0]],
        [[0,1,0], [0,0,-1], [-1,0,0]],
        [[0,0,-1], [1,0,0], [0,-1,0]],
        [[0,0,-1], [-1,0,0], [0,1,0]],
        [[0,0,1], [-1,0,0], [0,-1,0]],
        [[-1,0,0], [0,1,0], [0,0,-1]],
        [[-1,0,0], [0,-1,0], [0,0,1]],
        [[1,0,0], [0,-1,0], [0,0,-1]],
        [[0,0,-1], [0,-1,0], [-1,0,0]],
        [[0,0,1], [0,-1,0], [1,0,0]],
        [[0,0,1], [0,1,0], [-1,0,0]],
        [[0,0,-1], [0,1,0], [1,0,0]],
        [[-1,0,0], [0,0,-1], [0,-1,0]],
        [[1,0,0], [0,0,-1], [0,1,0]],
        [[1,0,0], [0,0,1], [0,-1,0]],
        [[-1,0,0], [0,0,1], [0,1,0]],
        [[0,-1,0], [-1,0,0], [0,0,-1]],
        [[0,1,0], [-1,0,0], [0,0,1]],
        [[0,1,0], [1,0,0], [0,0,-1]],
        [[0,-1,0], [1,0,0], [0,0,1]],
    ]

# Returns the hexagonal symmetry matrices
def get_hexagonal_symmetry_matrices():
    a = (3 ** 0.5) / 2
    return [
        [[1,0,0], [0,1,0], [0,0,1]],
        [[-0.5,a,0], [-a,-0.5,0], [0,0,1]],
        [[-0.5,-a,0], [a,-0.5,0], [0,0,1]],
        [[0.5,a,0], [-a,0.5,0], [0,0,1]],
        [[-1,0,0], [0,-1,0], [0,0,1]],
        [[0.5,-a,0], [a,0.5,0], [0,0,1]],
        [[-0.5,-a,0], [-a,0.5,0], [0,0,-1]],
        [[1,0,0], [0,-1,0], [0,0,-1]],
        [[-0.5,a,0], [a,0.5,0], [0,0,-1]],
        [[0.5,a,0], [a,-0.5,0], [0,0,-1]],
        [[-1,0,0], [0,1,0], [0,0,-1]],
        [[0.5,-a,0], [-a,-0.5,0], [0,0,-1]],
    ]

# Returns the tetrahedral symmetry matrices
def get_tetrahedral_symmetry_matrices():
    return [
        [[1,0,0], [0,1,0], [0,0,1]],
        [[-1,0,0], [0,1,0], [0,0,-1]],
        [[1,0,0], [0,-1,0], [0,0,-1]],
        [[-1,0,0], [0,-1,0], [0,0,1]],
        [[0,1,0], [-1,0,0], [0,0,1]],
        [[0,-1,0], [1,0,0], [0,0,1]],
        [[0,1,0], [1,0,0], [0,0,-1]],
        [[0,-1,0], [-1,0,0], [0,0,-1]],
    ]