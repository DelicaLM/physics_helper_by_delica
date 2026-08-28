import error_helper_by_delica as error_lib


def calc_momentum_1d(mass, velocity, use_sig_figs=False):
    error_lib.check_type(mass, float, "mass", alt_type=int)
    error_lib.check_value_is_positive_or_zero(mass, "mass")
    error_lib.check_type(velocity, float, "velocity", alt_type=int)
    return mass * velocity

def calc_momentum_2d(mass, v_x, v_y, use_sig_figs=False):
    error_lib.check_type(mass, float, "mass", alt_type=int)
    error_lib.check_value_is_positive_or_zero(mass, "mass")
    error_lib.check_type(v_x, float, "x-velocity", alt_type=int)
    error_lib.check_type(v_y, float, "y-velocity", alt_type=int)
    return mass * v_x, mass * v_y

def calc_momentum_3d(mass, v_x, v_y, v_z, use_sig_figs=False):
    error_lib.check_type(mass, float, "mass", alt_type=int)
    error_lib.check_value_is_positive_or_zero(mass, "mass")
    error_lib.check_type(v_x, float, "x-velocity", alt_type=int)
    error_lib.check_type(v_y, float, "y-velocity", alt_type=int)
    error_lib.check_type(v_z, float, "z-velocity", alt_type=int)
    return mass * v_x, mass * v_y, mass * v_z








