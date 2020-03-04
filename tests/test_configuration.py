"""pytest framework for PolarisConfig module
"""

import json

from polaris.common.config import PolarisConfig


def test_polaris_config_override_defaults(polaris_config_defaults, tmp_path):
    """Smoke test for overriding settings
    """
    file_config = {
        'file_layout': {
            'root_dir': '/override'
        },
        'satellite': {
            'name': 'AnotherSat',
            'batch': {
                'learn': False,
                'viz': True
            }
        }
    }
    fullpath = tmp_path / 'simple_config.json'
    with open(fullpath.as_posix(), 'w') as f_handle:
        f_handle.write(json.dumps(file_config))

    config_from_file = PolarisConfig(file=fullpath,
                                     defaults=polaris_config_defaults)

    assert config_from_file.name == 'AnotherSat'
    # The fetch setting is from the `polaris_config` fixture
    assert config_from_file.batch_settings['fetch'] is True
    assert config_from_file.batch_settings['learn'] is False
    assert config_from_file.batch_settings['viz'] is True
    assert config_from_file.root_dir == '/override'


def test_polaris_configuration_name(polaris_config, tmp_path):
    """Test getting name from satellite configuration
    """
    fullpath = tmp_path / 'simple_config.json'
    with open(fullpath.as_posix(), 'w') as f_handle:
        f_handle.write(polaris_config)

    config_from_file = PolarisConfig(file=fullpath)

    assert config_from_file.name == "LightSail-2"


def test_polaris_configuration_root_dir(polaris_config, tmp_path):
    """Test getting name from satellite configuration
    """
    fullpath = tmp_path / 'simple_config.json'
    with open(fullpath.as_posix(), 'w') as f_handle:
        f_handle.write(polaris_config)

    config_from_file = PolarisConfig(file=fullpath)
    assert config_from_file.root_dir == '/tmp/polaris'


def test_polaris_configuration_normalized_file_path(polaris_config, tmp_path):
    """Test getting name from satellite configuration
    """
    fullpath = tmp_path / 'simple_config.json'
    with open(fullpath.as_posix(), 'w') as f_handle:
        f_handle.write(polaris_config)

    config_from_file = PolarisConfig(file=fullpath)
    expected_path = '/tmp/polaris/LightSail-2/cache/normalized_frames.json'
    assert config_from_file.normalized_file_path == expected_path
