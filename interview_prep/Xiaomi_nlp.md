# Xiaomi NLP:

#### 1st round:

1. Comparative learning what are the losses and why the temperature coefficients are added?

   1. The primary goal is to ensure that similar pairs (positive pairs) are closer in the representation space, while dissimilar pairs (negative pairs) are farther apart. 

2. Transformer structure, bert input, bert parameter quantity calculation

   1. Encoder, Decoder
   2. Bidirectional Encoder Representations from Transformers
      1. Input Representation: 
         1. **Token Embeddings:** Embeddings of individual tokens from vocabulary 
         2. **Segment Embeddings:** BERT can take two sentences as inputs, separated by a special token ([SEP]). Segment embeddings are used to distinguish between the two sentences.
         3. **Positional Embeddings:** These embeddings provide information about the position of the tokens in the sequence. They allow the model to consider the order of the words.  
   3. The number of parameters in a BERT model 
      1. **Size of the Token Embeddings:** The size of the vocabulary (V) and the dimensionality of the embeddings (H or d_model).
         1. V * H
      2. **Number of Transformer Blocks (L):** L * (8 * H * H + 2 * H * H), (the factor 8 accounts for the Q, K, V, and output projections for the multi-head attention, and the factor 2 accounts for the two layers in the feed-forward network).
      3. **Number of Attention Heads (A)**

3. How to solve the problem of duplicate generation by the model?

   1. ##### Modify the Decoding Strategy

      1. **Beam Search**: Instead of generating one word at a time, beam search considers multiple possible next words at each step, keeping a fixed number of most likely sequence candidates at each time step. However, it might still lead to duplicates in different candidate sequences.
      2. **Top-k Sampling:** Limits the next word prediction only to the top-k most likely words. This reduces the chance of picking up less likely words that might lead to repetition.
      3. **Nucleus (Top-p) Sampling**: Instead of sampling from the top-k words, samples from the smallest set of words whose cumulative probability exceeds the threshold p. This helps in maintaining the diversity of the generated text.

   2. ##### Penalize Repetition: 

      1. **Modify the Scoring Function**: Adjust the scoring function used by the decoding algorithm to penalize words that have already appeared. For example, reducing the probability of words that occur frequently in the text can discourage repetition.
      2. **Use a Repetition Penalty**: Specifically design a penalty that decreases the scores of previously generated tokens.

   3. ##### Post-processing:

      1. **Deduplication**: Implement post-processing steps to remove repeated phrases or sentences after the text is generated. This might involve checking for repeated subsequences and removing or replacing them.
      2. **Rule-based Cleanup**: Apply heuristic rules to identify and eliminate common types of repetition. For instance, if a sentence ends with the same phrase it starts with, the repetition can be removed.

   4. ##### Adjust Training Data and Loss Function:

      1. **Diverse Dataset**: Ensure the training dataset is diverse and does not contain many examples of repetitions. The model learns from data, and if the data contains many repetitions, the model is likely to learn to repeat itself.
      2. **Custom Loss Functions**: Design loss functions that explicitly penalize the model for generating duplicate content. For instance, incorporate a term in the loss function that increases the loss for repeated n-grams.

   5. ##### Architectural Changes:

      1. **Incorporate a Coverage Mechanism**: Inspired by models in machine translation, a coverage mechanism can keep track of what has been generated so far to discourage repetition.
      2. **Use Pointer Networks**: In tasks like text summarization, pointer networks can help the model copy unique content from the source text and reduce mindless repetition.

   6. ##### Contextual Awareness and Attention Mechanism Tweaks

      1. **Enhance Contextual Awareness**: Ensure the model has a broad enough context window to understand what has been generated so far. Transformers typically handle this well due to their attention mechanisms, but for very long texts, even transformers might struggle.
      2. **Tweak Attention Mechanisms**: Adjust the attention mechanism to weigh earlier tokens less, thereby reducing their influence on future token generation.

4. Leetcode 121/2 stock buys



#### 2nd round:

1. Sentence-bert theory, training methods
2. Difference between roberta and bert
3. Difference between BPE and WordPiece Segmentation, Advantages and Disadvantages of Subword-based Segmentation
4. Algorithmic Problems:Finding Targets in Matrices with Increasing Rows and Ranks