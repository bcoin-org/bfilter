{
  "variables": {
    "bfilter_byteorder%":
      "<!(/usr/bin/env python2 -c 'from __future__ import print_function; import sys; print(sys.byteorder)')",
  },
  "targets": [{
    "target_name": "bfilter",
    "sources": [
      "./src/murmur3.cc",
      "./src/bfilter.cc"
    ],
    "cflags": [
      "-Wall",
      "-Wno-implicit-fallthrough",
      "-Wno-maybe-uninitialized",
      "-Wno-uninitialized",
      "-Wno-unused-function",
      "-Wextra",
      "-O3"
    ],
    "cflags_c": [
      "-std=c99"
    ],
    "cflags_cc+": [
      "-std=c++0x"
    ],
    "include_dirs": [
      "<!(node -e \"require('nan')\")"
    ],
    "conditions": [
      ["bfilter_byteorder=='little'", {
        "defines": [
          "BFILTER_LITTLE_ENDIAN"
        ]
      }, {
        "defines": [
          "BFILTER_BIG_ENDIAN"
        ]
      }]
    ]
  }]
}
