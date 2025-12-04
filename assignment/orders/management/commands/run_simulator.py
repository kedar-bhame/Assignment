from django.core.management.base import BaseCommand
import threading, re, time
from users.models import User as UserModel
from products.models import Product as ProductModel
from orders.models import Order as OrderModel

EMAIL_RE = re.compile(r"[^@]+@[^@]+\.[^@]+")

USERS = [
    (1, "Alice", "alice@example.com"),
    (2, "Bob", "bob@example.com"),
    (3, "Charlie", "charlie@example.com"),
    (4, "David", "david@example.com"),
    (5, "Eve", "eve@example.com"),
    (6, "Frank", "frank@example.com"),
    (7, "Grace", "grace@example.com"),
    (8, "Alice", "alice@example.com"),
    (9, "Henry", "henry@example.com"),
    (10, "", "jane@example.com"),
]

PRODUCTS = [
    (1, "Laptop", 1000.0),
    (2, "Smartphone", 700.0),
    (3, "Headphones", 150.0),
    (4, "Monitor", 300.0),
    (5, "Keyboard", 50.0),
    (6, "Mouse", 30.0),
    (7, "Laptop", 1000.0),
    (8, "Smartwatch", 250.0),
    (9, "Gaming Chair", 500.0),
    (10, "Earbuds", -50.0),
]

ORDERS = [
    (1, 1, 1, 2),
    (2, 2, 2, 1),
    (3, 3, 3, 5),
    (4, 4, 4, 1),
    (5, 5, 5, 3),
    (6, 6, 6, 4),
    (7, 7, 7, 2),
    (8, 8, 8, 0),
    (9, 9, 1, -1),
    (10, 10, 11, 2),
]

print_lock = threading.Lock()


def do_insert(rec, model, validator, create_kwargs_fn, tag):
    name = threading.current_thread().name
    errs = validator(rec)
    if errs:
        with print_lock:
            print(f"[{tag}][{name}] {rec[0]} FAILED: {'; '.join(errs)}")
        return
    model.objects.create(**create_kwargs_fn(rec))
    with print_lock:
        print(f"[{tag}][{name}] {rec[0]} SUCCESS")


class Command(BaseCommand):
    help = "Compact concurrent insert simulator"

    def handle(self, *a, **k):
        # clear previous data
        UserModel.objects.all().delete()
        ProductModel.objects.all().delete()
        OrderModel.objects.all().delete()

        threads = []

        # validators and create-fns
        u_val = lambda r: (
            []
            if r[1].strip() and EMAIL_RE.match(r[2])
            else (["name empty"] if not r[1].strip() else ["email invalid"])
        )
        p_val = lambda r: (
            []
            if r[1].strip() and float(r[2]) >= 0
            else (["name empty"] if not r[1].strip() else ["price invalid"])
        )

        def o_val(r):
            errs = []
            if not isinstance(r[3], int) or r[3] <= 0:
                errs.append("quantity must be > 0")
            if not UserModel.objects.filter(legacy_id=r[1]).exists():
                errs.append(f"user {r[1]} missing")
            if not ProductModel.objects.filter(legacy_id=r[2]).exists():
                errs.append(f"product {r[2]} missing")
            return errs

        u_create = lambda r: {"legacy_id": r[0], "name": r[1], "email": r[2]}
        p_create = lambda r: {"legacy_id": r[0], "name": r[1], "price": float(r[2])}
        o_create = lambda r: {
            "legacy_id": r[0],
            "user_legacy_id": r[1],
            "product_legacy_id": r[2],
            "quantity": r[3],
        }

        for i, r in enumerate(USERS, 1):
            threads.append(
                threading.Thread(
                    target=do_insert,
                    args=(r, UserModel, u_val, u_create, "USER"),
                    name=f"U-{i}",
                )
            )
        for i, r in enumerate(PRODUCTS, 1):
            threads.append(
                threading.Thread(
                    target=do_insert,
                    args=(r, ProductModel, p_val, p_create, "PRODUCT"),
                    name=f"P-{i}",
                )
            )
        for i, r in enumerate(ORDERS, 1):
            threads.append(
                threading.Thread(
                    target=do_insert,
                    args=(r, OrderModel, o_val, o_create, "ORDER"),
                    name=f"O-{i}",
                )
            )

        for t in threads:
            t.start()
            time.sleep(0.01)
        for t in threads:
            t.join()

        self.stdout.write(self.style.SUCCESS("=== SUMMARY ==="))
        self.stdout.write(f"Users: {UserModel.objects.count()}")
        self.stdout.write(f"Products: {ProductModel.objects.count()}")
        self.stdout.write(f"Orders: {OrderModel.objects.count()}")
        self.stdout.write(self.style.SUCCESS("Done."))