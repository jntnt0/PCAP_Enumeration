from setuptools import setup, find_packages

setup(
    name='pcap_enumerator',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'scapy',
        'dpkt',
        'plotly',
    ],
    entry_points={
        'console_scripts': [
            'pcap-enumerator=src.main:main',
        ],
    },
)
