{
    "targets": [
        {
            "target_name": "multihashing",
            "sources": [
                "multihashing.cc",
                "c_aes128.c",
                "blake2s.c",
                "c_blake2s256.c",
                "c_camellia128.c",
                "common.c",
                "c_crc32.c",
                "c_des.c",
                "c_gost.c",
                "c_haval5_256.c",
                "c_hmac_md5.c",
                "jtr_crc32.c",
                "jtr_gost.c",
                "jtr_haval.c",
                "jtr_skein.c",
                "keccak1600.c",
                "my_time.c",
                "oneWayFunction.c",
                "c_rc4.c",
                "c_ripemd160.c",
                "c_sha1.c",
                "c_sha3_256.c",
                "c_sha256.c",
                "c_sha512.c",
                "c_skein512_256.c",
                "c_whirlpool.c",
                "PoW.c"
            ],
            "include_dirs": [
                "crypto",
                "<!(node -e \"require('nan')\")",
            ],
            "cflags": [
                "-D_GNU_SOURCE -maes -fPIC -Ofast -flto -fuse-linker-plugin -funroll-loops -funswitch-loops -fpeel-loops -std=c99"
            ],
            "cflags!": [ 
                "-O2", "-fno-strict-aliasing", "-fno-tree-vrp", "-fno-omit-frame-pointer"
            ],
            "ldflags": [
                "-fPIC -Ofast -flto -fuse-linker-plugin"
            ],
            "cflags_cc": [
                "-std=c++0x -maes -march=native"
            ],
            "conditions": [
                ["OS==\"mac\"", {
                    "defines": ["SYS_OS_MAC"]
                }]
            ]
        }
    ]
}
