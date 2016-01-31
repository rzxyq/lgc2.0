from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

class NewStudentForm(forms.Form):
    name = forms.CharField(max_length=35, widget=forms.TextInput(attrs={'placeholder': 'Ron Weasley'}))
    netid = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'placeholder': 'rw447'}))
    # hometown = forms.CharField(max_length=35, widget=forms.TextInput(attrs={'placeholder': 'Dallas, Texas'}))
    YEAR = (
        ('Freshman', 'Freshman'),
        ('Sophomore', 'Sophomore'),
        ('Sophomore Transfer', 'Sophomore Transfer'),
        ('Junior', 'Junior'),
        ('Junior Transfer', 'Junior Transfer'),
        ('Senior', 'Senior'),
    )
    year = forms.ChoiceField(label=("Class Year"),
        choices=YEAR, widget=forms.Select(),)
    
    SURVEY = (
    ('Clubfest','Clubfest'),
    ('Advertising','Advertising'),
    ('Another organization','Another organization'),
    ('Social Media','Social Media'),
    ('Word of mouth','Word of mouth'),
    )
    survey = forms.MultipleChoiceField(label=("How did you hear about Let’s Get Coffee?"),
        choices=SURVEY, widget=forms.CheckboxSelectMultiple(), required=False)
 
    HEARD = (
        ('None','None'),
        ('ALANA','ALANA'),
        ('Alternative Breaks','Alternative Breaks'),
        ('APO','APO'),
        ('CAPSU','CAPSU'),
        ('Cornell Catholic','Cornell Catholic'),
        ('Cornell Minds Matter','Cornell Minds Matter'),
        ('Cornell Radio','Cornell Radio'),
        ('CIAS','CIAS'),
        ('ECO','ECO'),
        ('Greek Life','Greek Life'),
        ('Haven','Haven'),
        ('Hillel','Hillel'),
        ('ISU','ISU'),
        ('Slope Media','Slope Media'),
        ('Speech & Debate','Speech & Debate'),
        ('OSC','OSC'),        
    )
    heard = forms.ChoiceField(label=("If you heard about us from one of our partnering campus organizations, specify below:"),
        choices=HEARD, widget=forms.Select(), required=False)

    PARTICIPATED = (
        ('No','No'),
        ('Yes','Yes'),
    )
    participated = forms.ChoiceField(label=("Have you participated in Let's Get Coffee before?"),
        choices=PARTICIPATED, widget=forms.Select(),)

    SCHOOL = (
        ('Agriculture & Life Sciences', 'Agriculture & Life Sciences'),
        ('Arts & Sciences', 'Arts & Sciences'),
        ('Architecture, Art & Planning','Architecture, Art & Planning'),
        ('Engineering','Engineering'),
        ('Hotel Administration','Hotel Administration'),
        ('Human Ecology','Human Ecology'),
        ('Industrial & Labor Relations','Industrial & Labor Relations'),
    )
    school = forms.ChoiceField(label=("College"),
        choices=SCHOOL, widget=forms.Select(),)
    MAJOR = (
        #First entry is an abbreviation, second is how it appears on the site
        ('Africana Studies','Africana Studies'),
        ('Agricultural Sciences','Agricultural Sciences'),
        ('American Studies','American Studies'),
        ('Animal Science','Animal Science'),
        ('Anthropology','Anthropology'),
        ('Applied Economics and Management','Applied Economics and Management'),
        ('Archaeology','Archaeology'),
        ('Architecture','Architecture'),
        ('Asian Studies','Asian Studies'),
        ('Astronomy','Astronomy'),
        ('Atmospheric Science','Atmospheric Science'),
        ('Biological Engineering','Biological Engineering'),
        ('Biological Sciences','Biological Sciences'),
        ('Biology and Society','Biology and Society'),
        ('Biometry and Statistics','Biometry and Statistics'),
        ('Biomedical Engineering', 'Biomedical Engineering'),
        ('Chemical Engineering','Chemical Engineering'),
        ('Chemistry and Chemical Biology','Chemistry and Chemical Biology'),
        ('China and Asia-Pacific Studies','China and Asia-Pacific Studies'),
        ('Civil Engineering','Civil Engineering'),
        ('Classics','Classics'),
        ('College Scholar','College Scholar'),
        ('Communication','Communication'),
        ('Comparative Literature','Comparative Literature'),
        ('Computer Science','Computer Science'),
        ('Design and Environmental Analysis','Design and Environmental Analysis'),
        ('Development Sociology','Development Sociology'),
        ('Economics','Economics'),
        ('Electrical and Computer Engineering','Electrical and Computer Engineering'),
        ('Engineering Physics','Engineering Physics'),
        ('English','English'),
        ('Entomology','Entomology'),
        ('Environmental and Sustainable Sciences','Environmental and Sustainable Sciences'),
        ('Environmental Engineering','Environmental Engineering'),
        ('Feminist, Gender and Sexuality Studies','Feminist, Gender and Sexuality Studies'),
        ('Fiber Science and Apparel Design','Fiber Science and Apparel Design'),
        ('Fine Arts','Fine Arts'),
        ('Food Science','Food Science'),
        ('French','French'),
        ('German Studies','German Studies'),
        ('Global and Public Health Sciences','Global and Public Health Sciences'),
        ('Government','Government'),
        ('History','History'),
        ('History of Architecture','History of Architecture'),
        ('History of Art','History of Art'),
        ('Hotel Administration','Hotel Administration'),
        ('Human Biology, Health and Society','Human Biology, Health and Society'),
        ('Human Development','Human Development'),
        ('Industrial and Labor Relations','Industrial and Labor Relations'),
        ('Information Science','Information Science'),
        ('Information Science Systems and Technology','Information Science, Systems and Technology'),
        ('Interdisciplinary Studies','Interdisciplinary Studies'),
        ('International Agriculture and Rural Development','International Agriculture and Rural Development'),
        ('Italian','Italian'),
        ('Landscape Architecture','Landscape Architecture'),
        ('Linguistics','Linguistics'),
        ('Materials Science and Engineering','Materials Science and Engineering'),
        ('Mathematics','Mathematics'),
        ('Mechanical Engineering','Mechanical Engineering'),
        ('Music','Music'),
        ('Near Eastern Studies','Near Eastern Studies'),
        ('Nutritional Sciences','Nutritional Sciences'),
        ('Operations Research and Engineering','Operations Research and Engineering'),
        ('Performing and Media Arts','Performing and Media Arts'),
        ('Philosophy','Philosophy'),
        ('Physics','Physics'),
        ('Plant Sciences','Plant Sciences'),
        ('Policy Analysis and Management','Policy Analysis and Management'),
        ('Psychology','Psychology'),
        ('Religious Studies','Religious Studies'),
        ('Science and Technology Studies','Science and Technology Studies'),
        ('Science of Earth Systems','Science of Earth Systems'),
        ('Sociology','Sociology'),
        ('Spanish','Spanish'),
        ('Statistics','Statistics'),
        ('Urban and Regional Planning','Urban and Regional Planning'),
        ('Viticulture and Enology','Viticulture and Enology'),
    )
    major = forms.ChoiceField(label=("Major"),
        choices=MAJOR, widget=forms.Select(),)

    MINOR = (
        #First entry is an abbreviation, second is how it appears on the site
        ('None', 'None'),
        ('Aerospace Engineering','Aerospace Engineering'),
        ('Africana Studies','Africana Studies'),
        ('Agribusiness Management','Agribusiness Management'),
        ('American Indian Studies','American Indian Studies'),
        ('Animal Science','Animal Science'),
        ('Anthropology','Anthropology'),
        ('Applied Economics','Applied Economics'),
        ('Applied Exercise Science','Applied Exercise Science'),
        ('Applied Mathematics','Applied Mathematics'),
        ('Archaeology','Archaeology'),
        ('Architecture','Architecture'),
        ('Asian American Studies','Asian American Studies'),
        ('Astronomy','Astronomy'),
        ('Atmospheric Science','Atmospheric Science'),
        ('Biological Engineering','Biological Engineering'),
        ('Biological Sciences','Biological Sciences'),
        ('Biomedical Engineering','Biomedical Engineering'),
        ('Biomedical Sciences','Biomedical Sciences'),
        ('Biometry and Statistics','Biometry and Statistics'),
        ('Business','Business'),
        ('Business for Engineering Students','Business for Engineering Students'),
        ('China and Asia-Pacific Studies','China and Asia-Pacific Studies'),
        ('Civil Infrastructure','Civil Infrastructure'),
        ('Classics','Classics'),
        ('Climate Change','Climate Change'),
        ('Cognitive Science','Cognitive Science'),
        ('Communication','Communication'),
        ('Computer Science','Computer Science'),
        ('Computing in the Arts','Computing in the Arts'),
        ('Creative Writing','Creative Writing'),
        ('Crop Management','Crop Management'),
        ('Dance','Dance'),
        ('Design and Environmental Analysis','Design and Environmental Analysis'),
        ('Development Sociology','Development Sociology'),
        ('East Asia Program','East Asia Program'),
        ('English','English'),
        ('Education','Education'),
        ('Electrical and Computer Engineering','Electrical and Computer Engineering'),
        ('Engineering Management','Engineering Management'),
        ('Engineering Statistics','Engineering Statistics'),
        ('Entomology','Entomology'),
        ('Environmental and Resource Economics','Environmental and Resource Economics'),
        ('Environmental Engineering','Environmental Engineering'),
        ('European Studies','European Studies'),
        ('Feminist, Gender and Sexuality Studies','Feminist, Gender and Sexuality Studies'),
        ('Fiber Science','Fiber Science'),
        ('Film','Film'),
        ('Fine Arts','Fine Arts'),
        ('Food Science','Food Science'),
        ('French Studies','French Studies'),
        ('Game Design','Game Design'),
        ('German Studies','German Studies'),
        ('Gerontology','Gerontology'),
        ('Global Health','Global Health'),
        ('Globalization, Ethnicity and Development','Globalization, Ethnicity and Development'),
        ('Health Policy','Health Policy'),
        ('History','History'),
        ('History of Art','History of Art'),
        ('Horticulture','Horticulture'),
        ('Human Biology','Human Biology'),
        ('Industrical Systems and Information Technology','Industrial Systems and Information Technology'),
        ('Inequality Studies','Inequality Studies'),
        ('Information Science','Information Science'),
        ('International Relations','International Relations'),
        ('International Development Studies','International Development Studies'),
        ('International Trade and Development','International Trade and Development'),
        ('Italian','Italian'),
        ('Jewish Studies','Jewish Studies'),
        ('Landscape Studies','Landscape Studies'),
        ('Latin American Studies','Latin American Studies'),
        ('Latino Studies','Latino Studies'),
        ('Law and Regulation','Law and Regulation'),
        ('Law and Society','Law and Society'),
        ('Lesbian, Gay, Bisexual and Transgender Studies','Lesbian, Gay, Bisexual and Transgender Studies'),
        ('Linguistics','Linguistics'),
        ('Marine Biology','Marine Biology'),
        ('Materials Science And Engineering','Materials Science and Engineering'),
        ('Mathematics','Mathematics'),
        ('Mechanical Engineering','Mechanical Engineering'),
        ('Medieval Studies','Medieval Studies'),
        ('Minority Indigenous and Third World Studies','Minority, Indigenous and Third World Studies'),
        ('Music','Music'),
        ('Natural Resources','Natural Resources'),
        ('Near Eastern Studies','Near Eastern Studies'),
        ('Nutrition and Health','Nutrition and Health'),
        ('Operations Research and Management Science','Operations Research and Management Science'),
        ('Physics','Physics'),
        ('Plant Sciences','Plant Sciences'),
        ('Policy Analysis and Management','Policy Analysis and Management'),
        ('Portugues and Brazilian Studies','Portuguese and Brazilian Studies'),
        ('Real Estate','Real Estate'),
        ('Religious Studies','Religious Studies'),
        ('Science and Technology Studies','Science and Technology Studies'),
        ('Science of Earth Systems','Science of Earth Systems'),
        ('Science of Natural and Environmental Systems','Science of Natural and Environmental Systems'),
        ('Soil Science','Soil Science'),
        ('South Asia Studies','South Asia Studies'),
        ('Southeast Asia Studies','Southeast Asia Studies'),
        ('Spanish','Spanish'),
        ('Sustainable Energy Systems','Sustainable Energy System'),
        ('Theatre','Theatre'),
        ('Urban and Regional Studies','Urban and Regional Studies'),
        ('Visual Studies','Visual Studies'),
        ('Viticulture and Enology','Viticulture and Enology'),
    )
    minor = forms.ChoiceField(label=("Second Major (only select a second if you are seriously considering this major)"),
        choices=MINOR, widget=forms.Select(),)

    EXTRACURRICULARS = (
        #First entry is an abbreviation, second is how it appears on the site
        ('Acapella','Acapella'),
        ('Art','Art'),
        ('Club or Intramural Sports','Club or Intramural Sports'),
        ('Comedy','Comedy'),
        ('Community Service','Community Service'),
        ('Cultural','Cultural'),
        ('Dance','Dance'),
        ('Design and Graphics','Design and Graphics'),
        ('Entrepreneurship','Entrepreneurship'),
        ('Environmental Sustainability','Environmental Sustainability'),
        ('Fashion','Fashion'),
        ('Greek Life','Greek Life'),
        ('Journalism','Journalism'),
        ('Languages','Languages'),
        ('LGBTQ','LGBTQ'),
        ('Media','Media'),
        ('Music','Music'),
        ('Outdoor Recreation','Outdoor Recreation'),
        ('Partying','Partying'),
        ('Pre-Professional Organizations','Pre-Professional Organizations'),
        ('Project Team','Project Team'),
        ('Political Activism','Political Activism'),
        ('Science Research','Science Research'),
        ('Social Science Research','Social Science Research'),
        ('Teaching/Tutoring','Teaching/Tutoring'),
        ('Travel','Travel'),
        ('Religious','Religious'),
        ('ROTC','ROTC'),
        ('Speech and Debate','Speech and Debate'),
        ('Student Government','Student Government'),
        ('Theatre','Theatre'),
        ('Varsity Sports','Varsity Sports'),
    )

    extracurriculars = forms.MultipleChoiceField(label=("Select up to five activities of extracurricular interest"),
        choices=EXTRACURRICULARS, widget=forms.CheckboxSelectMultiple())

    extra_sa = forms.CharField(label=("Feel free to list any other specific extracurricular activities (125 words max)."),
        widget=forms.Textarea, max_length=638, required=False)

    CAREER = (
        #First entry is an abbreviation, second is how it appears on the site
        ('Agriculture','Agriculture'),
        ('Art/Design','Art/Design'),
        ('Biomedical Research','Biomedical Research'),
        ('Business and Finance','Business and Finance'),
        ('Computer and Technology','Computer and Technology'),
        ('Education','Education'),
        ('Engineering','Engineering'),
        ('Entertainment','Entertainment'),
        ('Graduate Study','Graduate Study'),
        ('Government','Government'),
        ('Health Professions','Health Professions'),
        ('Hospitality','Hospitality'),
        ('International Clubs','International Clubs'),
        ('International Development','International Development'),
        ('Journalism','Journalism'),
        ('Law','Law'),
        ('Management','Management'),
        ('Media Communications','Media Communications'),
        ('Military and ArmedForces','Military and Armed Forces'),
        ('Non-Profit','Non-Profit'),
        ('Public Health','Public Health'),
        ('Sales and Marketing','Sales and Marketing'),
        ('Social Science Research','Social Science Research'),
    )

    career = forms.MultipleChoiceField(label=("Select up to three prospective fields of career interest"),
        choices=CAREER, widget=forms.CheckboxSelectMultiple())

    career_sa = forms.CharField(label=("Feel free to list any other specific prospective careers (125 words max)."),
        widget=forms.Textarea, max_length=638, required=False)

    sa1 = forms.CharField(label=("What do you want to gain from this meeting with your upperclassman? (125 words max)"),
        widget=forms.Textarea(attrs={'placeholder': 'Help choosing classes, advice for careers, just a new friend, etc.'}), max_length=638)

    sa2 = forms.CharField(label=("What questions do you want to ask of your upperclassman? (125 words max)"),
        widget=forms.Textarea(attrs={'placeholder': 'How do you balance your studies and social life, keep in touch with family and friends back home, approach professors, etc.'}), max_length=638)
    sa3 = forms.CharField(label=("Tell us something interesting about yourself. (125 words max)"),
        widget=forms.Textarea(attrs={'placeholder': 'Whatever comes to mind! Don’t spend too much time on it.'}), max_length=638)

    PARTNERING = (
        #First entry is an abbreviation, second is how it appears on the site
        ('Alternative Breaks','Alternative Breaks: Organizing student service-learning breaks during academic breaks'),
        ('APO','Alpha Phi Omega (APO): A student organization for community service at Cornell and in Ithaca'),
        ('BEARS','BEARS: Helping freshmen utilize campus resources and get more out of their year by matching them with an upperclassman mentor'),
        ('CAPSU','Cornell Asian Pacific Islander Student Union (CAPSU): Representing and connecting the Asian community at Cornell'),
        ('CIAS','Cornell International Affairs Society (CIAS): Discussions of international affairs and the Cornell group for Model UN'),
        ('Cornell Radio','CornellRadio.com: An online radio station programmed by and for Cornell students'),
        ('ECO','ECO (Cornell Environmental Collaborative): The umbrella organization for all environmental and sustainability clubs at Cornell'),
        ('Greek Life','Greek Life Tri-Council: The IFC, PHC, and MGLC comprising greek life at Cornell'),
        ('Haven','Haven: The LGBTQ+ student union is an organization that provides community, support and education for LGBTQ+ students and allies'),
        ('Hillel','Hillel: The hub for Jewish community, religious, and cultural life for Jewish students of all backgrounds'),
        ('ISU','International Student Union (ISU): A diverse board of students promoting engagement about world events, cultures, and issues'),
        ('OSC','Orientation Steering Committee (OSC): The student group responsible for organizing new student orientation'),
        ('Slope Media','Slope Media: As the Cornell multimedia powerhouse, Slope is a leader in Cornell-related media and entertainment'),
        ('Speech and Debate','Cornell Speech & Debate Society: Organizing intercollegiate speech and debate competition at Cornell'),
)   

    partnering = forms.MultipleChoiceField(label=("We partner with some of the best organizations on campus. Let them know if you’re interested in what they do."),
        choices=PARTNERING, widget=forms.CheckboxSelectMultiple(), required=False)

