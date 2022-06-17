import pandas as pd

# Importing URL files
df=pd.read_csv('URL_DEGREES.txt')
df.columns=['URL Links']

# Note how degree plan links are formatted as: 
# "https://www.utdallas.edu/fact-sheets/" + (department) + "/" + (degree plan name)
# With this in mind, I will find all the corresponding department link names.

# getting rid of the first part of the URL links
links = df['URL Links']
links = links.map(lambda link: link.replace('https://www.utdallas.edu/fact-sheets/',''))

# to get the department initials, we need to traverse each string until it hits a '/' character, then remove everything past that including the '/'
# first, need to write out helper function that lets us do as described
def find_dept_intials(str_):
  for counter, c in enumerate(str_):
    if(c=='/'): # no need for else statement as all str_ will be assumed to have a '/' in the str_
      return str_[0:counter]

# map function over links, then add to main dataframe
df['Department Initials'] = links.map(find_dept_intials)

# exporting as csv
df.to_csv('output.csv', index=False)
