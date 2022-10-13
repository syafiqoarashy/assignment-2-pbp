# ASSIGNMENT 5

## Difference Between Inline, Internal, and External CSS

#### Each Definitions

##### Inline CSS

When you want to style a specific HTML element, you can use Inline CSS. This one directly puts the style attribute directly onto the HTML tag that you want to stylized. Therefore, they relate only to a specific HTML tag.

Example:
```<h1 style="color:blue;12px;">This is Inline!</h1>```


##### Internal CSS

Internal CSS requires you to add the styles onto the header of the HTML file. In there, specific rules of styles are applied to the HTML tags that are written inside it.

Example:
```<!DOCTYPE html>
<html>
<head>
<style>
body {
    background-color: red;
}
p {
    color: white;
    padding: 30px;
} 
</style>
</head>```

##### External CSS

Unlike the two others, external CSS uses a separate .css file. The .css file is then link back onto the HTML file in the document head.

Example:
```
.leftcol {
   width: 34%;
   background:#ffffff;
}```

| Type | Advantages | Disadvantages |
| --- | --- | --- |
| Inline CSS | Easily and quickly insert CSS rules to HTML, performance is quicker| Difficult to keep up and reuse, makes the HTML file unorganized |
| Internal CSS | One style of same element so there's no need to repeat | Unable to use the defined style on another HTML page, may increase the page’s size and loading time. |
| External CSS | Full control of page structure, you can reuse the .css file for multiple pages, HTML file would be much structured and cleaner | May not be rendered correctly up until the external css is loaded, may increase website's download time. |

## HTML5 Tags

```
<body>    : Tag that describes the documents body.
<head>    : Tag that contains information about the document, belongs to the head portion.
<h1>      : The largest heading, usually used as the web's title. 
<p>       : Tag that is used to create a paragraph.
<a>       : Tag that is used as a hyperlink.
<button>  : Tag that creates a button.
<input>   : Tag to define input control.
<script>  : Tag that specifies a script.
<title>   : Tag that specifies the document title.
```

## CSS Tags
  
Universal Selector  : It eithers selects all elements or select specific namespaces.
Type Selector       : It selects all elements that has the given node name.
Class Selector      : It selects all elements that has the given class attribute.
ID Selector         : It selects an element based on the given id attribute.
Attribute Selector  : It selects all elements that has the given attribute.

## Implementation

#### Customize the Template Using a CSS Framework

Because of my familiarity of Tailwind CSS, in this specific assignment I used Tailwind CSS as my framework. The steps to install Tailwind CSS into the Django project was abit difficult.

The documentation I used to install the framework was gathered from here:
https://django-tailwind.readthedocs.io/en/latest/installation.html

Afterwards, I look a bunch of references online (i.e. Dribbble, Pinterest, and Youtube) to easily know better which colors and layout we'll be implementing on our web design.

Continuing on, I browse around the Tailwind CSS documentation to stylize my pages as attractive as possible. Some of the examples are,
1. How to use flex (flex-direction, flex-wrap, and so on)
2. Margins and Paddings
3. Text and Item Alignments
4. etc

Then, we were to asked to create cards for each tasks. For each card I created a <div> tag.  I added a hover animation so that you'll be able to delete and change the status of the task. I used last weeks assignment as my reference for the data in the card to make it as similar as possible to last weeks assignment. Lastly, to make the whole pages responsive, I mostly use the breakpoint name provided by Tailwind CSS (sm, md, and so on)
