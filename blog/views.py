from rest_framework.views import APIView
from rest_framework.response import Response
from blog.models import Post, Category
from blog.serializers import PostSerializer
from rest_framework.generics import ListCreateAPIView
from blog.serializers import CategorySerialozer

# Create your views here.
#MVC => MTV
# JAVAのVとDjangoのViewは別物（DjangoのViewはContorolerと同意）
# M = M
# V = View = Templete
# C = View

# 認証を使用した実装
# もう少し楽に（汎用ビュー）
#　オーソドックスな書き方
class PostListAppView(APIView):
  #get POST メソッドの振り分けをする
  def get(self, request):
    posts = Post.objects.all()

    serializer = PostSerializer(posts, many = True)

    print(posts)
    # dataはJson形式　Instanceがmodelにして返す
    return Response(serializer.data, status= 200)

  # 作成API 記事作成
  # def post.create(self, request)
  # def create(self, request):
  #   postData = Post.objects.all()
  #   serializer = PostSerializer(posts, many = True)

#　テキストの内容はきれいだが汎用性が低いらしい

class CategoryListView(ListCreateAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerialozer


# class CategoryListAPIView(APIView):
