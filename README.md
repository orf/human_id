# Human ID

A simple library for generating human IDs like `look-dead-game-story` or `get-nice-office-side`. 

Install with `pip install human-id`

Usage:

```python
from human_id import generate_id

# Simple: "appear-hard-idea-case"
generate_id()

# Custom separator: "do,past,job,number"
generate_id(separator=",")

# More words: "say-may-ask-traditional-power-week"
generate_id(word_count=10)

# Custom seed - the same UUID will produce the same ID.
import uuid
generate_id(seed=uuid.uuid4())
```

## Implementation

This library contains 100 of the most common English nouns, adjectives and verbs, and will 
generate a phrase containing several of each type, in the order `verb, adjective, noun`.

The most common words where chosen because they are typically shorter and simpler to read or type, 
which is a key property of human readable IDs.

By default the ID will contain 4 words, which means there are `300^4` possible IDs (8,100,000,000). If your 
use case requires more IDs then you can up the number of words at the expense of the readability factor. To 
have the same number of possible IDs as UUIDs you require 15 words:

`may-hold-come-foreign-low-white-cold-team-point-study-others-home-service-body-child`
