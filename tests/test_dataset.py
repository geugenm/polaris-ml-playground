"""pytest framework for dataset module
"""

from polaris.dataset.dataset import PolarisDataset
from polaris.dataset.frame import PolarisFrame
from polaris.dataset.metadata import PolarisMetadata


def test_metadata_creation_from_dict(polaris_metadata_dict):
    """Test creation of PolarisMetadata object from dictionary
    """
    new_metadata_obj = PolarisMetadata(polaris_metadata_dict)
    # Need to add one for the 'data_format_version' key added
    assert len(new_metadata_obj) == len(polaris_metadata_dict) + 1


def test_metadata_creation_from_keywords():
    """Test creation of PolarisMetadata object from keywords
    """
    new_metadata_obj = PolarisMetadata(foo="bar", baz="bum", bling="baz")
    assert new_metadata_obj['foo'] == 'bar'
    assert new_metadata_obj['baz'] == 'bum'
    assert new_metadata_obj['bling'] == 'baz'


def test_metadata_creation_from_json(polaris_metadata_obj):
    """Test metadata creation via from_json(to_json())
    """
    new_metadata_obj = PolarisMetadata()
    new_metadata_obj.from_json(polaris_metadata_obj.to_json())
    assert new_metadata_obj == polaris_metadata_obj


def test_frame_creation_from_dict(polaris_frame_dict):
    """Test creation of PolarisFrame object from dictionary
    """
    new_frame_obj = PolarisFrame(polaris_frame_dict)
    assert len(new_frame_obj) == len(polaris_frame_dict)


def test_frame_creation_from_json(polaris_frame_obj):
    """Test frame creation via from_json(to_json())
    """
    new_frame_obj = PolarisFrame()
    new_frame_obj.from_json(polaris_frame_obj.to_json())
    assert new_frame_obj == polaris_frame_obj


def test_dataset_creation_from_json(polaris_dataset_obj):
    """Test dataset creation to_json() method via from_json(to_json())
    """
    new_dataset_obj = PolarisDataset()
    new_dataset_obj.from_json(polaris_dataset_obj.to_json())
    assert new_dataset_obj == polaris_dataset_obj


def test_dataset_to_json(polaris_dataset_obj, polaris_dataset_json):
    """Test dataset to_json() method
    """
    assert polaris_dataset_obj.to_json() == polaris_dataset_json


def test_dataset_creation_from_frame_list(polaris_metadata_dict,
                                          polaris_frame_dict,
                                          polaris_dataset_obj):
    """Test dataset creation from dictionary objects
    """
    new_dataset_obj = PolarisDataset(metadata=polaris_metadata_dict,
                                     frames=[polaris_frame_dict])
    assert new_dataset_obj == polaris_dataset_obj


def test_dataset_creation_from_single_frame(polaris_metadata_dict,
                                            polaris_frame_dict,
                                            polaris_dataset_obj):
    """Test dataset creation from dictionary objects
    """
    new_dataset_obj = PolarisDataset(metadata=polaris_metadata_dict,
                                     frames=polaris_frame_dict)
    assert new_dataset_obj == polaris_dataset_obj


def test_dataset_creation_from_objs(polaris_metadata_obj, polaris_frame_obj,
                                    polaris_dataset_obj, polaris_dataset_json):
    """Test dataset creation from metadata and frame objects
    """
    new_dataset_obj = PolarisDataset(metadata=polaris_metadata_obj,
                                     frames=polaris_frame_obj)
    assert new_dataset_obj == polaris_dataset_obj
    assert new_dataset_obj.to_json() == polaris_dataset_json
