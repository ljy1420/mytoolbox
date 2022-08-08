from mlproject.distance import haversine

lat1, lon1 = 48.865070, 2.380009
lat2, lon2 = 31.2364015, 121.4314601

def test_result_type_is_float():
    assert type(haversine(lon1, lat1, lon2, lat2)) == float

def test_result_is_valid():
    assert haversine(lon1, lat1, lon2, lat2) == 9257.638004479584
