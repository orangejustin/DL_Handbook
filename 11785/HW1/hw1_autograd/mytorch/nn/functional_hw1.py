import numpy as np
from mytorch.autograd_engine import Autograd

"""
Mathematical Functionalities
    These are some IMPORTANT things to keep in mind:
    - Make sure grad of inputs are exact same shape as inputs.
    - Make sure the input and output order of each function is consistent with
        your other code.
    Optional:
    - You can account for broadcasting, but it is not required 
        in the first bonus.
"""


def add_backward(grad_output, a, b):
    a_grad = grad_output * np.ones(a.shape)
    b_grad = grad_output * np.ones(b.shape)
    return a_grad, b_grad


def sub_backward(grad_output, a, b):
    # TODO: implement the backward function for subtraction.
    raise NotImplementedError


def matmul_backward(grad_output, a, b):
    # TODO: implement the backward function for matrix product.
    raise NotImplementedError



def mul_backward(grad_output, a, b):
    # TODO: implement the backward function for multiply.
    raise NotImplementedError


def div_backward(grad_output, a, b):
    # TODO: implement the backward function for division.
    raise NotImplementedError


def log_backward(grad_output, a):
    # TODO: implement the backward function for log.
    raise NotImplementedError


def exp_backward(grad_output, a):
    # TODO: implement the backward function for calculating exponential.
    raise NotImplementedError


def max_backward(grad_output, a):
    # TODO: implement the backward function for max.
    pass


def sum_backward(grad_output, a):
    # TODO: implement the backward function for sum.
    pass


def SoftmaxCrossEntropy_backward(grad_output, a):
    """
    TODO: implement Softmax CrossEntropy Loss here. You may want to
    modify the function signature to include more inputs.
    NOTE: Since the gradient of the Softmax CrossEntropy Loss is
          is straightforward to compute, you may choose to implement
          this directly rather than rely on the backward functions of
          more primitive operations.
    """
    pass

