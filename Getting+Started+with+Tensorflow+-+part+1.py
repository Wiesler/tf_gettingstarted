
# coding: utf-8

# In[1]:

import tensorflow as tf


# In[3]:

node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0) # also tf.´float32

print(node1, node2)


# In[4]:

sess = tf.Session()
print(sess.run([node1, node2]))


# In[5]:

node3 = tf.add(node1, node2)
print("node3: ", node3)
print("sess.run(node3): ", sess.run(node3) )


# In[6]:

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = a + b # + provides a shortcut for tf.add(a,b)

print(sess.run(adder_node, {a: 3, b:4.5}))
print(sess.run(adder_node, {a: [1,3], b: [2, 4]}))


# In[7]:

add_and_triple = adder_node * 3.
print(sess.run(add_and_triple, {a: 3, b:4.5}))


# In[8]:

W = tf.Variable([.3], tf.float32)
b = tf.Variable([-.3], tf.float32)
x = tf.placeholder(tf.float32)
linear_model = W * x + b

init = tf.global_variables_initializer()
sess.run(init)

print(sess.run(linear_model, {x:[1,2,3,4]}))


# In[9]:

y = tf.placeholder(tf.float32)
squared_deltas = tf.square(linear_model - y)
loss = tf.reduce_sum(squared_deltas)
print(sess.run(loss, {x:[1,2,3,4], y:[0,-1,-2,-3]}))


# In[10]:

fixW = tf.assign(W, [-1.])
fixb = tf.assign(b, [1.])
sess.run([fixW, fixb])
print(sess.run(loss, {x:[1,2,3,4], y:[0,-1,-2,-3]}))


# In[ ]:



