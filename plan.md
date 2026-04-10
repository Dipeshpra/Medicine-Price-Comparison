# Affordable Medicine Intelligence Platform — 10 Smart Features Upgrade

## Phase 1: Smart Substitution Confidence Score & Overpay Alert System ✅
- [x] Add confidence score calculation logic to medicine state (same active ingredient +40, same dosage +30, same release type +20, regulatory approval +10)
- [x] Add NTI drug detection and auto-cap at 60% for Warfarin, Digoxin, Lithium, Phenytoin
- [x] Build overpay alert banner on results page (triggered when savings > ₹20/strip)
- [x] Display confidence score badges on all alternative medicine cards with color-coded indicators
- [x] Add overpay thresholds: >₹200/month = "Significant overpayment", >₹2000/year = grocery equivalence

## Phase 2: Explain Like a Doctor, Monthly Cost Optimizer & Price Trends ✅
- [x] Build "Explain Like a Doctor" panel on results page with plain English explanation, mechanism, safety info, side effects
- [x] Create Monthly Cost Optimizer with table showing current vs optimized costs for each medicine
- [x] Add price trend simulation data (3-month history, rising/falling/stable indicators)
- [x] Build price alert banners for overpriced medicines (>20% above average)
- [x] Add annual savings projection for chronic condition medicines

## Phase 3: Smart Pharmacy Ranking, Community Trust, Drug Interactions & Jan Aushadhi Integration ✅
- [x] Implement Smart Pharmacy Score algorithm (price 40%, distance 30%, availability 20%, trust 10%)
- [x] Add community trust signals section with user confirmation counts, ratings, and issue reports
- [x] Build drug interaction checker for multiple medicines with severity levels (severe/moderate/mild)
- [x] Enhance Jan Aushadhi integration with government badge, price comparison, and nearest kendra
- [x] Polish combined output structure: overpay alert → overview → explanation → alternatives → Jan Aushadhi → trends → cost optimizer → pharmacy ranking → community trust → interactions

## Phase 4: Login/Signup Page & Auth State ✅
- [x] Create AuthState with login/signup/logout, session tracking, user profile (name, email, phone, address)
- [x] Build login page with email/password form, "Remember me", forgot password link
- [x] Build signup page with name, email, phone, password, confirm password, validation
- [x] Add auth-aware navbar (show user avatar + name when logged in, login/signup buttons when not)
- [x] Protect cart and checkout routes behind auth guard (redirect to login if not logged in)

## Phase 5: Online Medicine Shopping — Shop Page, Cart & Checkout ✅
- [x] Create ShopState with cart management (add/remove/update qty), order history, checkout flow
- [x] Build /shop page with medicine product cards (image placeholder, name, price, add-to-cart, qty selector)
- [x] Build /cart page with cart items list, quantity controls, subtotal/total, "Proceed to Checkout" button
- [x] Build /checkout page with delivery address form, order summary, payment method selection, place order
- [x] Add cart icon with badge count in navbar, order confirmation toast, order success page
