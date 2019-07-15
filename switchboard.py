from texasbbq import main, GitSource, GitTarget


class DaskSource(GitSource):

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


class XarrayTests(GitTarget):
    @property
    def name(self):
        return "xarray"

    @property
    def clone_url(self):
        return "https://github.com/pydata/xarray"

    @property
    def git_ref(self):
        return "master"

    @property
    def conda_dependencies(self):
        required = ["numpy", "pandas", "toolz"]
        optional = ["scipy", "zarr", "netCDF4", "bottleneck"]
        testing = ["pytest", "hypothesis"]
        all_deps = required + optional + testing
        return [" ".join(all_deps)]

    @property
    def install_command(self):
        return "pip install -e ."

    @property
    def test_command(self):
        return "pytest xarray"


if __name__ == "__main__":
    main(DaskSource())
