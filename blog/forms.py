from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'video']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'video': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'image': 'Upload Image (optional)',
            'video': 'Upload Video (optional)',
        }

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if image.size > 5*1024*1024:  # 5MB limit
                raise forms.ValidationError("Image file too large (max 5MB)")
        return image

    def clean_video(self):
        video = self.cleaned_data.get('video')
        if video:
            if video.size > 50*1024*1024:  # 50MB limit
                raise forms.ValidationError("Video file too large (max 50MB)")
        return video

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Write your comment here...'
            }),
        }