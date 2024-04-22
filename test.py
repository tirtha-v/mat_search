import mat_search


def test_mat():
    assert mat_search.get_mat(
        "dvztq5mRsEEl3o40YsimTrGItvOBXU1h", "band_gap", 0.1, 0.12, 1
    ) == ["Ag8 Te4"]
