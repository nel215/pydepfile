import os


class Presenter:

    def convert(self, deps):
        cwd = os.getcwd()
        res = []
        for d in deps:
            if str(d.path).find(cwd) != 0:
                continue

            res.append(str(d.path.relative_to(cwd)))
        return res
