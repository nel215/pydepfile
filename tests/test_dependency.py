from pydepfile.dependency import find_dependencies


def test_find_dependencies():
    deps = find_dependencies('examples/dag.py')
    names = list(sorted([d.path.name for d in deps]))
    assert names == ['a.py', 'b.py', 'common.py', 'dag.py', 'stat.py']
