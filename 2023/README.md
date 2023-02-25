# NGS Pipeline

## 1. 准备工作

### Linux 安装

- 如何在 Windows 系统中安装 Linux 子系统（微软官方教程）：https://learn.microsoft.com/en-us/windows/wsl/install.

### conda 安装

- conda user guide: https://docs.conda.io/projects/conda/en/latest/user-guide/index.html
- conda installation (recommend Miniconda): https://docs.conda.io/en/latest/miniconda.html

conda 安装完成后需要添加两个常用的channel：

```
conda config --add channels conda-forge
conda config --add channels bioconda
```

### 软件环境安装

- Python: `conda install python`
- R: `conda install R`

### NGS 分析流程概论

- Illumina Sequencing Overview: https://www.ogc.ox.ac.uk/wp-content/uploads/2017/09/Illumina_Sequencing_Overview_15045845_D.pdf

#### 测序种类

- target, WES, WGS
- DNA-seq, RNA-seq, ATAC-seq

#### 不同文件格式

- FASTQ, BAM, VCF, BED, GTF, GFF

### 测试数据准备

## 2. FASTQ 文件

### FASTQ 文件格式

- FASTQ files explained: https://support.illumina.com/bulletins/2016/04/fastq-files-explained.html

### FASTQ 文件处理

- seqtk: `conda install seqtk`; https://github.com/lh3/seqtk
- fastp: `conda install fastp`; https://github.com/OpenGene/fastp

## 3. BAM 文件

### 序列比对

Introduction to Sequence Alignment: https://learn.gencore.bio.nyu.edu/wp-content/uploads/2018/01/IntroSeqAlign2018.pdf

### NGS 比对工具

- bwa: `conda install bwa`; https://bio-bwa.sourceforge.net/bwa.shtml
- STAR: `conda install star`; https://github.com/alexdobin/STAR/blob/master/doc/STARmanual.pdf
- minimap2: `conda install minimap2`; https://github.com/lh3/minimap2/blob/master/README.md

### BAM 文件格式

- Sequence Alignment/Map Format Specification (可以直接查看 1.4 小节 "The alignment section: mandatory fields"): https://samtools.github.io/hts-specs/SAMv1.pdf

### BAM 文件处理

samtools: `conda install 'samtools>=1.10'`; http://www.htslib.org/doc/samtools.html

## 4. VCF 文件

### VCF 文件格式

### SNP calling

- bcftools
- freebayes
- GATK (Mutect2)
- DeepVariant

### VCF 文件处理

- bcftools
- vcftools

## 5. 注释文件

### BED 文件

bedtools

### GTF/GFF 文件

gffread

## 6. DEG 分析

### 通用统计方法

- t-test
- 秩和检验

### 成熟工具

- DESeq2
- edgeR

## 7. CNV 分析

- CNVKit
- Sequenza

## 8. 项目练习

复现一篇（自选）论文的结果：

- germline SNP calling;
- somatic SNP calling;
- DEG;
- CNV

## 恭喜结业
