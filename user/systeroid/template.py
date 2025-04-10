pkgname = "systeroid"
pkgver = "0.4.5"
pkgrel = 1
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "TUI and helper tool for sysctl values"
license = "Apache-2.0 OR MIT"
url = "https://systeroid.cli.rs"
source = (
    f"https://github.com/orhun/systeroid/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "ed8bea7d111de32d0885fd36664bed8a4acb77775a0cc0034d29b5aa5db255e1"
# needs kernel docs to exist
options = ["!check"]

if self.profile().arch in ["loongarch64"]:
    broken = "outdated nix crate, can't update"


def install(self):
    self.install_license("LICENSE-MIT")
    self.install_bin(f"target/{self.profile().triplet}/release/systeroid")
    self.install_bin(f"target/{self.profile().triplet}/release/systeroid-tui")
    self.install_man("man8/systeroid.8")
    self.install_man("man8/systeroid-tui.8")
