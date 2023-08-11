# Pyramid Calculator

# The pyramid is stacked according to one simple principle:
# each lower layer contains one block more than the layer above.
# See ../Screenshots/pyramid.png for a visual

# Write a program which reads the number of blocks the builders have,
# and outputs the height of the pyramid that can be built using these
# blocks.

# Note: the height is measured by the number of fully completed layers -
# if the builders don't have a sufficient number of blocks and cannot
# complete the next layer, they finish their work immediately.

# Starter Code:
# blocks = int(input("Enter the number of blocks: "))

# height = 0
# in_layer = 1
# while in_layer <= blocks:
    # The body of the while loop.

# print("The height of the pyramid:", height)

# This programmer's note: The layer number is equal to the number
# of blocks at the base. 

# Ask user to input number of blocks available
blocks = int(input('Enter the number of blocks: '))

# Start the pyramid's height at zero as no blocks have been laid yet.
height = 0

# Declare a next_layer variable to store blocks needed for next layer.
next_layer = 1

# Building can continue as long as there are more avaiable blocks
# than those necessary for the next pyramid layer.
while next_layer <= blocks:
    # add a layer to the pyramid's actual height
    height += 1
    # subtract blocks used for previous layer
    blocks = blocks - next_layer
    # update the next_layer variable
    next_layer += 1

# Get the proper grammar for the unit of height (layers).
if height != 1:
    layer_grammar = 'layers'
else:
    layer_grammar = 'layer'

print('The height of the pyramid:', height, layer_grammar)
