from taichi.lang import impl

import taichi as ti
from tests import test_utils

# TODO: these are not really tests...


@test_utils.test(arch=ti.cuda)
def test_do_nothing():
    @ti.kernel
    def test():
        for i in range(10):
            impl.call_internal("do_nothing")

    test()


@test_utils.test(arch=ti.cuda)
def test_active_mask():
    @ti.kernel
    def test():
        for i in range(48):
            if i % 2 == 0:
                impl.call_internal("test_active_mask")

    test()


@test_utils.test(arch=ti.cuda)
def test_shfl_down():
    @ti.kernel
    def test():
        for i in range(32):
            impl.call_internal("test_shfl")

    test()
