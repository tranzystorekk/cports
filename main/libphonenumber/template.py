pkgname = "libphonenumber"
pkgver = "9.0.7"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DREGENERATE_METADATA=OFF",
    "-DUSE_BOOST=OFF",
    "-DUSE_STDMUTEX=ON",
]
make_check_target = "tests"
cmake_dir = "cpp"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "abseil-cpp-devel",
    "gtest-devel",
    "icu-devel",
    "protobuf-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Library for parsing, formatting, and validating phone numbers"
license = "Apache-2.0"
url = "https://github.com/google/libphonenumber"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "15b929c24e9071847893cc2bbeb29631eab819ec6561baaf51250852773348b0"


@subpackage("libphonenumber-devel")
def _(self):
    self.depends += [
        "abseil-cpp-devel",
        "protobuf-devel",
    ]
    return self.default_devel()
