from django.db import models
from board.models import Board
from member.models import Member


class Comment(models.Model):
    cno = models.AutoField(primary_key=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True,blank=True)
    cname = models.CharField(max_length=50, blank=True, null=True)  # 비회원 이름
    cpw = models.CharField(max_length=10, blank=True, null=True)
    ccontent = models.TextField(blank=True)
    cdate = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f"{self.cno},{self.board.bno},{self.member.id if self.member else self.cname},{self.ccontent},{self.cdate}"
