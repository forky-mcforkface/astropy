from astropy.nddata import NDData, NDIOMixin, NDDataRef


# Alias NDDataAllMixins in case this will be renamed ... :-)
NDDataIO = NDDataRef


def test_simple_write_read(tmpdir):
    ndd = NDDataIO([1, 2, 3])
    assert hasattr(ndd, 'read')
    assert hasattr(ndd, 'write')
