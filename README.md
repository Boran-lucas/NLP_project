# NLP Text Similarity
This project is a component of the 3rd-year NLP course at ENSAE, where we opted to focus on subject 4, specifically: "Text Similarity as An Evaluation Measure of Text Generation."

The primary objective of this project is to assess the correlation between existing NLG evaluation metrics and human scores over time, with an emphasis on story generation.

Our project resources include a notebook titled "benchmark.ipynb," a directory containing the metric codes, a separate folder dedicated to data, and another folder housing the resulting figures.

# Acknowledgments

We derived a portion of our metrics from the repository located at https://github.com/PierreColombo/nlg_eval_via_simi_measures. During this process, we faced a challenge with the GPU implementation of InfoLM and could not rectify the problem. Nonetheless, all other computation methods from the original project were maintained without any modifications.

We utilized the 'hanna_stories_annotation.csv' and 'hanna_metric_scores.csv' files obtained from the https://github.com/dig-team/hanna-benchmark-asg repository. Additionally, the 'mans_roc.json' and the 'mans_wp.json' files obtained from the https://github.com/thu-coai/OpenMEVA repository.