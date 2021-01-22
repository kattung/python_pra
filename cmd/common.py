#!/usr/bin/env python3

linux_banner = "Linux version"
login_msg = "buildroot login: "

buildroot_prompt = r'# '

### cmd = [cmd, expected, timeout]
cmd_root = [("root", buildroot_prompt, 5)]

cmd_mnt_sd = [
    ("ls /", buildroot_prompt, 20),
    ("fdisk -l", buildroot_prompt, 5),
    ("mount /dev/mmcblk0p2 /mnt", buildroot_prompt, 30),
    ("ls /mnt", buildroot_prompt, 20),
    ("pwd", buildroot_prompt, 10),
]

cmd_chroot = [
    ("chroot /mnt", buildroot_prompt, 60),
    ("pwd", buildroot_prompt, 10),
    ("ls /", buildroot_prompt, 20),
]

cmd_chroot_sd = [
    cmd_mnt_sd,
    cmd_chroot,
]

cmd_booting = [
    cmd_root,
    cmd_chroot_sd,
]

cmd_ls = [
    ("ls /dev", buildroot_prompt, 3),
    ("ls /bin", "touch", 3),
    (None, buildroot_prompt, 3),
]

cmd_exit_sdrootfs = [
    ("", buildroot_prompt, 3),
    ("exit", buildroot_prompt, 10),
    ("exit", login_msg, 10),
    ("root", buildroot_prompt, 3),
    ("umount /mnt", buildroot_prompt, 10),
    ("ls /mnt", buildroot_prompt, 3),
    ("ls /", buildroot_prompt, 3),
]
