pkgname = "libpulse"
pkgver = "17.0"
pkgrel = 1
build_style = "meson"
configure_args = [
    "-Ddaemon=false",
    "-Ddoxygen=false",
    "-Dtests=false",
    "-Ddatabase=simple",
    "-Dman=true",
    "-Dbashcompletiondir=/usr/share/bash-completion/completions",
]
hostmakedepends = [
    "cmake",
    "meson",
    "perl",
    "perl-xml-parser",
    "pkgconf",
]
makedepends = [
    "dbus-devel",
    "glib-devel",
    "libcap-devel",
    "libsamplerate-devel",
    "libsndfile-devel",
    "linux-headers",
    "orc-devel",
    "udev-devel",
]
# not in a standard path and therefore not picked up by shlib scanner
provides = [f"so:libpulsecommon-{pkgver}.so=0"]
pkgdesc = "PulseAudio library"
license = "LGPL-2.1-or-later"
url = "https://www.freedesktop.org/wiki/Software/PulseAudio"
source = f"$(FREEDESKTOP_SITE)/pulseaudio/releases/pulseaudio-{pkgver}.tar.xz"
sha256 = "053794d6671a3e397d849e478a80b82a63cb9d8ca296bd35b73317bb5ceb87b5"
options = ["linkundefver"]


@subpackage("libpulse-devel")
def _(self):
    return self.default_devel()


@subpackage("libpulse-progs")
def _(self):
    self.pkgdesc = "PulseAudio utilities"
    # installs all zsh comps to single _pulseaudio file
    self.options = ["!lintcomp"]
    return self.default_progs()
