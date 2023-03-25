# 请简述 FASTQ 文件格式（列出重点，不需要长篇大论）
    #第一行：为序列ID

    #第二行：序列

    #第三行：固定为“+”

    #第四行：序列的质量值（quality score）——其中!为最低质量、~则为最高质量。以下字符从左到右代表从低到高的质量得分的： !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~


# reads QC
# 定义函数：去除adapter序列或前6个碱基
def trim_reads(raw_fq, trimmed_fq):
    with open(raw_fq, 'r') as f_raw, open(trimmed_fq, 'w') as f_trimmed:
        lines = []
        for line in f_raw:
            lines.append(line.strip())
            if len(lines) == 4:
                seq = lines[1]
                # 前6个碱基
                seq = seq[6:]
                f_trimmed.write('\n'.join([lines[0], seq, lines[2], lines[3]]) + '\n')
                lines = []

# 定义函数：删去reads测序质量低的连续一段碱基序列，比如长度大于 10 并且测序质量低于 B 的碱基比率高于 10% 的连续序列
def filter_reads(raw_fq, filtered_fq, b=20):
    with open(raw_fq, 'r') as f_trimmed, open(filtered_fq, 'w') as f_filtered:
        lines = []
        for line in f_trimmed:
            lines.append(line.strip())
            if len(lines) == 4:
                seq = lines[1]
                qual = lines[3]
                start = None
                i = 0
                while i < len(qual):
                    if ord(qual[i]) - 33 < b:
                        if start is None:
                            start = i
                    else:
                        if start is not None and i - start > 10:
                            seq = seq[:start] + seq[i:]
                            qual = qual[:start] + qual[i:]
                        i = start - 1
                        start = None
                    i += 1
        # 删去测序质量低于B的reads
        qual_scores = [ord(q) - 33 for q in qual]
        if sum([q < b for q in qual_scores]) < len(qual_scores) * 0.1:
            f_filtered.write('\n'.join([lines[0], seq, lines[2], qual]) + '\n')
            lines = []

# 依次调用函数进行处理
trim_reads('test.fastq', 'trimmed_reads.fastq')
filter_reads('trimmed_reads.fastq', 'filtered_reads.fastq')


#需要根据实际情况调整代码中的参数，如去除的adapter序列或前N个碱基、限定的最低测序质量阈值等。

import random

# 随机添加index序列
sample_index = ["ACGTACGT", "CGTACGTA", "GTACGTAC"]
with open('test.fastq', 'r') as f_raw, open('indexed_reads.fastq', 'w') as f_index:
    lines = []
    for line in f_raw:
        lines.append(line.strip())
        if len(lines) == 4:
            i = random.randint(0, 2)  # 随机选择一个index序列
            index_seq =sample_index[i]  + '+' +  lines[1][0:6] + '+' + lines[1][6:]
            lines[1] = index_seq
            f_index.write('\n'.join(lines) + '\n')
            lines = []

# demultiplexing
sample_reads = {'ACGTACGT': [], 'CGTACGTA': [], 'GTACGTAC': []}  # 分别存放三个样本的reads
with open('indexed_reads.fastq', 'r') as f_index:
    lines = []
    for line in f_index:
        lines.append(line.strip())
        if len(lines) == 4:
            # 根据index序列将read分配到相应的样本
            index = lines[1][0:6]
            if index in sample_reads:
                sample_reads[index].append('\n'.join(lines))
            lines = []

# 随机抽样10%的reads
with open('test.fastq', 'r') as f_raw, open('sampled_reads.fastq', 'w') as f_sample:
    num=(len(f_raw.readlines()))//4
    num_sampled = int(num_reads * 0.1)  # 抽样数量
    sample=random.sample(range(1,num),num_sampled)
    lines = []
    for line in f_raw:
        lines.append(line.strip())
        i=1
        if len(lines) == 4 and i in sample:
            f_sample.write('\n'.join(lines) + '\n')
            i+=1
