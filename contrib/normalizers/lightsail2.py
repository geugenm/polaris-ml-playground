"""
Normalizer class for LightSail-2 satellite

Converts raw digit values, decoded by satnogs-decoders,  into
normalized ("Si") units using the equations provided in the telemetry
documentation.
"""
from contrib.normalizers.common import Field, Normalizer, int2ddn


class Lightsail2(Normalizer):
    """
    The class providing equations for the satellite telemetry
    """
    def __init__(self):
        super(Lightsail2, self).__init__()
        self.normalizers = [  # pylint: disable=R0801
            Field('dest_callsign', lambda x: x, None, 'Destination Callsign'),
            Field('src_callsign', lambda x: x, None, 'Source Callsign'),
            Field('src_ssid', lambda x: x, None, 'Source SSID'),
            Field('dest_ssid', lambda x: x, None, 'Destination SSID'),
            Field('ctl', lambda x: x, None, 'CTL'),
            Field('pid', lambda x: x, None, 'PID'),
            Field('src_ip_addr', int2ddn, None, 'Source IP Address'),
            Field('dst_ip_addr', int2ddn, None, 'Destination IP Address'),
            Field('src_port', lambda x: x, None, 'Source port'),
            Field('dst_port', lambda x: x, None, 'Destination port'),
            Field('type', lambda x: x, None, 'Type is always 1'),
            Field('daughter_atmp', lambda x: x * 0.5 - 75, 'degC',
                  'Daughter Board A Temperature'),
            Field('daughter_btmp', lambda x: x * 0.5 - 75, 'degC',
                  'Daughter Board B Temperature'),
            Field('rf_amptmp', lambda x: x * 0.5 - 75, 'degC',
                  'RF Amplifier Temperature'),
            Field('threev_pltmp', lambda x: x * 0.5 - 75, 'degC',
                  '3V3 Payload Temperature'),
            Field('atmelpwrcurr', lambda x: x / 2048, 'A',
                  'CPU Power Current'),
            Field('atmelpwrbusv', lambda x: x / 32, 'V', 'CPU Power Voltage'),
            Field('threev_pwrcurr', lambda x: x / 2048, 'A',
                  '3V3 Power Current'),
            Field('threev_pwrbusv', lambda x: x / 32, 'V',
                  '3V3 Power Voltage'),
            Field('threev_plpwrcurr', lambda x: x / 128, 'A',
                  '3V3 Payload Current'),
            Field('threev_plpwrbusv', lambda x: x / 32, 'V',
                  '3V3 Payload Voltage'),
            Field('fivev_plpwrcurr', lambda x: x / 128, 'A',
                  '5V Payload Current'),
            Field('fivev_plpwrbusv', lambda x: x / 32, 'V',
                  '5V Payload Voltage'),
            Field('daughter_apwrcurr', lambda x: x / 128, 'A',
                  'Daughter Board A Power Current'),
            Field('daughter_apwrbusv', lambda x: x / 32, 'V',
                  'Daughter Board A Power Voltage'),
            Field('daughter_bpwrcurr', lambda x: x / 128, 'A',
                  'Daughter Board A Power Current'),
            Field('daughter_bpwrbusv', lambda x: x / 32, 'V',
                  'Daughter Board B Power Voltage'),
            Field('nx_tmp', lambda x: x * 0.5 - 75, 'degC', '-X Temperature'),
            Field('nx_intpwrcurr', lambda x: x / 64, 'A',
                  '-X Int Power Current'),
            Field('nx_intpwrbusv', lambda x: x / 32, 'V',
                  '-X Int Power Voltage'),
            Field('nx_extpwrcurr', lambda x: x / 64, 'A',
                  '-X Ext Power Current'),
            Field('nx_extpwrbusv', lambda x: x / 32, 'V',
                  '-X Ext Power Voltage'),
            Field('px_tmp', lambda x: x * 0.5 - 75, 'degC', '+X Temperature'),
            Field('px_intpwrcurr', lambda x: x / 64, 'A',
                  '+X Int Power Current'),
            Field('px_intpwrbusv', lambda x: x / 32, 'V',
                  '+X Int Power Voltage'),
            Field('px_extpwrcurr', lambda x: x / 64, 'A',
                  '+X Ext Power Current'),
            Field('px_extpwrbusv', lambda x: x / 32, 'V',
                  '+X Ext Power Voltage'),
            Field('ny_tmp', lambda x: x * 0.5 - 75, 'degC', '-Y Temperature'),
            Field('ny_intpwrcurr', lambda x: x / 64, 'A',
                  '-Y Int Power Current'),
            Field('ny_intpwrbusv', lambda x: x / 32, 'V',
                  '-Y Int Power Voltage'),
            Field('ny_extpwrcurr', lambda x: x / 64, 'A',
                  '-Y Ext Power Current'),
            Field('ny_extpwrbusv', lambda x: x / 32, 'V',
                  '-Y Ext Power Voltage'),
            Field('py_tmp', lambda x: x * 0.5 - 75, 'degC', '+Y Temperature'),
            Field('py_intpwrcurr', lambda x: x / 64, 'A',
                  '+Y Int Power Current'),
            Field('py_intpwrbusv', lambda x: x / 32, 'V',
                  '+Y Int Power Voltage'),
            Field('py_extpwrcurr', lambda x: x / 64, 'A',
                  '+Y Ext Power Current'),
            Field('py_extpwrbusv', lambda x: x / 32, 'V',
                  '+Y Ext Power Voltage'),
            Field('nz_tmp', lambda x: x * 0.5 - 75, 'degC', '-Z Temperature'),
            Field('nz_extpwrcurr', lambda x: x / 64, 'A',
                  '-Z Ext Power Current'),
            Field('nz_extpwrbusv', lambda x: x / 32, 'V',
                  '-Z Ext Power Voltage'),
            Field('pz_tmp', lambda x: x * 0.5 - 75, 'degC', '+Z Temperature'),
            Field('usercputime', lambda x: x, 's', 'User CPU Time'),
            Field('syscputime', lambda x: x, 's', 'System CPU Time'),
            Field('idlecputime', lambda x: x, 's', 'Idle CPU Time'),
            Field('processes', lambda x: x, None, 'Processes'),
            Field('memfree', lambda x: x, 'kB', 'Memory Free'),
            Field('buffers', lambda x: x, 'kB', 'Memory Buffered'),
            Field('cached', lambda x: x, 'kB', 'Memory Cached'),
            Field('datafree', lambda x: x, 'kB', 'Data Free'),
            Field('nanderasures', lambda x: x, None, 'NAND Erasure'),
            Field('beaconcnt', lambda x: x, None, 'Beacon Count'),
            Field('time', lambda x: x, None, 'RTC'),
            Field('boottime', lambda x: x, None, 'Boot Time'),
            Field('long_dur_counter', lambda x: x, None,
                  'Long Duration Counter'),
            Field('adcs_mode', lambda x: x, None, 'ADCS Mode'),
            Field('flags', lambda x: x, None, 'ADCS Flags'),
            Field('q0_act', lambda x: x / 128, None, 'Q0 Actuator'),
            Field('q1_act', lambda x: x / 128, None, 'Q1 Actuator'),
            Field('q2_act', lambda x: x / 128, None, 'Q2 Actuator'),
            Field('q3_act', lambda x: x / 128, None, 'Q3 Actuator'),
            Field('x_rate', lambda x: x / 128, 'deg/s', 'X Rotation Rate'),
            Field('y_rate', lambda x: x / 128, 'deg/s', 'Y Rotation Rate'),
            Field('z_rate', lambda x: x / 128, 'deg/s', 'Z Rotation Rate'),
            Field('gyro_px', lambda x: x / 8, None, 'X Payload Gyro'),
            Field('gyro_py', lambda x: x / 8, None, 'Y Payload Gyro'),
            Field('gyro_pz', lambda x: x / 8, None, 'Z Payload Gyro'),
            Field('gyro_ix', lambda x: x / 8, None, 'X InternalGyro'),
            Field('gyro_iy', lambda x: x / 8, None, 'Y InternalGyro'),
            Field('gyro_iz', lambda x: x / 8, None, 'Z InternalGyro'),
            Field('sol_nxx', lambda x: x, None, '-X Solar Sensor X'),
            Field('sol_nxy', lambda x: x, None, '-X Solar Sensor Y'),
            Field('sol_pxx', lambda x: x, None, '+X Solar Sensor X'),
            Field('sol_pxy', lambda x: x, None, '+X Solar Sensor Y'),
            Field('sol_nyx', lambda x: x, None, '-Y Solar Sensor X'),
            Field('sol_nyy', lambda x: x, None, '-Y Solar Sensor Y'),
            Field('sol_pyx', lambda x: x, None, '+Y Solar Sensor X'),
            Field('sol_pyy', lambda x: x, None, '+Y Solar Sensor Y'),
            Field('sol_nzx', lambda x: x, None, '-Z Solar Sensor X'),
            Field('sol_nzy', lambda x: x, None, '-Z Solar Sensor Y'),
            Field('mag_nxx', lambda x: x * 100, 'nT',
                  '-X panel magnetometer x channel'),
            Field('mag_nxy', lambda x: x * 100, 'nT',
                  '-X panel magnetometer y channel'),
            Field('mag_nxz', lambda x: x * 100, 'nT',
                  '-X panel magnetometer z channel'),
            Field('mag_pxz', lambda x: x * 100, 'nT',
                  '+X panel magnetometer z channel'),
            Field('mag_pxx', lambda x: x * 100, 'nT',
                  '+X panel magnetometer x channel'),
            Field('mag_pxy', lambda x: x * 100, 'nT',
                  '+X panel magnetometer y channel'),
            Field('mag_nyz', lambda x: x * 100, 'nT',
                  '-Y panel magnetometer z channel'),
            Field('mag_pyz', lambda x: x * 100, 'nT',
                  '+Y panel magnetometer z channel'),
            Field('mag_pyx', lambda x: x * 100, 'nT',
                  '+Y panel magnetometer x channel'),
            Field('mag_pyy', lambda x: x * 100, 'nT',
                  '+Y panel magnetometer y channel'),
            Field('wheel_rpm', lambda x: x, 'rpm', 'Wheel RPM'),
            Field('cam0_status', lambda x: x, None, 'Camera 0 Status Bits'),
            Field('cam0_temp', lambda x: x * 0.5 - 75, None,
                  'Camera 0 Temperature'),
            Field('cam0_last_contact', lambda x: x, None,
                  'Camera 0 Seconds Since Last Contact'),
            Field('cam0_pics_remaining', lambda x: x, None,
                  'Camera 0 Pics Remaining'),
            Field('cam0_retry_fails', lambda x: x, None,
                  'Camera 0 Retry Fails'),
            Field('cam1_status', lambda x: x, None, 'Camera 1 Status Bits'),
            Field('cam1_temp', lambda x: x * 0.5 - 75, 'degC',
                  'Camera 1 Temperature'),
            Field('cam1_last_contact', lambda x: x, 's',
                  'Camera 1 Seconds Since Last Contact'),
            Field('cam1_pics_remaining', lambda x: x, None,
                  'Camera 1 Pics Remaining'),
            Field('cam1_retry_fails', lambda x: x, None,
                  'Camera 1 Retry Fails'),
            Field('torqx_pwrcurr', lambda x: x / 128, 'A',
                  'X Torquer Current'),
            Field('torqx_pwrbusv', lambda x: x / 16, 'V', 'X Torquer Voltage'),
            Field('torqy_pwrcurr', lambda x: x / 128, 'A',
                  'Y Torquer Current'),
            Field('torqy_pwrbusv', lambda x: x / 16, 'V', 'Y Torquer Voltage'),
            Field('torqz_pwrcurr', lambda x: x / 128, 'A',
                  'Z Torquer Current'),
            Field('torqz_pwrbusv', lambda x: x / 16, 'V', 'Z Torquer Voltage'),
            Field('motor_pwrcurr', lambda x: x / 128, 'A', 'Motor Current'),
            Field('motor_pwrbusv', lambda x: x / 16, 'V', 'Motor Voltage'),
            Field('pic_panel_flags', lambda x: x, None, 'Pic/Panel Flags'),
            Field('motor_cnt', lambda x: x, None, 'Motor Count'),
            Field('motor_limit', lambda x: x, None, 'Motor Limit'),
            Field('bat0_curr', lambda x: x / 128, 'A', 'Battery 0 Current'),
            Field('bat0_volt', lambda x: x / 32, 'V', 'Battery 0 Voltage'),
            Field('bat0_temp', lambda x: x * 0.5 - 75, 'degC',
                  'Battery 0 Temperature'),
            Field('bat0_flags', lambda x: x, None, 'Battery 0 Flags'),
            Field('bat0_ctlflags', lambda x: x, None,
                  'Battery 0 Control Flags'),
            Field('bat1_curr', lambda x: x / 128, 'A', 'Battery 1 Current'),
            Field('bat1_volt', lambda x: x / 32, 'V', 'Battery 1 Voltage'),
            Field('bat1_temp', lambda x: x * 0.5 - 75, 'degC',
                  'Battery 1 Temperature'),
            Field('bat1_flags', lambda x: x, None, 'Battery 1 Flags'),
            Field('bat1_ctlflags', lambda x: x, None,
                  'Battery 1 Control Flags'),
            Field('bat2_curr', lambda x: x / 128, 'A', 'Battery 2 Current'),
            Field('bat2_volt', lambda x: x / 32, 'V', 'Battery 2 Voltage'),
            Field('bat2_temp', lambda x: x * 0.5 - 75, 'degC',
                  'Battery 2 Temperature'),
            Field('bat2_flags', lambda x: x, None, 'Battery 2 Flags'),
            Field('bat2_ctlflags', lambda x: x, None,
                  'Battery 2 Control Flags'),
            Field('bat3_curr', lambda x: x / 128, 'A', 'Battery 3 Current'),
            Field('bat3_volt', lambda x: x / 32, 'V', 'Battery 3 Voltage'),
            Field('bat3_temp', lambda x: x * 0.5 - 75, 'degC',
                  'Battery 3 Temperature'),
            Field('bat3_flags', lambda x: x, None, 'Battery 3 Flags'),
            Field('bat3_ctlflags', lambda x: x, None,
                  'Battery 3 Control Flags'),
            Field('bat4_curr', lambda x: x / 128, 'A', 'Battery 4 Current'),
            Field('bat4_volt', lambda x: x / 32, 'V', 'Battery 4 Voltage'),
            Field('bat4_temp', lambda x: x * 0.5 - 75, 'degC',
                  'Battery 4 Temperature'),
            Field('bat4_flags', lambda x: x, None, 'Battery 4 Flags'),
            Field('bat4_ctlflags', lambda x: x, None,
                  'Battery 4 Control Flags'),
            Field('bat5_curr', lambda x: x / 128, 'A', 'Battery 5 Current'),
            Field('bat5_volt', lambda x: x / 32, 'V', 'Battery 5 Voltage'),
            Field('bat5_temp', lambda x: x * 0.5 - 75, 'degC',
                  'Battery 5 Temperature'),
            Field('bat5_flags', lambda x: x, None, 'Battery 5 Flags'),
            Field('bat5_ctlflags', lambda x: x, None,
                  'Battery 5 Control Flags'),
            Field('bat6_curr', lambda x: x / 128, 'A', 'Battery 6 Current'),
            Field('bat6_volt', lambda x: x / 32, 'V', 'Battery 6 Voltage'),
            Field('bat6_temp', lambda x: x * 0.5 - 75, 'degC',
                  'Battery 6 Temperature'),
            Field('bat6_flags', lambda x: x, None, 'Battery 6 Flags'),
            Field('bat6_ctlflags', lambda x: x, None,
                  'Battery 6 Control Flags'),
            Field('bat7_curr', lambda x: x / 128, 'A', 'Battery 7 Current'),
            Field('bat7_volt', lambda x: x / 32, 'V', 'Battery 7 Voltage'),
            Field('bat7_temp', lambda x: x * 0.5 - 75, 'degC',
                  'Battery 7 Temperature'),
            Field('bat7_flags', lambda x: x, None, 'Battery 7 Flags'),
            Field('bat7_ctlflags', lambda x: x, None,
                  'Battery 7 Control Flags'),
            Field('comm_rxcount', lambda x: x, None, 'RX Packets'),
            Field('comm_txcount', lambda x: x, None, 'TX Packets'),
            Field('comm_rxbytes', lambda x: x, None, 'RX Bytes'),
            Field('comm_txbytes', lambda x: x, None, 'TX Bytes'),
        ]

    def validate_frame(self, frame):
        """ Validate frames for LightSail-2

            The source callsign for this satellite is KK6HIT. [citation needed]
        """
        try:
            return frame['fields']['src_callsign']['value'].lower() == 'kk6hit'
        except (KeyError, AttributeError):
            return False
