
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#f8f8fc">
<meta name="description" content="PulseCart makes order tracking and delivery management simple, clear, and delightful.">
<title>PulseCart — Every Delivery, A Better Experience</title>
<style>
:root {
  --ink: #19182d;
  --muted: #73738a;
  --purple: #6855e8;
  --purple-dark: #5140ce;
  --line: #e9e8f2;
  --surface: #ffffff;
  --green: #168452;
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  background: #fff;
  color: var(--ink);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI",
               Roboto, Helvetica, Arial, sans-serif;
  line-height: 1.6;
}
a { color: inherit; text-decoration: none; }
button, input { font: inherit; }
button, a { -webkit-tap-highlight-color: transparent; }
.container { width: min(1120px, calc(100% - 40px)); margin: auto; }
nav {
  height: 78px; display: flex; align-items: center;
  justify-content: space-between; gap: 20px;
}
.brand { display: inline-flex; align-items: center; gap: 10px;
  font-size: 23px; font-weight: 800; letter-spacing: -1px; }
.logo {
  display: grid; place-items: center; width: 40px; height: 40px;
  color: white; background: var(--purple); border-radius: 13px;
  font-size: 22px; box-shadow: 0 7px 18px #6855e82c;
}
.navlinks { display: flex; gap: 30px; align-items: center;
  color: #696980; font-size: 14px; }
.navlinks a:hover { color: var(--purple); }
.btn {
  display: inline-flex; justify-content: center; align-items: center;
  gap: 9px; border: 1px solid transparent; border-radius: 12px;
  padding: 12px 18px; font-weight: 650; font-size: 14px;
  transition: .2s ease; cursor: pointer;
}
.btn-primary { color: white; background: var(--purple);
  box-shadow: 0 7px 18px #6855e82a; }
.btn-primary:hover { background: var(--purple-dark); transform: translateY(-1px); }
.btn-light { background: white; border-color: #dedced; color: var(--ink); }
.btn-light:hover { border-color: var(--purple); }
.hero {
  padding: 78px 0 70px;
  background:
    radial-gradient(ellipse at 78% 38%, #e8e2ff 0%, transparent 38%),
    radial-gradient(ellipse at 10% 10%, #f1edff 0%, transparent 32%),
    #fbfaff;
  border-top: 1px solid #f1effa;
  overflow: hidden;
}
.hero-grid { display: grid; grid-template-columns: 1fr 1fr;
  align-items: center; gap: 60px; }
.eyebrow { display: inline-flex; align-items: center; gap: 8px;
  color: var(--purple); background: #efecff; border: 1px solid #e3ddff;
  border-radius: 30px; padding: 7px 12px; font-size: 11px;
  font-weight: 800; letter-spacing: 1.2px; }
.eyebrow-dot { width: 7px; height: 7px; border-radius: 50%;
  background: #806bff; }
h1 { font-size: clamp(43px, 5vw, 65px); line-height: 1.07;
  letter-spacing: -3px; margin: 23px 0 20px; font-weight: 800; }
.gradient-text { color: var(--purple); }
.hero-copy { color: var(--muted); max-width: 470px; font-size: 17px; }
.hero-actions { display: flex; gap: 12px; flex-wrap: wrap; margin: 28px 0; }
.trust { display: flex; align-items: center; gap: 10px;
  color: #77768c; font-size: 12px; }
.trust strong { color: #3b3a53; }
.avatar-stack { display: flex; }
.avatar { width: 27px; height: 27px; border-radius: 50%;
  border: 2px solid white; display: grid; place-items: center;
  background: #e5ddff; font-size: 12px; margin-left: -6px; }
.avatar:first-child { margin-left: 0; }
.dashboard {
  position: relative; background: #fff; border: 1px solid #e9e6f6;
  border-radius: 22px; padding: 23px;
  box-shadow: 0 28px 80px #38307118, 0 3px 12px #38307108;
}
.dashboard:before {
  content: ""; position: absolute; width: 90px; height: 90px;
  border-radius: 28px; background: #bdb1ff50; filter: blur(1px);
  right: -25px; top: -25px; z-index: -1;
}
.dash-head { display: flex; justify-content: space-between;
  align-items: center; gap: 12px; }
.dash-label { color: #88869b; font-size: 10px; letter-spacing: 1.2px;
  font-weight: 800; }
.dash-title { font-size: 19px; font-weight: 750; margin-top: 3px; }
.live { color: var(--green); background: #e8f8ef; border-radius: 20px;
  padding: 5px 9px; font-size: 10px; font-weight: 750; }
.metrics { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin: 22px 0; }
.metric { padding: 15px; border-radius: 14px; background: #f7f6ff; }
.metric.green { background: #effaf4; }
.metric-label { font-size: 11px; color: #77758c; }
.metric-value { font-size: 29px; font-weight: 800; letter-spacing: -1px; margin: 3px 0; }
.metric-note { color: var(--green); font-size: 10px; }
.order-list { border-top: 1px solid var(--line); padding-top: 17px; }
.order { display: flex; align-items: center; gap: 11px; padding: 12px 0; }
.order-icon { width: 38px; height: 38px; flex-shrink: 0;
  border-radius: 12px; display: grid; place-items: center;
  background: #f0edff; color: var(--purple); font-size: 18px; }
.order-icon.green { background: #eaf8f0; color: var(--green); }
.order-info { min-width: 0; flex: 1; }
.order-name { font-size: 12px; font-weight: 750; }
.order-desc { font-size: 10px; color: #89879b; }
.status { font-size: 10px; font-weight: 750; color: var(--purple);
  background: #f0edff; padding: 5px 8px; border-radius: 20px; white-space: nowrap; }
.status.done { color: var(--green); background: #eaf8f0; }
.dash-foot { border-top: 1px solid var(--line); padding-top: 13px;
  color: #9290a2; font-size: 10px; text-align: center; }
.section { padding: 86px 0; }
.section-head { max-width: 620px; text-align: center; margin: 0 auto 42px; }
.kicker { color: var(--purple); font-size: 11px; letter-spacing: 1.6px;
  font-weight: 800; text-transform: uppercase; }
h2 { font-size: clamp(30px, 4vw, 42px); letter-spacing: -1.7px;
  line-height: 1.15; margin: 12px 0; }
.section-head p { color: var(--muted); font-size: 15px; }
.features { display: grid; grid-template-columns: repeat(3, 1fr); gap: 18px; }
.feature { padding: 26px; border: 1px solid var(--line);
  border-radius: 18px; background: #fff; transition: .2s ease; }
.feature:hover { transform: translateY(-4px); box-shadow: 0 14px 35px #31216a0d; }
.feature-icon { display: grid; place-items: center; width: 46px; height: 46px;
  border-radius: 14px; background: #f0edff; font-size: 21px; }
.feature:nth-child(2) .feature-icon { background: #e9f8f0; }
.feature:nth-child(3) .feature-icon { background: #fff2e5; }
.feature h3 { font-size: 17px; margin: 19px 0 8px; }
.feature p { color: var(--muted); font-size: 13px; margin: 0; }
.tracking-section { background: #f8f7ff; }
.tracking-grid { display: grid; grid-template-columns: .9fr 1.1fr;
  gap: 60px; align-items: center; }
.tracking-copy p { color: var(--muted); font-size: 15px; }
.benefit { display: flex; gap: 11px; align-items: flex-start; margin-top: 18px; }
.benefit-mark { color: var(--green); font-weight: 900; }
.timeline { padding: 26px; background: #fff; border: 1px solid var(--line);
  border-radius: 18px; box-shadow: 0 15px 45px #3830710a; }
.timeline h3 { margin: 0 0 23px; font-size: 17px; }
.timeline-step { display: flex; gap: 14px; min-height: 72px; }
.timeline-symbol { width: 30px; height: 30px; flex-shrink: 0;
  display: grid; place-items: center; border-radius: 50%;
  background: #eaf8f0; color: var(--green); font-weight: 800; }
.timeline-step:not(:last-child) .timeline-symbol { position: relative; }
.timeline-step:not(:last-child) .timeline-symbol:after {
  content: ""; position: absolute; top: 30px; height: 42px;
  width: 2px; background: #d9eee2;
}
.timeline-step h4 { margin: 2px 0 3px; font-size: 13px; }
.timeline-step p { margin: 0; color: var(--muted); font-size: 11px; }
.cta { padding: 70px 0; }
.cta-card { position: relative; overflow: hidden; text-align: center;
  padding: 55px 25px; border-radius: 24px;
  background: linear-gradient(125deg, #211b4a, #5140a6 65%, #705ce7); color: white; }
.cta-card:after { content: ""; position: absolute; width: 260px; height: 260px;
  border-radius: 50%; border: 1px solid #ffffff20; right: -70px; top: -110px; }
.cta-card h2 { max-width: 650px; margin: 0 auto 15px; }
.cta-card p { color: #d8d3f7; max-width: 510px; margin: 0 auto 25px; font-size: 14px; }
.cta-card .btn { background: white; color: #392b8b; }
footer { border-top: 1px solid var(--line); padding: 25px 0; }
.footer-row { display: flex; align-items: center; justify-content: space-between;
  gap: 20px; color: #858398; font-size: 11px; }
.footer-links { display: flex; gap: 20px; }
footer .brand { font-size: 18px; color: var(--ink); }
footer .logo { width: 32px; height: 32px; font-size: 17px; border-radius: 10px; }
#tracking { scroll-margin-top: 25px; }
@media (max-width: 800px) {
  .hero { padding: 55px 0; }
  .hero-grid, .tracking-grid { grid-template-columns: 1fr; gap: 40px; }
  .hero-copy { max-width: 600px; }
  .dashboard { max-width: 520px; width: 100%; margin: auto; }
  .features { grid-template-columns: 1fr 1fr; }
  .navlinks { gap: 14px; }
  .navlinks .nav-hide { display: none; }
  .tracking-grid { gap: 30px; }
}
@media (max-width: 520px) {
  .container { width: min(100% - 28px, 1120px); }
  nav { height: 68px; }
  .brand { font-size: 20px; }
  .navlinks { display: none; }
  nav > .btn { padding: 10px 12px; font-size: 12px; }
  h1 { letter-spacing: -2px; }
  .hero { padding: 45px 0; }
  .hero-copy { font-size: 15px; }
  .dashboard { padding: 16px; }
  .metrics { gap: 8px; }
  .metric { padding: 12px; }
  .metric-value { font-size: 25px; }
  .section { padding: 62px 0; }
  .features { grid-template-columns: 1fr; }
  .feature { padding: 22px; }
  .footer-row { flex-direction: column; text-align: center; }
}
</style>
</head>
<body>
<header class="container">
  <nav aria-label="Main navigation">
    <a class="brand" href="#" aria-label="PulseCart home">
      <span class="logo">P</span>PulseCart
    </a>
    <div class="navlinks">
      <a href="#features">Features</a>
      <a href="#tracking">How it works</a>
      <a class="nav-hide" href="#about">About</a>
    </div>
    <a class="btn btn-primary" href="#tracking">Track a delivery <span>↗</span></a>
  </nav>
</header>

<main>
<section class="hero">
  <div class="container hero-grid">
    <div>
      <div class="eyebrow"><span class="eyebrow-dot"></span> SMART COMMERCE LOGISTICS</div>
      <h1>Every delivery.<br>A <span class="gradient-text">better experience.</span></h1>
      <p class="hero-copy">Bring every order into focus. PulseCart helps you follow deliveries, simplify logistics, and create a smoother experience from checkout to doorstep.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="#tracking">Explore tracking <span>→</span></a>
        <a class="btn btn-light" href="#features">Discover the platform</a>
      </div>
      <div class="trust">
        <div class="avatar-stack" aria-hidden="true">
          <span class="avatar">✦</span><span class="avatar">P</span><span class="avatar">✓</span>
        </div>
        <span><strong>One clear view.</strong> Every step of the way.</span>
      </div>
    </div>

    <div class="dashboard" aria-label="Sample delivery dashboard">
      <div class="dash-head">
        <div>
          <div class="dash-label">YOUR WORKSPACE</div>
          <div class="dash-title">Delivery overview</div>
        </div>
        <span class="live">● SYSTEM LIVE</span>
      </div>
      <div class="metrics">
        <div class="metric">
          <div class="metric-label">In transit</div>
          <div class="metric-value">128</div>
          <div class="metric-note">↗ Orders on the move</div>
        </div>
        <div class="metric green">
          <div class="metric-label">Delivered today</div>
          <div class="metric-value">1,284</div>
          <div class="metric-note">✓ Sample dashboard data</div>
        </div>
      </div>
      <div class="order-list">
        <div class="dash-label">RECENT DELIVERIES</div>
        <div class="order">
          <div class="order-icon">↗</div>
          <div class="order-info">
            <div class="order-name">Order #PC-2048</div>
            <div class="order-desc">Out for delivery · Today</div>
          </div>
          <span class="status">On track</span>
        </div>
        <div class="order">
          <div class="order-icon green">✓</div>
          <div class="order-info">
            <div class="order-name">Order #PC-2047</div>
            <div class="order-desc">Delivered · 10:42 AM</div>
          </div>
          <span class="status done">Delivered</span>
        </div>
        <div class="order">
          <div class="order-icon">⇄</div>
          <div class="order-info">
            <div class="order-name">Order #PC-2051</div>
            <div class="order-desc">Moving through regional hub</div>
          </div>
          <span class="status">In transit</span>
        </div>
      </div>
      <div class="dash-foot">Illustrative dashboard · Sample data, not live shipment tracking</div>
    </div>
  </div>
</section>

<section class="section" id="features">
  <div class="container">
    <div class="section-head">
      <div class="kicker">Built for better delivery</div>
      <h2>Less uncertainty.<br>More momentum.</h2>
      <p>Everything you need for a clearer delivery journey, thoughtfully brought together in one place.</p>
    </div>
    <div class="features">
      <article class="feature">
        <div class="feature-icon">⌖</div>
        <h3>Delivery visibility</h3>
        <p>Keep shipment progress easy to understand, from dispatch through the final mile.</p>
      </article>
      <article class="feature">
        <div class="feature-icon">↗</div>
        <h3>Smarter operations</h3>
        <p>Give teams a clear overview of delivery activity and help them focus on what matters.</p>
      </article>
      <article class="feature">
        <div class="feature-icon">♡</div>
        <h3>Customer confidence</h3>
        <p>Make the post-purchase experience feel more transparent, calm, and dependable.</p>
      </article>
    </div>
  </div>
</section>

<section class="section tracking-section" id="tracking">
  <div class="container tracking-grid">
    <div class="tracking-copy">
      <div class="kicker">A clearer journey</div>
      <h2>From checkout to doorstep, keep every step in view.</h2>
      <p>Great delivery experiences start with clarity. PulseCart brings the journey into focus with a simple, easy-to-follow delivery flow.</p>
      <div class="benefit"><span class="benefit-mark">✓</span><span>Understand each stage of the delivery journey.</span></div>
      <div class="benefit"><span class="benefit-mark">✓</span><span>See delivery status in one intuitive interface.</span></div>
      <div class="benefit"><span class="benefit-mark">✓</span><span>Build a stronger experience after checkout.</span></div>
    </div>
    <div class="timeline">
      <h3>Your delivery journey</h3>
      <div class="timeline-step">
        <div class="timeline-symbol">✓</div>
        <div><h4>Order confirmed</h4><p>Your order details are received and ready for processing.</p></div>
      </div>
      <div class="timeline-step">
        <div class="timeline-symbol">✓</div>
        <div><h4>Prepared for dispatch</h4><p>Your package is prepared for its journey.</p></div>
      </div>
      <div class="timeline-step">
        <div class="timeline-symbol">↗</div>
        <div><h4>On the way</h4><p>Follow progress as the package moves toward its destination.</p></div>
      </div>
      <div class="timeline-step">
        <div class="timeline-symbol">⌂</div>
        <div><h4>Delivered</h4><p>The final step: a package at its destination.</p></div>
      </div>
    </div>
  </div>
</section>

<section class="cta" id="about">
  <div class="container">
    <div class="cta-card">
      <h2>Make every delivery feel effortless.</h2>
      <p>Bring clarity to the journey and make the experience after checkout just as thoughtful as the purchase itself.</p>
      <a class="btn" href="#tracking">Discover the PulseCart experience →</a>
    </div>
  </div>
</section>
</main>

<footer>
  <div class="container footer-row">
    <a class="brand" href="#"><span class="logo">P</span>PulseCart</a>
    <span>Thoughtfully moving orders forward.</span>
    <div class="footer-links"><a href="#features">Features</a><a href="#tracking">How it works</a></div>
    <span>© 2026 PulseCart</span>
  </div>
</footer>
</body>
</html>
"""

@app.route("/health")
def health():
    return jsonify(status="healthy")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
      <title>PulseCart | Live Delivery</title>
      <style>
        body {
          font-family: Arial, sans-serif;
          background: #101827;
          color: white;
          text-align: center;
          padding: 70px 20px;
        }
        .card {
          max-width: 650px;
          margin: auto;
          padding: 35px;
          background: #1e293b;
          border-radius: 18px;
        }
        h1 { color: #38bdf8; font-size: 42px; }
        .status { color: #4ade80; font-size: 22px; }
      </style>
    </head>
    <body>
      <div class="card">
        <h1>PulseCart</h1>
        <h2>Smart Delivery Tracking</h2>
        <p class="status">● All systems operational</p>
        <p>Your orders, moving smarter.</p>
        <p>Release: v1.0 | Powered by Kubernetes</p>
      </div>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify(status="healthy")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
