## NGSPipeline Assignment4

### Q1 - NGS sequence alignment

- 请下载 hg38 genome 的 FASTA 文件；
- 对上述 FASTA 文件构建 bwa 索引；
- 用 bwa 将 assignment2 中的 FASTQ 文件比对到 hg38 基因组上，生成 BAM 文件。

### Q2 - BAM file manipulation

- 将 BAM 文件中标记为 duplicates 的 alignments 删去，并生成一个新的 BAM 文件 (`samtools view -F` and 
  `https://broadinstitute.github.io/picard/explain-flags.html`)。
- 从 BAM 文件中随机抽样 10% 的 alignments，并生成一个新的 BAM 文件 (`samtools view -s`)。
- 对 BAM 文件按坐标排序 (`samtools sort`)。
- 为上一步得到的 BAM 文件生成索引文件 (`samtools index`)。

### (可选) Q3 - pysam module

- 查看 pysam 文档：https://pysam.readthedocs.io/en/latest/api.html
