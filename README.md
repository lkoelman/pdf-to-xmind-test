# PdfToc2MindMap

Simple tool to convert PDF table of contents to popular mind map formats



# Installation

Automatic installation of dependencies:

```sh
git clone https://github.com/mananatee/PdfToc2MindMap.git
pip install --process-dependency-links ./PdfToc2MindMap
```

Manual installation of dependencies:

```sh
# Install XMind Python SDK
git clone https://github.com/andrii-z4i/xmind-sdk-python.git
python xmind-sdk-python/setup.py install

# Install PDF miner (https://github.com/pdfminer/pdfminer.six)
pip install pdfminer.six
```

# TODO

- [ ] support multiple mindmap formats
- [ ] add unit tests
- [ ] test with table of contents created by more pdf editors (currently only tested with PDF X-Change Editor)