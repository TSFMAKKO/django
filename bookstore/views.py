from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# views.py
from django.shortcuts import render
from .models import Book, Customer, Order

def index(request):
    # 獲取所有書籍
    books = Book.objects.all()
    # 獲取所有客戶
    customers = Customer.objects.all()
    # 獲取所有訂單
    orders = Order.objects.all()
    # 傳遞數據到模板
    return render(request, 'index.html', {
        'books': books,
        'customers': customers,
        'orders': orders,
    })

def search_customer_orders(request):
    # 從表單中獲取顧客姓名
    customer_name = request.POST.get("customer_name")
    print("customer_name:",customer_name)
    # 查詢顧客的訂單
    # customer = Customer.objects.get(name=customer_name)
    try:
    # 嘗試查詢指定名稱的顧客
        customer = Customer.objects.get(name=customer_name)
    except:
        customer = None
       # 如果顧客不存在，則返回一個空的顧客對象
         
    
    # customer = Customer.objects.get(name="yu")
    # print("customer:",customer)
    orders = Order.objects.filter(customer=customer)
    # print("orders:",orders)
    # 顯示查詢結果
    # orders=[{"id":"001"},{"id":"002"},{"id":"003"}]
    return render(request, "orders.html", {'orders': orders,"customer_name": customer_name})
    # return render(request, "search_customer_orders.html")