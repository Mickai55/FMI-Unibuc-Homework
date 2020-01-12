functie.smechera <- function()
{
  pi^5
}
functie.smechera()

f1 <- function(x)
{
  sin(x)
}
f1(pi)

all.equal(0, 1.224606e-16)
all.equal(0, 0.00001, tolerance = 1.0e-5)

w <- integrate(f1, 0, pi / 2)
valoare <- w[[1]]

integrate(f1, 0, 30)

t <- seq(0, 100, 0.01)
plot(t, f1(t), col = "red")

f2 <- function(x)
{
  exp(x)
}

integrate(f2, 0, Inf)

f3 <- function(x)
{
  x^2
}

integrate(f3, 0, Inf)

f4 <- function(x)
{
  1/(x+1)
}

integrate(f4, 0, Inf)











