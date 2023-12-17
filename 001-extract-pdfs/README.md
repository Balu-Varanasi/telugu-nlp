# Extracting text from PDFs

## Using PyPDFium2 and layoutparser

This is a simple Python script to extract text from PDFs. It uses the following packages:

```text
pypdfium2==4.25.0
Pillow==10.1.0
numpy==1.26.2
pytesseract==0.3.10
layoutparser==0.3.4
torch==2.1.1
torchvision==0.16.1
git+https://github.com/facebookresearch/detectron2.git@a0e22dbfa791e6235e4f196d5ce25e754d02be31#egg=detectron2
```

### Steps to extract text from PDFs

```bash
$ python3 -m venv .venv  # create a virtual environment if not already created
$ source .venv/bin/activate
(.venv) $ pip install --upgrade pip  # make sure pip is up-to-date
(.venv) $ pip install -r requirements.txt
(.venv) $ python extract_text_from_old_chandamama.py
(.venv) $ deactivate
$ 
```

### Sample input and output

- Input Image in PDF

![Jittulamari Nakka Bava](./images/story-image.png "Jittulamari Nakka Bava")


- Extracted Text

```text
ఆశగా అనగా ఒక అడివిలో ఒక

నక్క ఉండేది. అది చాలా జిత్తులు
'మారిది, అది ఎక్కడినించి వచ్చిందో,
ఎప్పుడు వచ్చిందో. ఎవరికీ తెలియదు.
'దానికరహా అంతా చిత్రంగా ఉండేది,
అందుకని మిగతా నక్కలన్నీ. “నువు
మా కులమదానివేకాదు పొ” మృన్నవి.
దానితో మాట్లాడటంకూడా మాని వేసినై.

ఇక నక్క ఏమిచేస్తుంది? అక్కడ
తన ఆటలు సాగకపోయేవరకు అడివికి
దగ్గరగా ఉన్న ఊరు పోయి. అక్కడ
'మంగలివానితో స్నేహం చేనుకున్నది.
పానం, ఆ మంగలి చాలా మంచివాడు.

వాళ్లిద్దరికీ మంచిస్నేహం కలిసింది,
ఒకనాడు. నక్క మంగలితో అన్నది
కదా. "మంగలి మామా, మంగలి
మామాః మనం వళ్లతోట వేసుకుంటే
ఎట్లా ఉంటుంది? మనం తిన్నన్ని
తినవచ్చు, మిగతావి అమ్ముకుని పొడి
నిండా డబ్బులు పోనుకోవచ్చు.”
పాపం మంగలికి ఈ మాటలు
వినేవరకు నోరు వూరింది. మామిడి,
మొక్కలు, పపోటామొక్కలు, అరిటి
మొక్కలూ తెచ్చి తోటవేశాడు, అక్క
'డక్కడా గుమ్మడిపాదులూ, దోసపాదు
లూ పెట్టాడు. తనూ పెళ్లిమూ కలిసి
] పాదులుచేని సళ్ళు తెచ్చి,
చెట్లకు పోసేవాబ్ళు, నక్క
```
