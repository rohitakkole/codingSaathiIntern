#!/usr/bin/env python
# coding: utf-8

# In[26]:


import cv2
import matplotlib.pyplot as plt
img=cv2.imread("C:/Users/ROHIT/Downloads/elon.jpg")
plt.imshow(img)
plt.axis(False)
plt.show()
plt.imshow(img[:,:,::-1])
plt.axis(False)
plt.show()
RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(RGB_img)
plt.axis(False)
plt.show()


# In[27]:


grey_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
invert_img=cv2.bitwise_not(grey_img)


# In[28]:


blur_img=cv2.GaussianBlur(invert_img, (111,111),0)


# In[29]:


invblur_img=cv2.bitwise_not(blur_img)


# In[30]:


sketch_img=cv2.divide(grey_img,invblur_img, scale=256.0)


# In[31]:


cv2.imwrite('sketch.png', sketch_img)


# In[32]:


cv2.imshow('sketch image',sketch_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[33]:


plt.figure(figsize=(14,8))
plt.subplot(1,2,1)
plt.title('Original image', size=18)
plt.imshow(RGB_img)
plt.axis('off')
plt.subplot(1,2,2)
plt.title('Sketch', size=18)
rgb_sketch=cv2.cvtColor(sketch_img, cv2.COLOR_BGR2RGB)
plt.imshow(rgb_sketch)
plt.axis('off')
plt.show()


# In[ ]:




