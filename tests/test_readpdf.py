import refs.readpdf

_example_file = 'tests/data/re_manifold.pdf'

def test_geturi():
    uri = refs.readpdf.geturi(_example_file)
    assert uri.startswith('bib')

def test_md5sum():
    assert refs.readpdf.md5sum(_example_file) != refs.readpdf.md5sum(_example_file, include_size=True)
    assert refs.readpdf.md5sum(_example_file) == refs.readpdf.md5sum(_example_file, include_size=False)
    assert refs.readpdf.md5sum(_example_file) != refs.readpdf.md5sum(_example_file, 122)

