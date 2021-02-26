import pandas as pd
url='https://en.wikipedia.org/wiki/List_of_Greek_and_Latin_roots_in_English/A%E2%80%93G'

df=pd.read_html(url, header=0)[0]

df.head()
