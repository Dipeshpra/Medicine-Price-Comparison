# Affordable Medicine Intelligence Platform — Full Feature Upgrade

## Phase 1: Smart Substitution Confidence Score & Overpay Alert System ✅
- [x] Add confidence score calculation logic to medicine state
- [x] Add NTI drug detection and auto-cap at 60%
- [x] Build overpay alert banner on results page
- [x] Display confidence score badges on all alternative medicine cards
- [x] Add overpay thresholds

## Phase 2: Explain Like a Doctor, Monthly Cost Optimizer & Price Trends ✅
- [x] Build "Explain Like a Doctor" panel
- [x] Create Monthly Cost Optimizer
- [x] Add price trend simulation data
- [x] Build price alert banners
- [x] Add annual savings projection

## Phase 3: Smart Pharmacy Ranking, Community Trust, Drug Interactions & Jan Aushadhi Integration ✅
- [x] Implement Smart Pharmacy Score algorithm
- [x] Add community trust signals section
- [x] Build drug interaction checker
- [x] Enhance Jan Aushadhi integration
- [x] Polish combined output structure

## Phase 4: Login/Signup Page & Auth State ✅
- [x] Create AuthState with login/signup/logout
- [x] Build login page with email/password
- [x] Build signup page with validation
- [x] Add auth-aware navbar
- [x] Protect checkout route behind auth guard

## Phase 5: Online Medicine Shopping — Shop Page, Cart & Checkout ✅
- [x] Create ShopState with cart management
- [x] Build /shop page with product cards
- [x] Build /cart page
- [x] Build /checkout page
- [x] Add cart icon with badge count in navbar

## Phase 6: Enhanced Auth with Database, Password Hashing, Sessions & Profile
- [ ] Create SQLModel database models (User, UserMedicine, MedicineReminder) with proper fields (UUID PKs, hashed passwords, provider, email_verified)
- [ ] Implement bcrypt password hashing in AuthState (hash on signup, verify on login)
- [ ] Add secure session token generation and cookie-based session persistence
- [ ] Rebuild login/signup to use database with proper error handling and duplicate prevention
- [ ] Add logout confirmation modal popup ("Are you sure?")

## Phase 7: Medicine Expiry Tracker, Reminders & Profile Page
- [ ] Build /profile page showing user info, editable fields, saved medicines list
- [ ] Build /tracker page for Medicine Expiry Tracker (add medicine name, expiry date, dosage, reminders)
- [ ] Add medicine CRUD operations (add/edit/delete tracked medicines)
- [ ] Add reminder system (set reminder time, frequency daily/weekly, toggle active)
- [ ] Add expiry monitoring dashboard (color-coded: expired/expiring soon/safe, sorted by expiry date)
