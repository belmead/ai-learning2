# Concept Review (5–10 min)

## What is inference?
In machine learning, inference is the process of using a trained model to make predictions on new, unseen data. It follows the training phase, where the model learns patterns from historical data. During inference, the model applies this learned knowledge to generate outputs, such as classifications or numerical predictions, based on input features. This step is essential for deploying machine learning models in real-world applications like fraud detection, medical diagnosis, and recommendation systems

## What are logits, attention, and tokenization?
### *Logits* are the raw, unnormalized outputs produced by a model's final layer before applying an activation function like softmax or sigmoid. They represent the model's confidence scores for each class in classification tasks. For instance, in a binary classification, a logit might be any real number, which is then transformed into a probability between 0 and 1 using the sigmoid function. In multi-class classification, the softmax function is applied to the logits to obtain a probability distribution over classes.

### *Attention* mechanisms allow models to focus on specific parts of the input data when generating each part of the output. In the context of NLP, attention helps models weigh the importance of different words in an input sequence, enabling them to capture context more effectively. This mechanism is fundamental to transformer architectures, where it facilitates the modeling of relationships between all words in a sequence simultaneously, rather than sequentially.

### *Tokenization* is the process of breaking down text into smaller units called tokens. These tokens can be words, subwords, or characters, depending on the tokenization strategy. Tokenization is a crucial preprocessing step in NLP, as it converts raw text into a format that models can process. For example, the sentence "The quick brown fox" might be tokenized into ["The", "quick", "brown", "fox"] using word-level tokenization.
