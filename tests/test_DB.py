import refs.DB
import refs.bibliography
def test_lazy_connect():
    cursor = refs.DB.lazy_connect()
    cursor2 = refs.DB.lazy_connect()
    assert cursor.connection is cursor2.connection

def test_add_lookup():
    cursor = refs.DB.lazy_connect()
    bib = refs.bibliography.Bibliography(
            author='Luis Pedro Coelho',
            title='Universe: Theory and Practice')
    refs.DB.add(bib)
    refs.DB.addlink(bib,'bib+id:123')
    bib2 = refs.DB.lookup('bib+id:123')
    assert bib2 is not None
    assert bib2 == bib.id

