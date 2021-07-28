import pandas as pd
 
def pyspelling_reporter(fn='typos.txt', out_csv='typos.csv', out_report=None,
                        typo_report=None, typo_wordlist=None):
    """Generate report dataframe."""
    with open(fn, 'r') as f:
        txt = f.readlines()
    
    # aspell
    df = pd.DataFrame(columns=['filename', 'cell_type', 'typo'])
    
    currfile = ''
    cell_type = ''
    
    for t in txt:
        t = t.strip('\n').strip()
        if not t or t in ['Misspelled words:', '!!!Spelling check failed!!!'] or t.startswith('-----'):
            continue
        
        if t.startswith('<htmlcontent>') or t.startswith('<py-'):
            if t.startswith('<html'):
                cell_type = 'md'
            elif t.startswith('<py-'):
                cell_type = 'code'
            else:
                cell_type=''
    
            currfile = t.split('/')[-1].split('.ipynb')[0]#+'.ipynb'
            continue
            
        df = df.append({'filename': currfile, 'cell_type': cell_type,
                        'typo': t}, ignore_index=True)

    if out_csv:
        df.to_csv(out_csv, index=False)

    if out_report:
        reports = pd.DataFrame()
        # Do we want to allow for some sort of pattern match on filename to limit files shown in summary report?
        df_group = df[(df['cell_type']=='md')][['filename','typo']].groupby(['filename'])
     
        for key, item in df_group:
            reports = pd.concat([reports, df_group.get_group(key).value_counts().to_frame()])

        print(f"Writing summary report to {out_report}")
        reports.to_csv(out_report, header=False)

    if typo_report:
        print(f"Writing typo report to {typo_report}")
        df['typo'].value_counts().to_csv(typo_report, header=False)

    if typo_wordlist:
        print(f"Writing typo wordlist to {typo_wordlist}")
        with open(typo_wordlist, 'w') as outfile:
            outfile.write('\n'.join(df['typo'].value_counts().index))

    return df
