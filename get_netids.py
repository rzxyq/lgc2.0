from newstudent.models import NewStudent
import sys
f = open('newstudent.txt', 'w')

for s in NewStudent.objects.all():
    print(s.netid)

from upperclassman.models import Upperclassman
for u in Upperclassman.objects.all():
    print(u.netid)

f.close()