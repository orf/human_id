import uuid

import pytest

from human_id import generate_id


def test_with_seed():
    random_uuid = uuid.uuid4()
    id1 = generate_id(seed=random_uuid)
    id2 = generate_id(seed=random_uuid)
    assert id1 == id2


def test_without_seed():
    id1 = generate_id()
    id2 = generate_id()
    assert id1 != id2


def test_separator():
    result = generate_id(separator="!")
    assert len(result.split("!")) == 4


def test_word_count_throws():
    with pytest.raises(ValueError, match="word_count cannot be lower than 3"):
        generate_id(word_count=1)


def test_word_count():
    result = generate_id(word_count=5)
    assert len(result.split("-")) == 5
