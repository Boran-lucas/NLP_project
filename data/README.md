
#### Data Instruction

The structure of the directory is described as follows. And we retain 2 examples in each file at present. We will publish the whole dataset after the anomyous period.

```markdown
├── data
   └── `mans_data`
       ├── `mans_roc.json`	# sampled stories and corresponding human annotation.   
       ├── `mans_wp.json`		# sampled stories and corresponding human annotation.       
   └── `autos_data`
       ├── `roc`
              └── `roc_train_ipt.txt`	# input for training set
              └── `roc_train_opt.txt`	# output for training set
              └── `roc_valid_ipt.txt`	# input for validation set
              └── `roc_valid_opt.txt`	# output for validation set
              └── `roc_test_ipt.txt`	# input for test set
              └── `roc_test_opt.txt`	# output for test set
              └── `discrimination_test`	# different names correspons to different aspects                     
                 ├── `roc_lexical_rept.txt`
                 ├── `roc_lexical_rept_perturb.txt`										
                 ├── `roc_semantic_rept.txt`
                 ├── `roc_semantic_rept_perturb.txt`
                 ├── `roc_character.txt`
                 ├── `roc_character_perturb.txt`
                 ├── `roc_commonsense.txt`
                 ├── `roc_commonsense_perturb.txt`												
                 ├── `roc_relatedness.txt`
                 ├── `roc_relatedness_perturb.txt`
                 ├── `roc_consistency.txt`
                 ├── `roc_consistency_perturb.txt`								
                 ├── `roc_cause.txt`
                 ├── `roc_cause_perturb.txt`       										
                 ├── `roc_time.txt`
                 ├── `roc_time_perturb.txt`                    
              └── `invariance_test`
                 ├── `roc_synonym_substitute_perturb.txt`
                 ├── `roc_semantic_substitute_perturb.txt`
                 ├── `roc_contraction_perturb.txt`
                 ├── `roc_delete_punct_perturb.txt`
                 ├── `roc_typos_perturb.txt`
                 ├── `roc_negative_sample.txt`	# sampled negative samples from the discrimination test.	
                 ├── `roc_negative_sample_synonym_substitute_perturb.txt`
                 ├── `roc_negative_sample_semantic_substitute_perturb.txt`
                 ├── `roc_negative_sample_contraction_perturb.txt`
                 ├── `roc_negative_sample_delete_punct_perturb.txt`
                 ├── `roc_negative_sample_typos_perturb.txt`
       ├── `wp`
              └── ...
```
