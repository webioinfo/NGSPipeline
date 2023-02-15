# NGS Pipeline

## 1. 准备工作

### Linux 安装

- 如何在 Windows 系统中安装 Linux 子系统（微软官方教程）：https://learn.microsoft.com/en-us/windows/wsl/install.

### conda 安装

- conda user guide: https://docs.conda.io/projects/conda/en/latest/user-guide/index.html
- conda installation (recommend Miniconda): https://docs.conda.io/en/latest/miniconda.html

### NGS 分析流程概论

#### 测序种类

- target, WES, WGS
- DNA-seq, RNA-seq, ATAC-seq

#### 不同文件格式

- FASTQ, BAM, VCF, BED, GTF, GFF

### 测试数据准备

## 2. FASTQ 文件

### FASTQ 文件格式

### FASTQ 文件处理

- seqtk
- fastp

## 3. BAM 文件

### BAM 文件格式

### 比对工具

- bwa
- STAR
- minimap2

### BAM 文件处理

samtools

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
