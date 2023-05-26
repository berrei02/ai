# Building a Generatively Pretrained Transformer (GPT)

Inspired by [Andrej Karpathy's walkthrough](https://www.youtube.com/watch?v=kCc8FmEb1nY&t)

- Status: Until min 52:00

Learnings so far:
- Could work with any arbitrary text (here: Shakespear)
- Characters are translated to integers (there are multiple strategies subwords or whole words or single chars)
- Each text can be encoded and decoded again
- Sequences of chars are drawn upon to "predict" the upcoming character
- If you have a sequence "hello", you can predict "h->e", "he->l", "hel->l", "hell->o"
- Kaparthi uses a simple NN (bigram)
- Attention basically means looking to the left (what do I know of my string already to predict the next char)
- Attention is achieved in this case by matrix multiplication (the quant trick)
- With his char-by-char encoding and Bigram NN, Karpathi is using dumb-simple versions for illustration, IRL better performance is achieved by more sophistication
- I should maybe view Karpathis video on Bigram before