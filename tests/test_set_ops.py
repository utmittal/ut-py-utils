from ututils.set_ops import intersect_non_empty


def test_intersect_non_empty_with_two_sets():
    set1 = {0, 1, 2}
    set2 = {0, 2, 3}

    intersection = intersect_non_empty(set1, set2)

    assert intersection == {0, 2}


def test_intersect_non_empty_with_multiple_sets():
    set1 = {0, 1, 2}
    set2 = {0, 2, 3}
    set3 = {0, 1, 4}
    set4 = {0, 1, 3}
    set5 = {0, 6, 7}

    intersection = intersect_non_empty(set1, set2, set3, set4, set5)

    assert intersection == {0}


def test_intersect_non_empty_with_multiple_sets_where_intersection_is_empty():
    set1 = {0, 1, 2}
    set2 = {0, 2, 3}
    set3 = {0, 1, 4}
    set4 = {0, 1, 3}
    set5 = {5, 6, 7}

    intersection = intersect_non_empty(set1, set2, set3, set4, set5)

    assert intersection == set()


def test_intersect_non_empty_other_sets_are_empty():
    set1 = {0, 1, 2}
    set2 = {0, 2, 3}
    set3 = set()

    intersection = intersect_non_empty(set1, set2, set3)

    assert intersection == {0, 2}


def test_intersect_non_empty_set1_is_empty():
    set1 = set()
    set2 = {0, 1, 2}
    set3 = {0, 3, 4}

    intersection = intersect_non_empty(set1, set2, set3)

    assert intersection == {0}


def test_intersect_non_empty_set2_is_empty():
    set1 = {0, 1, 2}
    set2 = set()
    set3 = {0, 3, 4}

    intersection = intersect_non_empty(set1, set2, set3)

    assert intersection == {0}


def test_intersect_non_empty_set1_and_set2_is_empty():
    set1 = set()
    set2 = set()
    set3 = {0, 3, 4}
    set4 = {0, 2, 3}

    intersection = intersect_non_empty(set1, set2, set3, set4)

    assert intersection == {0, 3}


def test_intersect_non_empty_doesnt_modify_arguments():
    set1 = {0, 1, 2}
    set2 = {0, 2, 3}
    set3 = {0, 1, 3}

    intersection = intersect_non_empty(set1, set2, set3)

    assert intersection == {0}
    assert set1 == {0, 1, 2}
    assert set2 == {0, 2, 3}
    assert set3 == {0, 1, 3}


def test_intersect_non_empty_doesnt_modify_arguments_if_only_one_set_non_empty():
    set1 = {0, 1, 2}
    set2 = set()
    set3 = set()

    intersection = intersect_non_empty(set1, set2, set3)

    assert intersection == {0, 1, 2}
    assert set1 == {0, 1, 2}
    assert set2 == set()
    assert set3 == set()
