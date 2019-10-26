"""
Normalizer class for ACRUX-1 satellite

Converts raw digit values, decoded by satnogs-decoders,  into
normalized ("Si") units using the equations provided in the telemetry
documentation.
"""
from contrib.normalizers.common import Field, Normalizer


class Acrux1(Normalizer):
    """
    The class providing equations for the satellite telemetry
    """

    def __init__(self):
        super(Acrux1, self).__init__()
        self.normalizers = [  # pylint: disable=R0801
            Field('dest_callsign', lambda x: x, None,
                  'AX25 Destination Callsign'),
            Field('src_callsign', lambda x: x, None, 'AX25 Source Callsign'),
            Field('src_ssid', lambda x: x, None, 'AX25 Source SSID'),
            Field('dest_ssid', lambda x: x, None, 'AX25 Destination SSID'),
            Field('ctl', lambda x: x, None, 'AX25 CTL'),
            Field('pid', lambda x: x, None, 'AX25 PID'),
            Field('tx_count', lambda x: x, None, 'TX byte count'),
            Field('rx_count', lambda x: x, None, 'RX byte count'),
            Field('rx_valid', lambda x: x, None, 'n.a.'),
            Field('payload_type', lambda x: x, None, 'Payload type'),
            Field('comouti1', lambda x: x * ((20 * 2) / 65536), 'A',
                  'COM Out I1'),
            Field('comoutv1', lambda x: x * ((20 * 2) / 65536), 'V',
                  'COM Out V1'),
            Field('comouti2', lambda x: x * ((20 * 2) / 65536), 'A',
                  'COM Out I2'),
            Field('comoutv2', lambda x: x * ((20 * 2) / 65536), 'V',
                  'COM Out V2'),
            Field('comt2', lambda x: x * ((128 * 2) / 65536), 'degC',
                  'COM Temperature 2'),
            Field('epsadcbatv1', lambda x: x * ((20 * 2) / 65536), 'V',
                  'EPS ADC Bat V1'),
            Field('epsloadi1', lambda x: x * ((20 * 2) / 65536), 'A',
                  'EPS Load 1'),
            Field('epsadcbatv2', lambda x: x * ((20 * 2) / 65536), 'V',
                  'EPS ADC Bat V2'),
            Field('epsboostini2', lambda x: x * ((20 * 2) / 65536), 'A',
                  'EPS boost inrush current'),
            Field('epsrail1', lambda x: x * ((20 * 2) / 65536), 'V',
                  'EPS rail 1 voltage'),
            Field('epsrail2', lambda x: x * ((20 * 2) / 65536), 'V',
                  'EPS rail 2 voltage'),
            Field('epstoppanelv', lambda x: x * ((20 * 2) / 65536), 'V',
                  'EPS top panel voltage'),
            Field('epstoppaneli', lambda x: x * ((20 * 2) / 65536), 'A',
                  'EPS top panel current'),
            Field('epst1', lambda x: x * ((128 * 2) / 65536), 'degC',
                  'EPS Temperature 1'),
            Field('epst2', lambda x: x * ((128 * 2) / 65536), 'degC',
                  'EPS Temperature 2'),
            Field('xposv', lambda x: x * ((20 * 2) / 65536), 'V',
                  '+X panel voltage'),
            Field('xposi', lambda x: x * ((20 * 2) / 65536), 'A',
                  '+X panel current'),
            Field('xpost1', lambda x: x * ((128 * 2) / 65536), 'degC',
                  '+X panel temperature'),
            Field('yposv', lambda x: x * ((20 * 2) / 65536), 'V',
                  '+Y panel voltage'),
            Field('yposi', lambda x: x * ((20 * 2) / 65536), 'A',
                  '+Y panel current'),
            Field('ypost1', lambda x: x * ((128 * 2) / 65536), 'degC',
                  '+Y panel temperature'),
            Field('xnegv', lambda x: x * ((20 * 2) / 65536), 'V',
                  '-X panel voltage'),
            Field('xnegi', lambda x: x * ((20 * 2) / 65536), 'A',
                  '-X panel current'),
            Field('xnegt1', lambda x: x * ((128 * 2) / 65536), 'degC',
                  '-X panel temperature'),
            Field('ynegv', lambda x: x * ((20 * 2) / 65536), 'V',
                  '-Y panel voltage'),
            Field('ynegi', lambda x: x * ((20 * 2) / 65536), 'A',
                  '-Y panel current'),
            Field('ynegt1', lambda x: x * ((128 * 2) / 65536), 'degC',
                  '-Y panel temperature'),
            Field('znegv', lambda x: x * ((20 * 2) / 65536), 'V',
                  '-Z panel voltage'),
            Field('znegi', lambda x: x * ((20 * 2) / 65536), 'A',
                  '-Z panel current'),
            Field('znegt1', lambda x: x * ((128 * 2) / 65536), 'degC',
                  '-Z panel temperature'),
            Field('zpost', lambda x: x * ((128 * 2) / 65536), 'degC',
                  '+Z panel temperature'),
            Field('cdhtime', lambda x: x, 's', 'Timestamp'),
            Field('swcdhlastreboot', lambda x: x, 's', 'Timestamp'),
            Field('swsequence', lambda x: x, None, 'n.a.'),
            Field('outreachmessage', lambda x: x, None, 'Textmessage'),
        ]
