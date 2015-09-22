df = pd.read_table('UPF1-KnockDown-UP-Yepiskoposyan.etal.exp')
dfx = df[(df.Mock > 20) & (df.RSV > 20)]
