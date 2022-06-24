import string

class product_info:
    def __init__ (self, title = "N/A", price = 0.0, reviewTotal = 0.0 , reviewStars = "N/A", sponsoredTag = "N?A", link = "", productId = "N/A"):
        self.title = title
        self.price = price
        self.reviewTotal = reviewTotal
        self.reviewStars = reviewStars
        self.sponsoredTag = sponsoredTag
        self.link = link
        self.productId = productId

    def getTitle(self):
        return self.title
    def getPrice(self):
        return self.price
    def getReviewTotal(self):
        return self.reviewTotal
    def getReviewStars(self):
        return self.reviewStars
    def getSponsoredTag(self):
        return self.sponsoredTag
    def getLink(self):
        return self.link
    def getproductID(self):
        return self.productID

    def print_product(self):
        str = '''{:50}\n
                 Price:$ {} \n
                 Total Num of Reviwers: {} \n
                 Review Stars: {} \n
                 Sponsered?: {} \n
                 {}
              '''.format(self.title, self.price, self.reviewTotal, self.reviewStars, self.sponsoredTag, self.link)
        print(str)
