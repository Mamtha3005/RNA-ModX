import requests

url = "http://localhost:9696/predict"
rna_sequence = 'CCCCATACCCCTAGTCATCCTCGGCAGGTCTCAGTCCCGGCTCCATCTGTGCCCTCGCCCCAGCCGCAGCTATGTTGCACACCGAGGGCCACGCTCTTCTTCGGGCGGTGGGTCAGGGTAAGCTACGCTTGGCCCGTTTGCTTCTGGAGGGAGGCGCCTACGTGAATGAGGGTGATGCGCAGGGGGAGACTGCGCTAATGGCAGCCTGTCGGGCCCGCTACGACGACCCCCAGAACAAGGCACGCATGGTACGCTACCTCCTGGAGCAAGGCGCGGACCCCAATATCGCAGACCGATTAGGGCGCACGGCGCTCATGCACGCTTGCGCCGGGGGTGGGGGCGCCGCGGTGGCCTCGCTGCTCCTTGCCCACGGCGCAGACCCCTCAGTCCGAGATCACGCGGGCGCCTCGGCTCTTGTCCACGCCCTGGACCGCGGGGACCGCGAGACCCTTGCCACACTGCTGGACGCCTGCAAGGCCAAGGGTACGGAGGTCATCATCATCACCACCGATACCTCGCCCTCAGGCACCAAGAAGACCCGGCAGTATCTCAATTCTCCACCATCCCCAGGGGTGGAGGACCCTGCTCCCGCCTCTCCTAGCCCGGGGTTCTGCACGTCGCCTTCGGAAATCCAACTGCAGACCGCTGGAGGAGGAGGGCGTGGGATGTTATCCCCTCGCGCCCAGGAAGAAGAGGAGAAGCGGGACGTATTTGAATTCCCTCTTCCTAAGCCCCCCGATGACCCATCCCCTTCCGAGCCGCTCCCCAAACCACCACGCCATCCCCCAAAACCACTCAAAAGGCTCAACTCCGAGCCCTGGGGCCTAGTGGCCCCTCCTCAACCAGTCCCACCCACTGAAGGGAGACCGGGGATCGAGCGCTTGACTGCCGAATTCAATGGCCTGACCCTGACCGGTCGACCCCGTCTTTCCCGACGTCACAGCACCGAAGGCCCTGAGGACCCGCCCCCATGGGCGGAGAAAGTGACTAGCGGGGGTCCT'

result = {
    'input': rna_sequence
}

print("Posting : ", result)
r = requests.post(url, json=result)
print(r.text.strip())

