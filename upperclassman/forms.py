from django import forms

class UpperClassmanForm(forms.Form):
    name = forms.CharField(max_length=35, widget=forms.TextInput(attrs={'placeholder': 'Jon Snow'}))
    netid = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'placeholder': 'js274'}))
    YEAR = (
        ('Freshman', 'Freshman'),
        ('Sophomore', 'Sophomore'),
        ('Junior', 'Junior'),
        ('Senior', 'Senior'),
    )
    year = forms.ChoiceField(label=("Class Year"),
        choices=YEAR, widget=forms.Select(), initial='FR')
    SCHOOL = (
        ('Agriculture & Life Sciences', 'Agriculture & Life Sciences'),
        ('Architecture, Art & Planning','Architecture, Art & Planning'),
        ('Arts & Sciences', 'Arts & Sciences'),
        ('Engineering','Engineering'),
        ('Hotel Administration','Hotel Administration'),
        ('Human Ecology','Human Ecology'),
        ('Industrial & Labor Relations','Industrial & Labor Relations'),
    )
    school = forms.ChoiceField(label=("College"),
        choices=SCHOOL, widget=forms.Select(), initial='AS')
    MAJOR1 = (
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
    MAJOR2 = (
        #First entry is an abbreviation, second is how it appears on the site
        ('None', 'None'),
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
    major1 = forms.ChoiceField(label=("Area of Study 1"),
        choices=MAJOR1, widget=forms.Select(), initial='Africana Studies')
    major2 = forms.ChoiceField(label=("Area of Study 2"),
        choices=MAJOR2, widget=forms.Select())
    major3 = forms.ChoiceField(label=("Area of Study 3"),
        choices=MAJOR2, widget=forms.Select())

    SURVEY = (
        ('Clubfest','Clubfest'),
        ('Advertising','Advertising'),
        ('Another organization','Another organization'),
        ('Social Media','Social Media'),
        ('Word of mouth','Word of mouth'),
        )

    survey = forms.MultipleChoiceField(label=("How did you hear about us?"),
        choices=SURVEY, widget=forms.CheckboxSelectMultiple(), required=False)

    PARTICIPATED = (
        ('No','No'),
        ('Yes','Yes'),
    )
    participated = forms.ChoiceField(label=("Have you participated in Let's Get Coffee before?"),
        choices=PARTICIPATED, widget=forms.Select(),)

    ORGANIZATIONS = (
        ('',''),
        ('Alternative Breaks','Alternative Breaks'),
        ('APO','APO'),
        ('BEARS','BEARS'),
        ('CAPSU','CAPSU'),
        ('CIAS','CIAS'),
        ('CornellRadio.com','CornellRadio.com'),
        ('ECO','ECO'),
        ('Haven','Haven'),
        ('Hillel','Hillel'),
        ('IFC','IFC'),
        ('ISU','ISU'),
        ('MGLC','MGLC'),
        ('OSC','OSC'),
        ('PHC','PHC'),
        ('Slope Media','Slope Media'),
        ('Speech & Debate','Speech & Debate'),   
        )

    organization = forms.ChoiceField(label=("Are you a part of a partnering campus organization? If so, which one?"),
        choices=ORGANIZATIONS, widget=forms.Select(), required=False 
        )