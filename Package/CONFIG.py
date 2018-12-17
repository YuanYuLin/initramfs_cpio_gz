import ops
import iopc

pkg_path = ""
output_dir = ""
initramfs_name = "initramfs.cpio.gz"
mkinitramfs = "mkinitramfs.sh"
initramfs_file = ""

def set_global(args):
    global pkg_path
    global output_dir
    global initramfs_file
    pkg_path = args["pkg_path"]
    output_dir = args["output_path"]
    initramfs_file = ops.path_join(iopc.getOutputRootDir(), initramfs_name)

def MAIN_ENV(args):
    set_global(args)

    ops.exportEnv(ops.setEnv("LINUX_INITRAMFS_NAME", initramfs_name))
    return False

def MAIN_EXTRACT(args):
    set_global(args)

    return True

def MAIN_PATCH(args, patch_group_name):
    set_global(args)
    for patch in iopc.get_patch_list(pkg_path, patch_group_name):
        if iopc.apply_patch(output_dir, patch):
            continue
        else:
            sys.exit(1)

    return True

def MAIN_CONFIGURE(args):
    set_global(args)

    return True

def MAIN_BUILD(args):
    set_global(args)

    ops.copyto(ops.path_join(pkg_path, mkinitramfs), iopc.getOutputRootDir())
    CMD = [ops.path_join(iopc.getOutputRootDir(), mkinitramfs), ops.path_join(iopc.getOutputRootDir(), "rootfs"), initramfs_file]
    res = ops.execCmd(CMD, iopc.getOutputRootDir(), False, None)
    print res

    return False

def MAIN_INSTALL(args):
    set_global(args)

    return False

def MAIN_SDKENV(args):
    set_global(args)

    return False

def MAIN_CLEAN_BUILD(args):
    set_global(args)
    return False

def MAIN(args):
    set_global(args)
    print "initramfs_cpio_gz"

