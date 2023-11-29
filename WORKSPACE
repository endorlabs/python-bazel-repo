load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

SHA="84aec9e21cc56fbc7f1335035a71c850d1b9b5cc6ff497306f84cced9a769841"
VERSION="0.23.1"

http_archive(
    name = "rules_python",
    sha256 = SHA,
    strip_prefix = "rules_python-{}".format(VERSION),
    url = "https://github.com/bazelbuild/rules_python/releases/download/{}/rules_python-{}.tar.gz".format(VERSION,VERSION),
)

load("@rules_python//python:repositories.bzl", "py_repositories")
py_repositories()

load("@rules_python//python:repositories.bzl", "python_register_toolchains")
python_register_toolchains(
    name = "python_3_11",
    python_version = "3.11",
)

load("@rules_python//python:pip.bzl", "pip_parse")

pip_parse(
   name = "my_deps",
   requirements_lock = "//:requirements.txt",
)
load("@my_deps//:requirements.bzl", "install_deps")
install_deps()

http_archive(
    name = "rules_endor",
    sha256 = "a6cc70e7ce5d6663425aa3b1359267e0a80692c628b0b36a0bde9eb853d3b7e8",
    strip_prefix = "rules_endor-1.1.0",
    urls = [
        "https://github.com/endorlabs/rules_endor/archive/refs/tags/v1.1.0.tar.gz",
    ],
)

load("@rules_endor//endorctl:repositories.bzl", "rules_endorctl_toolchains")
rules_endorctl_toolchains(repository_url = "https://api.staging.endorlabs.com")