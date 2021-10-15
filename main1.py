from flask import Flask,render_template,request,redirect,session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://root:@localhost/shop"
app.secret_key = 'the random string'
db=SQLAlchemy(app)



class Products(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    slug = db.Column(db.String(120),  nullable=False)
    image = db.Column(db.String(120),  nullable=False)
    price = db.Column(db.String(120),  nullable=False)
    seller = db.Column(db.String(120),  nullable=False)
    category = db.Column(db.String(120),  nullable=False)
    active = db.Column(db.String(120),  nullable=False) 
    date = db.Column(db.String(120),  nullable=True)
    description = db.Column(db.String(120),  nullable=False)

class Category(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    categoryName = db.Column(db.String(80), nullable=False)
    seller = db.Column(db.String(120),  nullable=False)
    categoryNumber = db.Column(db.String(120),  nullable=False)
    active = db.Column(db.String(120),  nullable=False)


class User(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120),  nullable=False)
    mobile = db.Column(db.String(120),  nullable=False)
    image = db.Column(db.String(120),  nullable=False)
    password = db.Column(db.String(120),  nullable=False)
    
class Orders(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    full_address = db.Column(db.String(80), nullable=False)
    payment_method = db.Column(db.String(120),  nullable=False)
    product_id = db.Column(db.String(120),  nullable=True)
    product_name = db.Column(db.String(120),  nullable=True)
    product_seller = db.Column(db.String(120),  nullable=True)
    product_price = db.Column(db.String(120),  nullable=True)
    total_order = db.Column(db.String(120),  nullable=True)
    user_name = db.Column(db.String(120),  nullable=True)
    user_email = db.Column(db.String(120),  nullable=True)
    user_mobile = db.Column(db.String(120),  nullable=True)
    active = db.Column(db.String(120),  nullable=True)


class Seller(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(120),  nullable=False)
    phone = db.Column(db.String(120),  nullable=False)
    email = db.Column(db.String(120),  nullable=False)
    image = db.Column(db.String(120),  nullable=False)





"""-----------------dashboard--------------"""

@app.route("/product_table")
def product_table():
    posts=Products.query.filter_by().all()
    return render_template("product_table.html",posts=posts)



@app.route("/product_edit/<string:sno>",methods=["GET","POST"])
def product_edit(sno):
    if request.method=="POST":
        box_name=request.form.get("pro_name")
        box_slug=request.form.get("pro_slug")
        box_image=request.form.get("pro_image")
        box_price=request.form.get("pro_price")
        box_seller=request.form.get("pro_seller")
        box_category=request.form.get("pro_category")
        box_description=request.form.get("pro_description")
        if sno =="0":
            entry=Products(name=box_name,slug=box_slug,category=box_category,image=box_image,price=box_price,seller=box_seller,description=box_description,date=datetime.now(),active="1")
            db.session.add(entry)
            db.session.commit()
            return redirect("/product_table")
        else:
            posts=Products.query.filter_by(sno=sno).first()
            posts.name=box_name
            posts.slug=box_slug
            posts.image=box_image
            posts.price=box_price
            posts.seller=box_seller
            posts.description=box_description
            posts.category=box_category
            db.session.commit()
            return redirect("/product_table")
    posts=Products.query.filter_by(sno=sno).first()
    return render_template("product_edit.html",posts=posts,sno=sno)
    




@app.route("/product_delete/<string:sno>",methods=["GET","POST"])
def product_delete(sno):
    posts=Products.query.filter_by(sno=sno).first()
    db.session.delete(posts)
    db.session.commit()
    return redirect("/product_table")







"""-----------------Seller--------------"""

@app.route("/seller_table")
def seller_table():
    posts=Seller.query.filter_by().all()
    return render_template("seller_table.html",posts=posts)



@app.route("/seller_edit/<string:id>",methods=["GET","POST"])
def seller_edit(id):
    if request.method=="POST":
        box_name=request.form.get("pro_name")
        box_username=request.form.get("pro_username")
        box_password=request.form.get("pro_password")
        box_phone=request.form.get("pro_phone")
        box_email=request.form.get("pro_email")
        box_image=request.form.get("pro_image")
        if id =="0":
            entry=Seller(name=box_name,username=box_username,password=box_password,phone=box_phone,email=box_email,image=box_image)
            db.session.add(entry)
            db.session.commit()
            return redirect("/seller_table")
        else:
            posts=Seller.query.filter_by(id=id).first()
            posts.name=box_name
            posts.username=box_username
            posts.image=box_image
            posts.password=box_password
            posts.phone=box_phone
            posts.email=box_email
            db.session.commit()
            return redirect("/seller_table")
    posts=Seller.query.filter_by(id=id).first()
    return render_template("seller_edit.html",posts=posts,id=id)
    




@app.route("/seller_delete/<string:id>",methods=["GET","POST"])
def Seller_delete(id):
    posts=Seller.query.filter_by(id=id).first()
    db.session.delete(posts)
    db.session.commit()
    return redirect("/seller_table")









@app.route("/user_table")
def user_table():
    users=User.query.filter_by().all()
    return render_template("user_table.html",users=users)



    




@app.route("/user_delete/<string:sno>",methods=["GET","POST"])
def user_delete(sno):
    users=User.query.filter_by(sno=sno).first()
    db.session.delete(users)
    db.session.commit()
    return redirect("/user_table")





@app.route("/order_table")
def order_table():
    orders=Orders.query.filter_by().all()
    return render_template("order_table.html",orders=orders)



@app.route("/order_edit/<string:sno>",methods=["GET","POST"])
def order_edit(sno):
    if request.method=="POST":
        product_id=request.form.get("form_product_id")
        product_name=request.form.get("form_product_name")
        product_seller=request.form.get("form_product_seller")
        full_address=request.form.get("form_full_address")
        payment_method=request.form.get("form_payment_method")
        user_name=request.form.get("form_user_name")
        user_mobile=request.form.get("form_user_mobile")
        user_email=request.form.get("form_user_email")

        if sno =="0":
            entry=Orders(product_id=product_id,product_name=product_name,product_seller=product_seller,full_address=full_address,payment_method=payment_method,user_name=user_name,user_mobile=user_mobile,user_email=user_email)
            db.session.add(entry)
            db.session.commit()
            return redirect("/user_table")
        else:
            orders=Orders.query.filter_by(sno=sno).first()
            orders.product_id=product_id
            orders.product_name=product_name
            orders.product_seller =product_seller
            orders.full_address =full_address
            orders.payment_method =payment_method
            orders.user_name =user_name
            orders.user_mobile =user_mobile
            orders.user_email=user_email
            db.session.commit()
            return redirect("/order_table")
    orders=Orders.query.filter_by(sno=sno).first()
    return render_template("order_edit.html",orders=orders,sno=sno)
    




@app.route("/order_delete/<string:sno>",methods=["GET","POST"])
def order_delete(sno):
    orders=Orders.query.filter_by(sno=sno).first()
    db.session.delete(orders)
    db.session.commit()
    return redirect("/order_table")





"""-------------seller------------"""

"""@app.route("/artsy")
def artsy():
    product=Products.query.filter_by().all()
    return render_template("artsy.html",product=product)

@app.route("/cakes")
def cakes():
    product=Products.query.filter_by().all()
    return render_template("cakes.html",product=product)

@app.route("/crafts")
def crafts():
    product=Products.query.filter_by().all()
    return render_template("crafts.html",product=product)"""


"""@app.route("/home/<string:seller>",methods=["POST","GET"])
def seller():
    products=Products.query.filter_by(seller=seller).all()
    return render_template("seller.html",products=products)"""



@app.route("/order_page/<string:product_id>",methods=["GET","POST"])
def order_page(product_id):
    order=Products.query.filter_by(sno=product_id).first()
    order.sno=product_id
    dt=session["user"]
    data=User.query.filter_by(email=dt).first()

    if request.method=="POST":
        box_full_address=request.form.get("user_full_address")
        box_product_price=request.form.get("user_product_price")
        box_total_order=request.form.get("user_total_order")
        box_payment_method=request.form.get("user_payment_method")
        entry=Orders(full_address=box_full_address,payment_method=box_payment_method,product_id=product_id,product_name=order.name,user_email=data.email,user_name=data.last_name,user_mobile=data.mobile,product_seller=order.seller,active="0",product_price=box_product_price,total_order=box_total_order)
        db.session.add(entry)
        db.session.commit()
        return redirect("/orderConfirm")

    return render_template("order.html",order=order)

@app.route("/orderConfirm")
def orderConfirm():
    return render_template("orderConfirm.html")


"""Autincation"""


@app.route("/admin_login", methods=['GET','POST'])
def admin_login():
    if request.method=="POST":
        box_name=request.form.get("name")
        box_password=request.form.get("password")
        if box_name=="esha123" and box_password=="12345":
            return redirect("/product_table")

    return render_template("admin_login.html")



@app.route("/signup", methods=["GET","POST"])
def signup():
    if request.method=="POST":
        box_first_name=request.form.get("first_name")
        box_last_name=request.form.get("last_name")
        box_email=request.form.get("email")
        box_mobile=request.form.get("mobile")
        box_password=request.form.get("password")
        
        entry=User(first_name=box_first_name,last_name=box_last_name,email=box_email,mobile=box_mobile,password=box_password)
        db.session.add(entry)
        db.session.commit()
        return redirect("/user_signin")
    return render_template("signup.html")



@app.route("/user_signin",methods=["GET","POST"])
def signin():
    if request.method=="POST":
        box_email=request.form.get("user_email")
        box_password=request.form.get("user_password")
        
        try:
            data=User.query.filter_by(email=box_email,password=box_password).first()
            if data is not None:
                session["user"]=data.email
                if "seller" in session:
                    session.pop("seller")
                return redirect("/home")
            else:
                return redirect("/wrong_signin_password")
        except:
            return "<h1>database error</h1>"
    return render_template("user_signin.html")



@app.route("/sellerLogin",methods=["GET","POST"])
def sellerLogin():
    if request.method=="POST":
        box_username=request.form.get("username")
        box_password=request.form.get("password")
         
        try:
            data=Seller.query.filter_by(username=box_username,password=box_password).first()
            if data is not None:
                session["seller"]=data.username
                if "user" in session:
                    session.pop("user")
                return redirect("/home")
            else:
                return redirect("/wrong_signin_password")
        except:
            return "<h1>database error</h1>"
    return render_template("sellerLogin.html")

@app.route("/wrong_signin_password")
def wrong_signin_password():
    return render_template("wrong_signin_password.html")


@app.route("/profile")
def profile():
    if "user" in session:
        posts=User.query.filter_by(email=session["user"]).first()
        return render_template("profile.html",posts=posts)

    if "seller" in session:
        posts=Seller.query.filter_by(username=session["seller"]).first()
        return render_template("profile.html",posts=posts)

    else:
        return redirect("/user_signin")



        
@app.route("/logout")
def logout():
    session.pop("user")
    return redirect("/home")

@app.route("/sellerLogout")
def sellerLogout():
    session.pop("seller")
    return redirect("/home")


@app.route("/home")
def home():
    sellers=Seller.query.filter_by().all()
    return render_template("home.html",sellers=sellers)



@app.route("/seller/<string:username>",methods=["GET","POST"])
def seller(username):
    sellers=Seller.query.filter_by(username=username).first()
    categorys=Category.query.filter_by().all()
    products=Products.query.filter_by(seller=username).all()
    return render_template("seller.html",sellers=sellers,products=products,categorys=categorys)


@app.route("/category/<string:categoryName>/<string:username>",methods=["GET","POST"])
def category(categoryName,username):
    categorys=Category.query.filter_by(categoryName=categoryName).first()
    sellers=Seller.query.filter_by(username=username).first()
    categorys2=Category.query.filter_by().all()
    products=Products.query.filter_by(category=categorys.categoryName,seller=sellers.username).all()
    return render_template("category.html",products=products,categorys=categorys,sellers=sellers,categorys2=categorys2)




@app.route("/product/<string:post_slug>", methods=['GET'])
def product(post_slug):
    product=Products.query.filter_by(slug=post_slug).first()
    if "user" in session:
        return render_template("product.html",product=product)
    else:
        return redirect("/user_signin")


@app.route("/about")
def about():
    return render_template("about.html")



@app.route("/contact",methods=["GET","POST"])
def contact():
    if request.methods=="POST":
        name=request.method.get("name")
        email=request.method.get("email")
        phone=request.method.get("phone")
        message=request.method.get("message")

        msg = Message(message,sender=email,recipients=[" "])
        mail.send(msg)

    return render_template("contact.html")



"""sellerProfile"""

@app.route("/sellerAddProduct",methods=["POST","GET"])
def sellerAddProduct():
    if request.method=="POST":
        box_name=request.form.get("pro_name")
        box_slug=request.form.get("pro_slug")
        box_image=request.form.get("pro_image")
        box_price=request.form.get("pro_price")
        box_seller=request.form.get("pro_seller")
        box_category=request.form.get("pro_category")
        box_description=request.form.get("pro_description")
        entry=Products(name=box_name,slug=box_slug,category=box_category,image=box_image,price=box_price,seller=box_seller,description=box_description,date=datetime.now(),active="0")
        db.session.add(entry)
        db.session.commit()
        return redirect("/profile")
    return render_template("sellerAddProduct.html")

@app.route("/sellerAddCategory",methods=["POST","GET"])
def sellerAddCategory():
    if request.method=="POST":
        box_categoryName=request.form.get("pro_categoryName")
        box_categoryNumber=request.form.get("pro_categoryNumber")
        dt=session["seller"]
        entry=Category(categoryName=box_categoryName,categoryNumber=box_categoryNumber,active="0",seller=dt)
        db.session.add(entry)
        db.session.commit()
        return redirect("/profile")
    return render_template("sellerAddCategory.html")

@app.route("/approval_table")
def approval_table():
    posts=Products.query.filter_by().all()
    return render_template("approval_table.html",posts=posts)



@app.route("/add_product/<string:sno>", methods=["GET","POST"])
def add_product(sno):
    products=Products.query.filter_by(sno=sno).first()
    products.active="1"
    db.session.commit()
    return redirect("/approval_table")



@app.route("/category_approval")
def category_approval():
    posts=Category.query.filter_by().all()
    return render_template("category_approval.html",posts=posts)


@app.route("/add_category/<string:sno>", methods=["GET","POST"])
def add_category(sno):
    products=Category.query.filter_by(sno=sno).first()
    products.active="1"
    db.session.commit()
    return redirect("/category_approval")


@app.route("/category_delete/<string:sno>",methods=["GET","POST"])
def category_delete(sno):
    posts=Category.query.filter_by(sno=sno).first()
    db.session.delete(posts)
    db.session.commit()
    return redirect("/category_approval")


@app.route("/userOrderHistory",methods=["GET","POST"])
def userOrderHistory():
    data=session["user"]
    orders=Orders.query.filter_by(user_email=data).all()
    return render_template("userOrderHistory.html",orders=orders)


@app.route("/sellerOrder",methods=["GET","POST"])
def sellerOrder():
    data=session["seller"]
    print(data)
    orders=Orders.query.filter_by(product_seller=data).all()
    return render_template("sellerOrder.html",orders=orders)


@app.route("/sellerConfirmOrder/<string:sno>", methods=["GET","POST"])
def sellerConfirmOrder(sno):
    orders=Orders.query.filter_by(sno=sno).first()
    orders.active="1"
    db.session.commit()
    return redirect("/sellerOrder")

@app.route("/editProfile",methods=["GET","POST"])
def editProfile():
    if "user" in session:
        posts=User.query.filter_by(email=session["user"]).first()
        return render_template("editProfile.html",posts=posts)


@app.route("/changePassword",methods=["GET","POST"])
def changePassword():
    if "user" in session:
        users=User.query.filter_by(email=session["user"]).first()
        if request.method=="POST":
            box_old_password=request.form.get("old_password")
            box_new_password=request.form.get("new_password")
            box_confirm_password=request.form.get("confirm_password")
            if users.password==box_old_password:
                print(box_new_password)
                print(box_confirm_password)
                if box_new_password==box_confirm_password:
                    users.password=box_new_password
                    db.session.commit()
                    return redirect("/editProfile")
                else:
                    return "new password and confirm password doesn't match"
            else:
                return "old password not correct"
    return render_template("changePassword.html",users=users)

@app.route("/changeImage",methods=["GET","POST"])
def changeImage():
    if "user" in session:
        users=User.query.filter_by(email=session["user"]).first()
        if request.method=="POST":
            new_image=request.form.get("image")
            users.image=new_image
            db.session.commit()
            return redirect("/editProfile")
        return render_template("changeImage.html",users=users)

@app.route("/changeName",methods=["GET","POST"])
def changeName():
    if "user" in session:
        users=User.query.filter_by(email=session["user"]).first()
        if request.method=="POST":
            new_first_name=request.form.get("first_name")
            new_last_name=request.form.get("last_name")
            users.first_name=new_first_name
            users.last_name=new_last_name
            db.session.commit()
            return redirect("/editProfile")
        return render_template("changeName.html",users=users)

      


app.run(debug=True)


