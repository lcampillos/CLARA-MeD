## CLARA-MeD Corpus


### Documents

The CLARA-MeD corpus version 1 gathers a collection of 24 298 pairs of professional and simplified texts (>96M tokens) for automatic medical text simplification in Spanish.

A parallel corpus with a subset of 3800 sentence pairs of professional and laymen variants (149 862 tokens) is released as a benchmark for medical text simplification. 

DISCLAIMER: this corpus was built for research and educational purposes. Because not all contents might be updated when using this resource, no medical decision should be taken from the data here provided. Please, check the current version of each source contents at the corresponding website (see below).


### Folders

1) Comparable corpus: the data of each source can be found in the corresponding folder. Each folder contains two other subfolders:

    - source: professional, specialized texts (".src" file extension)
    - target: simplified texts (".trg" file extension)

2) Aligned sentences: these can be found file "aligned.tsv" (in folder "aligned")

The folder structure is as follows:

    - aligned/
        - aligned.tsv
    - cima/
        - source/
        - target/
    - eudract/
        - source/
        - target/
    - nci/
        - source/
        - target/


### Source of the data

- [Centro de Información de Medicamentos (CIMA, 'Medicine Online Information Center')](https://cima.aemps.es), from the Agencia Española de Medicamentos y Productos Sanitarios (AEMPS). 
- [EU Clinical Trials Register](https://www.clinicaltrialsregister.eu)
- [National Cancer Institute (NCI)](https://www.cancer.gov)

### License

These data is aimed at research and educational purposes. 


### Contact

leonardo.campillos AT csic.es


## How to cite

If you use this corpus, please cite the reference as follows:

```
@article{2022claramedcorpus,
  title={Building a comparable corpus and a benchmark for Spanish medical text simplification},
  author={Campillos-Llanos, Leonardo and Terroba Reinares, Ana R., and Zakhir Puig, Sofía, and Valverde-Mateos, Ana and Capllonch-Carri{\'o}n},
  title={Procesamiento del Lenguaje Natural},
  volume={69},
  year={2022},
  publisher={Sociedad Espa{\~n}ola para el Procesamiento del Lenguaje Natural}

}
```
