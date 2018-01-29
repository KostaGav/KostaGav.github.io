import codecs, nltk

dataset = codecs.open("presse/fdp/fdp.tsv", "r", "utf-8").read().strip().split("\n")

output = codecs.open("presse/fdp/fdp_final.tsv","w","utf-8")

print type(dataset)

dataset_final =[]
# how to quickly find an article from the dataset
for k in range(len(dataset)):
    article = dataset[k]
    if "\tFDP-Fraktion\t" in article:
        meta = article.split("\t")[0]
        frak = article.split("\t")[1]
        header = article.split("\t")[2]
        content = article.split("\t")[3]
        output.write(article.split("\t")[0] + "\t" + article.split("\t")[1] + "\t" + article.split("\t")[2] + '\t' + article.split("\t")[3] + '\n')

output.close()

