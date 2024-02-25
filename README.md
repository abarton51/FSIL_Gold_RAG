# FSIL_Gold_RAG (FRALM)

FRALM, (Financial Retrieval-Augmented Language Models) is a project to test the efficacy of Retrieval-Augmented Language Models (RALMS) as a possible substitute for supervised fine-tuning approaches in pursuit of the construction of a finance domain language model. 

Our project proposal, which can give a more detailed overview of our objectives, can be found [here](https://drive.google.com/file/d/14DgoEsQXqudRCquihNhUoUzRDLaKNamA/view?usp=sharing).

### Models

In pursuit of our goal, we plan to implement the following LLama2-base RALM models. 

- Llama2-7B with Naive RAG
- Llama2-7B with RA-DIT
- Llama2-7B with Self-RAG

### Benchmarks

We will evaluate our models over the FLARE financial NLP benchmark presented in the [PIXIU paper](https://arxiv.org/abs/2306.05443). We may further limit our testing to specific benchmark tasks in the future, as we further refine the desired capabilities of our Financial RALM. 
