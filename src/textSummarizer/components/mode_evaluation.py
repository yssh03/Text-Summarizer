from typing import Generator
from tqdm import tqdm
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from datasets import load_from_disk
import pandas as pd
from textSummarizer.entity import ModelEvaluationConfig
from evaluate import load


class ModelEvaluation:
    def __init__(self, config=ModelEvaluationConfig) -> None:
        self.config = config

    def generate_batch_sized_chunk(self, dataset, batch) -> Generator[list, None, None]:
        for i in range(0, len(dataset), batch):
            yield list(dataset[i:i+batch])

    def metric_for_test_data(self, dataset, metric,  model, tokenizer, device, column_text, column_summary, batch_size=16) -> None:
        article_batch = list(self.generate_batch_sized_chunk(
            dataset[column_text], batch_size))
        summary_batch = list(self.generate_batch_sized_chunk(
            dataset[column_summary], batch_size))
        for article_batch, target_batch in tqdm(
                zip(article_batch, summary_batch), total=len(summary_batch)):

            inputs = tokenizer(article_batch, max_length=1024,  truncation=True,
                               padding="max_length", return_tensors="pt")

            summaries = model.generate(input_ids=inputs["input_ids"].to(device),
                                       attention_mask=inputs["attention_mask"].to(
                                           device),
                                       length_penalty=0.8, num_beams=8, max_length=128)
            ''' parameter for length penalty ensures that the model does not generate sequences that are too long. '''
            decoded_summaries = [tokenizer.decode(s, skip_special_tokens=True,
                                                  clean_up_tokenization_spaces=True)
                                 for s in summaries]
            decoded_summaries = [d.replace("", " ") for d in decoded_summaries]

            metric.add_batch(predictions=decoded_summaries,
                             references=target_batch)
        score = metric.compute()
        return score

    def evaluate(self) -> None:
        device = "cuda" if torch.cuda.is_available() else "cpu"
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(
            self.config.model).to(device)

        # loading data
        dataset_samsum_pt = load_from_disk(self.config.data)

        rouge_names = ["rouge1", "rouge2", "rougeL", "rougeLsum"]

        rouge_metric = load('rouge')
        score = self.metric_for_test_data(
            dataset_samsum_pt['test'][1:10], rouge_metric, model_pegasus, tokenizer, device, 'dialogue', 'summary', 2)
        rouge_dict = dict((rn, score[rn]) for rn in rouge_names)

        df = pd.DataFrame(rouge_dict, index=['pegasus'])
        df.to_csv(self.config.metrics_file, index=False)
