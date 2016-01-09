majorslong = '''Africana Studies
Agricultural Sciences
American Studies
Animal Science
Anthropology
Applied Economics and Management
Archaeology
Architecture
Asian Studies
Astronomy
Atmospheric Science
Biological Engineering
Biological Sciences
Biology and Society
Biometry and Statistics
Chemical Engineering
Chemistry and Chemical Biology
China and Asia-Pacific Studies
Civil Engineering
Classics (Greek, Latin)
College Scholar Program
Communication
Comparative Literature
Computer Science
Design and Environmental Analysis
Development Sociology
Economics
Electrical and Computer Engineering
Engineering Physics
English
Entomology
Environmental and Sustainability Sciences
Environmental Engineering
Feminist, Gender & Sexuality Studies
Fiber Science and Apparel Design
Fine Arts
Food Science
French
German Studies
Global and Public Health Sciences
Government
History
History of Architecture
History of Art
Hotel Administration
Human Biology, Health and Society
Human Development
Independent Major
Industrial and Labor Relations
Information Science
Information Science, Systems, and Technology
Interdisciplinary Studies
International Agriculture and Rural Development
Italian
Landscape Architecture
Linguistics
Materials Science and Engineering
Mathematics
Mechanical Engineering
Music
Near Eastern Studies
Nutritional Sciences
Operations Research and Engineering
Performing and Media Arts
Philosophy
Physics
Plant Science
Policy Analysis and Management
Psychology
Religious Studies
Science and Technology Studies
Science of Earth Systems
Sociology
Spanish
Statistical Science
Urban and Regional Studies
Viticulture and Enology'''



majorslong = majorslong.split('\n')
finishedS = ''
for major in majorslong:
    finishedS += "('" + major + "','" + major + "'),\n"
print(finishedS)