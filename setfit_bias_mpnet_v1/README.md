---
library_name: setfit
tags:
- setfit
- sentence-transformers
- text-classification
- generated_from_setfit_trainer
base_model: sentence-transformers/all-mpnet-base-v2
metrics:
- accuracy
widget:
- text: "More Than 300 Scientists, Physicians Sign Online Letter Supporting RFK Jr.\
    \ For HHS Secretary - More than 300 scientists and physicians signed a letter\
    \ in support for President-elect Donald Trumpâ€™s nominee to lead the Department\
    \ of Health and Human Services (HHS), environmental lawyer Robert F. Kennedy Jr.\
    \ â€œThe cornerstone of scientific progress has always been the fearless pursuit\
    \ of truth through rigorous inquiry and open debate,â€\x9D the letter reads. â€œWe\
    \ want the United States Secretary of Health and Human Services to champion people\
    \ with concerns about their health, chronic diseases, health policies, and environmental\
    \ toxins, and who will not avoid discussing contentious issues."
- text: Biden administration finalizes crackdown on Chinese vehicles - President Joe
    Bidenâ€™s outgoing administration is finalizing rules on Tuesday that will effectively
    bar nearly all Chinese cars and trucks from the U.S. market, as part of a crackdown
    on vehicle software and hardware from China. Washingtonâ€™s latest move against
    Chinese vehicles comes after the Commerce Department said this month it was considering
    a similar crackdown on Chinese-made drones, in the wake of last yearâ€™s steep
    tariff hikes on imports of its electric vehicles. â€œItâ€™s really important because
    we donâ€™t want two million Chinese cars on the road and then realize ... we have
    a
- text: "Military Vet Tells Megyn Kelly CNN â€˜Doubled Downâ€™ On Slander â€˜Till\
    \ The Very End,â€™ Retracted Apology During Deposition -  Navy veteran Zachary\
    \ Young, who won his lawsuit against CNN, told SiriusXMâ€™s Megyn Kelly on Friday\
    \ that the network had â€œdoubled downâ€\x9D on their slander â€œuntil the very\
    \ end,â€\x9D describing how witnesses retracted their apologies during the deposition.\
    \ A six-person jury in Florida found CNN liable for defamation on Jan. 17, after\
    \ the network portrayed Youngâ€™s evacuation efforts to help those escaping Afghanistan\
    \ during the Biden-Harris administrationâ€™s botched withdrawal as exploiting\
    \ Afghans. On â€œThe Megyn Kelly Show,â€\x9D Kelly asked Young about the apology\
    \ he received following hi"
- text: 'Reuters


    Republican congressman introduces amendment allowing 3rd Trump term


    Jan 23 - A Republican congressman from Tennessee introduced a proposal to amend
    the U.S. Constitution, which would allow President Donald Trump to potentially
    serve a third term. Rep. Andy Oglesâ€™ resolution targets the 22nd Amendment,
    which restricts presidents from serving more than two terms. As Oglesâ€™ amendment
    is written, it would allow a president to serve up to three terms but blocks those
    who served two consecutive terms from serving a third. Download the SAN app today
    to stay up-to-date with Unbiased. Straight Factsâ„¢. Point phone camera here That
    language would disqualify former President'
- text: 'Getty Images


    Lina Khanâ€™s last-minute moves spark strong rebuke from Trumpâ€™s FTC chair


    Jan 20 - Thereâ€™s a leadership change in Washington that will have a massive
    impact on business. As President Donald Trump enters the Oval Office, he signals
    a changing of the guard at the Federal Trade Commission, which has made a flurry
    of moves in the final weeks of the Biden administration.  FTC Chair Lina Khanâ€™s
    term has already expired and Trump named Commissioner Andrew Ferguson to helm
    the regulator during his administration. Ferguson criticized his predecessorâ€™s
    regulatory activity as her time as chair ran out.  Download the SAN app today
    to stay up-to-date with Unbiased. Straight Factsâ„'
pipeline_tag: text-classification
inference: true
model-index:
- name: SetFit with sentence-transformers/all-mpnet-base-v2
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
      value: 0.8083832335329342
      name: Accuracy
---

# SetFit with sentence-transformers/all-mpnet-base-v2

This is a [SetFit](https://github.com/huggingface/setfit) model that can be used for Text Classification. This SetFit model uses [sentence-transformers/all-mpnet-base-v2](https://huggingface.co/sentence-transformers/all-mpnet-base-v2) as the Sentence Transformer embedding model. A [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) instance is used for classification.

The model has been trained using an efficient few-shot learning technique that involves:

1. Fine-tuning a [Sentence Transformer](https://www.sbert.net) with contrastive learning.
2. Training a classification head with features from the fine-tuned Sentence Transformer.

## Model Details

### Model Description
- **Model Type:** SetFit
- **Sentence Transformer body:** [sentence-transformers/all-mpnet-base-v2](https://huggingface.co/sentence-transformers/all-mpnet-base-v2)
- **Classification head:** a [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) instance
- **Maximum Sequence Length:** 384 tokens
- **Number of Classes:** 3 classes
<!-- - **Training Dataset:** [Unknown](https://huggingface.co/datasets/unknown) -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Repository:** [SetFit on GitHub](https://github.com/huggingface/setfit)
- **Paper:** [Efficient Few-Shot Learning Without Prompts](https://arxiv.org/abs/2209.11055)
- **Blogpost:** [SetFit: Efficient Few-Shot Learning Without Prompts](https://huggingface.co/blog/setfit)

### Model Labels
| Label  | Examples                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|:-------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Right  | <ul><li>'Rumored Kentucky Senate Candidate Nate Morris Slams Sen. McConnell for Voting Against Hegseth Confirmation - Rumored Kentucky candidate for U.S. Senate Nate Morris slammed Sen. Mitch McConnell (R-KY) for voting against newly-confirmed Defense Secretary Pete Hegseth, arguing that Kentuckians deserve elected officials who â€œstand with President Trump and always tell it like it is.â€\x9d Morris, the founder of Rubicon Technologies and CEO of the Lexington-based Morris Industries, wrote on X that while he â€œcouldnâ€™t be more thrilledâ€\x9d to see Hegseth be confirmed in the Senate, â€œItâ€™s a disgrace that Mitch McConnell sided with leftwing Democrats to try to tank his confirmationâ€\x9d: â€œMitch once again'</li><li>'Seven Reasons Biden Was One Of Our Worst Presidents - As Joe Biden prepares to leave office, itâ€™s worth reflecting on where he ranks among the 45 men who have served as president of the United States. By combining Carter-level incompetence on economic and foreign policy, radical leftism on social policy, and a singular disregard for the Constitution, Biden has perhaps earned the 45th and last place on the historical list. The Biden presidency has had no widely recognized major accomplishments â€” at least none that have risen to the level of an historic achievement â€” while it has been marked by at least seven major failings. Letâ€™s take thes'</li><li>'Exclusive â€” Sen. John Barrasso: Republicans to Hold Senate Open Nights, Weekends to Confirm Trump Nominees - Senate Majority Whip John Barrasso (R-WY) told Breitbart News Saturday that Senate Republicans will hold the Senate in session nights and weekends to confirm President Donald Trumpâ€™s nominees. Barrasso spoke to Breitbart News Saturday host Matthew Boyle after the Senate confirmed Pete Hegseth on Friday night to become the next Department of Defense secretary and right before Senate Republicans voted to make Kristi Noem the next Department of Homeland Security (DHS) secretary. Also on Saturday the Senate will vote to advance Treasury Department Secretary nominee Scott Bessent. Senate Republic'</li></ul> |
| Center | <ul><li>'Trump pardons 1,500 Jan. 6 rioters, abandons Biden-era policies - This was CNBCâ€™s coverage of President Donald J. Trumpâ€™s inauguration on Jan. 20, 2025, and his first day in office.'</li><li>'Getty Images\n\nTikTok restores service after Trump promises to issue executive order\n\nJan 18 - TikTok restored its U.S. service after the company temporarily shut down access to its app and website for its 170 million American users, shortly before a nationwide ban on the platform went into effect at midnight Sunday, Jan. 19. TikTokâ€™s announcement comes after President-elect Donald Trump earlier in the day said he would issue an executive order on his first day in office â€“â€“ Monday, Jan. 20 â€“â€“ giving the platformâ€™s China-based parent company, ByteDance, more time to work out a deal. â€œI will issue an executive order on Monday to extend the period of time before the lawâ€™s p'</li><li>'TikTok Is Back Online as Trump Proposes Nationalizing It - Just hours after going dark, TikTok is back onlineâ€”though nothing, legally, has changed. Just after midnight on Sunday, the popular but maligned Chinese-owned app ceased operation in the United States; users logging on received a message that the service "isn\'t available right now" but "we are fortunate that President [Donald] Trump has indicated that he will work with us on a solution to reinstate TikTok once he takes office." As it turned out, they didn\'t even have to wait for Trump\'s inauguration on Monday. "I\'m asking companies not to let TikTok stay dark!" Trump posted on Truth Social S'</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Left   | <ul><li>'Trump To Visit Disaster Zones In North Carolina And California On First Trip Of Second Term - WASHINGTON (AP) â€” President Donald Trump is heading to hurricane-battered western North Carolina and wildfire-ravaged Los Angeles on Friday, using the first trip of his second administration to tour areas where politics has clouded the response to deadly disasters. The Republican president has criticized former President Joe Biden for his administrationâ€™s response in North Carolina, and heâ€™s showered disdain on California leaders for water policies that he falsely claimed worsened the recent blazes. Trump is also considering overhauling the Federal Emergency Management Agency. Some of hi'</li><li>"won't do anything to change the national narrative - Error fetching article"</li><li>'GOP shows \'fascinating political\' divide over looming TikTok ban â€º - Republican senators are at odds over the looming ban of the social media website, TikTok, expected to take place Sunday, January 19 if the US Supreme Court doesn\'t stop or delay it. Punchbowl News reporter Andrew Desiderio wrote via X on Thursday, "Fascinating political dynamics on TikTok. [Senate Minority Leader Chuck] Schumer (D-NY) just now backed a delay in implementation of the TikTok forced divestiture law that Congress passed last year, effectively siding with Trump. [Senator] Tom Cotton (R-AR) , Intel chair and No. 3 in leadership, blocked an effort to extend the deadline yesterday." D'</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

## Evaluation

### Metrics
| Label   | Accuracy |
|:--------|:---------|
| **all** | 0.8084   |

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
preds = model("Biden administration finalizes crackdown on Chinese vehicles - President Joe Bidenâ€™s outgoing administration is finalizing rules on Tuesday that will effectively bar nearly all Chinese cars and trucks from the U.S. market, as part of a crackdown on vehicle software and hardware from China. Washingtonâ€™s latest move against Chinese vehicles comes after the Commerce Department said this month it was considering a similar crackdown on Chinese-made drones, in the wake of last yearâ€™s steep tariff hikes on imports of its electric vehicles. â€œItâ€™s really important because we donâ€™t want two million Chinese cars on the road and then realize ... we have a")
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
| Training set | Min | Median  | Max |
|:-------------|:----|:--------|:----|
| Word count   | 9   | 98.5768 | 143 |

| Label  | Training Sample Count |
|:-------|:----------------------|
| Center | 222                   |
| Left   | 221                   |
| Right  | 221                   |

### Training Hyperparameters
- batch_size: (16, 16)
- num_epochs: (1, 1)
- max_steps: -1
- sampling_strategy: oversampling
- num_iterations: 5
- body_learning_rate: (1e-05, 1e-05)
- head_learning_rate: 0.01
- loss: CosineSimilarityLoss
- distance_metric: cosine_distance
- margin: 0.25
- end_to_end: False
- use_amp: False
- warmup_proportion: 0.1
- seed: 42
- eval_max_steps: -1
- load_best_model_at_end: True

### Training Results
| Epoch   | Step    | Training Loss | Validation Loss |
|:-------:|:-------:|:-------------:|:---------------:|
| 0.0024  | 1       | 0.2992        | -               |
| 0.0241  | 10      | 0.3278        | -               |
| 0.0482  | 20      | 0.2922        | -               |
| 0.0723  | 30      | 0.2595        | -               |
| 0.0964  | 40      | 0.2598        | -               |
| 0.1205  | 50      | 0.2618        | -               |
| 0.1446  | 60      | 0.2946        | -               |
| 0.1687  | 70      | 0.2299        | -               |
| 0.1928  | 80      | 0.2358        | -               |
| 0.2169  | 90      | 0.2564        | -               |
| 0.2410  | 100     | 0.2762        | -               |
| 0.2651  | 110     | 0.2398        | -               |
| 0.2892  | 120     | 0.2157        | -               |
| 0.3133  | 130     | 0.2323        | -               |
| 0.3373  | 140     | 0.2304        | -               |
| 0.3614  | 150     | 0.2105        | -               |
| 0.3855  | 160     | 0.2155        | -               |
| 0.4096  | 170     | 0.2001        | -               |
| 0.4337  | 180     | 0.2537        | -               |
| 0.4578  | 190     | 0.2536        | -               |
| 0.4819  | 200     | 0.1762        | -               |
| 0.5060  | 210     | 0.2061        | -               |
| 0.5301  | 220     | 0.2762        | -               |
| 0.5542  | 230     | 0.2017        | -               |
| 0.5783  | 240     | 0.1539        | -               |
| 0.6024  | 250     | 0.148         | -               |
| 0.6265  | 260     | 0.2113        | -               |
| 0.6506  | 270     | 0.1526        | -               |
| 0.6747  | 280     | 0.0965        | -               |
| 0.6988  | 290     | 0.143         | -               |
| 0.7229  | 300     | 0.1936        | -               |
| 0.7470  | 310     | 0.1716        | -               |
| 0.7711  | 320     | 0.2062        | -               |
| 0.7952  | 330     | 0.1713        | -               |
| 0.8193  | 340     | 0.1548        | -               |
| 0.8434  | 350     | 0.1686        | -               |
| 0.8675  | 360     | 0.135         | -               |
| 0.8916  | 370     | 0.2364        | -               |
| 0.9157  | 380     | 0.1649        | -               |
| 0.9398  | 390     | 0.1808        | -               |
| 0.9639  | 400     | 0.1004        | -               |
| 0.9880  | 410     | 0.122         | -               |
| **1.0** | **415** | **-**         | **0.1637**      |

* The bold row denotes the saved checkpoint.
### Framework Versions
- Python: 3.12.0
- SetFit: 1.0.3
- Sentence Transformers: 3.1.1
- Transformers: 4.39.0
- PyTorch: 2.11.0+cpu
- Datasets: 2.18.0
- Tokenizers: 0.15.2

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