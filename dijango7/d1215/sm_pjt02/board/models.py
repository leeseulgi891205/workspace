from django.db import models
from member.models import Member

class Board(models.Model):
    bno = models.AutoField(primary_key=True)
    member = models.ForeignKey(Member,on_delete=models.DO_NOTHING,null=True)
    btitle = models.CharField(max_length=1000)
    bcontent = models.TextField()
    bgroup = models.IntegerField(default=0)
    bstep = models.IntegerField(default=0)
    bindent = models.IntegerField(default=0)
    bhit = models.IntegerField(default=0)
    bfile = models.CharField(max_length=100,default='')
    bdate = models.DateTimeField(auto_now=True)
    
    # 답변달기 사용에 필요한 컬럼
    # bgroup,bstep,bindent
    # 파일첨부
    # bfile
    
    def __str__(self):
        return f'{self.bno},{self.btitle},{self.member.id},{self.bdate}'

class Comment(models.Model):
    cno = models.AutoField(primary_key=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.DO_NOTHING, null=True)
    ccontent = models.TextField()
    cdate = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.cno},{self.board.bno},{self.ccontent}'
    
