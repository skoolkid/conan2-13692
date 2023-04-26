from conan import ConanFile

class pkgRecipe(ConanFile):
    name = "pkg"
    version = "0.1"
    settings = "os"
    win_bash_run = True

    def build(self):
        self.run("echo HELLO", scope="run")
