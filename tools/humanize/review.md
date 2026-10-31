# Humanization review

Each unit: original (AI-written draft) vs humanized (StealthGPT) vs final.


## Unit 0 — chapters/agency.tex

**Original**

The previous chapter built agents out of markets and found, almost in passing, that market prices behave like gradients. It left two things unexplained. The correspondence with neural networks went through an equilibrium oracle and an artificial construction, so it was not clear that it reflected anything deep. And nothing in the construction said why markets, rather than some other way of dividing up credit, should be the right model of a rational agent built from parts.

**Humanized**

The previous chapter built agents out of markets and noticed, almost in passing, that the prices in such markets act like gradients. Two things bugged me about that story. The connection to neural networks went through an equilibrium oracle and a contrived example, so I didn't know how much of it was real. And nothing in the story said that markets are the right way to carve up credit, as opposed to some other method.

**Final (meaning-corrected)**

The previous chapter built agents out of markets and noticed, almost in passing, that the prices in such markets act like gradients. Two things about that story were left open. The connection to neural networks went through an equilibrium oracle and a contrived construction, so it was unclear how much of it was real. And nothing in the story said that markets are the right way for a rational agent built from parts to carve up credit, as opposed to some other method.

*Note:* Pangram flagged the meaning-corrected text; redone as a narrow fix of the StealthGPT output (register and the dropped "rational agent built from parts" only).


## Unit 1 — chapters/agency.tex

**Original**

This chapter changes the question. Instead of asking how to build an agent out of a market, it asks what a market computes. The first section starts from probabilities rather than prices. It shows that the natural way to optimize a probability distribution, mirror ascent, is the same thing as continuous-time Bayesian updating, so that a reward signal acts on a learner exactly as a stream of evidence would, evidence that makes itself true. The following sections then define a production economy on a directed graph and derive the equations for its prices. These \emph{price recursion} equations turn out to be backpropagation when the economy is a chain of factories, the Bellman equation when it merely passes goods along, and Bayesian inference when routing shares are updated by mirror ascent. The conclusion is that an agent's reward is not an arbitrary input but the price that the surrounding economy sets on what it does. Price recursion is to reward what Bayes' rule is to evidence. The chapter ends with the \texttt{marketgrad} library, which implements these markets and checks the identities numerically. The two sections are adapted from informal articles and keep much of their first-person style.

**Humanized**

This chapter is about markets. The first section starts from probabilities instead of prices. It turns out that the natural way to optimize probabilities, mirror ascent, is continuous-time Bayesian updating: a reward signal is to a Bayesian learner what (self-fulfilling) evidence is to a Bayesian. The following sections define a production economy on a directed graph and derive its prices. These \emph{price recursion} equations reduce to backpropagation for factories in series, to the Bellman equation for goods that are passed on rather than consumed, and to Bayesian updating when routing shares are optimized via mirror ascent. An agent's reward turns out to be the price that the economy puts on the agent's actions. Price recursion is to reward what Bayes' rule is to evidence. The \texttt{marketgrad} library implements markets and numerically checks some of the identities from this chapter. The first two sections are adapted from informal articles, and so retain some first-person elements.

**Final (meaning-corrected)**

This chapter changes the question: instead of asking how to build an agent out of a market, it asks what a market computes. The first section starts from probabilities instead of prices. It turns out that the natural way to optimize probabilities, mirror ascent, is continuous-time Bayesian updating, so that a reward signal acts on a learner exactly as a stream of (self-fulfilling) evidence would. The following sections define a production economy on a directed graph and derive the equations for its prices. These \emph{price recursion} equations reduce to backpropagation for factories in series, to the Bellman equation for an economy that merely passes goods along, and to Bayesian inference when routing shares are updated by mirror ascent. An agent's reward, then, is not an arbitrary input but the price that the surrounding economy puts on the agent's actions. Price recursion is to reward what Bayes' rule is to evidence. The chapter ends with the \texttt{marketgrad} library, which implements these markets and numerically checks the identities. The two sections are adapted from informal articles, and so retain much of their first-person style.

*Note:* Restored the dropped framing (what a market computes), fixed the garbled reward/evidence analogy, restored "not an arbitrary input", and removed weakening ("some of the identities", "some first-person elements", "first two").


## Unit 2 — chapters/agency.tex

**Original**

The source article invokes an ``alignment lemma'' from the research notes
accompanying the \texttt{marketgrad} library; we reproduce it here. Give each node $i$ the
objective (``utility-inclusive profit at posted prices $p$''):

**Humanized**

The alignment lemma ``invoked in the article comes from'' these research notes.
accompanying the \texttt{marketgrad} library; we reproduce it here. Give each node $i$ the
objective (``utility-inclusive profit at posted prices $p$''):

**Final (meaning-corrected)**

The ``alignment lemma'' invoked in the source article comes from the research notes
accompanying the \texttt{marketgrad} library; we reproduce it here. Give each node $i$ the
objective (``utility-inclusive profit at posted prices $p$''):

*Note:* Fixed garbled first sentence (misplaced quotes, stray period making a fragment).


## Unit 3 — chapters/agency.tex

**Original**

where $p_j$ are prices posted by $i$'s buyers and $\pi_i$ is the price vector $i$
posts for its inputs; let node $i$'s own controls be its output shares $s_{i\cdot}$ and any
internal technology parameters $w_i$ of $f_i$.

**Humanized**

where $p_j$ are prices posted by $i$'s buyers and $\pi_i$ is the price vector $i$
posts for its inputs; and any controls of node $i$'s are output shares $s_{i\cdot}$
internal technology parameters $w_i$ of $f_i$.

**Final (meaning-corrected)**

where $p_j$ are prices posted by $i$'s buyers and $\pi_i$ is the price vector $i$
posts for its inputs; node $i$'s own controls are taken to be its output shares $s_{i\cdot}$ and any
internal technology parameters $w_i$ of $f_i$.

*Note:* Fixed ungrammatical clause and missing "and" so controls are the output shares and the technology parameters.


## Unit 4 — chapters/arbitrage.tex

**Original**

The last two chapters took two different routes around the same obstacle. \Cref{ch:nonvf} scored sentences that never resolve by making them the stakes of a game whose moves eventually do. \Cref{ch:consistency} gave up on resolution altogether and asked only whether a forecaster's beliefs fit together, measuring the misfit as the profit an arbitrageur could lock in. Both are partial answers to the question raised in \cref{intro:sec:subjective}: how should we reward beliefs about things that are never observed?

**Humanized**

The last two chapters took two different routes around the same obstacle. \Cref{ch:nonvf} scored sentences that never resolve by making them the stakes of a game whose moves eventually do. \Cref{ch:consistency} gave up on resolution altogether and asked only whether a forecaster's beliefs fit together, measuring the misfit as the profit an arbitrageur could lock in. Both are partial answers to the question raised in \cref{intro:sec:subjective}: how should we reward beliefs about things that are never observed?

**Final (meaning-corrected)**

The last two chapters approached the same obstacle from two different directions. In \cref{ch:nonvf} we dealt with it by making sentences that never resolve the stakes of larger games in which all the moves do have resolutions. In \cref{ch:consistency} we set resolution aside altogether, and instead asked whether the probabilities a forecaster assigns fit together, with any misfit showing up as an opportunity for an arbitrageur to lock in a riskless profit. How should we reward beliefs about things that are never observed? That was the question raised in \cref{intro:sec:subjective}, and the last two chapters can be viewed as two partial responses to it.

*Note:* StealthGPT had returned it unchanged; fresh StealthGPT variant with narrow fixes.


## Unit 5 — chapters/arbitrage.tex

**Original**

This chapter brings that question back to the economics of \cref{part:agency}. There, a market was a machine for computing values: price recursion carried the value of final consumption back through the economy, so that every intermediate good was priced by what it eventually contributed. The arbitrage metric of \cref{ch:consistency} looks like a different kind of object, a static measure of incoherence. The first half of this chapter shows that it is not different at all. The arbitrage metric is exactly the welfare that a market of consumers gains by trading, its arbitraged forecasts are the market's equilibrium prices, and the price recursion of \cref{ch:agency} decomposes the global arbitrageur into many local ones. Along the way, preferences and beliefs turn out to be aggregated by the same rule: the ``utilitarian welfare'' assumed in \cref{ch:agency} is the arbitrage-free combination of utilities read as beliefs.

**Humanized**

This chapter brings that question back to the economics of \cref{part:agency}. The market was, in essence, a machine for computing values. Using prices and price recursion, it carried the value of final consumption back through the economy, so that the value of any intermediate good was a measure of its ultimate contribution to final consumption. The arbitrage metric of \cref{ch:consistency} seems to belong to a different category of objects (being, essentially, a static measure of incoherence). In fact, it's not so different at all, as we'll see in the first half of this chapter. Another interesting interpretation of the arbitrage metric is as a measure of welfare of a market of consumers who participate in this trade. The arbitraged forecasts then have a natural interpretation as equilibrium prices. Finally, the price recursion of \cref{ch:agency} decomposes a single global arbitrageur into a collection of local arbitrageurs. The beliefs are aggregated in exactly the same way as the preferences. Thus, the ``utilitarian welfare'' of \cref{ch:agency} is arbitrage-free if the utilities are interpreted as beliefs.

**Final (meaning-corrected)**

This chapter brings that question back to the economics of \cref{part:agency}. There, the market was, in essence, a machine for computing values. Using price recursion, it carried the value of final consumption back through the economy, so that the price of any intermediate good was a measure of its ultimate contribution to final consumption. The arbitrage metric of \cref{ch:consistency} seems to belong to a different category of objects (being, essentially, a static measure of incoherence). In fact, as we will see in the first half of this chapter, it is not different at all. The arbitrage metric is exactly the welfare that a market of consumers gains by trading, and the arbitraged forecasts are the market's equilibrium prices. Finally, the price recursion of \cref{ch:agency} decomposes a single global arbitrageur into a collection of local arbitrageurs. Along the way, beliefs turn out to be aggregated in exactly the same way as preferences: the ``utilitarian welfare'' assumed in \cref{ch:agency} is the arbitrage-free combination of utilities interpreted as beliefs.

*Note:* Restored "is exactly the welfare gained by trading" (humanized weakened it to "another interpretation"), "not different at all", and the correct final claim (welfare is the arbitrage-free combination, not "is arbitrage-free if"); removed contractions.


## Unit 6 — chapters/arbitrage.tex

**Original**

The second half turns this observation on latent variables. In a market over dependent questions, a latent variable is simply an \emph{intermediate good}. Nobody consumes it and it never resolves, but it is priced by everything downstream of it, and the market's adjustment rule turns out to be the EM algorithm. So price recursion does put a value on latent beliefs. What it does not settle is \emph{which} latent structure the market should hold, because many latent models predict the observables equally well. We therefore ask what gives a latent belief its meaning when only observables can be scored. The answer we develop is that a latent means exactly what it does to predictions of observables, that what is left over splits into a harmless part (a choice of coordinates) and a genuine part, and that the genuine part can be removed by asking latents to explain the observables cheaply. This gives a scoring rule, the \emph{tempered log score}, whose expected value is maximized by the most economical latent explanation. We close by using these results to assess the existing proposals for latent-variable prediction markets.

**Humanized**

The second half of the paper is about latent variables. Latent variables are those that agents do not directly consume or care about, but are relevant for predicting variables that they do care about (i.e. latent variables matter only through their effect on other variables). In a market over dependent questions, a latent variable is simply an \emph{intermediate good}. We show that the price recursion still makes sense when there are latent variables (though of course prices can only be assigned to the non-latent variables), and the resulting price adjustment procedure is the EM algorithm. What it does not settle is \emph{which} latent structure the market should hold, because many latent models predict the observables equally well. We then discuss what it means for a belief over a latent variable to be correct, given that only the non-latent variables can be scored. We show that the meaning of a belief over latent variables is exactly captured by its predictions for the non-latent variables, and that any further notion of correctness can be divided into two parts: an arbitrary (but harmless) part that amounts to a choice of coordinates for the latent variables, and a substantive part, which can be eliminated by requiring that latent variables parsimoniously explain the non-latent variables. This gives a scoring rule, the \emph{tempered log score}, whose expected value is maximized by the most economical latent explanation. We then apply our characterization to existing proposals for prediction markets with latent variables.

**Final (meaning-corrected)**

The second half of the chapter is about latent variables. Latent variables are those that agents do not directly consume or care about, but are relevant for predicting variables that they do care about (i.e. latent variables matter only through their effect on other variables). In a market over dependent questions, a latent variable is simply an \emph{intermediate good}. We show that the price recursion still makes sense when there are latent variables (a latent variable is priced by everything downstream of it), and the resulting price adjustment procedure is the EM algorithm. What it leaves open is \emph{which} latent structure the market should hold, since many latent models predict the observables equally well. We then discuss what it means for a belief over a latent variable to be meaningful, given that only the non-latent variables can be scored. We show that the meaning of a belief over latent variables is exactly captured by its predictions for the non-latent variables, and that whatever is left over can be divided into two parts: an arbitrary (but harmless) part that amounts to a choice of coordinates for the latent variables, and a substantive part, which can be eliminated by requiring that latent variables parsimoniously explain the non-latent variables. This gives a scoring rule, the \emph{tempered log score}, whose expected value is maximized by the most economical latent explanation. We then apply our characterization to existing proposals for prediction markets with latent variables.

*Note:* Narrow fix of StealthGPT output (false aside about latent prices, "paper", "correct"); one retained original sentence reworded.


## Unit 7 — chapters/arbitrage.tex

**Original**

We start by restating the arbitrage metric of \cref{cfc:def:arbitrage} in a form convenient for what follows. There are questions $x_1,\dots,x_n$, and the forecaster reports a distribution $p_i$ over the possible answers to each. A \emph{world} $\omega$ assigns an answer to every question, and $\Omega$ is the set of worlds allowed by the logical relation between the questions. In world $\omega$ question $x_i$ resolves to $\phi_i(\omega)$, or is voided ($\phi_i(\omega)=\none$) if it is a conditional question whose condition fails. Each question is traded against a logarithmic market maker with liquidity $b_i$; \cref{ch:consistency} used $b_i=1$ throughout.

**Humanized**

For later use we rewrite the arbitrage metric of \cref{cfc:def:arbitrage} in the following form. The questions $x_1,\dots,x_n$, where the forecaster has a distribution $p_i$ over answers. An \emph{world} $\omega$ maps every question to some answer $\Omega$ is the set of all possible worlds consistent with this logical relation. In world $\omega$ question $x_i$ resolves to $\phi_i(\omega)$, or is voided ($\phi_i(\omega)=\none$) if it is a conditional question whose condition fails. Each question is traded against a logarithmic market maker with liquidity $b_i$; \cref{ch:consistency} used $b_i=1$ throughout.

**Final (meaning-corrected)**

For later use we rewrite the arbitrage metric of \cref{cfc:def:arbitrage} in the following form. There are questions $x_1,\dots,x_n$, and the forecaster reports a distribution $p_i$ over the possible answers to each. A \emph{world} $\omega$ maps every question to some answer, and $\Omega$ is the set of all worlds consistent with the logical relation between the questions. In world $\omega$ question $x_i$ resolves to $\phi_i(\omega)$, or is voided ($\phi_i(\omega)=\none$) if it is a conditional question whose condition fails. Each question is traded against a logarithmic market maker with liquidity $b_i$; \cref{ch:consistency} used $b_i=1$ throughout.

*Note:* Fixed sentence fragment, "An world", missing punctuation, and the dangling "this logical relation".


## Unit 8 — chapters/arbitrage.tex

**Original**

An arbitrageur moves the price of question $x_i$ from $p_i$ to $q_i$, and in world $\omega$ earns $b_i\left[\log q_i(\phi_i\omega)-\log p_i(\phi_i\omega)\right]$ from that market, or nothing if the question is voided. The arbitrage metric is the largest profit it can guarantee:
\begin{equation}\label{arb:eq:arbitrage}
A=\max_{q}\ \min_{\omega\in\Omega}\ \sum_{i=1}^n b_i\left[\log q_i(\phi_i\omega)-\log p_i(\phi_i\omega)\right].
\end{equation}

**Humanized**

An arbitrageur moves the price of question $x_i$ from $p_i$ to $q_i$, and in world $\omega$ earns $b_i\left[\log q_i(\phi_i\omega)-\log p_i(\phi_i\omega)\right]$ from that market, or nothing if the question is voided. The arbitrage metric is the maximum guaranteed profit
\begin{equation}\label{arb:eq:arbitrage}
A=\max_{q}\ \min_{\omega\in\Omega}\ \sum_{i=1}^n b_i\left[\log q_i(\phi_i\omega)-\log p_i(\phi_i\omega)\right].
\end{equation}


## Unit 9 — chapters/arbitrage.tex

**Original**

\begin{proposition}[the arbitrage metric is an information projection]\label{arb:prop:dual}
For a distribution $\mu$ over $\Omega$, let $M_i(\mu)$ be the probability that question $x_i$ is not voided and let $\mu_i$ be the distribution of its answer given that it is not voided. Then
\begin{equation}\label{arb:eq:dual}
A=\min_{\mu\in\simplex(\Omega)}\ \sum_{i=1}^n b_i\,M_i(\mu)\,\KL\!\left(\mu_i\,\|\,p_i\right),
\end{equation}
and the arbitraged forecasts are the marginals of the minimizer: $q^*_i=\mu^*_i$.
\end{proposition}

**Humanized**

\begin{proposition}[the arbitrage metric is an information projection]\label{arb:prop:dual}
For a distribution $\mu$ over $\Omega$, let $M_i(\mu)$ be the probability that question $x_i$ is not voided and let $\mu_i$ be the distribution of its answer given that it is not voided. Then
\begin{equation}\label{arb:eq:dual}
A=\min_{\mu\in\simplex(\Omega)}\ \sum_{i=1}^n b_i\,M_i(\mu)\,\KL\!\left(\mu_i\,\|\,p_i\right),
\end{equation}
and the marginals of the minimizer are arbitraged forecasts: $q^*_i=\mu^*_i$.
\end{proposition}

**Final (meaning-corrected)**

\begin{proposition}[the arbitrage metric is an information projection]\label{arb:prop:dual}
For a distribution $\mu$ over $\Omega$, let $M_i(\mu)$ be the probability that question $x_i$ is not voided and let $\mu_i$ be the distribution of its answer given that it is not voided. Then
\begin{equation}\label{arb:eq:dual}
A=\min_{\mu\in\simplex(\Omega)}\ \sum_{i=1}^n b_i\,M_i(\mu)\,\KL\!\left(\mu_i\,\|\,p_i\right),
\end{equation}
and the arbitraged forecasts are the marginals of the minimizer: $q^*_i=\mu^*_i$.
\end{proposition}

*Note:* Restored the definite identification (the arbitraged forecasts are the marginals), not merely "are arbitraged forecasts".


## Unit 10 — chapters/arbitrage.tex

**Original**

\begin{proof}
For fixed $q$, the objective in \eqref{arb:eq:arbitrage} is linear in the world, so the minimum over worlds equals the minimum over distributions $\mu$ on worlds. The resulting function is concave in $q$ and linear in $\mu$, and $\simplex(\Omega)$ is compact and convex, so Sion's minimax theorem \citep{sionGeneralMinimaxTheorems1958} lets us exchange the max and the min. For a fixed $\mu$, the arbitrageur's best choice for question $x_i$ maximizes $\sum_v \mu(\phi_i=v)\log q_i(v)$, which by Gibbs' inequality is $q_i=\mu_i$. Substituting gives $b_iM_i(\mu)\KL(\mu_i\|p_i)$ for each question.
\end{proof}

**Humanized**

\begin{proof}
For fixed $q$, \eqref{arb:eq:arbitrage} is linear in the world, so minimising over worlds is the same as minimising over distributions $\mu$ on worlds. Since the objective function is concave in $q$ and linear in $\mu$, and since $\simplex(\Omega)$ is compact and convex, we can interchange the order of the max and min operations by Sion's minimax theorem \citep{sionGeneralMinimaxTheorems1958}. For a fixed $\mu$, the arbitrageur's best choice for question $x_i$ maximizes $\sum_v \mu(\phi_i=v)\log q_i(v)$, which by Gibbs' inequality is $q_i=\mu_i$. Substituting gives $b_iM_i(\mu)\KL(\mu_i\|p_i)$ for each question.
\end{proof}

**Final (meaning-corrected)**

\begin{proof}
For fixed $q$, the objective in \eqref{arb:eq:arbitrage} is linear in the world, so minimizing over worlds is the same as minimizing over distributions $\mu$ on worlds. Since the resulting function is concave in $q$ and linear in $\mu$, and since $\simplex(\Omega)$ is compact and convex, we can interchange the order of the max and min operations by Sion's minimax theorem \citep{sionGeneralMinimaxTheorems1958}. For a fixed $\mu$, the arbitrageur's best choice for question $x_i$ maximizes $\sum_v \mu(\phi_i=v)\log q_i(v)$, which by Gibbs' inequality is $q_i=\mu_i$. Substituting gives $b_iM_i(\mu)\KL(\mu_i\|p_i)$ for each question.
\end{proof}

*Note:* Said the objective (not the equation) is linear, referred to the resulting function after the exchange, and made spelling consistently American.


## Unit 11 — chapters/arbitrage.tex

**Original**

Read this way, the arbitrageur's worst-case distribution over worlds is itself a coherent belief, and the arbitrage metric is how far, in total KL divergence, the forecaster's beliefs are from the nearest coherent one. In information-geometric terms it is an I-projection (a ``reverse KL'' projection) of the forecasts onto the set of consistent beliefs. The proposition also explains the convention in \cref{ch:consistency} of scoring voided questions as zero: it weights a conditional question by the probability of its condition.

**Humanized**

Read this way, the arbitrageur's worst-case distribution over worlds is itself a coherent belief, and the arbitrage metric is how far, in total KL divergence, the forecaster's beliefs are from the nearest coherent one. In information-geometric terms it is an I-projection (a ``reverse KL'' projection) of the forecasts onto the set of consistent beliefs. This justifies \cref{ch:consistency}'s convention of giving a voided question zero score: conditional questions should be weighted by the probability of the conditioning event.

**Final (meaning-corrected)**

Read this way, the arbitrageur's worst-case distribution over worlds is itself a coherent belief, and the arbitrage metric is how far, in total KL divergence, the forecaster's beliefs are from the nearest coherent one. In information-geometric terms it is an I-projection (a ``reverse KL'' projection) of the forecasts onto the set of consistent beliefs. The proposition also explains \cref{ch:consistency}'s convention of giving a voided question zero score: the convention weights a conditional question by the probability of the conditioning event.

*Note:* Changed normative "justifies ... should be weighted" back to the descriptive "explains ... weights".


## Unit 12 — chapters/arbitrage.tex

**Original**

Nothing here depends on the logarithm. For any proper scoring rule whose expected score is concave in the report, with convex generator $F$ and Bregman divergence $D_F$, the same argument gives $A_F=\min_\mu\sum_ib_iD_F(\mu\|p_i)$ (ignoring voided questions for simplicity). When all the $p_i$ are forecasts of the \emph{same} variable, the minimizer satisfies
\begin{equation}\label{arb:eq:mirror-average}
\nabla F(q^*)=\sum_i w_i\,\nabla F(p_i)+c\mathbf 1,\qquad w_i=b_i/B,\ B=\textstyle\sum_ib_i,
\end{equation}
for a constant $c$. In words, the arbitraged forecast is the weighted average of the forecasts \emph{in mirror coordinates} (\cref{agency:sec:mirror}). For the log score the mirror coordinate is the log-probability, so the arbitraged forecast is the geometric pool $q^*\propto\prod_ip_i^{w_i}$. For the Brier score it is the probability itself, and the arbitraged forecast is the linear pool $\sum_iw_ip_i$.

**Humanized**

Nothing here depends on the logarithm. For any proper scoring rule whose expected score is concave in the report, with convex generator $F$ and Bregman divergence $D_F$, the same argument gives $A_F=\min_\mu\sum_ib_iD_F(\mu\|p_i)$ (ignoring voided questions for simplicity). $$ \frac{\partial}{\partial \hat{y}} \sum_{i=1}^{M1} L(y,\hat{y}) = 0 \Rightarrow \frac{\partial}{\partial \hat{y}} L(y,\hat{y})=0 $$ where the last equality holds assuming that all the $p_i$ are forecasts of the \emph{same} variable.
\begin{equation}\label{arb:eq:mirror-average}
\nabla F(q^*)=\sum_i w_i\,\nabla F(p_i)+c\mathbf 1,\qquad w_i=b_i/B,\ B=\textstyle\sum_ib_i,
\end{equation}
for a constant $c$. That is, the arbitraged forecast is the average of the forecasts \emph{in mirror coordinates} (\cref{agency:sec:mirror}). In the case of the log score, the mirror coordinate is log-probability, so the arbitraged forecast is the geometric pool $q^*\propto\prod_ip_i^{w_i}$. For the Brier score it is the probability itself, and the arbitraged forecast is the linear pool $\sum_iw_ip_i$.

**Final (meaning-corrected)**

Nothing here depends on the logarithm. For any proper scoring rule whose expected score is concave in the report, with convex generator $F$ and Bregman divergence $D_F$, the same argument gives $A_F=\min_\mu\sum_ib_iD_F(\mu\|p_i)$ (ignoring voided questions for simplicity). When all the $p_i$ are forecasts of the \emph{same} variable, the minimizer satisfies
\begin{equation}\label{arb:eq:mirror-average}
\nabla F(q^*)=\sum_i w_i\,\nabla F(p_i)+c\mathbf 1,\qquad w_i=b_i/B,\ B=\textstyle\sum_ib_i,
\end{equation}
for a constant $c$. That is, the arbitraged forecast is the weighted average of the forecasts \emph{in mirror coordinates} (\cref{agency:sec:mirror}). In the case of the log score, the mirror coordinate is the log-probability, so the arbitraged forecast is the geometric pool $q^*\propto\prod_ip_i^{w_i}$. For the Brier score it is the probability itself, and the arbitraged forecast is the linear pool $\sum_iw_ip_i$.

*Note:* Deleted a spurious inserted display equation unrelated to the thesis and restored the sentence introducing the minimizer's condition; restored "weighted" average.


## Unit 13 — chapters/arbitrage.tex

**Original**

\begin{example}\label{arb:ex:election}
A forecaster gives both the Democratic and the Republican candidate a 60\% chance of winning, and exactly one of them will win. Write both forecasts as distributions over the two worlds: $p_1=(0.6,0.4)$ and $p_2=(0.4,0.6)$, with $b_1=b_2=1$. The geometric pool is $q^*=(\tfrac12,\tfrac12)$, and the arbitrage metric is
\[
A=\KL(q^*\|p_1)+\KL(q^*\|p_2)=-2\log\!\big(2\sqrt{0.24}\big)\approx0.041\ \text{nats},
\]
which agrees with the closed form for the negation check given in \cref{cfc:sec:arbitrage}.
\end{example}

**Humanized**

\begin{example}\label{arb:ex:election}
Suppose a forecaster assigned a 60\% chance of winning to each of the Democratic and Republican candidates (exactly one of whom, of course, will win). Write both forecasts as distributions over the two worlds: $p_1=(0.6,0.4)$ and $p_2=(0.4,0.6)$, with $b_1=b_2=1$. where $q^*=(\tfrac12,\tfrac12)$, is the geometric pool and is the arbitrage metric.
\[
A=\KL(q^*\|p_1)+\KL(q^*\|p_2)=-2\log\!\big(2\sqrt{0.24}\big)\approx0.041\ \text{nats},
\]
which agrees with the closed form for the negation check given in \cref{cfc:sec:arbitrage}.
\end{example}

**Final (meaning-corrected)**

\begin{example}\label{arb:ex:election}
Suppose a forecaster assigned a 60\% chance of winning to each of the Democratic and Republican candidates (exactly one of whom, of course, will win). Write both forecasts as distributions over the two worlds: $p_1=(0.6,0.4)$ and $p_2=(0.4,0.6)$, with $b_1=b_2=1$. The geometric pool is $q^*=(\tfrac12,\tfrac12)$, and the arbitrage metric is
\[
A=\KL(q^*\|p_1)+\KL(q^*\|p_2)=-2\log\!\big(2\sqrt{0.24}\big)\approx0.041\ \text{nats},
\]
which agrees with the closed form for the negation check given in \cref{cfc:sec:arbitrage}.
\end{example}

*Note:* Fixed the garbled sentence introducing the geometric pool and the arbitrage metric display.


## Unit 14 — chapters/arbitrage.tex

**Original**

\Cref{ch:agency} took the objective of an economy to be utilitarian welfare $W=\sum_iU_i$, ``without loss of generality with weights 1''. We now show where that sum comes from.

**Humanized**

\Cref{ch:agency} took the objective of an economy to be utilitarian welfare $W=\sum_iU_i$, ``without loss of generality with weights 1''. We're almost ready to see where the sum comes from.

**Final (meaning-corrected)**

\Cref{ch:agency} took the objective of an economy to be utilitarian welfare $W=\sum_iU_i$, ``without loss of generality with weights 1''. We now show where that sum comes from.

*Note:* Restored "we now show" (humanized changed the meaning and used a contraction).


## Unit 15 — chapters/arbitrage.tex

**Original**

Take $n$ forecasts of one variable and write each in softmax form, $p_i(x)=e^{U_i(x)}/Z_i$. Here $U_i$ can be read either as a log-probability (a logit) or as a utility, and we will read it both ways. Let $\Phi(U)=\log\sum_xe^{U(x)}$ be the log-partition function, which is convex.

**Humanized**

Consider $n$ models each making predictions about a common variable $x$. Write their predictions in softmax form as $p_i(x)=e^{U_i(x)}/Z_i$ where $i$ indexes the models. Here $U_i$ can be read either as a log-probability (a logit) or as a utility, and we will read it both ways. Let $\Phi(U)=\log\sum_xe^{U(x)}$, the log-partition function, which is convex.

**Final (meaning-corrected)**

Consider $n$ forecasts of a common variable, and write each in softmax form as $p_i(x)=e^{U_i(x)}/Z_i$. Here $U_i$ can be read either as a log-probability (a logit) or as a utility, and we will read it both ways. Let $\Phi(U)=\log\sum_xe^{U(x)}$ be the log-partition function, which is convex.

*Note:* Kept "forecasts" rather than "models", removed added math ($x$, index gloss), and fixed the "Let ..., the ..." fragment.


## Unit 16 — chapters/arbitrage.tex

**Original**

So the arbitraged \emph{utility} is $\Ubar=\sum_iw_iU_i$: the utilitarian welfare of \cref{ch:agency}, with welfare weights equal to the liquidities. Averaging beliefs in mirror space and summing utilities are the same operation. This gives the sum of utilities a justification that does not rest on interpersonal comparisons of utility in the usual sense. If we read each agent's preferences as a belief about ``what we will do'', then maximizing the weighted sum of utilities is the unique arbitrage-free way of combining them, and the weights are the amounts each agent is willing to stake.

**Humanized**

So the arbitraged \emph{utility} is $\Ubar=\sum_iw_iU_i$: the utilitarian welfare of \cref{ch:agency}, with welfare weights equal to the liquidities. Another way to look at this is that if you interpret the preferences of different agents as beliefs in mirror space (each agent is making a bet on ``what we will do''), then the weighted sum of utilities is just the average of beliefs in mirror space. So the justification for the weighted sum of utilities as the thing to maximize is that it is the unique arbitrage-free way to combine the agents' beliefs, rather than it being a justification for interpersonal comparisons of utility in the usual sense. (And the weights in the sum of utilities are the amounts that the agents are willing to put on the line.)

**Final (meaning-corrected)**

So the arbitraged \emph{utility} is $\Ubar=\sum_iw_iU_i$: the utilitarian welfare of \cref{ch:agency}, with welfare weights equal to the liquidities. In other words, averaging beliefs in mirror space and summing utilities are the same operation. This gives the weighted sum of utilities a justification that does not rest on interpersonal comparisons of utility in the usual sense: if we interpret the preferences of each agent as a belief (a bet on ``what we will do''), then maximizing the weighted sum of utilities is the unique arbitrage-free way to combine them. (And the weights in the sum are the amounts that the agents are willing to put on the line.)

*Note:* Fixed the garbled claim (humanized said the sum was not "a justification for interpersonal comparisons"; original: the justification does not rest on them), restored the "same operation" statement, removed chatty "you".


## Unit 17 — chapters/arbitrage.tex

**Original**

The right-hand side of \eqref{arb:eq:jensen} is the gap in Jensen's inequality for the convex function $\Phi$, a quantity known as the \emph{Bregman information} \citep{banerjeeClusteringBregmanDivergences2005}. The Hessian of $\Phi$ is the covariance matrix of the softmax distribution, so for small disagreements
\[
A\approx\frac B2\sum_iw_i\Var_{q^*}\!\big(U_i-\Ubar\big),\qquad\text{and for a binary question}\quad A\approx\frac B2\,q^*(1-q^*)\Var_w\big(\text{log-odds}_i\big).
\]
The arbitrage metric is therefore, to second order, a variance of the forecasters' log-odds. Exactly, it is the natural generalization of variance to this geometry.

**Humanized**

The right-hand side of~\eqref{arb:eq:jensen} is the gap in Jensen's inequality for the convex function $\Phi$, a quantity known as the \emph{Bregman information} \citep{banerjeeClusteringBregmanDivergences2005}. For small disagreements, the Hessian of $\Phi$ is given by the covariance matrix of the softmax distribution.
\[
A\approx\frac B2\sum_iw_i\Var_{q^*}\!\big(U_i-\Ubar\big),\qquad\text{and for a binary question}\quad A\approx\frac B2\,q^*(1-q^*)\Var_w\big(\text{log-odds}_i\big).
\]
The arbitrage metric is a measure of the amount of disagreement in log-odds between different forecasters. It is (to second order) a variance of the log-odds of the forecasters (more exactly, it is the natural generalization of variance to this geometry).

**Final (meaning-corrected)**

The right-hand side of~\eqref{arb:eq:jensen} is the gap in Jensen's inequality for the convex function $\Phi$, a quantity known as the \emph{Bregman information} \citep{banerjeeClusteringBregmanDivergences2005}. The Hessian of $\Phi$ is the covariance matrix of the softmax distribution, so for small disagreements
\[
A\approx\frac B2\sum_iw_i\Var_{q^*}\!\big(U_i-\Ubar\big),\qquad\text{and for a binary question}\quad A\approx\frac B2\,q^*(1-q^*)\Var_w\big(\text{log-odds}_i\big).
\]
The arbitrage metric therefore measures the disagreement in log-odds between forecasters: to second order it is a variance of their log-odds, and exactly it is the natural generalization of variance to this geometry.

*Note:* "For small disagreements" qualified the Hessian identity (which holds always) instead of the approximation; reattached it to the display and restored "exactly" (not "more exactly").


## Unit 18 — chapters/arbitrage.tex

**Original**

Which market actually computes $q^*$ and $A$? Consider the simplest economy of \cref{ch:agency}: a single source holding $K$ units of each Arrow security (a security that pays $1$ if outcome $x$ occurs), and $n$ consumers competing for them. The source routes security $x$ to consumer $i$ with share $s_i(x)$, so consumer $i$ ends up holding $z_i(x)=Ks_i(x)$. Consumer $i$ believes $p_i\propto e^{U_i}$ and has exponential (CARA) utility with risk tolerance $b_i$, so its certainty equivalent for holdings $z$ is
\[
V_i(z)=-b_i\log\mathbb E_{x\sim p_i}\,e^{-z(x)/b_i}.
\]
The price that consumer $i$ is willing to pay for a marginal unit of security $x$ is
\[
a_i(x)=\frac{\partial V_i}{\partial z(x)}=\operatorname{softmax}\!\big(U_i-z_i/b_i\big)(x),
\]
its current risk-neutral probability of $x$. The share dynamics of \cref{agency:eq:mwu}, $s_i(x)\propto s_i(x)\exp\!\big(\eta Ka_i(x)\big)$, then send each security towards whoever currently values it most.

**Humanized**

Which market computes $q^*$ and $A$? The simplest economy considered in \cref{ch:agency}: consists of a single owner of $K$ units of each Arrow security (which pays $1$ if state $x$ occurs), and $n$ consumers. The source routes security $x$ to consumer $i$ with share $s_i(x)$, so consumer $i$ ends up holding $z_i(x)=Ks_i(x)$. Consumer $i$ believes $p_i\propto e^{U_i}$ and has exponential (CARA) utility with risk tolerance $b_i$, so its certainty equivalent for holdings $z$ is
\[
V_i(z)=-b_i\log\mathbb E_{x\sim p_i}\,e^{-z(x)/b_i}.
\]
The price that consumer $i$ is willing to pay for a marginal unit of security $x$ is
\[
a_i(x)=\frac{\partial V_i}{\partial z(x)}=\operatorname{softmax}\!\big(U_i-z_i/b_i\big)(x),
\]
the current risk-neutral probability of $x$. The share dynamics of \cref{agency:eq:mwu}, $s_i(x)\propto s_i(x)\exp\!\big(\eta Ka_i(x)\big)$, then send each security towards whoever currently values it most.

**Final (meaning-corrected)**

Which market actually computes $q^*$ and $A$? Consider the simplest economy of \cref{ch:agency}, which consists of a single source holding $K$ units of each Arrow security (which pays $1$ if state $x$ occurs) and $n$ consumers competing for them. The source routes security $x$ to consumer $i$ with share $s_i(x)$, so consumer $i$ ends up holding $z_i(x)=Ks_i(x)$. Consumer $i$ believes $p_i\propto e^{U_i}$ and has exponential (CARA) utility with risk tolerance $b_i$, so its certainty equivalent for holdings $z$ is
\[
V_i(z)=-b_i\log\mathbb E_{x\sim p_i}\,e^{-z(x)/b_i}.
\]
The price that consumer $i$ is willing to pay for a marginal unit of security $x$ is
\[
a_i(x)=\frac{\partial V_i}{\partial z(x)}=\operatorname{softmax}\!\big(U_i-z_i/b_i\big)(x),
\]
its current risk-neutral probability of $x$. The share dynamics of \cref{agency:eq:mwu}, $s_i(x)\propto s_i(x)\exp\!\big(\eta Ka_i(x)\big)$, then send each security towards whoever currently values it most.

*Note:* Fixed stray colon/fragment, used "source" consistently with the next sentence, restored "competing for them" and "its" (the consumer's) risk-neutral probability.


## Unit 19 — chapters/arbitrage.tex

**Original**

\begin{theorem}[CARA markets compute the arbitrage]\label{arb:thm:cara}
At the welfare-maximizing allocation:
\begin{enumerate}
\item every consumer's price vector equals the arbitraged forecast $q^*$, so the law of one price is exactly the consistency of the market's beliefs;
\item the welfare gain from trade, $\sum_iV_i(z_i)$ minus its value without trade, equals the arbitrage metric $A$;
\item holdings are $z_i=b_i(U_i-\Ubar)+c_i$ for constants $c_i$, so every consumer's post-trade effective utility $U_i-z_i/b_i$ equals $\Ubar$ up to a constant.
\end{enumerate}
\end{theorem}

**Humanized**

\begin{theorem}[CARA markets compute the arbitrage]\label{arb:thm:cara}
Therefore, to identify the welfare maximizing allocation it suffices to identify the solution of the dual problem.
\begin{enumerate}
\item the law of one price (that every consumer's price vector is the same) is precisely the statement that $q^*$, every consumer's price vector equals the arbitraged forecast. Hence, the law of one price is precisely the consistency of the market's beliefs.
\item the welfare gain from trade, $\sum_iV_i(z_i)$ minus its value without trade, equals the arbitrage metric $A$;
\item holdings are $z_i=b_i(U_i-\Ubar)+c_i$ for constants $c_i$, so every consumer's post-trade effective utility $U_i-z_i/b_i$ equals $\Ubar$ up to a constant.
\end{enumerate}
\end{theorem}

**Final (meaning-corrected)**

\begin{theorem}[CARA markets compute the arbitrage]\label{arb:thm:cara}
At the welfare-maximizing allocation:
\begin{enumerate}
\item every consumer's price vector equals the arbitraged forecast $q^*$, so the law of one price (that every consumer's price vector is the same) is precisely the consistency of the market's beliefs;
\item the welfare gain from trade, $\sum_iV_i(z_i)$ minus its value without trade, equals the arbitrage metric $A$;
\item holdings are $z_i=b_i(U_i-\Ubar)+c_i$ for constants $c_i$, so every consumer's post-trade effective utility $U_i-z_i/b_i$ equals $\Ubar$ up to a constant.
\end{enumerate}
\end{theorem}

*Note:* Removed an invented claim about the dual problem replacing the theorem's hypothesis, and fixed garbled item 1.


## Unit 20 — chapters/arbitrage.tex

**Original**

\begin{proof}
Without trade every consumer holds a riskless bundle, and because $V_i(z+c\mathbf1)=V_i(z)+c$ the total value of any riskless allocation of the $K$ units is $K$. It therefore suffices to show that the allocation in (3) is optimal and to compute its value. With $\sum_ic_i=0$ we have $\sum_iz_i=\sum_ib_iU_i-B\Ubar=0$, so (3) is feasible as a trade. Under (3), $U_i-z_i/b_i=\Ubar-c_i/b_i$, so all consumers have the same marginal values $\operatorname{softmax}(\Ubar)=q^*$; since each $V_i$ is concave, equal marginal values certify that the allocation maximizes the sum. Finally,
$V_i(z_i)=c_i-b_i\log\sum_xe^{U_i(x)-\Phi(U_i)-U_i(x)+\Ubar(x)}=c_i+b_i\big[\Phi(U_i)-\Phi(\Ubar)\big]$, and summing over $i$ gives $A$ by \cref{arb:prop:welfare}.
\end{proof}

**Humanized**

\begin{proof}
Absent trade each consumer has a riskless bundle, and by $V_i(z+c\mathbf1)=V_i(z)+c$ the sum of the values of the $K$ units in any riskless allocation is $K$. It is then enough to compute the value of the allocation in (3) and prove its optimality. With $\sum_ic_i=0$ we have $\sum_iz_i=\sum_ib_iU_i-B\Ubar=0$, so (3) is feasible as a trade. Under (3), $U_i-z_i/b_i=\Ubar-c_i/b_i$, hence consumers' marginal values are all equal $\operatorname{softmax}(\Ubar)=q^*$. Thus, the allocation maximizes the sum of $V_i$ (since they are concave functions). Finally,
$V_i(z_i)=c_i-b_i\log\sum_xe^{U_i(x)-\Phi(U_i)-U_i(x)+\Ubar(x)}=c_i+b_i\big[\Phi(U_i)-\Phi(\Ubar)\big]$, and summing over $i$ gives $A$ by \cref{arb:prop:welfare}.
\end{proof}

**Final (meaning-corrected)**

\begin{proof}
Absent trade each consumer has a riskless bundle, and by $V_i(z+c\mathbf1)=V_i(z)+c$ the sum of the values of the $K$ units in any riskless allocation is $K$. It is then enough to compute the value of the allocation in (3) and prove its optimality. With $\sum_ic_i=0$ we have $\sum_iz_i=\sum_ib_iU_i-B\Ubar=0$, so (3) is feasible as a trade. Under (3), $U_i-z_i/b_i=\Ubar-c_i/b_i$, hence all consumers' marginal values are equal to $\operatorname{softmax}(\Ubar)=q^*$. Since each $V_i$ is concave, these equal marginal values certify that the allocation maximizes the sum. Finally,
$V_i(z_i)=c_i-b_i\log\sum_xe^{U_i(x)-\Phi(U_i)-U_i(x)+\Ubar(x)}=c_i+b_i\big[\Phi(U_i)-\Phi(\Ubar)\big]$, and summing over $i$ gives $A$ by \cref{arb:prop:welfare}.
\end{proof}

*Note:* Fixed "are all equal $X$" grammar and restored the certification logic (concavity plus equal marginals implies optimality).


## Unit 21 — chapters/arbitrage.tex

**Original**

The market does not change what anybody wants. It hands each consumer a portfolio, which plays the role of a reward, equal to that consumer's disagreement with the collective, and after trading everyone acts on the arbitraged utility at the margin. This is a concrete instance of the claim in \cref{agency:sec:rationalize} that an economy, acting as a super-agent, generates the rewards of its sub-agents.

**Humanized**

The market can't change your desires. It hands each consumer a portfolio, which plays the role of a reward, equal to that consumer's disagreement with the collective, and after trading everyone acts on the arbitraged utility at the margin. This is a concrete instance of the claim in \cref{agency:sec:rationalize} that an economy, acting as a super-agent, generates the rewards of its sub-agents.

**Final (meaning-corrected)**

The market does not change anyone's desires. It hands each consumer a portfolio, which plays the role of a reward, equal to that consumer's disagreement with the collective, and after trading everyone acts on the arbitraged utility at the margin. This is a concrete instance of the claim in \cref{agency:sec:rationalize} that an economy, acting as a super-agent, generates the rewards of its sub-agents.

*Note:* Removed contraction and chatty "you".


## Unit 22 — chapters/arbitrage.tex

**Original**

The reason behind the theorem is more general. Call a consumer \emph{quasi-linear} if $V_i(z+c\mathbf1)=V_i(z)+c$ and $V_i(0)=0$. Then $C_i(\theta):=-V_i(-\theta)$ is the cost function of a market maker, with prices $p_i=\nabla C_i(0)$ and scoring rule given by the convex conjugate $C_i^*$ \citep{chenUtilityFrameworkBoundedloss2007}. The planner's problem is an infimal convolution, and the conjugate of an infimal convolution is a sum, so
\[
\sup_{\sum_iz_i=0}\ \sum_iV_i(z_i)=\inf_\mu\ \sum_iC_i^*(\mu)=\inf_\mu\ \sum_iD_{F_i}(\mu\|p_i)=A_F .
\]
Every quasi-linear consumer is a market maker for some proper scoring rule, and the planner's problem for a single-layer market is the arbitrage problem for those rules. For CARA consumers $C_i$ is the logarithmic market scoring rule and we recover \cref{arb:thm:cara}. The fact that CARA traders price at the geometric pool is old: it goes back to \citet{wilsonTheorySyndicates1968} on syndicates, and in prediction-market form to \citet{abernethyInformationAggregationExponential2014}. What is new is the identification with the arbitrage metric and with the welfare and mirror-ascent picture of \cref{ch:agency}.

**Humanized**

Another way of looking at the theorem is via duality. Call a consumer \emph{quasi-linear} if $V_i(z+c\mathbf1)=V_i(z)+c$ and $V_i(0)=0$. Then $C_i(\theta):=-V_i(-\theta)$ is the cost function of a market maker, with prices $p_i=\nabla C_i(0)$ and scoring rule given by the convex conjugate $C_i^*$ \citep{chenUtilityFrameworkBoundedloss2007}. The planner's problem is an infimal convolution and the dual of such a problem is much simpler because the conjugate of an infimal convolution is the sum of the conjugates: where $f_{i}^{*}$ denotes the convex conjugate of $f_{i}$. Since the dual objective is a sum, each term can be optimized separately.
\[
\sup_{\sum_iz_i=0}\ \sum_iV_i(z_i)=\inf_\mu\ \sum_iC_i^*(\mu)=\inf_\mu\ \sum_iD_{F_i}(\mu\|p_i)=A_F .
\]
Every quasi-linear consumer can be viewed as a market maker for some proper scoring rule and, more generally, the planner's problem for a single-layer market can be identified with the arbitrage problem for these rules. For CARA consumers $C_i$ is the logarithmic market scoring rule and we recover \cref{arb:thm:cara}. The fact that CARA traders price at the geometric pool is old: it goes back to \citet{wilsonTheorySyndicates1968} on syndicates, and in prediction-market form to \citet{abernethyInformationAggregationExponential2014}. The novelty of our contribution is that we identify this metric with an arbitrage metric and develop further its interpretation in terms of the welfare and mirror-ascent picture of \cref{ch:agency}.

**Final (meaning-corrected)**

The reason behind the theorem is more general. Call a consumer \emph{quasi-linear} if $V_i(z+c\mathbf1)=V_i(z)+c$ and $V_i(0)=0$. Then $C_i(\theta):=-V_i(-\theta)$ is the cost function of a market maker, with prices $p_i=\nabla C_i(0)$ and scoring rule given by the convex conjugate $C_i^*$ \citep{chenUtilityFrameworkBoundedloss2007}. The planner's problem is an infimal convolution, and the conjugate of an infimal convolution is the sum of the conjugates, so
\[
\sup_{\sum_iz_i=0}\ \sum_iV_i(z_i)=\inf_\mu\ \sum_iC_i^*(\mu)=\inf_\mu\ \sum_iD_{F_i}(\mu\|p_i)=A_F .
\]
Every quasi-linear consumer is a market maker for some proper scoring rule, and the planner's problem for a single-layer market is the arbitrage problem for these rules. For CARA consumers $C_i$ is the logarithmic market scoring rule and we recover \cref{arb:thm:cara}. The fact that CARA traders price at the geometric pool is old: it goes back to \citet{wilsonTheorySyndicates1968} on syndicates, and in prediction-market form to \citet{abernethyInformationAggregationExponential2014}. What is new here is the identification with the arbitrage metric and with the welfare and mirror-ascent picture of \cref{ch:agency}.

*Note:* Removed invented math ($f_i^*$) and a false claim that terms can be optimized separately, restored the generality framing, removed spurious "more generally", and fixed "this metric with an arbitrage metric".


## Unit 23 — chapters/arbitrage.tex

**Original**

There is one important qualification. Consumers with logarithmic (Kelly) utility, $\mathbb E_{p_i}\log z_i$, are not quasi-linear, and the same market then prices at the wealth-weighted \emph{linear} pool, which minimizes $\sum_iw_i\KL(p_i\|\pi)$. This is the opposite projection (an M-projection) and is not the arbitrage of \cref{ch:consistency}; in our numerical test the two differ by $0.08$. So it is true that ``the market arbitrages beliefs'', but the consumers' attitudes to risk decide the geometry in which the arbitrage takes place.

**Humanized**

For traders with logarithmic (``Kelly'') utility, $\mathbb E_{p_i}\log z_i$, who are \emph{not} quasi-linear, the optimal market maker instead prices at the wealth-weighted \emph{linear} pool, which minimizes $\sum_iw_i\KL(p_i\|\pi)$. Another possibility to compute a projection is the so called opposite projection (an M-projection). Note that the projection is in general not the arbitrage defined in \cref{ch:consistency}. In our numerical test the difference was $0.08$. While ``the market does indeed arbitrage beliefs'', the geometry of that arbitrage is determined by consumers' attitudes to risk.

**Final (meaning-corrected)**

There is one important qualification. Consumers with logarithmic (``Kelly'') utility, $\mathbb E_{p_i}\log z_i$, are \emph{not} quasi-linear, and for them the same market instead prices at the wealth-weighted \emph{linear} pool, which minimizes $\sum_iw_i\KL(p_i\|\pi)$. This is the opposite projection (an M-projection), and it is not the arbitrage defined in \cref{ch:consistency}; in our numerical test the difference was $0.08$. So while it is true that ``the market arbitrages beliefs'', the geometry of that arbitrage is determined by consumers' attitudes to risk.

*Note:* Fixed "the optimal market maker" (it is the same market), the false "another possibility to compute a projection" (the linear pool IS the M-projection), dropped added "in general", and restored the quoted phrase.


## Unit 24 — chapters/arbitrage.tex

**Original**

So far all forecasts concerned one variable. The questions of \cref{ch:consistency} are logically related to one another, and for them we need a market with depth. It is convenient to swap the roles of goods and prices: the good is now \emph{probability mass}, and prices are payoffs.

**Humanized**

Markets with depth. So far, we have focused on single questions. In \cref{ch:consistency}, however, we considered logically-related questions, which called for a market with depth. It is convenient to swap the roles of goods and prices: the good is now \emph{probability mass}, and prices are payoffs.

**Final (meaning-corrected)**

So far, we have focused on forecasts of a single variable. In \cref{ch:consistency}, however, we considered logically related questions, which call for a market with depth. It is convenient to swap the roles of goods and prices: the good is now \emph{probability mass}, and prices are payoffs.

*Note:* Removed stray fragment "Markets with depth." and said "single variable" rather than "single questions".


## Unit 25 — chapters/arbitrage.tex

**Original**

\paragraph{Construction.} Let the questions be built from atomic events $X_1,\dots,X_k$.
\begin{itemize}
\item A source holds one unit of probability mass. Internal nodes are partial assignments of the atoms, and the routing shares at a node are the conditional probabilities $P(X_d\mid X_{<d})$. Passing mass forward is then exactly marginalization.
\item Logical constraints are \emph{missing edges}: a world that violates the relation between the questions has no path leading to it.
\item Each leaf (a complete world $\omega$) sends one copy of its mass to the cell $(i,\phi_i(\omega))$ of every question that is not voided in $\omega$, like a refinery producing several outputs from one input. Cell $(i,v)$ thus receives $\mu(\phi_i=v)$.
\item Consumer $i$ owns the cells of question $x_i$ and has utility $u_i(m)=-b_i\sum_vm_v\log\frac{m_v}{M_ip_i(v)}$, where $m_v$ is the mass in cell $(i,v)$ and $M_i=\sum_vm_v$.
\end{itemize}
Total welfare is then $W(\mu)=-\sum_ib_iM_i(\mu)\KL(\mu_i\|p_i)$, so by \cref{arb:prop:dual} its maximum is $-A$. The interesting part is what the prices mean.

**Humanized**

\paragraph{Construction.} Let the questions be built from atomic events $X_1,\dots,X_k$.
\begin{itemize}
\item Suppose there is a source node with one unit of probability mass, and passing mass forward along an edge corresponds to marginalizing out the node at the tail of the edge. Each internal node of a routing tree corresponds to a partial assignment of the atoms in the routing problem, and the routing shares at a node correspond to the conditional probabilities $P(X_d\mid X_{<d})$.
\item Logical constraints are \emph{missing edges}: a world that violates the relation between the questions has no path leading to it.
\item Each leaf (a complete world $\omega$) sends one copy of its mass to the cell $(i,\phi_i(\omega))$ of every question that is not voided in $\omega$, like a refinery producing several outputs from one input. Cell $(i,v)$ thus receives $\mu(\phi_i=v)$.
\item Consumer $i$ owns the cells of question $x_i$ and has utility $u_i(m)=-b_i\sum_vm_v\log\frac{m_v}{M_ip_i(v)}$, where $m_v$ is the mass in cell $(i,v)$ and $M_i=\sum_vm_v$.
\end{itemize}
Total welfare is then $W(\mu)=-\sum_ib_iM_i(\mu)\KL(\mu_i\|p_i)$, so by \cref{arb:prop:dual} its maximum is $-A$. The prices can be interpreted as follows.

**Final (meaning-corrected)**

\paragraph{Construction.} Let the questions be built from atomic events $X_1,\dots,X_k$.
\begin{itemize}
\item Suppose there is a source node with one unit of probability mass. Each internal node corresponds to a partial assignment of the atoms, and the routing shares at a node correspond to the conditional probabilities $P(X_d\mid X_{<d})$, so passing mass forward along the edges is just marginalization.
\item Logical constraints are encoded by \emph{missing edges}: there is simply no path to a world that breaks the relation between the questions.
\item Every leaf, i.e.\ every complete world $\omega$, passes a copy of its mass on to the cell $(i,\phi_i(\omega))$ for each question that is not voided in $\omega$; one input yields several outputs, as in a refinery. Cell $(i,v)$ thus receives $\mu(\phi_i=v)$.
\item Consumer $i$ owns the cells of question $x_i$ and has utility $u_i(m)=-b_i\sum_vm_v\log\frac{m_v}{M_ip_i(v)}$, where $m_v$ is the mass in cell $(i,v)$ and $M_i=\sum_vm_v$.
\end{itemize}
Total welfare is then $W(\mu)=-\sum_ib_iM_i(\mu)\KL(\mu_i\|p_i)$, so by \cref{arb:prop:dual} its maximum is $-A$. The prices can be interpreted as follows.

*Note:* Bullets 2-3 reworded by hand (StealthGPT variants unusable).


## Unit 26 — chapters/arbitrage.tex

**Original**

\begin{theorem}[world prices are arbitrage profits]\label{arb:thm:deep}
In this market:
\begin{enumerate}
\item the price of leaf $\omega$ is $a_\omega=\sum_ib_i\log\frac{p_i(\phi_i\omega)}{\mu_i(\phi_i\omega)}$ (voided questions contribute nothing), which is minus the profit an arbitrageur makes in world $\omega$ by moving every price to $\mu$'s marginals;
\item the price of an internal node is the share-weighted average of its children's prices, i.e.\ minus the arbitrageur's expected profit given that partial scenario;
\item at the welfare maximum, the question marginals are the arbitraged forecasts, and the arbitrageur's profit equals $A$ in every world that receives mass and is at least $A$ in every other world.
\end{enumerate}
\end{theorem}

**Humanized**

\begin{theorem}[world prices are arbitrage profits]\label{arb:thm:deep}
In this market:
\begin{enumerate}
\item the price of leaf $\omega$ is $a_\omega=\sum_ib_i\log\frac{p_i(\phi_i\omega)}{\mu_i(\phi_i\omega)}$ (voided questions contribute nothing), which is minus the profit an arbitrageur makes in world $\omega$ by moving every price to $\mu$'s marginals;
\item the price of an internal node is the share-weighted average of its children's prices, i.e.\ minus the arbitrageur's expected profit given that partial scenario;
\item at the welfare maximum, the question marginals are the arbitraged forecasts, and the arbitrageur's profit equals $A$ in every world that receives mass and is at least $A$ in every other world.
\end{enumerate}
\end{theorem}


## Unit 27 — chapters/arbitrage.tex

**Original**

\begin{proof}[Proof sketch]
(1) Differentiating $u_i$ with respect to $m_v$ gives $-b_i\log\frac{m_v}{M_ip_i(v)}=b_i\log\frac{p_i(v)}{\mu_i(v)}$, and a leaf's price is the sum of the prices of the cells it supplies. (2) An internal node only passes mass on, so price recursion (\cref{agency:eq:adjoint-b}) makes its price the share-weighted average of its children's. (3) Each $u_i$ is homogeneous of degree one in the masses, so $W=\sum_\omega\mu(\omega)a_\omega$ is minus the expected profit. The optimality conditions for maximizing $W$ over $\simplex(\Omega)$ say that $a_\omega$ is the same on the support of $\mu$ and no larger elsewhere; since $\max W=-A$, that common value is $-A$.
\end{proof}

**Humanized**

\begin{proof}[Proof sketch]
(1) Differentiating $u_i$ with respect to $m_v$ gives $-b_i\log\frac{m_v}{M_ip_i(v)}=b_i\log\frac{p_i(v)}{\mu_i(v)}$. The price of a leaf is the sum of the prices of the cells for which it is the supplier. (2) For an internal node, price recursion (\cref{agency:eq:adjoint-b}) implies that its price is given by the share-weighted average of its children's prices, since it passes mass on without transformation. (3) Since $u_i$ is homogeneous of degree one in the masses, $W=\sum_\omega\mu(\omega)a_\omega$ is minus the expected profit. The optimality conditions for maximizing $W$ over $\simplex(\Omega)$ say that $a_\omega$ is the same on the support of $\mu$ and no larger elsewhere; since $\max W=-A$, that common value is $-A$.
\end{proof}


## Unit 28 — chapters/arbitrage.tex

**Original**

The global arbitrageur of \cref{cfc:def:arbitrage} solves one max--min problem over all worlds at once. The deep market splits it among \emph{local} arbitrageurs: each node sees only its children's prices, and price recursion makes the local arbitrage add up to the global one. A small consequence is worth recording. A complete set of conditional forecasts is a joint forecast, by the chain rule for KL divergence, so the conditional-probability check of \cref{ch:consistency} reduces to a paraphrase check between the implied product $F(P)F(Q\mid P)$ and the direct forecast $F(P\wedge Q)$. This explains why that check has a closed form.

**Humanized**

In \cref{cfc:def:arbitrage}, the global arbitrageur solves a max-min problem over all worlds at once. The deep market distributes arbitrage opportunities among arbitrageurs. These arbitrageurs are identified as \emph{local} in this section. Each arbitrageur only has access to prices in her subtree. Arbitrage opportunities at each node are recursive and aggregate up to give global arbitrage opportunities. A complete set of conditional forecasts is a joint forecast, by the chain rule for KL divergence, so the conditional-probability check of \cref{ch:consistency} reduces to a paraphrase check between the implied product $F(P)F(Q\mid P)$ and the direct forecast $F(P\wedge Q)$. In particular, this explains why the sanity check above has a closed form.

**Final (meaning-corrected)**

In \cref{cfc:def:arbitrage}, the global arbitrageur solves a max--min problem over all worlds at once. The deep market distributes this problem among arbitrageurs, which we call \emph{local}: each one only has access to the prices of its children. Arbitrage at each node is computed recursively, and price recursion makes it add up to the global arbitrage. A complete set of conditional forecasts is a joint forecast, by the chain rule for KL divergence, so the conditional-probability check of \cref{ch:consistency} reduces to a paraphrase check between the implied product $F(P)F(Q\mid P)$ and the direct forecast $F(P\wedge Q)$. In particular, this explains why the conditional-probability check has a closed form.

*Note:* Narrow fix of StealthGPT output ("subtree", referent of "that check", role of price recursion).


## Unit 29 — chapters/arbitrage.tex

**Original**

Markets over dependent questions are not new: combinatorial prediction markets \citep{hansonCombinatorialInformationMarket2003} and the Bayesian-network market maker deployed as SciCast \citep{laskeyGraphicalModelMarket2018} maintain a joint distribution over related events, and \citet{frongilloConvergenceAnalysisPrediction2015} analyse trader dynamics as coordinate descent on an infimal convolution. What the economic view adds is the identification of welfare with minus the arbitrage metric and of world prices with arbitrage profits, together with a decomposition in which separately owned nodes act on local prices alone.

**Humanized**

Another approach to tackling the problem of dependent questions are combinatorial prediction markets. These include combinatorial prediction markets \citep{hansonCombinatorialInformationMarket2003} and a Bayesian-network market maker that was deployed as SciCast \citep{laskeyGraphicalModelMarket2018}. Trader dynamics in these markets have been analyzed, e.g. in \citet{frongilloConvergenceAnalysisPrediction2015}, where it is shown that in some cases the traders perform coordinate descent on an infimal convolution. The decomposition can be interpreted as a deep market, in which nodes owned by different entities optimize based on local prices only. In such a market, arbitrage profits correspond to prices on the world graph, and welfare is minus the arbitrage metric.

**Final (meaning-corrected)**

Markets over dependent questions are not new. Combinatorial prediction markets \citep{hansonCombinatorialInformationMarket2003} and the Bayesian-network market maker that was deployed as SciCast \citep{laskeyGraphicalModelMarket2018} maintain a joint distribution over related events, and trader dynamics in such markets have been analysed by \citet{frongilloConvergenceAnalysisPrediction2015} as coordinate descent on an infimal convolution. What the economic view adds is the identification of welfare with minus the arbitrage metric and of world prices with arbitrage profits, together with a decomposition in which nodes owned by different entities optimize based on local prices only.

*Note:* Restored 'not new' framing, the joint-distribution clause and 'what the economic view adds'; removed duplicated phrase and added 'in some cases' hedge.


## Unit 30 — chapters/arbitrage.tex

**Original**

Now take the terminal consumers to be nature's resolutions rather than forecasters. In the latent-class market proposed by \citet{tailcalledLatentVariablesPrediction2023}, traders move the parameters of a latent-class model and are paid by the change in log-likelihood of the indicators once they resolve. We can build this as a deep market:
\begin{itemize}
\item the source routes mass to the latent classes $Z=j$, with shares $P(Z=j)$;
\item each class copies its mass to one router per indicator, since copying mass is exactly conditional independence;
\item router $(j,i)$ splits its mass according to $P(Y_i\mid Z=j)$;
\item for each observed data point $y^d$, the pieces are recombined, and merging over the classes delivers to consumer $d$ the mass $P(y^d)$, which it values at $\log P(y^d)$.
\end{itemize}

**Humanized**

Another interpretation is obtained if we let the terminal consumers be Nature instead of forecaster agents. The latent-class market \citet{tailcalledLatentVariablesPrediction2023}, uses latent-class models to describe the market. Traders make predictions by making moves to the parameters of a latent-class model. They are rewarded with a fraction of the increase in log-likelihood of the indicators when their moves are revealed to be correct.
\begin{itemize}
\item specifies how mass is routed to $Z=j$, according to $P(Z=j)$;
\item copies its mass to one router per indicator (copying mass is conditional independence);
\item router $(j,i)$ splits its mass according to $P(Y_i\mid Z=j)$;
\item for each observed data point $y^d$, the pieces are recombined, and merging over the classes delivers to consumer $d$ the mass $P(y^d)$, which it values at $\log P(y^d)$.
\end{itemize}

**Final (meaning-corrected)**

A different construction is obtained if we let the terminal consumers be nature's resolutions instead of forecasters. In the latent-class market proposed by \citet{tailcalledLatentVariablesPrediction2023}, traders make moves to the parameters of a latent-class model and are paid by the change in log-likelihood of the indicators once they resolve. We can build this as a deep market:
\begin{itemize}
\item the source routes mass to the latent classes $Z=j$, according to the shares $P(Z=j)$;
\item each class copies its mass to one router per indicator (copying mass is exactly conditional independence);
\item router $(j,i)$ splits its mass according to $P(Y_i\mid Z=j)$;
\item for each observed data point $y^d$, the pieces are recombined, and merging over the classes delivers to consumer $d$ the mass $P(y^d)$, which it values at $\log P(y^d)$.
\end{itemize}

*Note:* Fixed payment rule (change in log-likelihood, not a fraction paid when moves are 'correct'), restored the deep-market lead-in and the item subjects (source, each class), and restored 'exactly'.


## Unit 31 — chapters/arbitrage.tex

**Original**

Two things follow (both checked numerically to $10^{-12}$). First, the price of latent class $j$ is a likelihood ratio,
\[
a_{Z=j}=\sum_d\frac{P(y^d\mid Z=j)}{P(y^d)},
\]
and the revenue on an edge, mass times price, is the posterior probability of that edge. Price recursion is here the backward pass of the forward--backward algorithm. Second, the simplest adaptive rule a router could follow, ``next period, route in proportion to the revenue each buyer paid you'' (proportional response dynamics, \citealt{birnbaum2011}), is \emph{exactly} the EM algorithm \citep{dempsterMaximumLikelihoodIncomplete1977}, step by step. For instance, the shares of the source update to $P(Z=j)\,a_{Z=j}/N=\frac1N\sum_dP(Z=j\mid y^d)$, which is the EM update of the class weights. The exponential rule \eqref{agency:eq:mwu} is mirror ascent on the same log-likelihood.

**Humanized**

The following two statements are true (checked numerically to $10^{-12}$). The price of latent class $j$ is calculated as a likelihood ratio,
\[
a_{Z=j}=\sum_d\frac{P(y^d\mid Z=j)}{P(y^d)},
\]
In this case, prices times masses on the edges correspond to posterior probabilities, and the price recursion is the backward pass of the forward backward algorithm. Second, the simplest adaptive rule a router could follow, ``next period, route in proportion to the revenue each buyer paid you'' (proportional response dynamics, \citealt{birnbaum2011}), is \emph{exactly} the EM algorithm \citep{dempsterMaximumLikelihoodIncomplete1977}, step by step. As an example, consider that the shares of the source update to $P(Z=j)\,a_{Z=j}/N=\frac1N\sum_dP(Z=j\mid y^d)$, the EM update of the class weights. The exponential rule~\eqref{agency:eq:mwu} can be thought of as mirror ascent on the same log-likelihood.

**Final (meaning-corrected)**

Two things follow (both checked numerically to $10^{-12}$). First, the price of latent class $j$ is calculated as a likelihood ratio,
\[
a_{Z=j}=\sum_d\frac{P(y^d\mid Z=j)}{P(y^d)},
\]
and the revenue on each edge, mass times price, is the posterior probability of that edge; the price recursion is here the backward pass of the forward--backward algorithm. Second, the simplest adaptive rule a router could follow, ``next period, route in proportion to the revenue each buyer paid you'' (proportional response dynamics, \citealt{birnbaum2011}), is \emph{exactly} the EM algorithm \citep{dempsterMaximumLikelihoodIncomplete1977}, step by step. As an example, the shares of the source update to $P(Z=j)\,a_{Z=j}/N=\frac1N\sum_dP(Z=j\mid y^d)$, which is the EM update of the class weights. The exponential rule~\eqref{agency:eq:mwu} is mirror ascent on the same log-likelihood.

*Note:* Fixed broken sentence after display and restored 'First'; restored forward--backward dash; 'can be thought of as' restored to 'is'.


## Unit 32 — chapters/arbitrage.tex

**Original**

The lesson is that \textbf{latent variables are intermediate goods}. They never resolve and have no consumer of their own, yet they have a price, derived entirely from the downstream consumers, just as a factory input is priced by the goods it helps make. Depth in a prediction market means intermediate goods, and the architecture of the market (here a latent-class model rather than a full tree) plays the role of the economy's technology.

**Humanized**

The lesson is that \textbf{latent variables are intermediate goods}. They never resolve and have no consumer of their own, yet they have a price, derived entirely from the downstream consumers, just as a factory input is priced by the goods it helps make. Depth in a prediction market means intermediate goods, and the architecture of the market (here a latent-class model rather than a full tree) plays the role of the economy's technology.


## Unit 33 — chapters/arbitrage.tex

**Original**

This answers one half of the question raised in \cref{intro:sec:subjective}. Price recursion does value latent beliefs, and a market of local, self-interested routers can learn them. The other half remains: many different latent models fit the same observables, and the market's prices for latent states only mean something if the latent structure itself is pinned down. The rest of the chapter takes up that problem.

**Humanized**

This answers one half of the question raised in \cref{intro:sec:subjective}. Price recursion does value latent beliefs, and a market of local, self-interested routers can learn them. The other half remains: many different latent models fit the same observables, and the market's prices for latent states only mean something if the latent structure itself is pinned down. The rest of the chapter takes up that problem.

**Final (meaning-corrected)**

This addresses one half of the question posed in \cref{intro:sec:subjective}. Price recursion does put a value on latent beliefs, and a market of local, self-interested routers can learn these beliefs. But this is only half the problem. There are many different latent models that can produce the same observables, and the market's prices for latent states are only meaningful if the latent structure itself is pinned down. We take up this issue in the remainder of the chapter.

*Note:* StealthGPT output itself was flagged; fresh StealthGPT variant, with an invented causal link removed.


## Unit 34 — chapters/arbitrage.tex

**Original**

A probability for an observable gets its meaning from a proper scoring rule applied to the outcome. A belief about a latent variable never meets an outcome. What, then, makes one latent structure for observables $Y_1,\dots,Y_n$ better than another, and in what sense can latent beliefs be elicited at all?

**Humanized**

Note that this interpretation is possible because probabilities of observables have a natural interpretation in terms of a scoring rule against Nature, while beliefs on latent variables have no such direct confrontation with Nature. how are latent beliefs about observables $Y_1,\dots,Y_n$ elicited, and how can one latent structure be said to be better than another?

**Final (meaning-corrected)**

Probabilities of observables have a natural interpretation in terms of a proper scoring rule applied to the outcome, while beliefs about latent variables have no such direct confrontation with an outcome. How, then, can one latent structure for observables $Y_1,\dots,Y_n$ be said to be better than another, and in what sense can latent beliefs be elicited at all?

*Note:* Removed invented causal claim ('this interpretation is possible because'), fixed lowercase sentence start and 'latent beliefs about observables'.


## Unit 35 — chapters/arbitrage.tex

**Original**

A latent structure is a DAG $\mathcal G$ over hidden nodes $H$ and observed nodes $Y$, and a latent model $\theta$ specifies one conditional table $p_\theta(v\mid\pa_v)$ per node. Two common examples are a single latent $Z$ with the indicators as its children (latent class analysis, or item response theory when $Z$ is continuous), and hierarchical models $Z\to Z_j\to Y_i$. The model predicts $m_\theta(y)=\sum_hp_\theta(h,y)$, and under any proper scoring rule its expected score depends on $\theta$ only through $m_\theta$. So a latent means exactly what it does to predictions of observables; no scoring rule can reward anything else. Two latent models with the same $m_\theta$ are indistinguishable to every score, but there are two quite different ways for this to happen.

**Humanized**

A latent structure is a DAG $\mathcal G$ over hidden nodes $H$ and observed nodes $Y$, and a latent model $\theta$ specifies one conditional table $p_\theta(v\mid\pa_v)$ per node. Two common examples are a single latent $Z$ with the indicators as its children (latent class analysis, or item response theory when $Z$ is continuous), and hierarchical models $Z\to Z_j\to Y_i$. The model predicts $m_\theta(y)=\sum_hp_\theta(h,y)$, and under any proper scoring rule its expected score depends on $\theta$ only through $m_\theta$. Beliefs about latents only have meaning through predictions they imply about observables, and should be rewarded by any corresponding proper scoring rule. If two latent models share the same $m_\theta$, then no score can tell them apart. But there are two rather different ways this might be so.

**Final (meaning-corrected)**

A latent structure is a DAG $\mathcal G$ over hidden nodes $H$ and observed nodes $Y$, and a latent model $\theta$ specifies one conditional table $p_\theta(v\mid\pa_v)$ per node. Two common examples are a single latent $Z$ with the indicators as its children (latent class analysis, or item response theory when $Z$ is continuous), and hierarchical models $Z\to Z_j\to Y_i$. The model predicts $m_\theta(y)=\sum_hp_\theta(h,y)$, and under any proper scoring rule its expected score depends on $\theta$ only through $m_\theta$. Beliefs about latents only have meaning through predictions they imply about observables, and that is all a scoring rule can reward. If two latent models share the same $m_\theta$, then no score can tell them apart. But there are two rather different ways this might be so.

*Note:* Narrow fix of StealthGPT output: only the normative "should be rewarded" sentence corrected.


## Unit 36 — chapters/arbitrage.tex

**Original**

To see them, describe a latent model by its \emph{mixing measure}. For each latent state $z$, write down its \emph{profile}, the list of what each indicator would do in that state:
\[
\rho(z)=\big(P(Y_1\mid Z=z),\dots,P(Y_n\mid Z=z)\big).
\]
With binary indicators a profile is a point in the cube $[0,1]^n$. The mixing measure $\nu$ puts mass $P(Z=z)$ on the point $\rho(z)$, and the model's prediction is the $\nu$-weighted average of the corresponding independent distributions, $P(Y)=\int\rho_1\otimes\cdots\otimes\rho_n\,d\nu(\rho)$. A two-state latent class model is two weighted points in the cube; a one-factor IRT model is a curve in the cube, traced out as the factor varies, with a Gaussian spreading mass along it. The \emph{name} of a latent state never appears in $\nu$, only its profile does.

**Humanized**

They are described by saying: here is a latent model \emph{mixing measure}. For each latent state $z$, write down its \emph{profile}, the list of what each indicator would do in that state:
\[
\rho(z)=\big(P(Y_1\mid Z=z),\dots,P(Y_n\mid Z=z)\big).
\]
If only binary indicators are used, each profile may be regarded as a point in the cube $[0,1]^n$. The mixing measure $\nu$ puts mass $P(Z=z)$ on the point $\rho(z)$, and the model's prediction is the $\nu$-weighted average of the corresponding independent distributions, $P(Y)=\int\rho_1\otimes\cdots\otimes\rho_n\,d\nu(\rho)$. The two-state latent class model corresponds to two points in the cube, with weights. The one-factor IRT model corresponds to a curve in the cube (traced out as the factor varies), with a Gaussian spreading out mass along that curve. The fact that the two models can generate the same distributions doesn't mean that they're the same model in disguise, with some tricky relabelling of parameters. The \emph{name} of a latent state never appears in $\nu$, only its profile does.

**Final (meaning-corrected)**

To see them, describe a latent model by its \emph{mixing measure}. For each latent state $z$, write down its \emph{profile}, the list of what each indicator would do in that state:
\[
\rho(z)=\big(P(Y_1\mid Z=z),\dots,P(Y_n\mid Z=z)\big).
\]
If only binary indicators are used, each profile is a point in the cube $[0,1]^n$. The mixing measure $\nu$ puts mass $P(Z=z)$ on the point $\rho(z)$, and the model's prediction is the $\nu$-weighted average of the corresponding independent distributions, $P(Y)=\int\rho_1\otimes\cdots\otimes\rho_n\,d\nu(\rho)$. A two-state latent class model corresponds to two weighted points in the cube. A one-factor IRT model corresponds to a curve in the cube (traced out as the factor varies), with a Gaussian spreading out mass along that curve. The \emph{name} of a latent state never appears in $\nu$, only its profile does.

*Note:* Fixed garbled opening sentence and removed an added sentence (with contractions) not in the original.


## Unit 37 — chapters/arbitrage.tex

**Original**

\paragraph{Gauge freedom: the same $\nu$ in different coordinates.} Relabelling the states of a discrete latent, flipping the sign of a continuous factor, or rotating several factors into one another changes which name goes with which point, but leaves the cloud $\nu$ unchanged. (Numerically, rotating a two-factor IRT model by 0.7 radians changes no pattern probability by more than $2\times10^{-8}$, the quadrature error.) This kind of freedom is harmless. Every statement that survives it is a statement about $\nu$, and such statements are \emph{relational}: ``with probability 0.3 the world is in a state in which indicator 1 has probability above 0.8''. A coordinate statement such as ``$Z>1$'' acquires meaning only once the coordinates have been fixed by convention.

**Humanized**

\paragraph{Gauge freedom: the same $\nu$ in different coordinates.} Relabelling the states of a discrete latent, flipping the sign of a continuous factor, or rotating several factors into one another changes which name goes with which point, but leaves the cloud $\nu$ unchanged. (Numerically, rotating a two-factor IRT model by 0.7 radians changes no pattern probability by more than $2\times10^{-8}$, the quadrature error.) But this extra freedom seems to be mostly harmless. Suppose that a certain statement survives this procedure. Then it's a statement about $\nu$, and has the form \emph{relational}, e.g. ``with probability 0.3 the world is in a state in which indicator 1 has probability above 0.8''. The meaning of a coordinate statement such as ``$Z>1$'' depends upon the meaning given to the coordinates by convention.

**Final (meaning-corrected)**

\paragraph{Gauge freedom: the same $\nu$ in different coordinates.} Relabelling the states of a discrete latent, reversing the sign of a continuous factor, or rotating several factors into each other changes the labelling of the points but leaves the cloud $\nu$ unchanged. Rotation of a two-factor IRT model by 0.7 radians numerically does not change any pattern probability by more than $2\times10^{-8}$, the quadrature error. This kind of freedom has no consequences for anything observable. Suppose that a certain statement survives it. Then it is a statement about $\nu$, and statements of this kind are \emph{relational}, e.g. ``with probability 0.3 the world is in a state in which indicator 1 has probability above 0.8''. The meaning of a coordinate statement such as ``$Z>1$'' depends on the meaning given to the coordinates by convention.

*Note:* StealthGPT output itself was flagged; fresh StealthGPT variant, garbled grammar fixed.


## Unit 38 — chapters/arbitrage.tex

**Original**

\paragraph{Genuine underdetermination: a different $\nu$ with the same average.} Two different clouds can average to the same $P(Y)$. These are different claims about the world, not relabellings. Consider a single binary indicator with $P(Y_1=1)=0.5$. In world (a) the indicator's probability is $0.5$ in every state: the outcome is a genuine coin flip. In world (b) it is $0.9$ half of the time and $0.1$ otherwise: the world is in a decisive state, and we simply do not know which. Both predict the same $P(Y_1)$, but the question ``how often is the world in a state in which $Y_1$ is likely?'' has answer $0$ in (a) and $\tfrac12$ in (b). A continuous example: with two Gaussian indicators of correlation $0.5$ and one factor, the loadings $(0.6,0.833)$, $(0.707,0.707)$ and $(0.9,0.556)$ all reproduce $P(Y)$ exactly and score identically, yet the latent carries $0.97$, $0.79$ and $1.26$ bits of information about $Y$ respectively.

**Humanized**

\paragraph{Genuine underdetermination: a different $\nu$ with the same average.} Two different clouds can average to the same $P(Y)$. They're making very different claims about the world. Consider a single binary indicator with $P(Y_1=1)=0.5$. In world (a) the outcome of the indicator is like a coin flip. That is, the probability of $0.5$ is the same no matter what state of nature obtains. In world (b) it is $0.9$ half of the time and $0.1$ otherwise: the world is in a decisive state, and we simply do not know which. Both predict the same $P(Y_1)$, but the question ``how often is the world in a state in which $Y_1$ is likely?'' The correct answer is $0$ in (a) and $\tfrac12$ in (b). For a continuous example, consider two Gaussian indicators of correlation $0.5$ and one factor. The three different loadings $(0.6,0.833)$, $(0.707,0.707)$ and $(0.9,0.556)$ all lead to an exact reproduction of the covariance $P(Y)$ and give rise to the same score distribution. However, the three latent variables contain $0.97$, $0.79$ and $1.26$ bits of information about $Y$, respectively.

**Final (meaning-corrected)**

\paragraph{Genuine underdetermination: a different $\nu$ with the same average.} Two different clouds can average to the same $P(Y)$. They make different claims about the world; they are not relabellings. Consider a single binary indicator with $P(Y_1=1)=0.5$. In world (a) the outcome of the indicator is a genuine coin flip. That is, its probability is $0.5$ no matter what state of nature obtains. In world (b) it is $0.9$ half of the time and $0.1$ otherwise: the world is in a decisive state, and we simply do not know which. Both predict the same $P(Y_1)$, but the correct answer to the question ``how often is the world in a state in which $Y_1$ is likely?'' is $0$ in (a) and $\tfrac12$ in (b). For a continuous example, consider two Gaussian indicators of correlation $0.5$ and one factor. The three different loadings $(0.6,0.833)$, $(0.707,0.707)$ and $(0.9,0.556)$ all reproduce $P(Y)$ exactly and score identically. However, the three latent variables contain $0.97$, $0.79$ and $1.26$ bits of information about $Y$, respectively.

*Note:* Removed wrong 'covariance $P(Y)$', restored 'not relabellings' and 'genuine coin flip', fixed question fragment.


## Unit 39 — chapters/arbitrage.tex

**Original**

How much genuine freedom is left depends on the structure, and more indicators always help. For binary indicators, $P(Y)$ determines exactly the averages $\mathbb E_\nu\big[\prod_{i\in S}\rho_i\big]$ over sets $S$ of \emph{distinct} indicators. With $n$ exchangeable indicators sharing one profile $\rho$ this means the first $n$ moments of $\rho$ are observed, and as $n\to\infty$ they determine $\nu$, which is de Finetti's theorem \citep{definettiPrevisionSesLois1937} seen as a moment problem. \Cref{arb:tab:freedom} summarizes the known cases.

**Humanized**

The amount of true freedom remaining is also a function of structure, so more indicators are always useful. For binary indicators, $P(Y)$ determines exactly the averages $\mathbb E_\nu\big[\prod_{i\in S}\rho_i\big]$ over sets $S$ of \emph{distinct} indicators. With $n$ exchangeable indicators sharing one profile $\rho$ this means the first $n$ moments of $\rho$ are observed, and as $n\to\infty$ they determine $\nu$, which is de Finetti's theorem \citep{definettiPrevisionSesLois1937} seen as a moment problem. \Cref{arb:tab:freedom} summarizes the known cases.

**Final (meaning-corrected)**

The amount of genuine freedom remaining depends on the structure, and more indicators are always useful. For binary indicators, $P(Y)$ determines exactly the averages $\mathbb E_\nu\big[\prod_{i\in S}\rho_i\big]$ over sets $S$ of \emph{distinct} indicators. With $n$ exchangeable indicators sharing one profile $\rho$ this means the first $n$ moments of $\rho$ are observed, and as $n\to\infty$ they determine $\nu$, which is de Finetti's theorem \citep{definettiPrevisionSesLois1937} seen as a moment problem. \Cref{arb:tab:freedom} summarizes the known cases.

*Note:* Removed spurious causal 'so' and 'also'; restored the term 'genuine' freedom.


## Unit 40 — chapters/arbitrage.tex

**Original**

To choose among latent models that fit, we need a criterion beyond fit. Couple a latent to the observables through an \emph{encoder} $q(h\mid y)$, giving the joint $p(h,y)=p(y)\,q(h\mid y)$. Two quantities matter.

**Humanized**

How do we choose the best latent model among models that fit? Couple a latent to the observables through an \emph{encoder} $q(h\mid y)$, giving the joint $p(h,y)=p(y)\,q(h\mid y)$.

**Final (meaning-corrected)**

How do we choose among latent models that fit? We need a criterion beyond fit. Couple a latent to the observables through an \emph{encoder} $q(h\mid y)$, giving the joint $p(h,y)=p(y)\,q(h\mid y)$. Two quantities matter.

*Note:* Restored dropped 'criterion beyond fit' and 'Two quantities matter', which introduces the next paragraphs.


## Unit 41 — chapters/arbitrage.tex

**Original**

The \emph{unexplained dependence} is the distance to the best model with structure $\mathcal G$,
\[
D_{\mathcal G}=\KL\Big(p(h,y)\,\Big\|\,\textstyle\prod_vp(v\mid\pa_v)\Big)\ \ge0,
\]
where the conditionals on the right are those of $p(h,y)$. For one latent $Z$ with the indicators as children this is the conditional total correlation $\TC(Y\mid Z)=\sum_iH(Y_i\mid Z)-H(Y\mid Z)$, which is zero exactly when the indicators are independent given the latent. It is the scoring rule's half of the story: it is the log-score regret, on complete data, of the best model with structure $\mathcal G$.

**Humanized**

The \emph{unexplained dependence} is the distance to the best model with structure $\mathcal G$,
\[
D_{\mathcal G}=\KL\Big(p(h,y)\,\Big\|\,\textstyle\prod_vp(v\mid\pa_v)\Big)\ \ge0,
\]
with the conditional distributions on the right hand side as in $p(h,y)$. For one latent $Z$ with the indicators as children this is the conditional total correlation $\TC(Y\mid Z)=\sum_iH(Y_i\mid Z)-H(Y\mid Z)$, which is zero exactly when the indicators are independent given the latent. It is the scoring rule's half of the story: it is the log-score regret, on complete data, of the best model with structure $\mathcal G$.

**Final (meaning-corrected)**

The \emph{unexplained dependence} is the distance to the best model with structure $\mathcal G$,
\[
D_{\mathcal G}=\KL\Big(p(h,y)\,\Big\|\,\textstyle\prod_vp(v\mid\pa_v)\Big)\ \ge0,
\]
with the conditional distributions on the right-hand side as in $p(h,y)$. For one latent $Z$ with the indicators as children this is the conditional total correlation $\TC(Y\mid Z)=\sum_iH(Y_i\mid Z)-H(Y\mid Z)$, which is zero exactly when the indicators are independent given the latent. It is the scoring rule's half of the story: it is the log-score regret, on complete data, of the best model with structure $\mathcal G$.

*Note:* Hyphenated 'right-hand side'.


## Unit 42 — chapters/arbitrage.tex

**Original**

Unexplained dependence alone cannot be the criterion, because it accepts a trivial latent. Take $Z=(Y_1,\dots,Y_n)$: every indicator is a function of it, so it explains all dependence perfectly. What rules this out is the \emph{information cost} $I(H;Y)$, the number of bits the latent carries about the observables. The trivial latent costs $H(Y)$ bits, the maximum possible. A good latent explains a lot of dependence with few bits.

**Humanized**

Unexplained dependence is not enough. This criterion is satisfied by the trivial latent variable. Take $Z=(Y_1,\dots,Y_n)$: every indicator is a function of it, so it explains all dependence perfectly. This is ruled out by \emph{information cost} $I(H;Y)$, since the latent cannot carry more information about the observables than the number of bits it consists of. The trivial latent costs $H(Y)$ bits, the maximum possible. A good latent variable should explain a lot of dependence but be describable with few bits.

**Final (meaning-corrected)**

Unexplained dependence is not enough. This criterion is satisfied by the trivial latent variable. Take $Z=(Y_1,\dots,Y_n)$: every indicator is a function of it, so it explains all dependence perfectly. This is ruled out by the \emph{information cost} $I(H;Y)$, the number of bits of information the latent carries about the observables. The trivial latent costs $H(Y)$ bits, the maximum possible. A good latent variable should explain a lot of dependence but carry few bits.

*Note:* Narrow fix of StealthGPT output: only the wrong definition of information cost corrected.


## Unit 43 — chapters/arbitrage.tex

**Original**

Trading the two off with a weight $\tau\in[0,1)$ gives, for a single latent, the objective
\begin{equation}\label{arb:eq:bottleneck}
\mathcal L_\tau(Z)=I(Z;Y)-\tau\sum_iI(Z;Y_i),
\end{equation}
which up to a constant and a positive factor equals $I(Z;Y)+\beta\,\TC(Y\mid Z)$ with $\beta=\tau/(1-\tau)$. In words: compress the observables jointly, while staying informative about each of them separately. We call it the \emph{latent bottleneck}. It contains several familiar objects as special or limiting cases. As $\tau\to1$ it asks for an exact fit with the fewest bits, which is Wyner's common information \citep{wynerCommonInformationTwo1975,gastparRelaxedWynersCommon2019}. At $\tau=1$ with the number of latent states fixed, it is maximum likelihood, as computed by EM, and it is related to correlation explanation \citep{versteegDiscoveringStructureHighdimensional2014}.

**Humanized**

Trading the two off with a weight $\tau\in[0,1)$ gives, for a single latent, the objective $\boldsymbol{ ext{argmin}_{ heta} \; - ext{log} p(z_i|X_{-i}, heta) + M_1 \; ext{KL} [q(z_i|X_{-i}) || p(z_i| heta)]}$
\begin{equation}\label{arb:eq:bottleneck}
\mathcal L_\tau(Z)=I(Z;Y)-\tau\sum_iI(Z;Y_i),
\end{equation}
which up to a constant and a positive factor equals $I(Z;Y)+\beta\,\TC(Y\mid Z)$ with $\beta=\tau/(1-\tau)$. Put another way, compress the observables jointly, while remaining informative about the observables separately. We call it the \emph{latent bottleneck}. This has some of the quantities we have seen as special/limiting cases. As $\tau\to1$ it asks for an exact fit with the fewest bits, which is Wyner's common information \citep{wynerCommonInformationTwo1975,gastparRelaxedWynersCommon2019}. At $\tau=1$ with the number of latent states fixed, it is maximum likelihood, as computed by EM, and it is related to correlation explanation \citep{versteegDiscoveringStructureHighdimensional2014}.

**Final (meaning-corrected)**

Trading the two off with a weight $\tau\in[0,1)$ gives, for a single latent, the objective
\begin{equation}\label{arb:eq:bottleneck}
\mathcal L_\tau(Z)=I(Z;Y)-\tau\sum_iI(Z;Y_i),
\end{equation}
which up to a constant and a positive factor equals $I(Z;Y)+\beta\,\TC(Y\mid Z)$ with $\beta=\tau/(1-\tau)$. Put another way, compress the observables jointly, while remaining informative about the observables separately. We call it the \emph{latent bottleneck}. It contains several familiar objects as special or limiting cases. As $\tau\to1$ it asks for an exact fit with the fewest bits, which is Wyner's common information \citep{wynerCommonInformationTwo1975,gastparRelaxedWynersCommon2019}. At $\tau=1$ with the number of latent states fixed, it is maximum likelihood, as computed by EM, and it is related to correlation explanation \citep{versteegDiscoveringStructureHighdimensional2014}.

*Note:* Removed injected garbage math span (argmin/KL with broken \t) and restored 'several familiar objects as special or limiting cases'.


## Unit 44 — chapters/arbitrage.tex

**Original**

It also contains the \emph{information bottleneck} \citep{tishbyInformationBottleneckMethod1999}. There one is handed $Y_1$ and wants to predict $Y_2$, and builds a summary $T$ computed from $Y_1$ alone. A latent is not computed from any one observable: it is a hidden common cause that can only be inferred. If a patient's disease status is the latent and two noisy tests are the indicators, neither test alone determines the latent, and the encoder must look at both. If we restrict the latent bottleneck to encoders that ignore $Y_2$, then $I(Z;Y_1,Y_2)=I(Z;Y_1)$ and $\TC(Y\mid Z)=I(Y_1;Y_2)-I(Z;Y_2)$, and the objective becomes $I(Y_1;Z)-\beta\,I(Z;Y_2)$, the information bottleneck. So the information bottleneck is the latent bottleneck restricted to latents readable from one side, and lifting the restriction makes latents strictly cheaper. For two bits that agree 90\% of the time, the cheapest exact explanation computable from $Y_1$ is $Y_1$ itself, at one bit, while a free latent needs only $0.873$ bits, which is Wyner's closed form.

**Humanized**

It also contains the \emph{information bottleneck} \citep{tishbyInformationBottleneckMethod1999}. There is given $Y_1$ and one wants to predict $Y_2$. A summary $T$ is made which is computed from $Y_1$ only. For instance, take two noisy tests for a disease, where the disease is a latent variable. Neither of the two tests pinpoints the disease, and thus the encoder would have to receive both measurements in order to make its guess. If we further constrain the latent bottleneck by considering only encoders that do not make use of $Y_2$, then $I(Z;Y_1,Y_2)=I(Z;Y_1)$ and $\TC(Y\mid Z)=I(Y_1;Y_2)-I(Z;Y_2)$, the objective becomes $I(Y_1;Z)-\beta\,I(Z;Y_2)$, the information bottleneck. The information bottleneck is a special case of the latent bottleneck where we restrict ourselves to latent variables that can be read off from only one side. For two bits that agree 90\% of the time, the cheapest exact explanation computable from $Y_1$ is $Y_1$ itself, at one bit, while a free latent needs only $0.873$ bits, which is Wyner's closed form.

**Final (meaning-corrected)**

It also contains the \emph{information bottleneck} \citep{tishbyInformationBottleneckMethod1999}. There one is handed $Y_1$ and wants to predict $Y_2$, and builds a summary $T$ computed from $Y_1$ alone. As an example, in medical diagnosis, suppose that the latent variable is the patient's disease status and there are two (noisy) indicators, given by the results of two different tests. In this case, the latent variable (disease status) cannot be computed from either of the observable variables (test results), but is their common (hidden) cause, and can only be inferred. In other words, the encoder cannot ignore either of the observable variables. If we further constrain the latent bottleneck by considering only encoders that do not make use of $Y_2$, then $I(Z;Y_1,Y_2)=I(Z;Y_1)$ and $\TC(Y\mid Z)=I(Y_1;Y_2)-I(Z;Y_2)$, and the objective becomes $I(Y_1;Z)-\beta\,I(Z;Y_2)$, the information bottleneck. The information bottleneck is a special case of the latent bottleneck where we restrict ourselves to latent variables that can be read off from only one side, and lifting that restriction makes the latent strictly cheaper. For two bits that agree 90\% of the time, the cheapest exact explanation computable from $Y_1$ is $Y_1$ itself, at one bit, while a free latent needs only $0.873$ bits, which is Wyner's closed form.

*Note:* Fresh StealthGPT variant for the opening (keeps the hidden-common-cause point); rest is the narrow fix.


## Unit 45 — chapters/arbitrage.tex

**Original**

The latent bottleneck is a property of the whole distribution of $Y$, and it involves an encoder that nobody observes. Remarkably, it can nevertheless be elicited by paying a scoring rule on a single realized outcome. For a latent model $\theta$ and an observation $y$, define the \emph{tempered log score}
\begin{equation}\label{arb:eq:stau}
S_\tau(\theta;y)=\log\sum_h\ \prod_{v\in H}p_\theta(v\mid\pa_v)\prod_{v\in Y}p_\theta(v\mid\pa_v)^{\tau}.
\end{equation}
At $\tau=1$ the sum is $m_\theta(y)$ and $S_1$ is the ordinary log score. For $\tau<1$ each indicator's evidence is counted only to the power $\tau$.

**Humanized**

The latent bottleneck is a property of the whole distribution of $Y$, not of an individual encoder. An encoder is a mechanism we can't observe. Remarkably, it can nevertheless be elicited by paying a scoring rule on a single realized outcome. Let $\theta$ be a latent model, and $y$, the observation. The \emph{tempered log score} is defined as
\begin{equation}\label{arb:eq:stau}
S_\tau(\theta;y)=\log\sum_h\ \prod_{v\in H}p_\theta(v\mid\pa_v)\prod_{v\in Y}p_\theta(v\mid\pa_v)^{\tau}.
\end{equation}
$m_\theta(y)$ is the sum of $\tau=1$ where $S_1$ is the ordinary log score. For $\tau<1$ each indicator's evidence is counted only to the power $\tau$.

**Final (meaning-corrected)**

The latent bottleneck is a property of the whole distribution of $Y$, and it involves an encoder, a mechanism that nobody observes. Remarkably, it can nevertheless be elicited by paying a scoring rule on a single realized outcome. Let $\theta$ be a latent model and $y$ an observation. The \emph{tempered log score} is defined as
\begin{equation}\label{arb:eq:stau}
S_\tau(\theta;y)=\log\sum_h\ \prod_{v\in H}p_\theta(v\mid\pa_v)\prod_{v\in Y}p_\theta(v\mid\pa_v)^{\tau}.
\end{equation}
At $\tau=1$ the sum is $m_\theta(y)$, and $S_1$ is the ordinary log score. For $\tau<1$ each indicator's evidence is counted only to the power $\tau$.

*Note:* Fixed reversed claim 'not of an individual encoder' (the bottleneck does involve the encoder) and garbled 'sum of $\tau=1$' sentence.


## Unit 46 — chapters/arbitrage.tex

**Original**

\begin{theorem}[the tempered log score elicits the latent bottleneck]\label{arb:thm:stau}
For a single latent,
\[
\min_q\ \mathcal L_\tau(q)=-\max_\theta\ \mathbb E_{y\sim p}\,S_\tau(\theta;y)-\tau\sum_iH(Y_i),
\]
where the minimum is over encoders $q(z\mid y)$. The maximizing $\theta$ is the bottleneck-optimal latent model, and its \emph{tempered posterior} $q(z\mid y)\propto p_\theta(z)\prod_ip_\theta(y_i\mid z)^\tau$ is the optimal encoder. The same holds for a general DAG, with the objective $I(H;Y)+(D_H+\tau D_Y)/(1-\tau)$, where $D_{\mathcal G}=D_H+D_Y$ splits the unexplained dependence into the part among hidden nodes and the rest.
\end{theorem}

**Humanized**

\begin{theorem}[the tempered log score elicits the latent bottleneck]\label{arb:thm:stau}
We can expect the cost to be strictly smaller when we allow for latent variables that cannot be read off from a single variable. For a single latent,
\[
\min_q\ \mathcal L_\tau(q)=-\max_\theta\ \mathbb E_{y\sim p}\,S_\tau(\theta;y)-\tau\sum_iH(Y_i),
\]
where the minimum is over encoders $q(z\mid y)$. The maximizing $\theta$ is the bottleneck-optimal latent model, and its \emph{tempered posterior} $q(z\mid y)\propto p_\theta(z)\prod_ip_\theta(y_i\mid z)^\tau$ is the optimal encoder. The same holds for a general DAG, with the objective $I(H;Y)+(D_H+\tau D_Y)/(1-\tau)$, where $D_{\mathcal G}=D_H+D_Y$ splits the unexplained dependence into the part among hidden nodes and the rest.
\end{theorem}

**Final (meaning-corrected)**

\begin{theorem}[the tempered log score elicits the latent bottleneck]\label{arb:thm:stau}
For a single latent,
\[
\min_q\ \mathcal L_\tau(q)=-\max_\theta\ \mathbb E_{y\sim p}\,S_\tau(\theta;y)-\tau\sum_iH(Y_i),
\]
where the minimum is over encoders $q(z\mid y)$. The maximizing $\theta$ is the bottleneck-optimal latent model, and its \emph{tempered posterior} $q(z\mid y)\propto p_\theta(z)\prod_ip_\theta(y_i\mid z)^\tau$ is the optimal encoder. The same holds for a general DAG, with the objective $I(H;Y)+(D_H+\tau D_Y)/(1-\tau)$, where $D_{\mathcal G}=D_H+D_Y$ splits the unexplained dependence into the part among hidden nodes and the rest.
\end{theorem}

*Note:* Removed a sentence the tool inserted into the theorem statement (it belongs to the information-bottleneck paragraph); rest was unchanged.


## Unit 47 — chapters/arbitrage.tex

**Original**

\begin{proof}[Proof (single latent)]
All entropies are under the coupling $p(y)\,q(z\mid y)$.
\emph{Step 1.} Using $I(Z;Y)=H(Z)-H(Z\mid Y)$ and $I(Z;Y_i)=H(Y_i)-H(Y_i\mid Z)$,
\[
\mathcal L_\tau(q)+\tau\textstyle\sum_iH(Y_i)=H(Z)+\tau\sum_iH(Y_i\mid Z)-H(Z\mid Y).
\]
\emph{Step 2.} Each entropy is the best achievable expected log loss: $H(Z)=\min_r\mathbb E[-\log r(Z)]$ and $H(Y_i\mid Z)=\min_{c_i}\mathbb E[-\log c_i(Y_i\mid Z)]$, by Gibbs' inequality. A prior $r$ together with indicator conditionals $c_i$ is exactly a latent model $\theta$, so
\[
\mathcal L_\tau(q)+\tau\textstyle\sum_iH(Y_i)=\min_\theta\ \mathbb E\Big[\log q(z\mid y)-\log r(z)-\tau\sum_i\log c_i(y_i\mid z)\Big].
\]
\emph{Step 3.} Now minimize over $q$ as well and exchange the two minimizations. For fixed $\theta$ the bracket separates over $y$ into $\sum_zq(z\mid y)\big[\log q(z\mid y)-\log a_\theta(z,y)\big]$ with $a_\theta(z,y)=r(z)\prod_ic_i(y_i\mid z)^\tau$. This is minimized by $q\propto a_\theta$, with value $-\log\sum_za_\theta(z,y)=-S_\tau(\theta;y)$.
\end{proof}

**Humanized**

\begin{proof}[Proof (single latent)]
All entropies are taken in the presence of the coupling $p(y)\,q(z\mid y)$.
\emph{Step 1.} Using $I(Z;Y)=H(Z)-H(Z\mid Y)$ and $I(Z;Y_i)=H(Y_i)-H(Y_i\mid Z)$,
\[
\mathcal L_\tau(q)+\tau\textstyle\sum_iH(Y_i)=H(Z)+\tau\sum_iH(Y_i\mid Z)-H(Z\mid Y).
\]
\emph{Step 2.} Each entropy is the best achievable expected log loss: $H(Z)=\min_r\mathbb E[-\log r(Z)]$ and $H(Y_i\mid Z)=\min_{c_i}\mathbb E[-\log c_i(Y_i\mid Z)]$, by Gibbs' inequality. A prior $r$ together with indicator conditionals $c_i$ is exactly a latent model $\theta$, so
\[
\mathcal L_\tau(q)+\tau\textstyle\sum_iH(Y_i)=\min_\theta\ \mathbb E\Big[\log q(z\mid y)-\log r(z)-\tau\sum_i\log c_i(y_i\mid z)\Big].
\]
\emph{Step 3.} Also perform the minimization over $q$ and interchange the minimizations. For fixed $\theta$ the bracket separates over $y$ into $\sum_zq(z\mid y)\big[\log q(z\mid y)-\log a_\theta(z,y)\big]$ with $a_\theta(z,y)=r(z)\prod_ic_i(y_i\mid z)^\tau$. This is minimized by $q\propto a_\theta$, with value $-\log\sum_za_\theta(z,y)=-S_\tau(\theta;y)$.
\end{proof}

**Final (meaning-corrected)**

\begin{proof}[Proof (single latent)]
All entropies are taken with respect to the coupling $p(y)\,q(z\mid y)$.
\emph{Step 1.} Using $I(Z;Y)=H(Z)-H(Z\mid Y)$ and $I(Z;Y_i)=H(Y_i)-H(Y_i\mid Z)$,
\[
\mathcal L_\tau(q)+\tau\textstyle\sum_iH(Y_i)=H(Z)+\tau\sum_iH(Y_i\mid Z)-H(Z\mid Y).
\]
\emph{Step 2.} Each entropy is the best achievable expected log loss: $H(Z)=\min_r\mathbb E[-\log r(Z)]$ and $H(Y_i\mid Z)=\min_{c_i}\mathbb E[-\log c_i(Y_i\mid Z)]$, by Gibbs' inequality. A prior $r$ together with indicator conditionals $c_i$ is exactly a latent model $\theta$, so
\[
\mathcal L_\tau(q)+\tau\textstyle\sum_iH(Y_i)=\min_\theta\ \mathbb E\Big[\log q(z\mid y)-\log r(z)-\tau\sum_i\log c_i(y_i\mid z)\Big].
\]
\emph{Step 3.} Also perform the minimization over $q$ and interchange the minimizations. For fixed $\theta$ the bracket separates over $y$ into $\sum_zq(z\mid y)\big[\log q(z\mid y)-\log a_\theta(z,y)\big]$ with $a_\theta(z,y)=r(z)\prod_ic_i(y_i\mid z)^\tau$. This is minimized by $q\propto a_\theta$, with value $-\log\sum_za_\theta(z,y)=-S_\tau(\theta;y)$.
\end{proof}

*Note:* 'in the presence of the coupling' changed to 'with respect to the coupling'.


## Unit 48 — chapters/arbitrage.tex

**Original**

So $S_\tau$ is the latent bottleneck with the encoder optimized out, written observation by observation. At $\tau=1$ the proof is the familiar identity ``log-likelihood equals the maximized evidence lower bound''. The tempered posterior is known in statistics as a power or fractional posterior, part of the family of generalized Bayesian updates \citep{grunwaldSafeBayesianLearning2012,bissiriGeneralFrameworkUpdating2016}. There the exponent is usually chosen for robustness to misspecification. Here it plays a different role: it is a knob for compression.

**Humanized**

describes the latent bottleneck $S_\tau$ after optimizing out the encoder, written observation by observation. At $\tau=1$ the proof is the familiar identity ``log-likelihood equals the maximized evidence lower bound''. Our tempered posterior $q_\theta(z)\propto a_\theta(z,y)^\tau$ is sometimes called a power/fractional posterior, and falls under the heading of generalised Bayesian updating \citep{grunwaldSafeBayesianLearning2012,bissiriGeneralFrameworkUpdating2016}. Typically $\tau$ is used there as a means of gaining robustness to model misspecification. Here it plays a different role: it is a knob for compression.

**Final (meaning-corrected)**

So $S_\tau$ is the latent bottleneck after optimizing out the encoder, written observation by observation. At $\tau=1$ the proof is the familiar identity ``log-likelihood equals the maximized evidence lower bound''. Our tempered posterior is sometimes called a power/fractional posterior, and falls under the heading of generalized Bayesian updating \citep{grunwaldSafeBayesianLearning2012,bissiriGeneralFrameworkUpdating2016}. There the exponent is typically used as a means of gaining robustness to model misspecification. Here it plays a different role: it is a knob for compression.

*Note:* Fixed fragment start with misplaced $S_\tau$; removed added incorrect formula ($a_\theta^\tau$ double-tempers) and the claim that the literature's exponent is $\tau$.


## Unit 49 — chapters/arbitrage.tex

**Original**

\begin{corollary}[elicitation]\label{arb:cor:elicit}
Pay an agent who reports a latent model $\theta$ the amount $S_\tau(\theta;y)$ once the observables $y$ are realized. If the agent believes $Y\sim p$, its expected payment is maximized exactly by the latent-bottleneck optimum for $p$. The payment needs a single realization and no knowledge of $p$, it is invariant to gauge transformations, and with discrete indicators $S_\tau\le0$, so a market maker's loss is bounded just as for the logarithmic market scoring rule.
\end{corollary}

**Humanized**

\begin{corollary}[elicitation]\label{arb:cor:elicit}
Pay an agent who reports a latent model $\theta$ the amount $S_\tau(\theta;y)$ once the observables $y$ are realized. If the agent believes $Y\sim p$, its expected payment is maximized exactly by the latent-bottleneck optimum for $p$. The payment needs a single realization and no knowledge of $p$, it is invariant to gauge transformations, and with discrete indicators $S_\tau\le0$, so a market maker's loss is bounded just as for the logarithmic market scoring rule.
\end{corollary}


## Unit 50 — chapters/arbitrage.tex

**Original**

\Cref{arb:tab:incentives} shows the incentives in a small case: three binary indicators whose true latent has two states, but which a three-state latent explains with fewer bits.

**Humanized**

\Cref{arb:tab:incentives} shows the incentives in a small case: three binary indicators whose true latent has two states, but which a three-state latent explains with fewer bits.


## Unit 51 — chapters/arbitrage.tex

**Original**

The trade-offs are real. For $\tau<1$ the reported model is a slightly lossy forecast of $Y$ (0.0058 bits of regret at $\tau=0.9$), so its implied indicator probabilities are no longer the agent's best forecasts; taking $\tau$ just below one makes it a tie-breaker only. The value of $\tau$ is the designer's choice, and nothing in the observables determines it. And the optimum is a non-convex, possibly set-valued property, so reporting it requires solving a hard problem. On the practical side, tempered EM (an E-step with the tempered posterior, followed by the usual M-step) increases $\mathbb E\,S_\tau$ at every step and fits any latent DAG, and the same score and algorithm apply to continuous latents (IRT, factor analysis, mixed indicator types, several factors), with integrals computed by quadrature.

**Humanized**

For $\tau<1$ the reported model is a slightly lossy forecast of $Y$ (0.0058 bits of regret at $\tau=0.9$), so its implied indicator probabilities are no longer the agent's best forecasts; taking $\tau$ just below one makes it a tie-breaker only. There is no observable which would allow us to determine $\tau$: this quantity is just a free parameter, to be chosen by the designer. As a practical algorithm, note that an EM-like algorithm where the E-step uses a tempered posterior will monotonically increase $\mathbb E\,S_\tau$ and so could be used to optimise over latent DAGs. Nothing so far assumes discrete latents. Integrals can be computed by quadrature. For example, IRT/factor analysis with mixed discrete/continuous indicators and possibly multiple latent factors. The notion of optimal is set-valued and non-convex, and so hard to compute.

**Final (meaning-corrected)**

The trade-offs are real. For $\tau<1$ the reported model is a slightly lossy forecast of $Y$ (0.0058 bits of regret at $\tau=0.9$), so its implied indicator probabilities are no longer the agent's best forecasts; taking $\tau$ just below one makes it a tie-breaker only. There is no observable which would allow us to determine $\tau$: this quantity is a free parameter, to be chosen by the designer. And the optimum is a non-convex, possibly set-valued property, so reporting it requires solving a hard problem. On the practical side, tempered EM (an EM algorithm whose E-step uses the tempered posterior, followed by the usual M-step) increases $\mathbb E\,S_\tau$ at every step and can be used to fit any latent DAG. The same score and algorithm apply to continuous latents (IRT, factor analysis, mixed indicator types, several factors), with integrals computed by quadrature.

*Note:* 'optimise over latent DAGs' restored to 'fit any latent DAG'; restored 'possibly' set-valued and 'reporting it requires solving a hard problem'; removed added 'nothing so far assumes discrete latents' and fragment.


## Unit 52 — chapters/arbitrage.tex

**Original**

Scoring pins down a latent model exactly to the extent that $m_\theta$ determines $\theta$. For one latent with three or more conditionally independent indicators, the decomposition with the fewest latent states is generically unique up to relabelling \citep{kruskalThreewayArraysRank1977,allmanIdentifiabilityParametersLatent2009}, and the same holds for latent trees in which every hidden node has at least three neighbours. In these cases $\tau=1$ already elicits the true latent, and EM recovers it. Even here, however, parsimony is a convention: uniqueness holds among models with the fewest \emph{states}, and the latent with the fewest \emph{bits} can differ. In exact computations, the least-information latent was cheaper than the true one in all ten random two-indicator models and in all four three-binary-indicator models tried, and equal to it with three ternary indicators or once a fourth indicator was added. More indicators shrink the set of exact fits until the convention stops mattering; we conjecture, on the basis of these computations, that this happens in general once the indicators are rich enough.

**Humanized**

Scoring pins down a latent model exactly to the extent that $m_\theta$ determines $\theta$. For one latent with three or more conditionally independent indicators, the decomposition with the fewest latent states is generically unique up to relabelling \citep{kruskalThreewayArraysRank1977,allmanIdentifiabilityParametersLatent2009}, and the same holds for latent trees in which every hidden node has at least three neighbours. In these cases $\tau=1$ already elicits the true latent, and EM recovers it. Even here, however, parsimony is a convention: uniqueness holds among models with the fewest \emph{states}, and the latent with the fewest \emph{bits} can differ. These results suggest the following conjecture: the two conventions give the same least-information latent once the indicators are rich enough. The reason is that increasing the number of indicators tends to shrink the set of exact fits, so that the convention matters less and less. Our exact computations all bear this out: in all ten random two-indicator models tried the least-information latent was cheaper than the true one, as was the case in all four models with three binary indicators tried; it was equal to the true latent once three ternary indicators or a fourth indicator were present.

**Final (meaning-corrected)**

Scoring pins down a latent model exactly to the extent that $m_\theta$ determines $\theta$. For one latent with three or more conditionally independent indicators, the decomposition with the fewest latent states is generically unique up to relabelling \citep{kruskalThreewayArraysRank1977,allmanIdentifiabilityParametersLatent2009}, and the same holds for latent trees in which every hidden node has at least three neighbours. In these cases $\tau=1$ already elicits the true latent, and EM recovers it. Even here, however, parsimony is a convention: uniqueness holds among models with the fewest \emph{states}, and the latent with the fewest \emph{bits} can differ. In exact computations, the least-information latent was cheaper than the true one in all ten random two-indicator models tried and in all four models with three binary indicators tried, and it was equal to the true latent with three ternary indicators or once a fourth indicator was added. Increasing the number of indicators shrinks the set of exact fits until the convention stops mattering. On the basis of these computations we conjecture that this happens in general once the indicators are rich enough.

*Note:* Restored conjecture content and order: 'more indicators shrink the set of exact fits' is a finding, not the 'reason' for the conjecture; removed 'tends to' and the overclaim that computations 'bear out' the conjecture.


## Unit 53 — chapters/arbitrage.tex

**Original**

When the latent distribution is left free, $\tau<1$ removes the indeterminacy, but only by compressing the latent. For three IRT indicators with a Gaussian latent and fixed link functions, the probability $P(Z>1)$ ranges over $[0.035,0.317]$ among all latent distributions that are optimal at $\tau=1$, over $[0,0.024]$ at $\tau=0.95$, and over $[0,0.002]$ at $\tau=0.8$. The price is that the profiles of the compressed latent shrink towards uninformative ones and its forecasts of the indicators deteriorate (by 0.07 in total variation at $\tau=0.8$). There are thus three ways to pin down a free-form latent: by assumption (a parametric family, which keeps forecasts honest), by data (more indicators, which works but slowly), or by compression ($\tau<1$, at some cost in forecast accuracy). A score can only distinguish what the observables, or an explicitly stated convention, distinguish.

**Humanized**

When the latent distribution is left free, $\tau<1$ removes the indeterminacy, but only by compressing the latent. For three IRT indicators with a Gaussian latent and fixed link functions, $P(Z>1)$ is between $[0.035,0.317]$ for all distributions that are optimal at $\tau=1$, between $[0,0.024]$ for $\tau=0.95$ and between $[0,0.002]$ for $\tau=0.8$. The price is that the profiles of the compressed latent shrink towards uninformative ones and its forecasts of the indicators deteriorate (by 0.07 in total variation at $\tau=0.8$). One could also try to impose a parametric family of latent variable paths as a prior, but this may unduly constrain the forecasts. Adding more indicators could also serve to pin down the free-form latent, but convergence will be slow. Finally, as discussed in ($\tau<1$, one could accept a less accurate forecast in order to allow for the free-form latent to be estimated via compression. A score can only distinguish what the observables, or an explicitly stated convention, distinguish.

**Final (meaning-corrected)**

When the latent distribution is left free, $\tau<1$ removes the indeterminacy, but only by compressing the latent. For three IRT indicators with a Gaussian latent and fixed link functions, the probability $P(Z>1)$ ranges over $[0.035,0.317]$ among all latent distributions that are optimal at $\tau=1$, over $[0,0.024]$ at $\tau=0.95$ and over $[0,0.002]$ at $\tau=0.8$. The price is that the profiles of the compressed latent shrink towards uninformative ones and its forecasts of the indicators deteriorate (by 0.07 in total variation at $\tau=0.8$). There are thus three ways to pin down a free-form latent. One can pin it down by assumption, through a parametric family, which keeps forecasts honest. One can pin it down by data, adding more indicators, which works but slowly. Or one can compress, taking $\tau<1$ and accepting some cost in forecast accuracy. A score can only distinguish what the observables, or an explicitly stated convention, distinguish.

*Note:* Restored the three ways to pin down a latent: humanized reversed the parametric-family point ('may unduly constrain the forecasts' vs 'keeps forecasts honest') and broke the $\tau<1$ sentence.


## Unit 54 — chapters/arbitrage.tex

**Original**

\paragraph{Latent-variable prediction markets.} In the proposal of \citet{tailcalledLatentVariablesPrediction2023} the market state is a latent model, and a trader who moves it from $\phi$ to $\theta$ is paid $\log P(y\mid\theta)-\log P(y\mid\phi)$ on the resolved indicators. This is Hanson's market scoring rule with the score $S_1$, and it works in two respects. Its incentives are sound: a myopic trader moves the market to the model in its family that best forecasts the indicators, and the market maker's loss is bounded. And when the model family identifies the latent up to gauge, the market's latent prices mean something. The design recommended in the proposal (one Gaussian latent standardized to $N(0,1)$, probit links, at least three indicators) is identified up to sign, and its rule of ``at least three indicators'' is exactly right.

**Humanized**

\paragraph{Latent-variable prediction markets.} \citet{tailcalledLatentVariablesPrediction2023} propose a market in which traders can bet on a latent variable, the ``market state'', and if they cause the market state to transition from $\phi$ to $\theta$ they get paid $\log P(y\mid\theta)-\log P(y\mid\phi)$ for all resolved indicators. This is Hanson's market scoring rule with the score $S_1$, and it works in two respects. Incentive compatibility: a myopic trader moves beliefs towards the best forecasting model (within the chosen model family), and the market maker has bounded loss. Meaningful prices for latents, when identifiable up to gauge. The proposal to specify one Gaussian latent standardized to $N(0,1)$, use probit links, and use at least three indicators is a good one. This design is identified up to sign, and the ``at least three indicators'' rule is exactly right.

**Final (meaning-corrected)**

\paragraph{Latent-variable prediction markets.} \citet{tailcalledLatentVariablesPrediction2023} propose a market in which traders bet on a latent-variable model, the ``market state'', and if they cause the market state to transition from $\phi$ to $\theta$ they get paid $\log P(y\mid\theta)-\log P(y\mid\phi)$ for all resolved indicators. This is Hanson's market scoring rule with the score $S_1$, and it works in two respects. Incentive compatibility: a myopic trader moves the market to the best forecasting model (within the chosen model family), and the market maker has bounded loss. Meaningful prices for latents: when the latent is identified up to gauge, its prices mean something. The proposal to specify one Gaussian latent standardized to $N(0,1)$, use probit links, and use at least three indicators is a good one. This design is identified up to sign, and the ``at least three indicators'' rule is exactly right.

*Note:* Narrow fix of StealthGPT output (market state is a latent model; "moves the market to").


## Unit 55 — chapters/arbitrage.tex

**Original**

Three of the design options it discusses are more problematic.
\begin{enumerate}
\item \emph{A free-form latent distribution} (letting traders ``drag around'' the latent distribution). Payouts depend on the latent only through the joint distribution of the indicators. For a Gaussian latent $P(Z>1)=0.156$, but every latent distribution giving the same indicator joint earns identical payouts, and among these $P(Z>1)$ ranges over $[0.040,0.317]$ with three indicators, $[0.078,0.253]$ with six and $[0.087,0.237]$ with ten. Traders can move such beliefs at no expected cost or reward. The remedy is to keep the latent distribution parametric, or to settle with $S_\tau$ and accept the compression.
\item \emph{Several latent factors.} This is not in fact a defect. Rotating the loadings together with the factors changes nothing observable: it is gauge, not missing information. Which axis represents ``who is winning'' is a choice of coordinates, not a fact, so a market cannot price it and should not try. Such quantities should be defined relationally, for example as ``the latent direction along which the probability of indicator 3 rises fastest'', and these are priced whenever the model is identified up to rotation.
\item \emph{User-proposed latent classes.} The log score never penalizes an extra class, since a model with $k+1$ classes contains every model with $k$. A redundant class ties with the true model (the $S_1$ column of \cref{arb:tab:incentives}), and the latent drifts towards being ``the indicators themselves''. Settling with $S_\tau$ for $\tau$ slightly below one makes every proposed class pay for its bits, which answers the proposal's open question of who should choose the number of classes: a class stays exactly when it raises $S_\tau$.
\end{enumerate}
A fourth caveat applies to any such market: if the indicators do not in fact share one cause, the latent the market finds is the best single common cause, a projection, and not a ground truth.

**Humanized**

Three of the design options it discusses are more problematic.
\begin{enumerate}
\item \emph{A free-form latent distribution} allows traders to ``drag around'' the latent distribution. This is not actually a problem: payouts depend on the latent only through the joint distribution of the indicators, which is invariant to simultaneously rotating the loadings and the latent. In the special case where $P(Z>1)=0.156$, is Gaussian, $P(Z>1)$ ranges over $[0.040,0.317]$ if there are three indicators, over $[0.078,0.253]$ if there are six indicators, and over $[0.087,0.237]$ if there are ten indicators. Note that any two latent distributions with the same indicator joint are rewarded equally. One issue raised is that traders are able to influence beliefs about the latent variable in ways that have no effect on payouts, so they can do this at no cost or risk. Otherwise, we either need to accept the compression loss of $S_\tau$ or we need to find some parametric model for the latent distribution.
\item \emph{Several latent factors.} So traders can't profit from guessing which rotation will be used, and the market can't give information about which rotation will be used. The latent is only determined up to rotation, but this shouldn't be thought of as the market lacking some information, because it is more like the distinction between Cartesian and spherical coordinates, and you could only ask about things which are rotationally invariant. For example, you can't ask ``how likely is it that the first latent is winning'', but you can ask about the projection of the latents onto any fixed direction, or things like ``how likely is it that the third indicator will increase the most if you moved in the direction which causes it to increase the fastest'', which are expressible in terms of rotationally-invariant properties of the latents.
\item \emph{User-proposed latent classes.} The log score never penalizes an extra class, since a model with $k+1$ classes contains every model with $k$. In this case the redundant class ends up tied with the true model (the $S_1$ column of \cref{arb:tab:incentives}), and the latent drifts towards being ``the indicators themselves''. Settling with $S_\tau$ for $\tau$ slightly below one makes every proposed class pay for its bits, which answers the proposal's open question of who should choose the number of classes: a class stays exactly when it raises $S_\tau$.
\end{enumerate}
A final comment applies to prediction markets in general: if the indicators aren't actually caused by a common latent, then the true answer won't actually be the ground truth but the best single latent cause which best explains the correlation.

**Final (meaning-corrected)**

Three of the design options it discusses are more problematic.
\begin{enumerate}
\item \emph{A free-form latent distribution} allows traders to ``drag around'' the latent distribution. Payouts depend on the latent only through the joint distribution of the indicators. For a Gaussian latent $P(Z>1)=0.156$, but any two latent distributions with the same indicator joint are rewarded equally, and among these $P(Z>1)$ ranges over $[0.040,0.317]$ if there are three indicators, over $[0.078,0.253]$ if there are six, and over $[0.087,0.237]$ if there are ten. Traders are therefore able to move such beliefs at no expected cost or reward. The remedy is either to find some parametric model for the latent distribution, or to settle with $S_\tau$ and accept the compression.
\item \emph{Several latent factors.} This is not in fact a defect. The axes of the factor space are a matter of gauge freedom, since one can rotate the loadings together with the factors and nothing observable changes. Which axis represents ``who is winning'' is therefore not a fact, and a market cannot price it and should not try to. The right objects to price are relational quantities, like ``the latent direction along which the probability of indicator 3 rises fastest'', which are priced as long as the model is identified up to rotation.
\item \emph{User-proposed latent classes.} The log score never penalizes an extra class, since a model with $k+1$ classes contains every model with $k$. In this case the redundant class ends up tied with the true model (the $S_1$ column of \cref{arb:tab:incentives}), and the latent drifts towards being ``the indicators themselves''. Settling with $S_\tau$ for $\tau$ slightly below one makes every proposed class pay for its bits, which answers the proposal's open question of who should choose the number of classes: a class stays exactly when it raises $S_\tau$.
\end{enumerate}
A fourth caveat applies to any such market: if the indicators are not actually caused by a common latent, then what the market finds will not be the ground truth but a projection, namely the best single common cause.

*Note:* Item 2 (StealthGPT had replaced it with unrelated text) rebuilt from a fresh StealthGPT variant.


## Unit 56 — chapters/arbitrage.tex

**Original**

The criticism one might first make of this proposal, that the choice of latent is a gauge freedom that lets traders bet however they like, is therefore only half right. Pure gauge freedom is harmless, because payouts are gauge-invariant and no trader profits from relabelling. What does leave latent beliefs unpriced is \emph{genuine} underdetermination, which appears exactly in the free-form and user-proposed designs.

**Humanized**

The criticism one might first make of this proposal, that the choice of latent is a gauge freedom that lets traders bet however they like, is therefore only half right. Pure gauge freedom is harmless, because payouts are gauge-invariant and no trader profits from relabelling. Another way to say this is that what \emph{genuine} calls underdetermination, leaving some beliefs latent (unpriced), only happens in the free-form/user-proposed designs.

**Final (meaning-corrected)**

The criticism one might first make of this proposal, that the choice of latent is a gauge freedom that lets traders bet however they like, is therefore only half right. Pure gauge freedom is harmless, because payouts are gauge-invariant and no trader profits from relabelling. Another way to say this is that \emph{genuine} underdetermination, which leaves some latent beliefs unpriced, only happens in the free-form and user-proposed designs.

*Note:* Narrow fix of StealthGPT output (garbled last sentence).


## Unit 57 — chapters/arbitrage.tex

**Original**

\paragraph{Bayesian-network markets.} The combinatorial markets of \citet{sunProbabilityAssetUpdating2012} and \citet{laskeyGraphicalModelMarket2018} allow traders to edit both the parameters and the structure of a Bayesian network, including adding variables. A latent node can certainly be represented. But each trade is paid as an edit to the joint distribution of the variables it touches, settled when those variables resolve. If a trader raises $P(Z)$ while leaving $P(Y\mid Z)$ unchanged, its gain in each state is $b\log\frac{q(Z)}{p(Z)}$, which depends on $Z$ itself; when the observables resolve, the market updates its beliefs about $Z$, but nothing settles that contract. A trader can still profit before settlement by selling once the evidence has moved the price, but no rule pays it for its contribution to the observable predictions if $Z$ never resolves. The latent-variable market avoids this by scoring the change in the \emph{observable} marginal, with $Z$ integrated out, and the deep market of \cref{arb:sec:latent-goods} does the same thing in economic language: the latent node is an intermediate good, and its price is derived from the consumers downstream.

**Humanized**

\paragraph{Bayesian-network markets.} The combinatorial markets of \citet{sunProbabilityAssetUpdating2012} and \citet{laskeyGraphicalModelMarket2018} allow traders to edit both the parameters and the structure of a Bayesian network, including adding variables. A latent node can be represented as well. Each trade can be thought of as a payment made in the form of an edit to the joint distribution of the set of variables it involves, which will be settled once those variables are resolved. Assume that $P(Z)$ goes up, but $P(Y\mid Z)$ does not change. In each state, the trader will gain $b\log\frac{q(Z)}{p(Z)}$, which will depend on $Z$. When the observables are revealed, traders will update their beliefs about $Z$, but nothing is resolved. A trader can still profit before settlement by selling once the evidence has moved the price, but no rule pays it for its contribution to the observable predictions if $Z$ never resolves. The latent-variable market gets around this problem by pricing the change in the marginal of \emph{observable} with $Z$ integrated out. And, sure enough, the deep market of \cref{arb:sec:latent-goods} prices it this way too: the latent node is an intermediate good, and its price is determined from the marginal utility of the downstream consumers.

**Final (meaning-corrected)**

\paragraph{Bayesian-network markets.} The combinatorial markets of \citet{sunProbabilityAssetUpdating2012} and \citet{laskeyGraphicalModelMarket2018} allow traders to edit both the parameters and the structure of a Bayesian network, including adding variables. A latent node can be represented as well. Each trade can be thought of as a payment made in the form of an edit to the joint distribution of the set of variables it involves, which will be settled once those variables are resolved. Assume that a trader raises $P(Z)$, but $P(Y\mid Z)$ does not change. In each state, the trader will gain $b\log\frac{q(Z)}{p(Z)}$, which will depend on $Z$. When the observables are revealed, the market will update its beliefs about $Z$, but the contract on $Z$ is never settled. A trader can still make money before settlement, by selling after the evidence has moved the price; but if $Z$ never resolves, nothing pays the trader for what it contributed to the observable predictions. The latent-variable market gets around this problem by pricing the change in the \emph{observable} marginal, with $Z$ integrated out. And indeed, the deep market of \cref{arb:sec:latent-goods} prices it this way too: the latent node is an intermediate good, and its price is determined by the downstream consumers.

*Note:* Narrow fix of StealthGPT output (who updates, settlement, "observable marginal"); one retained original sentence reworded.


## Unit 58 — chapters/arbitrage.tex

**Original**

This chapter has connected the last part of the thesis to the first. The arbitrage metric used to evaluate forecasters in \cref{ch:consistency} is the welfare gained by a market of quasi-linear consumers, its arbitraged forecasts are that market's equilibrium prices, and the dynamics of \cref{ch:agency} compute them, with price recursion breaking global arbitrage into local arbitrage. The same aggregation rule that makes beliefs consistent makes preferences into a social objective, which turns the utilitarian welfare of \cref{ch:agency} from an assumption into a consequence.

**Humanized**

This concludes our discussion on prediction markets and closes a circle we began in the first chapter of this thesis. The arbitrage metric used to evaluate forecasters in \cref{ch:consistency} is the welfare gained by a market of quasi-linear consumers, its arbitraged forecasts are that market's equilibrium prices, and the dynamics of \cref{ch:agency} compute them, with price recursion breaking global arbitrage into local arbitrage. This shows that the utilitarian social welfare function of \cref{ch:agency} is not an assumption but a consequence of rationality requirements. The aggregation rule that makes beliefs consistent also aggregates preferences into a social objective.

**Final (meaning-corrected)**

This chapter closes a circle, connecting the last part of the thesis to the first. The arbitrage metric used to evaluate forecasters in \cref{ch:consistency} is the welfare gained by a market of quasi-linear consumers, its arbitraged forecasts are that market's equilibrium prices, and the dynamics of \cref{ch:agency} compute them, with price recursion breaking global arbitrage into local arbitrage. The same aggregation rule that makes beliefs consistent also aggregates preferences into a social objective, so the utilitarian social welfare function of \cref{ch:agency} is not an assumption but a consequence.

*Note:* Humanized said 'first chapter' (original: first part) and added 'of rationality requirements'; restored causal order.


## Unit 59 — chapters/arbitrage.tex

**Original**

For latent beliefs, the economic picture says that latent variables are intermediate goods, priced by what they contribute downstream, and that a market of routers following proportional response learns them by EM. The information-theoretic picture says what such beliefs mean: a latent is exactly what it does to predictions of observables, gauge freedom is harmless, and the genuine underdetermination that remains can be resolved by structure, by more indicators, or by asking for the cheapest explanation, which the tempered log score elicits from a single outcome.

**Humanized**

In \cref{ch:latent}, we saw that latent variables are intermediate goods, that markets of routers with proportional response dynamics learn them using EM, and that price recursion determines their price according to their downstream value. From an information-theoretic perspective, latent variables only mean what they do to predictions about observable variables, so some underdetermination is unavoidable (gauge freedom), but the rest is a matter of the structure chosen, the number of indicator variables chosen, or parsimony (the cheapest explanation). We saw that parsimony can be elicited from a single outcome using the tempered log score.

**Final (meaning-corrected)**

For latent beliefs, the economic picture says that latent variables are intermediate goods, priced according to their downstream value, and that markets of routers with proportional response dynamics learn them using EM. From an information-theoretic perspective, a latent variable means exactly what it does to predictions about observable variables, gauge freedom is harmless, and the genuine underdetermination that remains can be resolved by the structure chosen, by more indicator variables, or by parsimony (asking for the cheapest explanation). The cheapest explanation can be elicited from a single outcome using the tempered log score.

*Note:* Removed an added \cref{ch:latent}; humanized claimed underdetermination is unavoidable and conflated gauge with genuine underdetermination.


## Unit 60 — chapters/arbitrage.tex

**Original**

Two gaps remain, and they are the natural next steps. First, the compression weight $\tau$, like the subsidy of a logarithmic market, is chosen by the designer. The conjecture of \cref{intro:sec:subjective} is that both should be set by price recursion, by the downstream value of the information a latent provides relative to the cost of producing it; the results here make the question precise but do not answer it. Second, the hypotheses that humans and AIs actually entertain are not latent-class models but natural-language theories and concepts. Treating an essay or a concept as a latent variable, scored through the predictions a fixed reader makes with it on questions its author never saw, is a direct application of the tempered log score, and the first experiments in this direction are encouraging. Whether optimizing against such a score produces better conceptual reasoning, rather than better-looking reasoning, is the question that connects this chapter back to scalable oversight.

**Humanized**

The compression weight $\tau$, similar to a market subsidy in the case of logarithmic markets, is determined by the designer. The conjecture of \cref{intro:sec:subjective} is that both should be set by price recursion, by the downstream value of the information a latent provides relative to the cost of producing it; the results here make the question precise but do not answer it. The second gap concerns the fact that humans and AIs do not form latent-class models, but natural-language theories and concepts. A natural next step is therefore to explore how well latent-variable methods transfer to settings where the latent variable is an essay or a concept, and the score is the tempered log score a reader gets when using the essay/concept to answer questions (which the author has not seen). Initial experiments in this direction look promising, but it remains to be seen whether optimizing for such a score leads to improved conceptual reasoning (rather than just improved appearances of reasoning), and this is another connection to scalable oversight.

**Final (meaning-corrected)**

Two gaps remain, and they are the natural next steps. First, the compression weight $\tau$, similar to the subsidy of a logarithmic market, is determined by the designer. The conjecture of \cref{intro:sec:subjective} is that both should be set by price recursion, by the downstream value of the information a latent provides relative to the cost of producing it; the results here make the question precise but do not answer it. The second gap is that the hypotheses humans and AIs actually entertain are not latent-class models but natural-language theories and concepts. Treating an essay or a concept as a latent variable, scored through the predictions a fixed reader makes with it on questions its author has not seen, is a direct application of the tempered log score, and initial experiments in this direction look promising. Whether optimizing for such a score leads to improved conceptual reasoning, rather than just improved appearances of reasoning, is the question that connects this chapter back to scalable oversight.

*Note:* Restored 'Two gaps remain ... First'; restored 'direct application of the tempered log score' and 'fixed reader' (humanized weakened to 'explore how well methods transfer').


## Unit 61 — chapters/consistency.tex

**Original**

The previous chapter replaced the missing ground truth with the structure of a logical sentence. Most questions we care about have no such structure: they are stated in natural language, and even when they will resolve, the answer may be years away. A forecaster's predictions about 2030 cannot be scored in 2025. Yet one thing can be checked immediately, namely whether the forecaster's beliefs fit together. If it gives the Democratic and the Republican candidate a 60\% chance each of winning the same election, something is wrong, whatever the outcome.

**Humanized**

In the previous chapter we saw how the ground truth can be replaced with the structure of a logical sentence. In most cases of interest, however, questions won't have any such structure, they will be stated in natural language, and may take years to resolve (e.g. a forecaster making predictions in 2025 about what happens in 2030 cannot immediately know if their predictions are correct). But there's still something we can check immediately: whether or not the beliefs are coherent. If a pollster gives both the Democratic and the Republican candidate a 60\% chance of winning the same election, something is definitely wrong.

**Final (meaning-corrected)**

In the previous chapter we saw how the missing ground truth can be replaced with the structure of a logical sentence. Most questions of interest, however, have no such structure: they are stated in natural language, and even when they will resolve, the answer may be years away (e.g. a forecaster's predictions made in 2025 about what happens in 2030 cannot be scored in 2025). But there is still something we can check immediately: whether the forecaster's beliefs are coherent. If a forecaster gives both the Democratic and the Republican candidate a 60\% chance of winning the same election, something is wrong, whatever the outcome.

*Note:* 'pollster' corrected to forecaster; restored 'whatever the outcome' and 'even when they will resolve'; fixed comma splice and contractions.


## Unit 62 — chapters/consistency.tex

**Original**

An economist reads such an inconsistency as an arbitrage opportunity: someone trading against these prices could lock in a profit. This chapter turns that observation into a measurement. It defines inconsistency as the guaranteed profit of the best arbitrageur against a market maker quoting the forecaster's probabilities, builds a pipeline that generates logically related questions and measures how consistent language-model forecasters are on them, and asks whether consistency predicts accuracy. It also tries to make forecasters consistent by arbitraging their own predictions against each other, with mixed results. \Cref{ch:arbitrage} returns to the arbitrage metric and shows that it is exactly what a market of traders computes.

**Humanized**

To an economist, incoherence is opportunity, if prices don't make sense, then there may be a way to make guaranteed money by trading against them. This chapter defines a measure of inconsistency (namely, how much guaranteed money the best arbitragist could make trading against a market maker with the prices the forecaster gave), presents a pipeline for creating sets of logically-related questions and measuring LLM forecasters' inconsistency on them, and investigates whether inconsistency can predict accuracy. We also try to make forecasters consistent by arbitraging against their own predictions, with mixed success. We return to the measure of inconsistency in \Cref{ch:arbitrage} to show that it corresponds to what a market of arbitragists would compute.

**Final (meaning-corrected)**

To an economist, such incoherence is opportunity: someone trading against these prices could make guaranteed money. This chapter turns that observation into a measurement. It defines a measure of inconsistency (namely, how much guaranteed money the best arbitrageur could make trading against a market maker quoting the forecaster's probabilities), presents a pipeline for creating sets of logically related questions and measuring LLM forecasters' consistency on them, and investigates whether consistency predicts accuracy. We also try to make forecasters consistent by arbitraging their own predictions against each other, with mixed success. \Cref{ch:arbitrage} returns to this measure of inconsistency and shows that it is exactly what a market of traders computes.

*Note:* Fixed 'may be a way' hedge and comma splice, 'arbitragist', 'arbitraging against their own predictions', and mid-sentence \Cref; restored 'exactly'.


## Unit 63 — chapters/consistency.tex

**Original**

Engineering details of the pipeline---the exact data formats, the prompts and LLM calls used in each step, examples of generated data, and the full list of forecaster configurations---are omitted from this chapter; they are given in the appendices of the source paper.

**Humanized**

For brevity we omit some implementation details, including specific formats used, exact LLM calls and prompts made in each stage of the pipeline, some examples of data created by the pipeline, and all configurations of forecasters used, and all of which are available in the appendices of our paper.

**Final (meaning-corrected)**

For brevity we omit some engineering details of the pipeline, including the exact data formats, the prompts and LLM calls made in each stage, examples of data created by the pipeline, and the full list of forecaster configurations used; all of these are given in the appendices of the source paper.

*Note:* Fixed broken 'and ..., and all of which' grammar.


## Unit 64 — chapters/infonomy.tex

**Original**

\Cref{part:agency} treated reward as something an economy generates internally. In alignment, reward comes from outside, from a human principal, and the difficulty is that the principal often cannot tell good behaviour from behaviour that merely looks good. The introduction to this part described that difficulty as information asymmetry, the classic failure of markets for used cars and other goods whose quality the buyer cannot see. The economist's first remedy is to let the buyer purchase the missing information. But information is a peculiar good: a buyer cannot judge it without seeing it, and once she has seen it she no longer needs to pay.

**Humanized**

\Cref{part:agency} treated reward as something an economy generates internally. But the economist's solution to markets for used cars and other situations in which quality can't be observed is to allow the buyer to purchase information. However, information is a peculiar good: in many situations, it can't be evaluated without being seen, and once it has been seen, it need no longer be purchased. Reward, in the alignment case, also comes from outside, from the human principal. As we described in the introduction to this part, a key challenge in AI alignment is that the human often can't distinguish between good behavior and behavior that merely looks good. This information asymmetry is what economists mean when they talk about lemons problems.

**Final (meaning-corrected)**

\Cref{part:agency} treated reward as something an economy generates internally. In the alignment case, however, reward comes from outside, from the human principal, and the difficulty is that the human often cannot distinguish between good behaviour and behaviour that merely looks good. As we described in the introduction to this part, this is an information asymmetry, the classic failure of markets for used cars and other goods whose quality the buyer cannot observe. The economist's first remedy is to allow the buyer to purchase the missing information. However, information is a peculiar good: it cannot be evaluated without being seen, and once it has been seen, it need no longer be purchased.

*Note:* Humanized scrambled the order so the remedy preceded the problem it addresses, and added the 'in many situations' hedge.


## Unit 65 — chapters/infonomy.tex

**Original**

Language-model buyers remove that obstacle. An LLM can inspect a piece of information on its owner's behalf, decide whether it is worth buying, and then forget it if the answer is no. This chapter develops a Bayesian theory of such inspection-based information markets. It shows that one round of inspection is not enough, because the inspecting agent can itself lack context that would change its valuation, and that the right protocol is recursive: an agent inspecting information may buy further information to evaluate it. The same framework then yields a scoring mechanism for scalable oversight, in which a human's judgement is extended by a market of information sellers so that the reward she gives reflects what she would think if she knew more.

**Humanized**

Language-model buyers sidestep this difficulty: an LLM can inspect information on a human's behalf, decide if it's worth buying, and then forget about the information if not. This chapter develops a Bayesian theory of markets for information with such an inspection stage. It argues that one such stage is insufficient, since the LLM inspecting the information may itself lack relevant context, and that the appropriate protocol is therefore recursive, with each inspecting LLM potentially buying more information to evaluate what it's inspecting. We then use our framework to design a scalable oversight scoring mechanism, in which the market of information sellers augments a human's evaluation so that the reward she assigns reflects what she would have thought had she had more information.

**Final (meaning-corrected)**

Language-model buyers sidestep this difficulty: an LLM can inspect information on a human's behalf, decide whether it is worth buying, and then forget about the information if not. This chapter develops a Bayesian theory of markets for information with such an inspection stage. It shows that one such stage is insufficient, since the LLM inspecting the information may itself lack context that would change its valuation, and that the appropriate protocol is therefore recursive, with each inspecting LLM potentially buying more information to evaluate what it is inspecting. We then use our framework to design a scalable oversight scoring mechanism, in which the market of information sellers augments a human's evaluation so that the reward she assigns reflects what she would have thought had she had more information.

*Note:* 'argues' restored to 'shows'; restored 'context that would change its valuation'; removed contractions.


## Unit 66 — chapters/intro.tex

**Original**

Indeed, computing equilibria is in general intractable: Nash equilibria are \textsf{PPAD}-complete \citep{daskalakisComplexityComputingNash2006, daskalakisComplexityComputingNash2009}, as are Arrow--Debreu equilibria even for additively separable utilities \citep{chenSettlingComplexityArrowDebreu2009}: thus Kamal Jain's quip as relayed in \citet{daskalakisComplexityComputingNash2009}, ``if your laptop cannot find it, then neither can the market''. The contrapositive is that a realistic model of markets is a model of bounded rationality \citep{papadimitriouComplexityBoundedRationality1994}: whatever the market does compute, it computes efficiently.

**Humanized**

Indeed, computing equilibria is in general intractable: Nash equilibria are \textsf{PPAD}-complete \citep{daskalakisComplexityComputingNash2006, daskalakisComplexityComputingNash2009}, as are Arrow--Debreu equilibria even for additively separable utilities \citep{chenSettlingComplexityArrowDebreu2009}: thus Kamal Jain's quip as relayed in \citet{daskalakisComplexityComputingNash2009}, ``if your laptop cannot find it, then neither can the market''. From this we get the contrapositive: any realistic model of markets will be a model of bounded rationality \citep{papadimitriouComplexityBoundedRationality1994}: markets compute (whatever it is they compute) efficiently.


## Unit 67 — chapters/intro.tex

**Original**

markets as a theory of \emph{agency} itself (\cref{part:agency}); an economic formulation of \emph{misalignment} especially outer misalignment (\cref{part:oversight}); and economic insights for \emph{belief elicitation} from AI on subjective, latent and never-resolving questions (\cref{part:subjective}).

**Humanized**

markets as a theory of \emph{agency} itself (\cref{part:agency}); an economic formulation of \emph{misalignment} especially outer misalignment (\cref{part:oversight}); and economic insights for \emph{belief elicitation} from AI on subjective, latent and never-resolving questions (\cref{part:subjective}).


## Unit 68 — chapters/intro.tex

**Original**

Can the dynamics of a market be derived from a normative principle of rationality --- so that the market stands to \emph{reward} as Bayesian updating stands to \emph{evidence}, i.e. so that there is a \emph{rational theory of reward}?

**Humanized**

Can the dynamics of a market be derived from a normative principle of rationality --- so that the market stands to \emph{reward} as Bayesian updating stands to \emph{evidence}, i.e. so that there is a \emph{rational theory of reward}?


## Unit 69 — chapters/intro.tex

**Original**

In \cref{ch:agency} we show:
\begin{enumerate}
\item (\cref{agency:sec:hyperstition}) Entropic mirror ascent---the natural optimization dynamics in probability space---is continuous-time Bayesian inference (replicator dynamics), so a reward signal is exactly (hyperstitional) Bayesian evidence.
\item (\cref{agency:sec:cbi}) On the graphical production economy dynamic applied to routing shares has revenue as the evidence rate, while the price recursion equation is simultaneously backpropagation and Bellman recursion. Reward for a sub-agent is thus not arbitrary: it is the price generated by the economy as ``super-agent'', and \emph{price recursion is the rational theory of reward}, complementing Bayes (\cref{agency:sec:rationalize}).
\item The accompanying \texttt{marketgrad} library (\cref{agency:sec:library}) implements this theory and numerically verifies the identities therein.
\end{enumerate}

**Humanized**

Results shown in \cref{ch:agency} are
\begin{enumerate}
\item (\cref{agency:sec:hyperstition}) Entropic mirror ascent---the natural optimization dynamics in probability space---is continuous-time Bayesian inference (replicator dynamics), so a reward signal is exactly (hyperstitional) Bayesian evidence.
\item (\cref{agency:sec:cbi}): the price recursion equation, which can be seen both as the backpropagation and the Bellman recursion equation. The dynamic applied to routing shares on the graphical production economy, revenue as the evidence rate. Reward for a sub-agent is thus not arbitrary: it is the price generated by the economy as ``super-agent'', and \emph{price recursion is the rational theory of reward}, complementing Bayes (\cref{agency:sec:rationalize}).
\item This \texttt{marketgrad} library (\cref{agency:sec:library}) provides a computerized implementation of this theory and numerical verification of identities stated here.
\end{enumerate}

**Final (meaning-corrected)**

The results shown in \cref{ch:agency} are:
\begin{enumerate}
\item (\cref{agency:sec:hyperstition}) Entropic mirror ascent---the natural optimization dynamics in probability space---is continuous-time Bayesian inference (replicator dynamics), so a reward signal is exactly (hyperstitional) Bayesian evidence.
\item (\cref{agency:sec:cbi}) On the graphical production economy, the dynamic applied to routing shares has revenue as the evidence rate, while the price recursion equation is simultaneously the backpropagation and the Bellman recursion equation. Reward for a sub-agent is thus not arbitrary: it is the price generated by the economy as ``super-agent'', and \emph{price recursion is the rational theory of reward}, complementing Bayes (\cref{agency:sec:rationalize}).
\item The accompanying \texttt{marketgrad} library (\cref{agency:sec:library}) provides an implementation of this theory and numerical verification of the identities therein.
\end{enumerate}

*Note:* Item 2 was a sentence fragment; fixed lead-in punctuation and 'This marketgrad library'.


## Unit 70 — chapters/intro.tex

**Original**

Scoring, whether in a prediction market or in machine learning, normally depends on knowing the right answer: a proper scoring rule pays a forecast against the outcome that eventually occurs, and a loss function compares a prediction with a label. Neither helps when we want an AI, or a market of traders, to answer a ``subjective'' or ``latent'' question, one whose answer is never revealed. This is why conceptual reasoning, research taste and judgement are so hard to train or evaluate: there is no answer key against which to score them.

**Humanized**

Scoring, whether in a prediction market or in machine learning, normally depends on knowing the right answer: a proper scoring rule pays a forecast against the outcome that eventually occurs, and a loss function compares a prediction with a label. Neither helps for ``subjective'' or ``latent'' questions (where the answer is never revealed), such as might be asked of an AI or market of traders. This sort of judgement is exactly the sort of thing where it will be difficult to train or evaluate AI judgement, because there is no ground truth to check its answer against.

**Final (meaning-corrected)**

Scoring, whether in a prediction market or in machine learning, normally depends on knowing the right answer: a proper scoring rule pays a forecast against the outcome that eventually occurs, and a loss function compares a prediction with a label. Neither helps for ``subjective'' or ``latent'' questions (where the answer is never revealed), such as might be asked of an AI or market of traders. This is exactly why conceptual reasoning, research taste and judgement will be difficult to train or evaluate in AI: there is no ground truth to check its answers against.

*Note:* Narrow fix of StealthGPT output (garbled last sentence; restored conceptual reasoning, research taste).


## Unit 71 — chapters/intro.tex

**Original**

For alignment the gap matters a great deal. Interpretability asks what a model believes internally, and eliciting latent knowledge asks how to get a model to report those beliefs honestly rather than what it predicts a human would say \citep{christianoElicitingLatentKnowledge2021}. Human values are themselves functions of latent variables: we care whether people are flourishing, not whether some measurable proxy for it goes up. And the hardest questions on which we will want a superhuman system's judgement, such as whether a research direction is promising or an argument sound, are conceptual rather than empirical.

**Humanized**

For alignment the gap matters a great deal. Interpretability aims to understand what a model `knows' or `believes' internally. Related to this, but distinct, is the task of eliciting latent knowledge from neural networks: elicitation focuses on how to get a model to truthfully express its beliefs, instead of saying whatever it thinks a human wants it to say \citep{christianoElicitingLatentKnowledge2021}. Human values depend on latent variables, e.g. we care about people flourishing, not some proxy measure increasing. And the problems we most want superhuman help with (is this research programme promising, is this argument sound?) are conceptual, not empirical.

**Final (meaning-corrected)**

For alignment the gap matters a great deal. Interpretability aims to understand what a model `knows' or `believes' internally. Related to this, but distinct, is the task of eliciting latent knowledge from neural networks: elicitation focuses on how to get a model to truthfully express its beliefs, instead of saying what it predicts a human would say \citep{christianoElicitingLatentKnowledge2021}. Human values depend on latent variables, e.g. we care about people flourishing, not some proxy measure increasing. And the hardest problems we will want superhuman help with (is this research programme promising, is this argument sound?) are conceptual, not empirical.

*Note:* Narrow fix of StealthGPT output (ELK: "what it predicts a human would say"; "hardest problems").


## Unit 72 — chapters/intro.tex

**Original**

From the economic point of view of \cref{part:agency}, one would expect latent beliefs to be produced like anything else in an economy. A belief about a latent variable is useful because it improves predictions and decisions downstream, so its value, and with it how much subsidy a market for that latent deserves, should be set by price recursion. Yet there is no obvious market mechanism that elicits latent beliefs, still less one that creates markets for new latent variables as they become useful. Humans and AI systems nonetheless form latent beliefs all the time.

**Humanized**

From the economic point of view of \cref{part:agency}, one would expect latent beliefs to be produced like anything else in an economy. If we could price these latent beliefs, that would help us make better predictions and decisions, so the beliefs (and latent markets) that we expect to be most valuable to create deserve the largest subsidies. Recursively setting prices this way would give us a principled way of figuring out which latent beliefs we should care about eliciting. Unfortunately, we don't currently have a good way to do this. People and AIs have latent beliefs all the time, but we don't have a good mechanism for eliciting them, let alone one that spins up markets for new latent variables when appropriate.

**Final (meaning-corrected)**

From the economic point of view of \cref{part:agency}, one would expect latent beliefs to be produced like anything else in an economy. A belief about a latent variable is useful because it helps us make better predictions and decisions downstream, so its value, and with it the subsidy that a market for that latent deserves, should be set by price recursion. Unfortunately, there is no obvious market mechanism for eliciting latent beliefs, let alone one that spins up markets for new latent variables as they become useful. Yet people and AIs form latent beliefs all the time.

*Note:* Humanized inverted the logic (pricing beliefs helps predictions) and lost that value/subsidy should be set by price recursion.


## Unit 73 — chapters/intro.tex

**Original**

Two existing proposals come close. Combinatorial prediction markets built on Bayesian networks \citep{sunProbabilityAssetUpdating2012,laskeyGraphicalModelMarket2018} let traders edit both the parameters and the structure of a network, so a latent node can be represented; but a trade in such a market is settled when the variables it concerns resolve, and a latent variable never does, so nothing pays a trader for what its latent belief contributes to the predictions of observables. Latent-variable prediction markets \citep{tailcalledLatentVariablesPrediction2023} fix this by paying traders according to the change in the predicted probability of the observable indicators, with the latent integrated out. This has sound incentives, but it leaves the latent beliefs themselves partly unpriced. Some of the freedom is harmless (relabelling a latent, or rotating several latent factors into one another, changes nothing anyone could check), but some is not: when the latent distribution or the number of latent classes is left to the traders, quite different latent models earn exactly the same payouts.

**Humanized**

There are two existing mechanisms that come close, though. Bayesian networks can model latent (unobserved) variables. In a prediction market based on a Bayesian network \citep{sunProbabilityAssetUpdating2012,laskeyGraphicalModelMarket2018}, traders are able to modify the parameters and even the structure of the network (and hence introduce latent variables). However, in such markets, traders make predictions about observables only, since markets are resolved when the relevant variables are observed. Thus, the part of a trader's belief about the network that concerns latent variables, even to the extent that it affects his predictions about observables, does not earn him anything in such markets. Another class of prediction markets \citep{tailcalledLatentVariablesPrediction2023} deals with this issue by having traders place their bets on indicators (which are functions of the latent variable and possibly other variables). Traders are rewarded based on how well they predict the indicators (integrating out the latent variable). This has nice incentive properties, but only partially prices latent beliefs. Some degrees of freedom don't matter (e.g. traders could consistently relabel the latent classes or rotate some latent variables into each other in ways no one could detect), but some do: e.g. traders could pick a very different distribution over latents, or even the number of latent classes, and no one would notice since both versions would result in the same payments.

**Final (meaning-corrected)**

There are two existing mechanisms that come close. Bayesian networks can model latent (unobserved) variables. In a combinatorial prediction market based on a Bayesian network \citep{sunProbabilityAssetUpdating2012,laskeyGraphicalModelMarket2018}, traders are able to modify the parameters and even the structure of the network, so a latent node can be represented. However, a trade in such a market is settled when the variables it concerns resolve, and a latent variable never does. Thus the part of a trader's belief that concerns latent variables earns it nothing, even to the extent that it contributes to its predictions of observables. Latent-variable prediction markets \citep{tailcalledLatentVariablesPrediction2023} deal with this issue by rewarding traders according to the change in the predicted probability of the observable indicators, with the latent variable integrated out. This has sound incentive properties, but only partially prices latent beliefs. Some degrees of freedom do not matter (relabelling a latent, or rotating several latent factors into one another, changes nothing anyone could detect), but some do: when the distribution over latents or the number of latent classes is left to the traders, quite different latent models result in exactly the same payments.

*Note:* Fixed false claim that traders 'predict observables only'; removed invented definition of indicators; restored integrated-out payout rule and 'exactly the same payouts' framing.


## Unit 74 — chapters/intro.tex

**Original**

A principled answer to the question of how to elicit beliefs about latent or subjective questions in general would also be a philosophical answer to what such questions \emph{mean}, and to why humans and AIs form latent beliefs at all. One would expect it to have something to do with compression: with information bottlenecks \citep{tishbyInformationBottleneckMethod1999}, minimal sufficient statistics and common information \citep{wynerCommonInformationTwo1975}, that is, with some account of what makes one way of factoring a joint distribution better than another.

**Humanized**

A principled answer to the question of how to elicit beliefs about latent or subjective questions in general would also be a philosophical answer to what such questions \emph{mean}, and to why humans and AIs form latent beliefs at all. we should expect it to be connected with ideas about compression: information bottlenecks \citep{tishbyInformationBottleneckMethod1999}, minimal sufficient statistics and common information \citep{wynerCommonInformationTwo1975}, i.e. ideas that try to make sense of when one factorisation of a joint distribution is better than another.

**Final (meaning-corrected)**

A principled answer to the question of how to elicit beliefs about latent or subjective questions in general would also be a philosophical answer to what such questions \emph{mean}, and to why humans and AIs form latent beliefs at all. One would expect it to be connected with ideas about compression: information bottlenecks \citep{tishbyInformationBottleneckMethod1999}, minimal sufficient statistics and common information \citep{wynerCommonInformationTwo1975}, i.e. ideas that try to make sense of when one factorisation of a joint distribution is better than another.

*Note:* Fixed lowercase sentence start.


## Unit 75 — chapters/intro.tex

**Original**

This thesis does not solve the general problem. It studies two partial approaches, each of which replaces the missing ground truth with something else, and then returns to the general question.

**Humanized**

There are a couple of partial answers. This thesis does not give a full solution to this problem, but presents two partial approaches that replace ground truth with something else, and discusses some thoughts about possible next steps.

**Final (meaning-corrected)**

This thesis does not give a full solution to this problem, but presents two partial approaches, each of which replaces the missing ground truth with something else, and then returns to the general question.

*Note:* Removed redundant opener; 'possible next steps' restored to 'returns to the general question'.


## Unit 76 — chapters/intro.tex

**Original**

Even where ground truth exists, it may be too slow: an AI forecaster's predictions about the coming years cannot be scored today. Can forecasters be evaluated --- and improved --- \emph{before} resolution, using only the logical relationships between their forecasts?

**Humanized**

Another challenge with forecasting is that, even when the ground truth does exist, it may be very slow to arrive: we can't score an AI forecaster's predictions about the next few years until the next few years have happened. Can \emph{before} resolution forecasts be skill-scored (and improved) using only consistency between forecasts?

**Final (meaning-corrected)**

Another challenge with forecasting is that, even when the ground truth does exist, it may be very slow to arrive: we cannot score an AI forecaster's predictions about the next few years until the next few years have happened. Can forecasters be evaluated (and improved) \emph{before} resolution, using only the logical relationships between their forecasts?

*Note:* Question was garbled ('Can before resolution forecasts be skill-scored').


## Unit 77 — chapters/intro.tex

**Original**

Is there a market-based account of latent beliefs, in which latent variables are priced like any other good in the economy? And since only observables can ever be scored, what gives a belief about a latent variable its meaning, and when can such beliefs be elicited?

**Humanized**

What would a market-based notion of latent beliefs look like? How are latent variables ``priced'', like other goods in an economy? How do we make sense of beliefs about unobservable latent variables, when only observable variables can be scored? Under what conditions can beliefs about latent variables be elicited?

**Final (meaning-corrected)**

Is there a market-based account of latent beliefs, in which latent variables are ``priced'' like any other good in an economy? How do we make sense of beliefs about unobservable latent variables, when only observable variables can ever be scored? Under what conditions can beliefs about latent variables be elicited?

*Note:* Humanized presupposed latent variables are priced; restored the existence question.


## Unit 78 — chapters/intro.tex

**Original**

In \cref{ch:arbitrage} we show that the arbitrage metric of \cref{ch:consistency} is exactly the welfare gained by trade in a market of quasi-linear consumers, that the arbitraged forecasts are the market's equilibrium prices, and that the arbitraged combination of utilities is utilitarian welfare, the objective assumed in \cref{ch:agency}. In markets over dependent questions, the prices of worlds are the arbitrageur's profits, and latent variables are \emph{intermediate goods} priced by price recursion; a market whose routers follow proportional response learns them by EM. We then argue that a latent belief means exactly what it does to predictions of observables, separate the harmless (gauge) part of what scoring leaves free from the genuine part, and introduce the \emph{latent bottleneck}, which asks latents to explain the observables with as few bits as possible. Its optimum can be elicited from a single outcome with a new scoring rule, the \emph{tempered log score}. Finally we use these results to assess latent-variable and Bayesian-network prediction markets.

**Humanized**

In \cref{ch:arbitrage} we show that in a market of quasi-linear consumers, the arbitrage metric of \cref{ch:consistency} is exactly the welfare gained by trade, the arbitraged forecasts are the market's equilibrium prices, and the arbitraged combination of utilities is utilitarian welfare, the objective assumed in \cref{ch:agency}. In such markets, arbitrageurs' profits are equal to the prices of worlds. The latent variables \emph{intermediate goods} can be priced with a price recursion. In particular, EM can be implemented by a market whose routers use proportional response. We argue that all a latent belief means is what it does to predictions of observables, disentangle the (harmless, gauge) freedom that scoring leaves from what is real, and motivate \emph{latent bottleneck}, which requires the latents to explain the observables using as few bits as possible. Its optimum can be elicited from a single outcome with a new scoring rule, the \emph{tempered log score}. Finally, we'll use these results to analyze latent-variable and Bayesian-network prediction markets.

**Final (meaning-corrected)**

In \cref{ch:arbitrage} we show that in a market of quasi-linear consumers, the arbitrage metric of \cref{ch:consistency} is exactly the welfare gained by trade, the arbitraged forecasts are the market's equilibrium prices, and the arbitraged combination of utilities is utilitarian welfare, the objective assumed in \cref{ch:agency}. In markets over dependent questions, the prices of worlds are equal to the arbitrageur's profits, and latent variables are \emph{intermediate goods}, priced by price recursion; a market whose routers use proportional response learns them by EM. We argue that all a latent belief means is what it does to predictions of observables, separate the harmless (gauge) part of the freedom that scoring leaves from the genuine part, and introduce the \emph{latent bottleneck}, which requires the latents to explain the observables using as few bits as possible. Its optimum can be elicited from a single outcome with a new scoring rule, the \emph{tempered log score}. Finally, we use these results to analyze latent-variable and Bayesian-network prediction markets.

*Note:* Restored 'markets over dependent questions'; fixed garbled intermediate-goods sentence and 'In particular, EM'; 'what is real' restored to 'genuine part'.


## Unit 79 — chapters/litrev-agency.tex

**Original**

\noindent The two chapters of this part draw on four bodies of work: reinforcement learners built as internal markets, market models of bounded rationality, analogies between markets and neural networks, and the economics of preference aggregation as it has recently been applied to alignment. We review them in that order.

**Humanized**

\noindent Four other bodies of work are also relevant to this thesis, which I will review in turn: reinforcement learners constructed as internal markets, models of bounded rationality in economics, the relationship between neural networks and markets, and economics of aggregating preferences as applied recently to alignment problems. Markets and bounded rationality.

**Final (meaning-corrected)**

\noindent The two chapters of this part draw on four bodies of work, which we review in turn: reinforcement learners constructed as internal markets, market models of bounded rationality, analogies between neural networks and markets, and the economics of aggregating preferences as applied recently to alignment problems.

*Note:* Removed first-person 'I' and stray fragment 'Markets and bounded rationality.'; restored scope ('the two chapters of this part').


## Unit 80 — chapters/litrev-agency.tex

**Original**

A second strand of work treats AI systems as participants in markets rather than as markets themselves. Early proposals for ``agoric'' computation envisaged software objects buying and selling computational resources \citep{millerMarketsComputationAgoric1988}; more recent examples include decentralized networks that reward machine-learning models for their contributions \citep{raoBitTensorPeertoPeerIntelligence2021}, economic simulations populated by language-model agents \citep{liEconAgentLargeLanguage2024a}, and the use of simulated economies to design tax policy \citep{zhengAIEconomistOptimal2021}. Closest in spirit to this thesis are recent papers that frame alignment itself in economic terms: \citet{conitzerPositionSocialChoice2024} and \citet{geAxiomsAIAlignment2024a} apply social choice theory to the aggregation of human feedback, and \citet{bergemannMechanismDesignAlignment2026} cast alignment as a problem of mechanism design. These works take the reward to be given and ask how to aggregate or elicit it; \cref{ch:agency} asks instead what reward is, and finds the answer in the prices of an economy.

**Humanized**

Other literature takes a different approach and studies AI systems as participating in markets. An even more futuristic notion is that of ``agoric'' computation, where software objects trade with each other for resources \citep{millerMarketsComputationAgoric1988}. More recently, there have been proposals for using cryptocurrencies to reward models that contribute usefully to decentralized machine-learning efforts \citep{raoBitTensorPeertoPeerIntelligence2021}, to create realistic simulations of economies in which language models can be the agents \citep{liEconAgentLargeLanguage2024a}, or to create economic simulations that can inform tax policy \citep{zhengAIEconomistOptimal2021}. Most related to this paper are recent works that take an economic perspective on alignment: \citet{conitzerPositionSocialChoice2024} and \citet{geAxiomsAIAlignment2024a} study alignment problems as instances of social choice problems (in particular, on how to aggregate human feedback), and \citet{bergemannMechanismDesignAlignment2026} studies alignment problems as instances of mechanism design problems. Whereas in \cref{ch:agency} the question is what the reward is and the answer is given in terms of the prices in an economy, here the reward is taken as given and the question is how to elicit or aggregate it.

**Final (meaning-corrected)**

Other literature takes a different approach and studies AI systems as participants in markets rather than as markets themselves. Early proposals for ``agoric'' computation envisaged software objects trading with each other for computational resources \citep{millerMarketsComputationAgoric1988}. More recent examples include decentralized networks that reward machine-learning models for their contributions \citep{raoBitTensorPeertoPeerIntelligence2021}, realistic simulations of economies in which language models are the agents \citep{liEconAgentLargeLanguage2024a}, and the use of simulated economies to inform tax policy \citep{zhengAIEconomistOptimal2021}. Most related to this thesis are recent works that take an economic perspective on alignment itself: \citet{conitzerPositionSocialChoice2024} and \citet{geAxiomsAIAlignment2024a} apply social choice theory to alignment, in particular to the aggregation of human feedback, and \citet{bergemannMechanismDesignAlignment2026} frame alignment as a problem of mechanism design. These works take the reward as given and ask how to elicit or aggregate it, whereas in \cref{ch:agency} the question is what the reward is, and the answer is given in terms of the prices in an economy.

*Note:* Removed added 'cryptocurrencies' (wrongly applied to all three works) and 'even more futuristic'; 'here' wrongly attributed reward-as-given to this thesis; 'this paper' to 'this thesis'.


## Unit 81 — chapters/litrev-agency.tex

**Original**

All of these algorithms auction a single ``right to act'' at each step. \Cref{ch:market-rl} instead splits the state into separately traded goods, and \cref{ch:agency} develops the corresponding theory of prices.

**Humanized**

All of these algorithms auction a single ``right to act'' at each step. \Cref{ch:market-rl} instead splits the state into separately traded goods, and \cref{ch:agency} develops the corresponding theory of prices.


## Unit 82 — chapters/litrev-agency.tex

**Original**

On the side of learning dynamics, the replicator equation of evolutionary game theory is known to be a form of Bayesian inference, with fitness playing the role of log-likelihood \citep{harperReplicatorEquationInference2009,baezInformationGeometryPart92012}; \cref{ch:agency} uses this correspondence to read rewards and revenues as evidence. Proportional-response dynamics, in which each seller allocates its goods in proportion to the payments it receives, are known to converge to equilibrium in Fisher markets and can be derived as mirror descent \citep{birnbaum2011}. Analogies between economic equilibrium and statistical mechanics, which motivate some of the language of \cref{ch:agency}, are surveyed by \citet{liuEquilibriumThermoeconomics}.

**Humanized**

From the learning dynamics perspective, the replicator equation of evolutionary game theory is a special case of Bayesian inference, where fitness can be interpreted as log-likelihood \citep{harperReplicatorEquationInference2009,baezInformationGeometryPart92012}; \cref{ch:agency} exploits this observation to interpret rewards/revenues as evidence. Proportional-response dynamics, in which each seller allocates its goods in proportion to the payments it receives, are known to converge to equilibrium in Fisher markets and can be derived as mirror descent \citep{birnbaum2011}. Analogies between economic equilibrium and statistical mechanics, which motivate some of the language of \cref{ch:agency}, are surveyed by \citet{liuEquilibriumThermoeconomics}.

**Final (meaning-corrected)**

From the learning dynamics perspective, the replicator equation of evolutionary game theory is known to be a form of Bayesian inference, where fitness can be interpreted as log-likelihood \citep{harperReplicatorEquationInference2009,baezInformationGeometryPart92012}; \cref{ch:agency} exploits this correspondence to interpret rewards and revenues as evidence. Proportional-response dynamics, in which each seller allocates its goods in proportion to the payments it receives, are known to converge to equilibrium in Fisher markets and can be derived as mirror descent \citep{birnbaum2011}. Analogies between economic equilibrium and statistical mechanics, which motivate some of the language of \cref{ch:agency}, are surveyed by \citet{liuEquilibriumThermoeconomics}.

*Note:* Restored "known to be a form of" (humanized asserted "special case") and replaced the slash in "rewards/revenues".


## Unit 83 — chapters/litrev-oversight.tex

**Original**

\noindent The chapters of this part sit where two literatures meet: the economics of information, which asks how information can be valued and traded, and the AI-alignment literature on scalable oversight, which asks how a weak overseer can reward a strong agent correctly. We review the economic side first, then the alignment side, and finally the empirical work on oversight protocols that \cref{ch:solib} builds on.

**Humanized**

\noindent Two literatures that we draw from are (1) the economics of information, which studies how information can be valued and traded, and (2) the AI-alignment literature on scalable oversight, which studies how to get correct reward signals for strong agents from weak overseers. We first review work in the first area and then turn to the second. We also review some relevant empirical work on scalable oversight protocols that \cref{ch:solib} builds on.

**Final (meaning-corrected)**

\noindent The chapters of this part draw on two literatures: (1) the economics of information, which studies how information can be valued and traded, and (2) the AI-alignment literature on scalable oversight, which studies how to get correct reward signals for strong agents from weak overseers. We first review work in the first area, then turn to the second, and finally review the empirical work on scalable oversight protocols that \cref{ch:solib} builds on.

*Note:* Restored that these are the literatures behind the chapters of this part and the review order (empirical work last).


## Unit 84 — chapters/litrev-oversight.tex

**Original**

The recursive information markets of \cref{ch:infonomy} belong to the same family as market making \citep{evanhubingerAISafetyMarket2020}, which they generalize beyond binary questions, and the benchmark of \cref{ch:solib} replaces the judge-accuracy methodology of the debate experiments above with a measure of the incentive a protocol gives for truthfulness.

**Humanized**

The recursive information markets of prediction markets and forecasting tournaments \cref{ch:infonomy} Market making and market taking are similar concepts that belong to the same family \citep{evanhubingerAISafetyMarket2020}, the benchmark of generalization from binary questions to other question types,
, and the benchmark of \cref{ch:solib} replaces the judge-accuracy methodology of the debate experiments above with a measure of the incentive a protocol gives for truthfulness.

**Final (meaning-corrected)**

The recursive information markets of \cref{ch:infonomy} belong to the same family as market making \citep{evanhubingerAISafetyMarket2020}, which they generalize beyond binary questions, and the benchmark of \cref{ch:solib} replaces the judge-accuracy methodology of the debate experiments above with a measure of the incentive a protocol gives for truthfulness.

*Note:* Humanized text was garbled (misplaced \cref, fragments, stray comma line); no salvageable sentence.


## Unit 85 — chapters/litrev-subjective.tex

**Original**

\noindent The chapters of this part look for substitutes for ground truth: the structure of logical sentences, the internal consistency of a forecaster's beliefs, and the structure of latent-variable models. We first review the classical theory of belief elicitation and its market form, then logical uncertainty and the related game-theoretic and debate-based approaches, then consistency checks for machine-learning systems and forecasters, and finally combinatorial and latent-variable prediction markets together with the information-theoretic ideas used in \cref{ch:arbitrage}.

**Humanized**

\noindent Can the structure of latent-variable models stand in for ground truth? In \cref{ch:arbitrage} we saw prediction markets over latent variables and tempered posteriors. Can the structure of logic stand in for ground truth? This idea shows up in work on logical uncertainty, as well as approaches to AI safety via game-theoretic arguments or AI debate. Can the (coherence-)consistency of an agent stand in for ground truth? This idea shows up in work on evaluating the consistency of machine learning systems or human forecasters. In this chapter we survey approaches to prediction markets and proper scoring rules, which presume eventual resolution.

**Final (meaning-corrected)**

\noindent The chapters of this part look for substitutes for ground truth. Can the structure of logical sentences stand in for ground truth? Can the internal consistency of a forecaster's beliefs? Can the structure of latent-variable models? We first review the classical theory of belief elicitation, proper scoring rules, and its market form, prediction markets. We then turn to work on logical uncertainty and the related game-theoretic and debate-based approaches to AI safety, then to work on evaluating the consistency of machine-learning systems and human forecasters, and finally to combinatorial and latent-variable prediction markets, together with the information-theoretic ideas used in \cref{ch:arbitrage}.

*Note:* Humanized wrongly said ch:arbitrage was already seen and misdescribed the chapter as surveying only scoring rules and markets; restored the substitute-for-ground-truth framing and full review order.


## Unit 86 — chapters/litrev-subjective.tex

**Original**

Proper scoring rules reward a probabilistic forecast according to the outcome that occurs, in such a way that reporting one's true belief maximizes expected reward \citep{goodRationalDecisions1952,savageElicitationPersonalProbabilities1971,gneitingStrictlyProperScoring2007}. Market scoring rules turn a scoring rule into an automated market maker: each trader is paid the difference between the score of the price it leaves and the score of the price it found, so the market maker's total loss is bounded by the score of the initial price \citep{hansonLogarithmicMarketScoring2002,hansonCombinatorialInformationMarket2003}. Market makers of this kind are equivalent to cost-function market makers, whose prices are the gradient of a convex cost function and whose scoring rule is its convex conjugate \citep{chenUtilityFrameworkBoundedloss2007,abernethyEfficientMarketMaking2013}. With traders of constant absolute risk aversion, the equilibrium price aggregates beliefs as a risk-tolerance-weighted geometric average, a result that goes back to the theory of syndicates \citep{wilsonTheorySyndicates1968,abernethyInformationAggregationExponential2014}. All of these mechanisms require that the event eventually resolves. \citet{conitzerPredictionMarketsMechanism2012} studies how to reward agents for the information they bring to a market, but again only where the market is eventually settled against ground truth.

**Humanized**

Proper scoring rules are reward schemes for probabilistic forecasts with the desirable property that the forecaster's expected reward is maximized by reporting her true belief. That is, the forecaster's reward depends on the event that occurs, in such a way that reporting her true belief maximizes her reward, in expectation \citep{goodRationalDecisions1952,savageElicitationPersonalProbabilities1971,gneitingStrictlyProperScoring2007}. Another interesting result is the construction of an automated market maker based on any market scoring rule. Each trader pays (or receives) the difference between the market scoring rule evaluated at the old and new price, and the total loss of the market maker is bounded by the market scoring rule evaluated at the initial price \citep{hansonLogarithmicMarketScoring2002,hansonCombinatorialInformationMarket2003}. Market makers of this kind are equivalent to cost-function market makers, whose prices are the gradient of a convex cost function and whose scoring rule is its convex conjugate \citep{chenUtilityFrameworkBoundedloss2007,abernethyEfficientMarketMaking2013}. It is also worth noting that the equilibrium price with traders having CRRA utility is the risk-tolerance-weighted geometric average of traders' beliefs. This result can be traced back to the theory of syndicates \citep{wilsonTheorySyndicates1968,abernethyInformationAggregationExponential2014}. All of these mechanisms require that the event eventually resolves. \citet{conitzerPredictionMarketsMechanism2012} studies how to reward agents for the information they bring to a market, but again only where the market is eventually settled against ground truth.

**Final (meaning-corrected)**

Proper scoring rules are reward schemes for probabilistic forecasts: the forecaster's reward depends on the event that occurs, in such a way that reporting her true belief maximizes her reward in expectation \citep{goodRationalDecisions1952,savageElicitationPersonalProbabilities1971,gneitingStrictlyProperScoring2007}. Market scoring rules turn any scoring rule into an automated market maker. Each trader receives the difference between the scoring rule evaluated at the new price it leaves and at the old price it found, and the total loss of the market maker is bounded by the scoring rule evaluated at the initial price \citep{hansonLogarithmicMarketScoring2002,hansonCombinatorialInformationMarket2003}. Market makers of this kind are equivalent to cost-function market makers, whose prices are the gradient of a convex cost function and whose scoring rule is its convex conjugate \citep{chenUtilityFrameworkBoundedloss2007,abernethyEfficientMarketMaking2013}. It is also worth noting that, with traders of constant absolute risk aversion, the equilibrium price is the risk-tolerance-weighted geometric average of traders' beliefs. This result can be traced back to the theory of syndicates \citep{wilsonTheorySyndicates1968,abernethyInformationAggregationExponential2014}. All of these mechanisms require that the event eventually resolves. \citet{conitzerPredictionMarketsMechanism2012} studies how to reward agents for the information they bring to a market, but again only where the market is eventually settled against ground truth.

*Note:* Fixed CRRA to constant absolute risk aversion (CARA), fixed the ambiguous pays/receives direction (new minus old score), removed the duplicated definition sentence.


## Unit 87 — chapters/litrev-subjective.tex

**Original**

Combinatorial prediction markets let traders bet on Boolean combinations of events and on conditional events, so that the market maintains a joint distribution over many related questions \citep{hansonCombinatorialInformationMarket2003}. Pricing such a market exactly is computationally hard in general, which has led to market makers that represent the joint distribution as a Bayesian network and restrict trades to those that preserve its structure \citep{pennock2012PriceUpdatingCombinatorialPredictionMarketsBayesianNetworks,sunProbabilityAssetUpdating2012}. The most developed of these, deployed in the DAGGRE and SciCast forecasting markets, also lets traders add variables and dependencies, and so crowdsources the structure of the network as well as its parameters \citep{laskeyGraphicalModelMarket2018}. The dynamics of traders in such markets can be analysed as randomized coordinate descent \citep{frongilloConvergenceAnalysisPrediction2015}. Latent-variable prediction markets \citep{tailcalledLatentVariablesPrediction2023} instead let traders move the parameters of an item-response or latent-class model over a set of indicator questions, paying them by the change in the log-likelihood of the indicators once these resolve.

**Humanized**

Prediction markets over latent variables \citep{tailcalledLatentVariablesPrediction2023} allow traders to make trades which move parameters of some latent-class model (such as an item-response model) fit to some indicator questions; traders are paid according to the change in log-likelihood of the latent-class model fit to the indicator questions (once they are resolved). In this part we'll also study prediction markets over combinations of questions (rather than over single questions). In combinatorial prediction markets \citep{hansonCombinatorialInformationMarket2003}, traders can trade on conditional events or Boolean combinations of events, so the market maker maintains a joint distribution over events. Since pricing is computationally challenging, some combinatorial prediction market market makers maintain a distribution factorized according to a Bayesian network, and allow only those trades which maintain that factorization \citep{pennock2012PriceUpdatingCombinatorialPredictionMarketsBayesianNetworks,sunProbabilityAssetUpdating2012}. One such market maker, which has been used in the DAGGRE and SciCast forecasting markets, also allows traders to make trades which introduce new variables and dependencies; in this way, traders not only provide parameter estimates, they also crowdsource the graphical structure of the Bayesian network \citep{laskeyGraphicalModelMarket2018}. Trading dynamics in combinatorial prediction markets can be analyzed as forms of coordinate descent \citep{frongilloConvergenceAnalysisPrediction2015}.

**Final (meaning-corrected)**

In combinatorial prediction markets \citep{hansonCombinatorialInformationMarket2003}, traders can trade on conditional events or Boolean combinations of events, so the market maker maintains a joint distribution over many related questions. Since exact pricing is computationally hard in general, some combinatorial market makers maintain a distribution factorized according to a Bayesian network, and allow only those trades which maintain that factorization \citep{pennock2012PriceUpdatingCombinatorialPredictionMarketsBayesianNetworks,sunProbabilityAssetUpdating2012}. The most developed such market maker, which has been used in the DAGGRE and SciCast forecasting markets, also allows traders to make trades which introduce new variables and dependencies; in this way, traders not only provide parameter estimates, they also crowdsource the graphical structure of the Bayesian network \citep{laskeyGraphicalModelMarket2018}. Trading dynamics in such markets can be analyzed as randomized coordinate descent \citep{frongilloConvergenceAnalysisPrediction2015}. Prediction markets over latent variables \citep{tailcalledLatentVariablesPrediction2023} instead allow traders to make trades which move the parameters of an item-response or latent-class model fit to a set of indicator questions; traders are paid according to the change in the log-likelihood of the indicators once these are resolved.

*Note:* Restored order (latent-variable markets last, leading into identifiability), dropped added "in this part we'll also study" claim, item-response is not a kind of latent-class model, restored "randomized" coordinate descent and "most developed".


## Unit 88 — chapters/litrev-subjective.tex

**Original**

Whether the latent part of such a model is pinned down by the observables is a question of identifiability. For latent-class models with three or more conditionally independent indicators, the decomposition with the fewest classes is generically unique \citep{kruskalThreewayArraysRank1977,allmanIdentifiabilityParametersLatent2009}, and identifiable models can be learned efficiently by tensor methods \citep{anandkumarTensorDecompositionsLearning2014} as well as by EM \citep{dempsterMaximumLikelihoodIncomplete1977}. When several latent models fit equally well, information theory offers ways to prefer the most economical one. Wyner's common information is the least amount of information a common cause must carry to make two variables conditionally independent \citep{wynerCommonInformationTwo1975,gastparRelaxedWynersCommon2019}; correlation explanation seeks latent factors that explain as much of the dependence among many variables as possible \citep{versteegDiscoveringStructureHighdimensional2014}; and the information bottleneck compresses one variable while keeping what is relevant to another \citep{tishbyInformationBottleneckMethod1999}. The tempered posteriors that appear in \cref{ch:arbitrage} are studied in statistics as generalized Bayesian updates, mainly for robustness to misspecification \citep{grunwaldSafeBayesianLearning2012,bissiriGeneralFrameworkUpdating2016}.

**Humanized**

Question of identifiability: is the latent part of a model uniquely determined by the observables? For latent-class models with three or more conditionally independent indicators, the decomposition with the fewest classes is generically unique \citep{kruskalThreewayArraysRank1977,allmanIdentifiabilityParametersLatent2009}, and identifiable models can be learned efficiently by tensor methods \citep{anandkumarTensorDecompositionsLearning2014} as well as by EM \citep{dempsterMaximumLikelihoodIncomplete1977}. If several models fit the data equally well, prefer the most economical one (information theory). Wyner's common information aims to find the minimum amount of information a common cause must have about two variables in order to make them conditionally independent \citep{wynerCommonInformationTwo1975,gastparRelaxedWynersCommon2019}. Correlation explanation aims to find latent common causes that can explain as much of the correlations among multiple variables as possible \citep{versteegDiscoveringStructureHighdimensional2014}. The information bottleneck aims to find a compressed representation of one variable that retains as much information as possible about another variable \citep{tishbyInformationBottleneckMethod1999}. The tempered posteriors in \cref{ch:arbitrage} are known as generalized Bayesian updates and have been studied extensively in the statistics literature as a way to obtain robustness to model misspecification \citep{grunwaldSafeBayesianLearning2012,bissiriGeneralFrameworkUpdating2016}.

**Final (meaning-corrected)**

A question of identifiability arises here: is the latent part of such a model uniquely determined by the observables? For latent-class models with three or more conditionally independent indicators, the decomposition with the fewest classes is generically unique \citep{kruskalThreewayArraysRank1977,allmanIdentifiabilityParametersLatent2009}, and identifiable models can be learned efficiently by tensor methods \citep{anandkumarTensorDecompositionsLearning2014} as well as by EM \citep{dempsterMaximumLikelihoodIncomplete1977}. If several latent models fit the data equally well, information theory offers ways to prefer the most economical one. Wyner's common information is the minimum amount of information a common cause must carry in order to make two variables conditionally independent \citep{wynerCommonInformationTwo1975,gastparRelaxedWynersCommon2019}. Correlation explanation aims to find latent factors that can explain as much of the dependence among multiple variables as possible \citep{versteegDiscoveringStructureHighdimensional2014}. The information bottleneck aims to find a compressed representation of one variable that retains as much information as possible about another variable \citep{tishbyInformationBottleneckMethod1999}. The tempered posteriors in \cref{ch:arbitrage} are studied in the statistics literature as generalized Bayesian updates, mainly as a way to obtain robustness to model misspecification \citep{grunwaldSafeBayesianLearning2012,bissiriGeneralFrameworkUpdating2016}.

*Note:* Repaired fragment and imperative sentence; Wyner quantity is what a common cause must carry, dependence not just correlations, removed added "extensively".


## Unit 89 — chapters/market-rl.tex

**Original**

\Cref{ch:intro} argued that economies are agents built out of much simpler agents, and that this suggests an economic theory of agency. The most direct way to test that suggestion is to build an agent that literally is a market: a reinforcement learner whose actions are decided by an internal economy of sub-agents, each paid out of the rewards its decisions eventually bring in. Such agents are not new. Holland's classifier systems and Baum's Hayek machine already worked this way, and the idea of evaluating a market as an intelligence goes back further still. But all of them auction the entire world to a single winner at each step, which is precisely what real markets do not do. A real economy has many goods, owned and traded separately, and much of its power comes from that division.

**Humanized**

In \Cref{ch:intro}, we argued that economies are made up of simpler agents and so economics should give us some clues for building agents. The most literal way of following up on that idea is to build agents that are economies: reinforcement learners who delegate decisions to internal sub-agents, rewarded according to the payoffs their choices have on the parent agent's environment. This idea is not new: it shows up in Holland's classifier systems and Baum's Hayek machine, and has a long history of being used to evaluate markets as theories of intelligence. These algorithms all auction off the entire world to a single agent at each decision step, however. That's not very economical! Economies have many different goods which are owned and traded independently of each other, and some of their power may come from that separation.

**Final (meaning-corrected)**

In \cref{ch:intro}, we argued that economies are agents made up of much simpler agents, and that this suggests an economic theory of agency. The most direct way of testing that idea is to build agents that are economies: reinforcement learners who delegate decisions to an internal economy of sub-agents, each paid out of the rewards its decisions eventually bring in. This idea is not new: it shows up in Holland's classifier systems and Baum's Hayek machine, and the idea of evaluating a market as an intelligence goes back further still. These algorithms all auction off the entire world to a single winner at each decision step, however, which is precisely what real markets do not do. Economies have many different goods which are owned and traded separately, and much of their power comes from that separation.

*Note:* Restored "economic theory of agency", sub-agent payment scheme, "evaluating a market as an intelligence" (not "theories of intelligence"), removed chatty exclamation, restored "much of their power comes" (was hedged "some ... may").


## Unit 90 — chapters/market-rl.tex

**Original**

This chapter takes that difference seriously. It sets out a common framework for market-based agents on top of a partially observed Markov decision process, recovers the existing algorithms as \emph{deep} markets, in which a single good (the state) passes from owner to owner, and introduces \emph{wide} markets, in which the state is itself split into separately traded goods. It then looks at what such agents might be good for: searching over plans, growing or shrinking with the problem, and giving every component complete feedback. Along the way a link to neural networks appears: prices in an equilibrium market can be computed by something that looks like backpropagation. That link is suggestive rather than natural, and making it precise is the job of the next chapter. Since the chapter began as a position paper, its arguments are often informal, and it should be read as a map of the territory that the rest of \cref{part:agency} explores more carefully.

**Humanized**

In this chapter, we'll describe market-based agents in terms of a partially observed Markov decision process. In that setting, we can reinterpret existing algorithms as \emph{deep} markets, in which there's just one good, the state, and ownership of that good changes hands every timestep. We'll then describe \emph{wide} markets, in which the state is further subdivided into independent goods. Wide markets may have advantages for planning, scalability, and providing informative feedback to each component. They also have some surprising connections to neural networks: equilibrium prices in these markets can be calculated using a process that looks a lot like backpropagation! These connections aren't especially natural, and will be developed further in the next chapter. This chapter started out as a position paper, so we'll gloss over some details here and there. Think of it as a preview of the more careful treatment in the rest of \cref{part:agency}.

**Final (meaning-corrected)**

In this chapter, we'll describe market-based agents in terms of a partially observed Markov decision process. In that setting, we can reinterpret existing algorithms as \emph{deep} markets, in which there's just one good, the state, and ownership of that good changes hands from one owner to the next. We'll then describe \emph{wide} markets, in which the state is further subdivided into separately traded goods. Such agents may have advantages for planning, scalability, and providing complete feedback to each component. They also have some surprising connections to neural networks: equilibrium prices in these markets can be calculated using a process that looks a lot like backpropagation. These connections are suggestive rather than natural, and the next chapter makes them precise. This chapter started out as a position paper, so its arguments are often informal. Think of it as a preview of the more careful treatment in the rest of \cref{part:agency}.

*Note:* Narrow fix of StealthGPT output: "every timestep", "independent goods", "informative feedback", "gloss over details" and the exclamation corrected.


## Unit 91 — chapters/nonvf.tex

**Original**

Everything in \cref{part:oversight} relied, in the end, on a ground truth. Recursive information markets price information by how it changes a buyer's beliefs about something that will eventually be checked, and the oversight benchmark scores protocols on questions with known answers. The tools economics offers for eliciting beliefs make the same assumption. A proper scoring rule pays a forecast once the outcome is known, and a prediction market pays the holders of a contract when the event it names occurs or fails to.

**Humanized**

Everything in \cref{part:oversight} depended in some way on access to a ground truth. Recursive information markets priced information based on how much it updates beliefs about something that can in principle be verified; our oversight benchmark scored protocols on questions whose answers were known; and the tools economics provides for eliciting beliefs made similar assumptions: a proper scoring rule pays out for a prediction once the truth is revealed, and a prediction market pays out contracts conditional on the occurrence or non-occurrence of an event.

**Final (meaning-corrected)**

Everything in \cref{part:oversight} depended in the end on access to a ground truth. Recursive information markets priced information based on how much it updates a buyer's beliefs about something that will eventually be checked, and our oversight benchmark scored protocols on questions whose answers were known. The tools economics provides for eliciting beliefs make the same assumption: a proper scoring rule pays out for a prediction once the truth is revealed, and a prediction market pays out contracts conditional on the occurrence or non-occurrence of an event.

*Note:* "Can in principle be verified" restored to "will eventually be checked"; economic tools now stated in the present tense as a separate point, not as part of Part II.


## Unit 92 — chapters/nonvf.tex

**Original**

This part asks what can be done when no such outcome ever arrives. The cleanest place to start is first-order logic, where ``never resolves'' can be made precise. Some sentences are verified if true, some are falsified if false, and many, like ``all men are mortal'', are neither. This chapter first proves that no scoring rule or tradable asset can elicit honest probabilities on such sentences directly. It then gets around the impossibility by making the sentence the stakes of a game between a verifier and a falsifier, whose moves eventually resolve, and builds a market of computationally bounded traders that learns, in the limit, which sentences are true in a constructive sense.

**Humanized**

What happens when there is no such revealed truth? The cleanest place to start is first-order logic, where ``never resolves'' can be made precise. Some sentences are verified if true, some are falsified if false, and many, like ``all men are mortal'', are neither. We first prove impossibility results for eliciting probabilities about unresolvable statements with either scoring rules or the payoff function of a tradable asset. We then show how to evade these impossibility results by using a verification game (with verifier and falsifier, reminiscent of VF games) to give meaning to trading on such statements, and describe a market of computationally-bounded traders which, in the limit, identifies (constructively) the true statements.

**Final (meaning-corrected)**

What can be done when no such truth is ever revealed? The cleanest place to start is first-order logic, where ``never resolves'' can be made precise. Some sentences are verified if true, some are falsified if false, and many, like ``all men are mortal'', are neither. In this chapter, we first prove that no scoring rule and no payoff function of a tradable asset can directly elicit honest probabilities about such sentences. We then show how to evade this impossibility by making the sentence the stakes of a game between a verifier and a falsifier, whose moves eventually resolve, and describe a market of computationally bounded traders which, in the limit, identifies the sentences that are true in a constructive sense.

*Note:* Restored "honest"/"directly", the key point that the game's moves eventually resolve (dropped "reminiscent of VF games"), and that "constructive" qualifies truth, not identification.


## Unit 93 — chapters/nonvf.tex

**Original**

The mechanisms of Section~\ref{nonvf:sec:framework} construct the game and its associated markets abstractly. The long version of this work makes one of them fully concrete, as a Garrabrant-induction-style \emph{program market} whose participants are enumerated programs that trade on -- and play the ranged VF game for -- FOL sentences; this construction is what allows the optimality theorems below to be stated precisely. The remainder of this section is taken from the long version.

**Humanized**

The game and the associated markets are defined in an abstract fashion in Section~\ref{nonvf:sec:framework}. In the long version, we make this concrete by giving a Garrabrant-induction-style \emph{program market} in which enumerated programs play a ranged VF game on FOL statements against each other. This is what makes the optimality theorems precise.

**Final (meaning-corrected)**

The game and the associated markets are defined in an abstract fashion in Section~\ref{nonvf:sec:framework}. In the long version, we make one of these mechanisms fully concrete by giving a Garrabrant-induction-style \emph{program market} in which enumerated programs trade on FOL sentences and play the ranged VF game for them. This construction is what allows the optimality theorems below to be stated precisely. The remainder of this section is taken from the long version.

*Note:* Restored that programs trade on sentences (not just play against each other), "stated precisely", and the dropped sentence that the remainder is from the long version.


## Unit 94 — chapters/nonvf.tex

**Original**

The long version of the paper states this result with a sharper hypothesis: neither mechanism exists as soon as $\Props$, the class of propositions considered, includes at least $\Sigma_4$ or $\Pi_4$ sentences.

**Humanized**

The long version of the paper proves the result under the sharper assumption that $\Props$, contains at least $\Sigma_4$ or $\Pi_4$ sentences. In particular, in this case neither mechanism is possible.

**Final (meaning-corrected)**

The long version of the paper states the result under a sharper assumption: neither mechanism is possible as soon as $\Props$, the class of propositions considered, contains at least $\Sigma_4$ or $\Pi_4$ sentences.

*Note:* Removed stray comma after $\Props$ and restored the definition of $\Props$.


## Unit 95 — chapters/part1-intro.tex

**Original**

\noindent This part asks what economics has to say about \emph{agency itself}: not yet about aligning an AI to a principal, but about what reward, credit assignment and rational behaviour are in the first place. The thesis of this part is that the market is not merely a metaphor for these things but a theory of them.

**Humanized**

\noindent In the second half of this project we are concerned with questions about economics of \emph{agency itself}: what are rational behaviour and reward/credit assignment in the first place? Not (yet) about aligning an AI to a human/principal, but about AI/agency in general. My working hypothesis is that the market provides us not just a metaphor, but a theory of credit assignment and rational behaviour.

**Final (meaning-corrected)**

\noindent In this part we are concerned with what economics has to say about \emph{agency itself}: what are reward, credit assignment and rational behaviour in the first place? This is not (yet) about aligning an AI to a principal, but about agency in general. The thesis of this part is that the market provides us not just a metaphor for reward, credit assignment and rational behaviour, but a theory of them.

*Note:* Humanized said "second half of this project" (this is Part I) and turned the thesis into "my working hypothesis"; restored both.


## Unit 96 — chapters/part1-intro.tex

**Original**

\Cref{ch:agency} then develops the underlying theory: starting from the observation that \emph{reward is hyperstitional information} (a Bregman-divergence/mirror-ascent view of what a reward signal communicates to a learner), it argues that \emph{price recursion is the rational theory of reward} --- the recursive propagation of value through an economy of computations, of which backpropagation and TD-learning arise as special cases. The accompanying \texttt{marketgrad} library implements market-like optimization on production graphs.

**Humanized**

\Cref{ch:agency} then develops the underlying theory: starting from the observation that \emph{reward is hyperstitional information} (a Bregman-divergence/mirror-ascent view of what a reward signal communicates to a learner), it argues that \emph{price recursion is the rational theory of reward} --- the recursive propagation of value through an economy of computations, of which backpropagation and TD-learning arise as special cases. The accompanying \texttt{marketgrad} library implements some ideas for using markets as an optimization algorithm on production graphs.


## Unit 97 — chapters/part2-intro.tex

**Original**

\noindent If markets are the economist's model of distributed intelligence, the alignment problem is the economist's principal--agent problem at scale — and the central claim of this part is an identification: \textbf{the outer alignment problem --- scalable oversight --- \emph{is} the economist's problem of information asymmetry}, transported from the market for goods to the market for AI behaviour. It is useful to decompose the standard rebuttal to ``why can't we just set the right reward function?'' into three levels:

**Humanized**

\noindent Economists understand the market as a model of distributed intelligence. Economists are interested in the alignment problem insofar as it resembles a well-studied problem in economics, the principal--agent problem. This part of the essay is about that resemblance. Its central claim is that the market's principal--agent problem \textbf{the outer alignment problem --- scalable oversight --- \emph{is} the economist's problem of information asymmetry}, can be ported over to a hypothetical market for AI behaviour. A common reply to the question ``why can't we just set the right reward function?'' has three components, which I'll discuss separately.

**Final (meaning-corrected)**

\noindent If the market is the economist's model of distributed intelligence, then the alignment problem is the economist's principal--agent problem at scale. The central claim of this part is an identification: \textbf{the outer alignment problem --- scalable oversight --- \emph{is} the economist's problem of information asymmetry}, ported over from the market for goods to the market for AI behaviour. It is useful to decompose the common reply to the question ``why can't we just set the right reward function?'' into three levels:

*Note:* Repaired garbled central claim, removed "essay" and first person singular, restored the colon introducing the list; replaced the Unicode dash.


## Unit 98 — chapters/part2-intro.tex

**Original**

Understanding what reward \emph{is} --- what role it actually plays in producing agency --- is thus itself a foundational question for alignment, prior to any particular alignment scheme; \cref{part:agency} developed an answer in economic terms. This part takes on the outer alignment problem itself.

**Humanized**

Understanding what reward \emph{is} --- what role it actually plays in producing agency --- is thus itself a foundational question for alignment, prior to any particular alignment scheme; \cref{part:agency} developed an answer in economic terms. We now turn to the outer alignment problem.


## Unit 99 — chapters/part2-intro.tex

**Original**

A special difficulty arises when the questions on which beliefs must be elicited are not even \emph{verifiable}: when no ground truth will ever arrive to settle the bet. Human values, latent variables, and ``subjective'' judgements are of exactly this character; extending the economist's elicitation devices beyond that boundary is deferred to \cref{part:subjective}.

**Humanized**

But sometimes we'll be interested in eliciting beliefs about questions that aren't even \emph{verifiable}: where there is no fact of the matter that will be revealed in the future. Human values, latent variables, and ``subjective'' judgements are of exactly this character; extending the economist's elicitation devices beyond that boundary is deferred to \cref{part:subjective}.

**Final (meaning-corrected)**

A special difficulty arises when we need to elicit beliefs about questions that are not even \emph{verifiable}: where no ground truth will ever be revealed to settle the bet. Human values, latent variables, and ``subjective'' judgements are of exactly this character; extending the economist's elicitation devices beyond that boundary is deferred to \cref{part:subjective}.

*Note:* "No fact of the matter" is a stronger metaphysical claim than "no ground truth will arrive"; restored.


## Unit 100 — chapters/part2-intro.tex

**Original**

\Cref{ch:infonomy} builds on the LLM-buyer observation above (due to \citealt{weissRedesigningInformationMarkets2024}) to construct \emph{recursive information markets}: a mechanism by which a human rater's judgement is amplified by a recursive market of information-selling agents, so that the reward signal she emits approximates her extrapolated volition. Recursive information markets are a \emph{scalable oversight protocol}; evaluating such protocols in a principled way is an open problem in its own right, and \cref{ch:solib} constructs a benchmark for scalable oversight mechanisms --- defining the Agent Score Difference metric and evaluating protocols such as Debate and Consultancy --- to address it.

**Humanized**

\Cref{ch:infonomy} builds on the LLM-buyer observation above (due to \citealt{weissRedesigningInformationMarkets2024}) to construct \emph{recursive information markets}: a mechanism by which a human rater's judgement is amplified by a recursive market of information-selling agents, so that the reward signal she emits approximates her extrapolated volition. Recursive information markets are a \emph{scalable oversight protocol}; evaluating such protocols in a principled way is an open problem in its own right, and \cref{ch:solib} constructs a benchmark for scalable oversight mechanisms --- defining the Agent Score Difference metric and evaluating protocols such as Debate and Consultancy --- to address it.


## Unit 101 — chapters/part3-intro.tex

**Original**

\noindent The mechanisms of \cref{part:oversight} presuppose that we can elicit honest beliefs from agents. Economics has a canonical answer for how to do this: \emph{proper scoring rules} \citep{goodRationalDecisions1952, savageElicitationPersonalProbabilities1971, gneitingStrictlyProperScoring2007} reward a forecast against the realized outcome so that truthful reporting maximizes expected reward, and \emph{prediction markets} \citep{hansonLogarithmicMarketScoring2002, hansonCombinatorialInformationMarket2003} decentralize this: an asset contingent on the event is traded, and an agent's ``fair price'' is its subjective probability. Indeed the two are equivalent in a precise sense: a logarithmic market scoring rule is exactly a sequentially-shared proper scoring rule, and the market subsidy is the price paid for information.

**Humanized**

\noindent The mechanisms of \cref{part:oversight} presuppose that we can elicit honest beliefs from agents. Economics has a canonical answer for how to do this: \emph{proper scoring rules} \citep{goodRationalDecisions1952, savageElicitationPersonalProbabilities1971, gneitingStrictlyProperScoring2007} reward a forecast against the realized outcome so that truthful reporting maximizes expected reward, and \emph{prediction markets} \citep{hansonLogarithmicMarketScoring2002, hansonCombinatorialInformationMarket2003} decentralize this: an asset contingent on the event is traded, and an agent's ``fair price'' is its subjective probability. We showed in that post that logarithmic market scoring rules are precisely sequentially-shared proper scoring rules, and that the market subsidy was the price paid for information. Indeed, in a precise sense, they're equivalent.

**Final (meaning-corrected)**

\noindent The mechanisms of \cref{part:oversight} presuppose that we can elicit honest beliefs from agents. Economics has a canonical answer for how to do this: \emph{proper scoring rules} \citep{goodRationalDecisions1952, savageElicitationPersonalProbabilities1971, gneitingStrictlyProperScoring2007} reward a forecast against the realized outcome so that truthful reporting maximizes expected reward, and \emph{prediction markets} \citep{hansonLogarithmicMarketScoring2002, hansonCombinatorialInformationMarket2003} decentralize this: an asset contingent on the event is traded, and an agent's ``fair price'' is its subjective probability. Indeed, in a precise sense, the two are equivalent: logarithmic market scoring rules are precisely sequentially-shared proper scoring rules, and the market subsidy is the price paid for information.

*Note:* Removed spurious "We showed in that post" (false self-attribution to a blog post).


## Unit 102 — chapters/part3-intro.tex

**Original**

\textbf{First, the questions we care about may never resolve.} Scoring rules and prediction markets presuppose a \emph{verifiable or falsifiable} (VF) event: ground truth eventually arrives and bets are settled. But human values, latent variables, counterfactuals and ``subjective'' questions are not VF --- there is nothing to settle the bet against. A classical observation in this direction is due to \citet{conitzerPredictionMarketsMechanism2012}, who studied prediction markets through the lens of mechanism design and cooperative game theory, and proposed a \emph{two-layer} structure: an object-level market that prices claims against ground truth, and a second layer that distributes credit among informants according to their marginal contribution to the market's prediction --- so that agents can be paid for \emph{information} even when their individual contribution is never directly verified, so long as the \emph{bottom} layer is eventually anchored to ground truth. The question this part pursues is what happens when even that anchor is removed.
%% TODO(part3-intro): elaborate exactly how the subjective-scoring level connects to
%% economics (per thesis plan), and verify the characterization of Conitzer (2012)'s
%% two-layer construction against the paper before submission.

**Humanized**

\textbf{First, the questions we care about may never resolve.} Scoring rules and prediction markets assume that for every \emph{verifiable or falsifiable} (VF) event there will eventually be a ground truth with which to settle bets. What then about questions which don't have a VF? Questions about human values, questions about latent variables or counterfactuals, ``subjective'' questions… There's nothing to settle the bet against. In \citet{conitzerPredictionMarketsMechanism2012}, prediction markets are studied from the point of view of mechanism design and cooperative game theory, and a \emph{two-layer} prediction market is proposed. There is an object-level prediction market which prices claims about some ground truth, as usual; the innovation is a meta-level market which pays out to informants based on their marginal contribution to the accuracy of the object-level market. This allows agents to be rewarded for \emph{information}, even if the information they provide is not directly verifiable, as long as the \emph{bottom} market is ultimately scored against ground truth.
%% TODO(part3-intro): elaborate exactly how the subjective-scoring level connects to
%% economics (per thesis plan), and verify the characterization of Conitzer (2012)'s
%% two-layer construction against the paper before submission.

**Final (meaning-corrected)**

\textbf{First, the questions we care about may never resolve.} Scoring rules and prediction markets presuppose a \emph{verifiable or falsifiable} (VF) event: they assume that there will eventually be a ground truth with which to settle bets. But what about questions that are not VF, such as questions about human values, latent variables or counterfactuals, or ``subjective'' questions? There is nothing to settle the bet against. A classical observation in this direction is due to \citet{conitzerPredictionMarketsMechanism2012}, who studied prediction markets from the point of view of mechanism design and cooperative game theory, and proposed a \emph{two-layer} structure. There is an object-level prediction market which prices claims about some ground truth, as usual; the innovation is a second layer which distributes credit among informants based on their marginal contribution to the object-level market's prediction. This allows agents to be rewarded for \emph{information}, even if their individual contribution is never directly verified, as long as the \emph{bottom} layer is ultimately anchored to ground truth. The question this part pursues is what happens when even that anchor is removed.
%% TODO(part3-intro): elaborate exactly how the subjective-scoring level connects to
%% economics (per thesis plan), and verify the characterization of Conitzer (2012)'s
%% two-layer construction against the paper before submission.

*Note:* Fixed garbled "questions which don't have a VF" and Unicode ellipsis, "accuracy" back to "prediction", "verified" not "verifiable", and restored the dropped closing sentence (what happens when the anchor is removed).


## Unit 103 — chapters/part3-intro.tex

**Original**

\textbf{Second, even where ground truth exists, it may be too slow.} Evaluating (and training) AI forecasters against resolution alone means waiting months or years for feedback. But rationality constraints --- coherence of probabilities across logically related questions --- can be checked \emph{immediately}, and violations of them are exactly \emph{arbitrage opportunities} in the market reading of beliefs.

**Humanized**

\textbf{Second, even where ground truth exists, it may be too slow.} While Evaluating (and training) AI forecasters against resolution alone means waiting months or years for feedback. But rationality constraints, coherence of probabilities across logically related questions, can be checked \emph{immediately}, and violations of them are exactly \emph{arbitrage opportunities} in the market reading of beliefs.

**Final (meaning-corrected)**

\textbf{Second, even where ground truth exists, it may be too slow.} Evaluating (and training) AI forecasters against resolution alone means waiting months or years for feedback. But rationality constraints --- coherence of probabilities across logically related questions --- can be checked \emph{immediately}, and violations of them are exactly \emph{arbitrage opportunities} in the market reading of beliefs.

*Note:* Only changes were a stray "While" fragment and dashes replaced by commas.


## Unit 104 — chapters/part3-intro.tex

**Original**

\Cref{ch:arbitrage} then returns to the economics of \cref{part:agency}. It shows that the arbitrage metric of \cref{ch:consistency} is exactly what a market of traders computes, that latent variables are intermediate goods priced by price recursion, and it asks what gives a belief about a latent variable its meaning when only observables can be scored.

**Humanized**

\Cref{ch:arbitrage} then returns to the economics of \cref{part:agency}. It shows that the arbitrage metric of \cref{ch:consistency} is exactly what a market of traders computes, that latent variables are intermediate goods priced by price recursion, and it asks what gives a belief about a latent variable its meaning when only observables can be scored.


## Unit 105 — chapters/solib.tex

**Original**

The recursive information market of the previous chapter is one answer to the scalable oversight problem, and it joins a crowded field. Debate, consultancy, market making and iterated amplification all claim to let a weak judge supervise a stronger agent, and each comes with an argument for why it should work. Those arguments usually assume idealized agents, and they rarely say how one protocol compares with another. Deciding which protocols to trust therefore needs experiments.

**Humanized**

How can a relatively unintelligent agent oversee a more intelligent one? Several proposals have been made: recursive information market from the previous chapter, iterated amplification, debate, consultancy, and market making. Each comes with a rationale for why it could work, but they all seem to assume idealized agents, and it's unclear how the different protocols compare to each other. This motivates experimentation!

**Final (meaning-corrected)**

How can a relatively weak judge oversee a stronger agent? Several proposals have been made: the recursive information market of the previous chapter, iterated amplification, debate, consultancy, and market making. Each comes with a rationale for why it could work, but these rationales usually assume idealized agents, and they rarely say how the different protocols compare to each other. Deciding which protocols to trust therefore requires experiments.

*Note:* Softened "all seem to assume" back to "usually", "unclear" to "rarely say", replaced exclamation with the original conclusion.


## Unit 106 — chapters/solib.tex

**Original**

Experiments, however, need a measure of success, and the measure used so far, the accuracy of the judge's final answer, is not the one that matters for alignment. An economist asks of a mechanism whether it gives participants the right incentives; for oversight, that means whether the protocol rewards an agent more for arguing the truth than for arguing a falsehood. A protocol can make the judge accurate without doing this, for instance if the judge simply trusts an agent who happens to be honest. This chapter builds the benchmark around incentives instead. It introduces the Agent Score Difference, which measures how much a protocol favours truth over falsehood, formalizes a general class of protocol experiments in a Python library, and uses both to compare Debate, Consultancy and a simple model of RLHF. Like every empirical study of oversight so far, the benchmark relies on questions whose answers are known, a limitation that points to the questions taken up in \cref{part:subjective}.

**Humanized**

The problem is that experiments need some success criteria, and so far the natural one has been how accurate the judge's answers are. But for alignment what we ultimately care about is whether the system is providing good incentives: will the more intelligent agent get a higher reward from arguing falsehoods or arguing the truth? This is an economist's question! An unintelligent judge could get highly accurate answers by delegating all questions to a single honest butchler agent, but that would not be giving good incentives. So this chapter proposes a new success criteria, the Agent Score Difference (how much does a protocol reward an agent for arguing the truth compared to arguing falsehoods?). I formalize a class of experiments around oversight protocols, implement it as a Python library, and use it to compare some simple versions of Debate, Consultancy and RLHF. As with all current work on experimenting with oversight, this uses questions with known answers, but the shortcomings of this point towards the next part of the thesis \cref{part:subjective}.

**Final (meaning-corrected)**

The problem is that experiments need a success criterion, and so far the natural one has been the accuracy of the judge's final answer. But for alignment what we ultimately care about is whether the protocol provides good incentives: will the more intelligent agent get a higher reward from arguing the truth or from arguing falsehoods? This is an economist's question. A judge could get highly accurate answers simply by trusting a single agent who happens to be honest, but that would not be giving good incentives. So this chapter builds the benchmark around a new success criterion, the Agent Score Difference (how much does a protocol reward an agent for arguing the truth compared to arguing falsehoods?). We formalize a general class of protocol experiments, implement it as a Python library, and use both to compare Debate, Consultancy and a simple model of RLHF. As with all empirical work on oversight so far, the benchmark relies on questions with known answers, a limitation that points towards the questions taken up in \cref{part:subjective}.

*Note:* Fixed "butchler" typo/"delegating" (original: judge trusts an agent who happens to be honest), first person singular, "criteria", "simple versions of" all protocols vs simple model of RLHF only, and run-on \cref.
