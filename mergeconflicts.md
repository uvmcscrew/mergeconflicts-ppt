---
title: Merge Conflicts Are Not That Bad
sub_title: and you shouldn't be afraid of them
author: Henrik Van Tassell
---

# What is a Merge Conflict?

A merge conflict is what occurs when two branches have changes that cannot be merged automatically.

<!-- pause -->

## Ok but what does that mean?

<!-- end_slide -->

<!-- column_layout: [2, 2] -->

<!-- column: 0 -->
# A basic example

Say we have some code in a repository:

```python
def hello():
    print("Hello, cscrew!")
```

Then both Violet and I clone that repository so we can work on it.  

<!-- pause -->

<!-- column: 1 -->

## I make a change:

```python
def hello():
    print("Hello, henrik!")
```

Then I commit and push my changes.

<!-- pause -->

## And Violet commits a change:

```python
def hello():
    print("Hello, violet!")
```

<!-- end_slide -->

# A basic example


<!-- column_layout: [2, 2] -->

<!-- column: 0 -->



## I make a change:

```python
def hello():
    print("Hello, henrik!")
```

Then I commit and push my changes.



## And Violet commits a change:

```python
def hello():
    print("Hello, violet!")
```

<!-- pause -->


<!-- column: 1 -->



## Enter: merging

Violet may try to push her changes but then she will run into an error: 

```
error: failed to push some refs!
```

**Oh no, a merge conflict!**





<!-- end_slide -->







<!-- column_layout: [1, 1] -->

<!-- column: 0 -->
# Oh no, a merge conflict!

`origin/main` now has Henrik's commit `a7f3c9e` but not hers.


Violet runs `git pull origin main`: 

```
$ git pull origin main
From github.com:cscrew/demo
 * branch  main -> origin/main (a7f3c9e)
Auto-merging hello.py
CONFLICT (content): Merge conflict in hello.py
Automatic merge failed; fix conflicts
```


<!-- pause -->

<!-- column: 1 -->

And then the code looks like this all of a sudden:

```python
def hello():
<<<<<<< HEAD
    print("Hello, violet!")
=======
    print("Hello, henrik!")
>>>>>>> a7f3c9e (origin/main)
```

<!-- end_slide -->

Why is this scary?
==================

Newer users of git are...
<!-- pause -->
- More likely to hit merge conflicts due to less than optimal use of git
<!-- pause -->
- Less likely to understand what's going on
<!-- pause -->
- Are not familiar with what to do with merge conflict syntax

<!-- pause -->

I've encountered many smart people here who are still afraid of merge conflicts. 

<!-- end_slide -->

<!-- jump_to_middle -->

How to avoid merge conflicts in the first place
==================

<!-- end_slide -->

<!-- column_layout: [1, 1] -->

<!-- column: 0 -->
# Commit often & commit small!

A commit = information about your changes. It helps git understand what changed, and when, relative to other changes. 

The more frequent your commits are, and the more detailed they are (tiny changes as opposed to massive blocks of code), the better. 

<!-- pause -->

<!-- column: 1 -->

# Stay updated

If you are working on a branch with someone, pull and push often. This means you keep other people updated with your changes and you can stay updated with theirs.
<!-- pause -->

<!-- reset_layout -->

## The more information the Git merging algorithm has, the easier it can merge your changes.

<!-- end_slide -->

<!-- jump_to_middle -->

Ok but I have a merge conflict anyway...
==================


<!-- end_slide -->

Making merge conflicts more manageable: separate branches & pull requests
==================

<!-- pause -->

Make your own branch and work on it by yourself!

This reduces hitting merge conflicts when you pull/push commits

<!-- pause -->

And when you have a merge conflict with your default branch (typically `main` or `master`), it can be handled at any time
