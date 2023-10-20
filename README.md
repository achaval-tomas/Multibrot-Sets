# Multibrot Sets
Generate different multibrot sets and explore the fractal world by choosing their exponent and precision.

Multibrot sets are a generalization of the famous Mandelbrot Set. These sets generate beautiful fractal patterns.

The sets we explore are, given **z_0 = 0 + 0i**, a **starting point c** = a + bi,
and an **exponent d**:

**z_(n+1) = (z_n)^d + c , for n >= 0**

The points that stay bounded after a given amount of iterations (precision) will be included in the set.

A point is defined to be bounded and will not diverge to infinity if **|z_n| <= 2 for any n >= 0**.

You can choose the exponent, precision and animation speed at the start of the multibrot.py file.

Run with ```` python3 multibrot.py ```` <br />
Get pygame ```` sudo apt-get install python3-pygame ````

Some examples:
(exponents = 2, 4, 8 and 16 respectively)
![mandel-demo](https://github.com/achaval-tomas/Multibrot-Sets/assets/134091945/e4f72c16-2712-4b6b-9606-460a05667c09)
