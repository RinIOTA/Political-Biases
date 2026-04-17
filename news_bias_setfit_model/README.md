---
tags:
- setfit
- sentence-transformers
- text-classification
- generated_from_setfit_trainer
widget:
- text: "Trump pledges a series of Day 1 executive actions to end â€˜four long years\
    \ of American declineâ€™ â–¶Follow live updates on President-elect Donald Trumpâ€™s\
    \ return to Washington WASHINGTON (AP) â€” President-elect Donald Trump used a\
    \ raucous rally Sunday on the eve of his inauguration to promise swift Day 1 action\
    \ remaking the federal government, shifting federal priorities at breakneck speed\
    \ and ensuring that â€œthe curtain closes on four long years of American decline.â€\x9D\
    \ Supporters filled nearly all of the 20,000-plus-seat Capital One Arena in downtown\
    \ Washington for a â€œMake America Greatâ€\x9D victory celebration, and cheered\
    \ as Trump said heâ€™d take quick action on everything from cracking down on the\
    \ U.S.-Mexico border to promoting oil drilling, reining in the federal workforce\
    \ and eradicating diversity programs. â€œWeâ€™re going to give them the best first\
    \ day, the biggest first week and the most extraordinary first 100 days of any\
    \ presidency in American history,â€\x9D said Trump, who also promised to roll\
    \ back executive actions by his predecessor, outgoing President Joe Biden,"
- text: '''Not going to happen'': Billionaire CEO shreds Trumpâ€™s biggest argument
    in favor of tariffs â€º Timothy Boyle â€“ the billionaire CEO of publicly traded
    apparel giant Columbia Sportswear â€” thinks the central argument President-elect
    Donald Trump is making in favor of new tariffs is bogus. Trump has proposed tariffs
    of 25 percent on goods imported from Canada and Mexico, and 10 percent on Chinese
    imports. In October, Trump told Bloomberg editor-in-chief John Micklethwait that
    he expected there to be a boom in U.S. manufacturing as companies considered their
    business strategy in the wake of significant new tariffs. But Boyle said Trump
    lacks a basic understanding of how corporations operate on a global scale. In
    a Tuesday interview with CNN, Boyle explained that his company is already one
    of the "largest duty payers and tariff payers in the United States," and that
    a potential new tariff imposed by the incoming Trump administration would only
    harm his customers, rather than foreign countries exporting goods. READ MORE:
    ''Chaos'': Small biz owner hit by Trump''s last tariff reveals k'
- text: 'Californiaâ€™s DEI-Obsessed Anarchotyrants Threw Money At Everything But
    Water And Firefighters Astonishingly devastating fires are burning mostly unchecked
    in Los Angeles, destroying whole neighborhoods, and see if you can spot the problem
    in this Yahoo News update I found in my inbox this week: As of that report, thousands
    of acres of fire burning into (and then straight through) neighborhoods; 1,400
    firefighters. In Pacific Palisades alone, where the biggest fire started first,
    weâ€™re below one firefighter per two acres of fire. Iâ€™ve spent most of my life
    in California, and a quite common experience is to be in way-Northern California,
    for example, and watch a line of fire engines go racing past from San Diego and
    Newport Beach, 500 miles from home. We deal with big fires with prompt statewide
    mutual aid, a well-practiced system. I live near the Eaton fire, which is burning
    in the hills above Pasadena, and I listened all Tuesday night for the cavalry
    to arrive. The cavalry, bizarrely, did not seem to arrive. And so I watched houses
    burn, on the news, with reporters present '
- text: 'Conservative legal scholar calls for impeachment of Judge Cannon: ''Member
    of the Trump defense team'' â€º A leading member of a conservative think tank
    is now calling for US District Judge Aileen Cannon â€” the Trump-appointed judge
    overseeing the former president''s classified documents trial â€” to be impeached.
    In a response to the news Thursday evening that Judge Cannon was refusing to set
    a key pre-trial deadline until next year, Norman Ornstein â€” an Emeritus scholar
    at the Koch-funded American Enterprise Institute â€” called for an impeachment
    resolution to be introduced against Cannon. "She is a full fledged member of the
    Trump defense team. Aileen Cannon is utterly unfit for the bench," Ornstein tweeted.
    "[The resolution] will go nowhere but will highlight her outrageous conduct."
    POLL: Should Trump be allowed to hold office again? Special counsel Jack Smith
    previously asked Judge Cannon to set a Section 5 deadline under the Classified
    Information Procedures Act (CIPA), which would make a defendant specify which
    classified information they intend to use at trial. Cannon, for her p'
- text: "â€˜I have two niecesâ€”one named McKinley, the other is Denali.â€™ A few\
    \ years ago, my wife and I spent the night at the Denali Overlook Inn, which,\
    \ like so many Alaska getaways, is beautiful, spare and, in the summer, overflowing\
    \ with sixty- and seventy-something males with rifles and fishing poles, seemingly\
    \ in search of their inner frontiersmen. Almost all of them are retired financial\
    \ planners and dentists and principals from places like Dallas and Dubuque. The\
    \ mountain is spectacularâ€”the sprawling green forests that give way to sharp\
    \ crags of gray rock that give rise to the white-silver ice rising to a peak of\
    \ 20,310 feet. Itâ€™s the highest mountain in North America. In a state filled\
    \ with people who live there because of the outdoors, it is central to Alaskaâ€™s\
    \ identity. â€œI see it every clear day while driving locally. Itâ€™s awe-inspiring,â€\x9D\
    \ the worldâ€™s best-known Alaskan, former state governor and vice-presidential\
    \ candidate Sarah Palin, told The Free Press. So what does it mean that last week,\
    \ President Trump renamed Denaliâ€”the nam"
metrics:
- accuracy
pipeline_tag: text-classification
library_name: setfit
inference: true
base_model: sentence-transformers/paraphrase-MiniLM-L3-v2
model-index:
- name: SetFit with sentence-transformers/paraphrase-MiniLM-L3-v2
  results:
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      name: Unknown
      type: unknown
      split: test
    metrics:
    - type: accuracy
      value: 0.6416184971098265
      name: Accuracy
---

# SetFit with sentence-transformers/paraphrase-MiniLM-L3-v2

This is a [SetFit](https://github.com/huggingface/setfit) model that can be used for Text Classification. This SetFit model uses [sentence-transformers/paraphrase-MiniLM-L3-v2](https://huggingface.co/sentence-transformers/paraphrase-MiniLM-L3-v2) as the Sentence Transformer embedding model. A [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) instance is used for classification.

The model has been trained using an efficient few-shot learning technique that involves:

1. Fine-tuning a [Sentence Transformer](https://www.sbert.net) with contrastive learning.
2. Training a classification head with features from the fine-tuned Sentence Transformer.

## Model Details

### Model Description
- **Model Type:** SetFit
- **Sentence Transformer body:** [sentence-transformers/paraphrase-MiniLM-L3-v2](https://huggingface.co/sentence-transformers/paraphrase-MiniLM-L3-v2)
- **Classification head:** a [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) instance
- **Maximum Sequence Length:** 128 tokens
- **Number of Classes:** 5 classes
<!-- - **Training Dataset:** [Unknown](https://huggingface.co/datasets/unknown) -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Repository:** [SetFit on GitHub](https://github.com/huggingface/setfit)
- **Paper:** [Efficient Few-Shot Learning Without Prompts](https://arxiv.org/abs/2209.11055)
- **Blogpost:** [SetFit: Efficient Few-Shot Learning Without Prompts](https://huggingface.co/blog/setfit)

### Model Labels
| Label | Examples                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|:------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 4     | <ul><li>'Republicans Need A Forceful Answer To Democratsâ€™ Deceptive Questions On The 2020 Election      â€œI think that question deserved a yes or no, and I think the length of your answer is an indication that you werenâ€™t prepared to answer yes,â€\x9d Durbin retorted.    As I last year when the legacy media hounded then-Sen. J.D. Vance to say Donald Trump lost the 2020 election, there is a fundamental flaw in the question: â€œThe query includes an undefined term â€” â€˜lostâ€™ â€” which holds a different meaning to Trump supporters and to the anti-Trump inquisitors.â€\x9d    In other words, it depends on what you mean by â€œlost.â€\x9d  â€œIf asked whether Trump â€˜lostâ€™ the 2020 election, meaning that if all legal votes were counted and all illegal counts discarded â€” and the counting was done legally pursuant to controlling election law â€”â€\x9d the answer should be a resounding, â€œI donâ€™t know.â€\x9d     Republicans need to make that point, and the confirmation hearings provide a perfect opportunity. So, hereâ€™s a simple, soundbite for the next Trump nominee cornered with the query, '</li><li>'Illegal Aliens Worried as Trump-Era ICE Raids Loom Illegal aliens fearful of U.S. Immigration and Customs Enforcement (ICE) raids under President Donald Trump are staying inside, reportedly causing foot traffic to drop by 50 percent in a busy Chicago shopping district known as â€œMexico of the Midwest.â€\x9d Chicagoâ€™s Little Village neighborhood dotted with taquerias and Mexican grocery stores â€œturned into a ghost townâ€\x9d by Monday afternoon, after Trump was sworn into office, according to a report by Bloomberg. By Tuesday morning, several shops in Little Village, which is also known as the â€œMexico of the Midwest,â€\x9d were closed. FLASHBACK: Trump Calls for Zero Tolerance for Illegal Aliens Who Kill Americans or Law Enforcement â€œBusiness was just down, people were staying home, people were worried about: one the cold, but two, they were fearful of engaging with ICE,â€\x9d Mike Rodriguez, an alderman for the 22nd ward, which includes Little Village, told Bloomberg. Rodriguez added that he was â€œwalking the business corridor three days'</li><li>'Nolte: Disgraced, Far-left CNN to Lay off Hundreds as Viewership Collapses CNN, a far-left propaganda outlet that spreads conspiracy theories and political violence, is set to lay off hundreds, according to various reports that have me so excited Iâ€™m having to call my doctor every four hours. â€œCNN is reportedly set to lay off â€˜hundredsâ€™ of employees in the early days of President Trumpâ€™s second administration,â€\x9d reports Fox Business. â€œCEO Mark Thompson will announce to his staff about the network cuts on Thursday[.]â€\x9d Naturally, over at CNN, the rich stay rich: Per CNBC, these layoffs â€œwonâ€™t affect CNNâ€™s most recognizable names, who are under contract.â€\x9d Gee, Jake Tapper could do a lot of good if he were willing to contribute just half of his reported annual $7 million salary to save those jobs. But he wonâ€™t because he loves the troops. The layoffs come as CNN is rearranging its linear TV lineup and building out digital subscription products. The cuts will help CNN lower production costs and consolidate teams, said the people, who spoke'</li></ul>        |
| 1     | <ul><li>'In Las Vegas, Trump once again pitches no taxes on tips President Trump speaks at a rally at Circa Resort & Casino on Saturday. The event focused on Trump\'s first week in office, including his proposed policy to eliminate taxes on tips for service industry employees. President Trump at a rally Saturday promised to fulfill his campaign pledge to eliminate taxes on tips. "In the coming weeks, I\'ll be working with Congress to get a bill on my desk that cuts taxes for workers, families, small businesses, and very importantly, keeps my promise," said Trump. "We\'re gonna get it for you â€” no tax on tips." The president, speaking at a casino in Las Vegas, said tax cuts are at the top of his legislative agenda for this new Congress. "If you\'re a restaurant worker, a server, a valet, a bell hop, a bartender, one of my caddies," the president said, "your tips will be 100% yours." Trump\'s comments came in a 40-minute speech over the weekend that sounded like a victory lap more than a policy plan. The president rattled off a list of changes he\'s made '</li><li>"Trump's inauguration brings supporters and protesters to Washington in droves WASHINGTON â€” Thousands of people came to the nationâ€™s capital this weekend, ready to party â€” or protest â€” despite the bitterly cold temperatures.  A number of progressive groups held marches around the country to protest President-elect Donald Trumpâ€™s inauguration, with a â€œPeopleâ€™s Marchâ€\x9d held in Washington on Saturday. It was planned by many of the same groups that organized the 2017 Womenâ€™s March, which had a far larger turnout.  Trump supporters headed into the city over the weekend in advance of the main inauguration ceremony and balls Monday, with a number of parties and a large rally at Capital One Arena. Because of the frigid weather forecast for Monday, the Trump team decided to move the swearing-in ceremony indoors, into the U.S. Capitol, forcing many supporters to adjust their plans.  Hereâ€™s a look at how Americans are gearing up for a second Trump term."</li><li>'Vivek Ramaswamy to announce run for Ohio governor: Sources Error fetching article'</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 0     | <ul><li>'In Spanish village, horses leap through flames in centuries-old ritual SAN BARTOLOME DE PINARES, Spain (AP) â€” On a chilly January night, hundreds of people gathered on the steep and narrow cobblestoned streets of San Bartolome de Pinares â€” population 500 â€” to watch a dramatic sight: horses galloping through towering flames. A man rides a horse through a bonfire as part of a ritual in honor of Saint Anthony the Abbot, the patron saint of domestic animals, in San Bartolome de Pinares, Spain, Thursday, Jan. 16, 2025. (AP Photo/Manu Fernandez)  Itâ€™s a centuries-old tradition in the Spanish village about 100 kilometers (60 miles) northwest of Madrid that takes place every year to honor St. Anthony the Abbott, the patron saint of animals. Riders guide horses through bonfires lit in the middle of the street in an act believed to purify the animals in the coming year.  Festivities started around nightfall Thursday as giant stacks of tree branches, later fuel for the flames, were placed on the side of the street, while locals mulled about sharing wine and '</li><li>'Trump Floats Plan for Gaza: â€˜Clean Out the Whole Thingâ€™ President Donald Trump suggested hundreds of thousands of Palestinians should leave Gaza in order to â€œjust clean outâ€\x9d the coastal enclave, stating they could be displaced to neighboring Egypt and Jordan â€œtemporarilyâ€\x9d or for the â€œlong term.â€\x9d Aboard Air Force One on Saturday, Trump told reporters he has encouraged Jordanâ€™s Abdullah II, a US ally, to â€œtake on moreâ€\x9d Palestinian refugees. Trump likened Gaza, ravaged by 15 months of war, to â€œa demolition site,â€\x9d adding, â€œIâ€™d rather get involved with some of the Arab nations and build housing in a different location where I think they could maybe live in peace for a change.â€\x9d Trumpâ€™s remarks could be seen as breaking with the USâ€™ long-held support for a two-state solution between Israel and Palestine. In an apparent rebuff of Trump, Jordanâ€™s Foreign Minister Ayman Safadi said Sunday that his countryâ€™s â€œrejection of displacement is fixed and unchangeableâ€\x9d and called a two-state solution â€œthe way to achie'</li><li>'So Long, Pink Pussy Hats â€” This Time, The Resistance Looks More Somber At Inauguration Today, a good friend who works in the federal government lamented having to report to his new boss with Donald Trumpâ€™s inauguration. â€œThere just seems like less of a resistance this go-around,â€\x9d he said. I beg to differ; though at first glance, it may appear that way. Through the lens of fashion, the gaze of social media, and the merchandise that brands are putting forward for consumption, we can analyze a collective mood. There are key differences between dissident dressing in 2017 and 2025, and parsing them provides insight into the collective consciousness of Americans over the past eight years and where weâ€™re at today. In 2017, dissident dressing was loud â€” a spectacle meant to grab attention and signify outrage. In 2025, dissident dressing is giving Depression Era, but thatâ€™s not because people are any less outraged. Before we dive into an analysis of fashion as a lens for cultural consciousness, a brief note on why studying fashion is not frivolous. â€œLooking back at '</li></ul>                  |
| 2     | <ul><li>'Biden Attempts To Ratify the Equal Rights Amendment by Blog Post Outgoing President Joe Biden announced today that he believes the Equal Rights Amendment (ERA) met ratification requirements and is now the official 28th amendment to the Constitutionâ€”a statement that has no legal force since the amendment remains unpublished. "I agree with the [American Bar Association] and with leading legal constitutional scholars that the Equal Rights Amendment has become part of our Constitution," Biden said in a statement released by the White House. "It is long past time to recognize the will of the American people. In keeping with my oath and duty to Constitution and country, I affirm what I believe and what three-fourths of the states have ratified: the 28th Amendment is the law of the land, guaranteeing all Americans equal rights and protections under the law regardless of their sex."  Biden\'s comments are not an executive order requiring the national archivist to publish the amendment, but rather a statement of belief that contradicts the current legal opi'</li><li>'Can Trump Rename the Gulf of Mexico With an Executive Order? Amid the head-spinning flurry of "Day 1" executive orders that stretched presidential power to new (and potentially illegal) heights, President Donald Trump attempted to leave his mark on the globe. Literally. As part of an executive order promising to restore "names that honor American greatness," Trump told acting Secretary of the Interior Walter Cruickshank to rename the Gulf of Mexico the "Gulf of America." Doing so, Trump wrote in the order, would reflect the gulf\'s status as a "flourishing economic resource and its critical importance" to America\'s economy and people. But can he do that? The answer is not straightforward. Technically, Trump ordered that the federal Geographic Names Information System (GNIS) should be updated to reflect the new name, and ordered the secretary to "remove all references to the Gulf of Mexico from the GNIS." Additionally, he ordered that "all federal references to the Gulf of America, including on agency maps, contracts, and other documents and commu'</li><li>'Donald Trump\'s Chaotic and Contradictory Day 1 In this week\'s The Reason Roundtable, editors Peter Suderman, Matt Welch, Katherine Mangu-Ward, and Nick Gillespie react to the second inauguration of President Donald Trump. The gang parses some of his contradictory ideas before touching on the saga of banning TikTok, the Chinese-owned social media application, in the United States. 01:46 - Donald Trump\'s second inauguration 14:20 - Trump\'s Day 1 executive actions 28:34 - Joe Biden\'s farewell address 42:25 - Weekly listener question 48:04 - TikTok ban 57:10 - This week\'s cultural recommendations   Mentioned in this podcast: "Day 1," by Liz Wolfe "Trump Signals a Crackdown on Legal and Illegal Immigration," by Fiona Harrigan "Trump Promises To Be a \'Peacemaker,\' Threatens Panama," by Eric Boehm "Trump\'s \'External Revenue Service\' Is a Public Relations Effort. It Won\'t Change How Tariffs Work," by Eric Boehm "Many Workers Don\'t Want To Return to the Office. That Could Help Shrink the Government," by J.D. Tuccille "The Equity Mess," by M'</li></ul>                                                                         |
| 3     | <ul><li>"Pritzker vows to 'stand in way' of certain Trump deportation policies, protect 'law-abiding' illegal migrants Dem Illinois Gov. JB Pritzker on Sunday vowed to â€œstand in the wayâ€™â€™ of certain Trump deportation policies, including those targeting â€œlaw-abidingâ€™â€™ illegal migrants. â€œWhen weâ€™re talking about violent criminals whoâ€™ve been convicted and who are undocumented, we donâ€™t want them in our state,â€\x9d Pritzker, 60, told CNNâ€™s â€œState of the Union.â€\x9d â€œWe want them out of the country. â€œWe hope they do get deported,â€\x9d he said, referring to Trumpâ€™s policy of targeting illegal migrant criminals first under his mass deportation plan. But â€œwe also have a law in the books in Illinois that says that our local law enforcement will stand up for those law-abiding undocumented people in our state,â€\x9d he said. Technically, by definition, all migrants here illegally have broken the law. Both the state of Illinois and its largest city, Chicago, have â€œsanctuaryâ€\x9d rules on the books, which limit local authoritiesâ€™ cooperation with the feds on deporting illegal migrants who "</li><li>'Acquiring Greenland Is a Good Idea. Threatening Force to Do So Is Not. Whether it was Will Rogers or Tony Soprano, the old suggestion to â€œbuy land, Godâ€™s not making any more of itâ€\x9d is good real estate advice, but itâ€™s hardly an iron law. First of all, God does make more land from time to time. And so do humans. This raises a second famous piece of advice, also of unclear authorship. When it comes to real estate only three things matter: location, location, and location. And that brings us to Greenland. Donald Trump wants to acquire it. Nay, he says we need to acquire it. The last time he was president, he floated the idea and was roundly mocked for it. But not by me, and I am hardly averse to mocking Trump when the moment calls for it. For myriad reasons, it would be in our interest for the United States to annex, lease, absorb, or otherwise acquire the giant island. The most important of these reasons is, of course, location. Thatâ€™s why Iâ€™ve long thought acquiring Greenlandâ€”peacefully!â€”was a good idea. (Indeed, last year, I despaired of t'</li><li>'Anti-Trump Nonprofit Will Slap DOGE With Immediate Lawsuit  An organization critical of President-elect Donald Trump will hit the new Department of Government Efficiency (DOGE) with a lawsuit on Monday. National Security Counselors (NSC), a nonprofit public interest law firm, will sue DOGE on Monday afternoon and allege that Elon Muskâ€™s cost-cutting advisory organization violates an existing law that sets rules for things like disclosure and hiring practices at executive branch advisory committees, the Daily Caller News Foundation confirmed. NSC has been highly critical of Trump and Musk in post-election posts to Bluesky, a social media platform popular among liberals, and even offered to provide â€œfree consultation for all feds facing the prospect of summary dismissal by Trump,â€\x9d including for people who worked with former Trump investigator Jack Smith. The statute that NSC plans to highlight in its lawsuit is the Federal Advisory Committee Act (FACA), which became law in 1972. Specifically, the lawsuit alleges that DOGE meets the definit'</li></ul> |

## Evaluation

### Metrics
| Label   | Accuracy |
|:--------|:---------|
| **all** | 0.6416   |

## Uses

### Direct Use for Inference

First install the SetFit library:

```bash
pip install setfit
```

Then you can load this model and run inference.

```python
from setfit import SetFitModel

# Download from the 🤗 Hub
model = SetFitModel.from_pretrained("setfit_model_id")
# Run inference
preds = model("â€˜I have two niecesâ€”one named McKinley, the other is Denali.â€™ A few years ago, my wife and I spent the night at the Denali Overlook Inn, which, like so many Alaska getaways, is beautiful, spare and, in the summer, overflowing with sixty- and seventy-something males with rifles and fishing poles, seemingly in search of their inner frontiersmen. Almost all of them are retired financial planners and dentists and principals from places like Dallas and Dubuque. The mountain is spectacularâ€”the sprawling green forests that give way to sharp crags of gray rock that give rise to the white-silver ice rising to a peak of 20,310 feet. Itâ€™s the highest mountain in North America. In a state filled with people who live there because of the outdoors, it is central to Alaskaâ€™s identity. â€œI see it every clear day while driving locally. Itâ€™s awe-inspiring,â€ the worldâ€™s best-known Alaskan, former state governor and vice-presidential candidate Sarah Palin, told The Free Press. So what does it mean that last week, President Trump renamed Denaliâ€”the nam")
```

<!--
### Downstream Use

*List how someone could finetune this model on their own dataset.*
-->

<!--
### Out-of-Scope Use

*List how the model may foreseeably be misused and address what users ought not to do with the model.*
-->

<!--
## Bias, Risks and Limitations

*What are the known or foreseeable issues stemming from this model? You could also flag here known failure cases or weaknesses of the model.*
-->

<!--
### Recommendations

*What are recommendations with respect to the foreseeable issues? For example, filtering explicit content.*
-->

## Training Details

### Training Set Metrics
| Training set | Min | Median   | Max |
|:-------------|:----|:---------|:----|
| Word count   | 4   | 137.4725 | 215 |

| Label | Training Sample Count |
|:------|:----------------------|
| 0     | 1511                  |
| 1     | 414                   |
| 2     | 256                   |
| 3     | 163                   |
| 4     | 422                   |

### Training Hyperparameters
- batch_size: (4, 4)
- num_epochs: (1, 1)
- max_steps: 100
- sampling_strategy: oversampling
- body_learning_rate: (2e-05, 1e-05)
- head_learning_rate: 0.01
- loss: CosineSimilarityLoss
- distance_metric: cosine_distance
- margin: 0.25
- end_to_end: False
- use_amp: True
- warmup_proportion: 0.1
- l2_weight: 0.01
- seed: 42
- eval_max_steps: -1
- load_best_model_at_end: False

### Training Results
| Epoch | Step | Training Loss | Validation Loss |
|:-----:|:----:|:-------------:|:---------------:|
| 0.01  | 1    | 0.4673        | -               |
| 0.5   | 50   | 0.2732        | -               |
| 1.0   | 100  | 0.2621        | -               |

### Framework Versions
- Python: 3.11.9
- SetFit: 1.1.3
- Sentence Transformers: 5.4.1
- Transformers: 4.57.6
- PyTorch: 2.11.0+cpu
- Datasets: 4.8.4
- Tokenizers: 0.22.2

## Citation

### BibTeX
```bibtex
@article{https://doi.org/10.48550/arxiv.2209.11055,
    doi = {10.48550/ARXIV.2209.11055},
    url = {https://arxiv.org/abs/2209.11055},
    author = {Tunstall, Lewis and Reimers, Nils and Jo, Unso Eun Seo and Bates, Luke and Korat, Daniel and Wasserblat, Moshe and Pereg, Oren},
    keywords = {Computation and Language (cs.CL), FOS: Computer and information sciences, FOS: Computer and information sciences},
    title = {Efficient Few-Shot Learning Without Prompts},
    publisher = {arXiv},
    year = {2022},
    copyright = {Creative Commons Attribution 4.0 International}
}
```

<!--
## Glossary

*Clearly define terms in order to be accessible across audiences.*
-->

<!--
## Model Card Authors

*Lists the people who create the model card, providing recognition and accountability for the detailed work that goes into its construction.*
-->

<!--
## Model Card Contact

*Provides a way for people who have updates to the Model Card, suggestions, or questions, to contact the Model Card authors.*
-->