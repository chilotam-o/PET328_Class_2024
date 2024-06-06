# A script to classify and count 'active' and 'inactive'
# gridblocks in a discretized reservoir

#################### Task 1 ############################
    # Request for reservoir dimensions and discretization parameters

# Lx
Lx = float(input('what is the length of the reservoir in the x axis'))
# Ly
Ly = float(input('what is the length of the reservoir in the y axis'))
# Lz
Lz = float(input('what is the length of thw reservoir in the z axis'))
# nx
nx = int(input('what is the number of the gridblocks in x axis'))
# ny
ny = int(input('what is the number of the gridblocks in y axis'))
# nz
nz = int(input('what is the number of the gridblocks in z axis'))


#################### Task 2 ############################
    # Request for the cut-off value
# cut_off
cut_off =

#################### Task 3 ############################
    # Initialize counters

# n_active
n_active = 0
# n_inactive
n_inactive = 0

#################### Task 4 ############################
    # Loop through all blocks (nested loop)
for k in range(1, nz+1):
    # Initialize layer counter
    n_active_layer=0
    # two nested loops go here
    for j range(1, ny +1):
for i in range(1, nx +1):
    perm = float(input("what is the permeabilty value?"))
    if perm < cut_off:
        catergory = 'inactive'
        inactive = n_inactive + 1
    else:
        category ='active'
        n_inactive = n_inactive + 1
        n_inactive_layer = n_inactive_layer + 1
        
    # Print layer count
    print( n_active_layer)

#################### Task 5 ############################
    # Print overall counts

# Print 'active'
all_blocks = n_active + n_active
n_active_percent = (n_active/all_blocks) * 100
round_n_active_percent =
round(n_active_percent,2) =

# Print 'inactive'
print('the percentage of the active blocks in the entire reservoirs is{round_n_active_percent}')
