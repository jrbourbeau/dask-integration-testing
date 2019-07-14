import os

from texasbbq import (
    main,
    execute,
    conda_install,
    git_ls_remote_tags,
    IntegrationTestGitSource,
    IntegrationTestProject,
    setup_git,
)


class DaskSource(IntegrationTestGitSource):

    module = __name__

    @property
    def name(self):
        return "dask"

    @property
    def clone_url(self):
        return "https://github.com/dask/dask"

    @property
    def git_ref(self):
        return "master"

    @property
    def install_command(self):
        return "pip install -e ."


class XarrayTests(IntegrationTestProject):
    @property
    def name(self):
        return "xarray"

    @property
    def clone_url(self):
        return "https://github.com/pydata/xarray"

    @property
    def target_tag(self):
        return "master"

    @property
    def conda_dependencies(self):
        required = ["numpy", "pandas"]
        optional = ["scipy", "zarr", "netCDF4", "bottleneck"]
        testing = ["pytest", "hypothesis"]
        all_deps = required + optional + testing
        return [" ".join(all_deps)]

    def install(self):
        execute("pip install -e .")

    def run_tests(self):
        execute("pytest xarray")


if __name__ == "__main__":
    main(DaskSource())
