from django import forms

from .models import Comment, Topic

class CreateTopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = [
            'title'
        ]


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'body', 'author', 'post'
        ]

    def __init__(self, *args, **kwargs):
        ...
        super(CreateCommentForm, self).__init__(*args, **kwargs)
        self.fields['body'].required = False
