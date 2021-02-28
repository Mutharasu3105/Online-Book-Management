
import mysql.connector;

connection = mysql.connector.connect(host='localhost',database='miniproject',user='root',password='muthuroot')

cur=connection.cursor(dictionary=True);

   
def purchase_list(list):
    l= list
    global product
    global c_name
    global p_amount
    c_name=input("Please enter your name:")
    print("Hello "+c_name+",Wellcome to our shop")
    q={}
    
    cur.execute("select ISBN,title,Author,publisher from bookinfo")
    books = cur.fetchall()
    
    b_title=[]
    for i in books:
        title =i["title"]
       # print("ISBN =",i["ISBN"])
        #print("Author=",i["Author"])
        #print("publisher =",i["publisher"])
        
        b_title.append(title)
       
    #b_isbn=[]
    #b_price=[]
    #b_quantity=[]
    #cur.execute("select ISBN,price,quantity from inventory")
    #market = cur.fetchall()
    #for i in market:
        #isbn =i["ISBN"]
        #price =i["price"]
        #quantity=i["quantity"]
        #b_isbn.append(isbn)
        #b_price.append(price)
        #b_quantity.append(quantity)
        
    
  
    product=input("Hi "+c_name+"\n Choose your mind partner:")
 
    #flag="Y"
    #if flag.upper=='Y':
    if product in b_title:
        print("Your book is available")
        if True:
            p_quantity=int(input("Hello "+c_name+",How many copies you want to buy ? :"))
            if True :
                    
                #print ISBN number for user given title
                var1 = cur.execute("select ISBN from bookinfo where title = '%s'"%(product))
                bookISBN = cur.fetchmany(var1)
                bookISBN_value = bookISBN[0]
                c_bookISBN = bookISBN_value['ISBN']
                print("Your Book ISBN number is : ",c_bookISBN)
                #print quantity for given title
                var3 = cur.execute("select quantity from bookinfo where title= '%s'"%(product)) 
                bookQuantity = cur.fetchmany(var3)
                bookQuantity_value = bookQuantity[0]
                c_bookquantity = bookQuantity_value['quantity']
                print("Book quantity is:",c_bookquantity)

                if c_bookquantity < p_quantity :#check no of copies in the store
                    print("Sorry "+c_name+",we have only ",c_bookquantity," no.of copies")
                    
                else:pass
                
                #print price for given title(book)
                var2 = cur.execute("select price from bookinfo where title= '%s'"%(product))
                bookPrice = cur.fetchmany(var2)
                bookPrice_value = bookPrice[0]
                c_bookprice= bookPrice_value['price']
                print("Book price is :",c_bookprice)
               
                
        #else:
         #    print("Sorry"+c_name+"Enter the integer values..like 1,2,3..")
    else:
            print("Sorry "+c_name+",This product not available from this store: ")
            print("Choose following Books please:")
            print("------------------------------")#30
            print("title\t\tAuthor\t\tpublisher\t\tquantity")
            print("------------------------------")#30
         
    #wer=(input(c_name+",You want to purchase another copies(Y/N)? :"))
    #if wer =="y":
     #   return flag
    #elif wer =="n":
     #   pass

    #if wer == "n":pass
    c_purchase=(product,c_bookISBN,c_bookquantity,c_bookprice)
    print("You purchase :","Book Title :",product,"ISBN number :",c_bookISBN,"Quantity :",c_bookquantity,"Price :",c_bookprice,"!")
    print(c_purchase)

    for k in c_purchase:
            gst_tax=25
            p_amount=c_bookprice*p_quantity
            p_total =p_amount*gst_tax
    print("Total amount of your purchase is :",p_amount)
    print("Tax is:",gst_tax)
    print("You choose these books :","Book Title:", product,"|","ISBN no:", c_bookISBN,"|","Quantity:", c_bookquantity,"|","price of your book with tax:", p_total,"\t")
    return q

def write_file():

    cus_id = input("Enter your customer id: >")
    cus_name = c_name
    contact_no = input("Enter your contactno: >")
    mail_id = input("Enter your supplieremailid: >")
    gender = input("Enter your gender: >")
    feedback = input("Enter your feedback : >")
    #purchased_books=input("Entered purchasedbooks: >")
    purchased_books = product
    cus_price = p_amount
    
    # cur.execute("drop table if exists bookcustomer"):
     #   pass
    #else:
      #  print("Table dropped...")
    # bookcustomer succefully created
    #sql = """create table miniproject.bookcustomer (
     #       cus_id int primary key ,
      #      cus_name varchar(30),
       #     contact_no bigint,
        #    mail_id varchar(30),
         #  feedback varchar(80));"""
    
    #cur.execute(sql)
    #alter table add new column
    #cur.execute("alter table bookcustomer add cus_price int(12) after purchased_books")
    
    cur.execute("""insert into bookcustomer (cus_id,cus_name,contact_no,mail_id,gender,feedback,purchased_books,cus_price) values(%s,'%s',%s,'%s','%s','%s','%s',%s)""" %(cus_id,cus_name,contact_no,mail_id,gender,feedback,purchased_books,cus_price))    
    
    connection.commit()
    connection.close()

    return
    
#again ="Y"
#while again.upper()=="Y":
#a=read_file()
b=purchase_list(list)
c=write_file()    

print("Thank You")
print("Please Check your purchase details")
    
