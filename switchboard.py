import os

from texasbbq import (
    main,
    execute,
    conda_install,
    git_ls_remote_tags,
    IntegrationTestProject,
    setup_git,
)


class DaskSource:

    module = __name__

    @property
    def name(self):
        return "dask"

    @property
    def needs_clone(self):
        return bool(self.clone_url)

    @property
    def clone_url(self):
        return "https://github.com/dask/dask"

    @property
    def target_tag(self):
        return "master"

    def install(self, env):
        setup_git(self)
        execute("conda run -n {} pip install -e .".format(env))
        os.chdir("../")


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
        optional = [
            "scipy",
            "zarr",
            "netCDF4",
            "bottleneck",
            "cartopy",
            "pynio",
            "pseudonetcdf",
        ]
        testing = ["pytest"]
        all_deps = required + optional + testing
        return [" ".join(all_deps)]

    def install(self):
        execute("pip install -e .")

    def run_tests(self):
        execute("pytest xarray")


if __name__ == "__main__":
    main(DaskSource())
