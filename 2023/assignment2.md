## NGSPipeline Assignment2

### Q1 - 请简述 FASTQ 文件格式（列出重点，不需要长篇大论）

### Q2 - reads QC

- 去除 adapter 序列，或者去除每条 reads 的前 6 个碱基；
- 删去每条 reads 测序质量低的连续一段碱基序列，比如长度大于 10 并且测序质量低于 B 的碱基比率高于 10% 的连续序列；
- 删去测序质量低的 reads，比如测序质量低于 B 的碱基比率高于 10% 的 reads；

### Q3 - FASTQ file manipulation

- 假设在 multiplexed samples 中共有 3 个样本，其 index 序列分别是 "ACGTACGT", "CGTACGTA", "GTACGTAC"，
  请将这三个 index 序列随机添加到每条 reads 的开头，并生成一个新的 FASTQ 文件。
- 对上面生成的添加了 index 序列的 FASTQ 文件进行 demultiplexing。
- 从 FASTQ 文件中随机抽样 10% 的 reads，并生成一个新的 FASTQ 文件。

上面 Q2 和 Q3 的任务可以自行编写脚本实现（比如用 python 或 R），或者用 seqtk，fastp 等工具实现。一个小提示：如果是自行
编写脚本，请注意 FASTQ 文件一般是 gz 压缩文件格式，所以需要用相应的模块支持 gz 文件的读写（比如 python 中的 `gzip`
模块）。
