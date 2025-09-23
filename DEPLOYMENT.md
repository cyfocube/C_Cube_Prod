# C-Cube Web Deployment Guide

This guide covers how to deploy C-Cube Tutorial Wallet to various web hosting platforms.

## Pre-Deployment Checklist

1. ✅ Ensure your code is committed to GitHub
2. ✅ Test the build locally: `npm run build-web`
3. ✅ Test locally with: `npm run preview`
4. ✅ Verify all educational disclaimers are in place
5. ✅ Update any environment-specific configurations

## Deployment Platforms

### 1. Netlify (Recommended)

Netlify offers excellent support for React applications with automatic deployments.

#### Method 1: Git Integration (Recommended)
1. Push your code to GitHub
2. Go to [netlify.com](https://netlify.com) and sign up/login
3. Click "New site from Git"
4. Choose GitHub and select your repository
5. Configure build settings:
   - **Build command**: `npm run build-web`
   - **Publish directory**: `build`
   - **Node version**: Set environment variable `NODE_VERSION` to `18`
6. Click "Deploy site"

#### Method 2: Manual Upload
1. Build the project: `npm run build-web`
2. Go to [netlify.com](https://netlify.com)
3. Drag and drop the `build` folder to the deployment area

#### Custom Domain (Optional)
1. In Netlify dashboard, go to Site settings > Domain management
2. Add your custom domain
3. Configure DNS records as instructed

### 2. Vercel

Vercel provides excellent React support with zero configuration.

#### Git Integration
1. Push your code to GitHub
2. Go to [vercel.com](https://vercel.com) and sign up/login
3. Click "New Project"
4. Import your GitHub repository
5. Vercel will auto-detect React settings
6. Click "Deploy"

#### Manual Deployment
```bash
# Install Vercel CLI
npm i -g vercel

# Build and deploy
npm run build-web
vercel --prod
```

### 3. GitHub Pages

Free hosting directly from your GitHub repository.

#### Using GitHub Actions (Included)
1. Push your code to GitHub
2. Go to repository Settings > Pages
3. Choose "GitHub Actions" as the source
4. The included workflow will automatically deploy on push to main branch

#### Manual Setup
```bash
# Install gh-pages
npm install --save-dev gh-pages

# Add to package.json scripts:
"deploy": "gh-pages -d build"

# Build and deploy
npm run build-web
npm run deploy
```

### 4. Firebase Hosting

Google's Firebase offers fast, secure hosting.

#### Setup
```bash
# Install Firebase CLI
npm install -g firebase-tools

# Login and initialize
firebase login
firebase init hosting

# Configure firebase.json:
{
  "hosting": {
    "public": "build",
    "ignore": ["firebase.json", "**/.*", "**/node_modules/**"],
    "rewrites": [
      {
        "source": "**",
        "destination": "/index.html"
      }
    ]
  }
}

# Build and deploy
npm run build-web
firebase deploy
```

### 5. Heroku

Deploy to Heroku with a simple Node.js server.

#### Setup
1. Create `server.js` in project root:
```javascript
const express = require('express');
const path = require('path');
const app = express();
const port = process.env.PORT || 3000;

app.use(express.static(path.join(__dirname, 'build')));

app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'build', 'index.html'));
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
```

2. Add to `package.json`:
```json
{
  "scripts": {
    "heroku-postbuild": "npm run build-web",
    "start": "node server.js"
  },
  "dependencies": {
    "express": "^4.18.2"
  }
}
```

3. Deploy:
```bash
# Install Heroku CLI and login
heroku create your-app-name
git push heroku main
```

### 6. AWS S3 + CloudFront

Enterprise-grade hosting with AWS.

#### Setup
1. Create S3 bucket with static website hosting
2. Upload build files to S3
3. Configure CloudFront distribution
4. Set up Route 53 for custom domain (optional)

```bash
# Using AWS CLI
aws s3 sync build/ s3://your-bucket-name --delete
aws cloudfront create-invalidation --distribution-id YOUR_DISTRIBUTION_ID --paths "/*"
```

## Environment Configuration

### Environment Variables
Create `.env.production` for production-specific settings:
```
REACT_APP_NODE_ENV=production
REACT_APP_VERSION=1.0.0
GENERATE_SOURCEMAP=false
```

### Custom Domain Setup
1. **DNS Configuration**: Point your domain to the hosting platform
2. **HTTPS**: Ensure SSL certificate is configured
3. **Security Headers**: Configure security headers (included in netlify.toml and vercel.json)

## Post-Deployment Checklist

1. ✅ Test the live application thoroughly
2. ✅ Verify all pages load correctly
3. ✅ Test wallet creation and operations
4. ✅ Confirm educational disclaimers are visible
5. ✅ Test on different browsers and devices
6. ✅ Verify HTTPS is working
7. ✅ Test performance with browser dev tools
8. ✅ Confirm analytics/monitoring (if implemented)

## Monitoring and Maintenance

### Analytics
Consider adding analytics to track usage:
- Google Analytics
- Plausible Analytics (privacy-focused)
- Fathom Analytics

### Error Monitoring
- Sentry for error tracking
- LogRocket for session replay
- Bugsnag for error monitoring

### Performance Monitoring
- Lighthouse CI for automated auditing
- Web Vitals monitoring
- CDN performance tracking

## Troubleshooting

### Common Issues

#### Build Failures
```bash
# Clear cache and rebuild
npm run clean  # If available
rm -rf node_modules package-lock.json
npm install
npm run build-web
```

#### Routing Issues
- Ensure your hosting platform redirects all routes to index.html
- Check that the `_redirects` file (Netlify) or `vercel.json` is configured correctly

#### Environment Variables Not Working
- Prefix React environment variables with `REACT_APP_`
- Check that variables are defined in the hosting platform's settings

#### HTTPS Mixed Content
- Ensure all external resources use HTTPS
- Check that API calls are made to HTTPS endpoints

### Performance Optimization

#### Bundle Size Optimization
```bash
# Analyze bundle size
npm install --save-dev webpack-bundle-analyzer
npm run build-web
npx webpack-bundle-analyzer build/static/js/*.js
```

#### Image Optimization
- Use WebP format for better compression
- Implement lazy loading for images
- Use responsive images with different sizes

#### Caching Strategy
- Configure proper cache headers
- Use service workers for offline functionality
- Implement bundle splitting for better caching

## Security Considerations

### Web-Specific Security
1. **Content Security Policy**: Configure CSP headers
2. **HTTPS Only**: Force HTTPS redirects
3. **Secure Headers**: Implement security headers
4. **Regular Updates**: Keep dependencies updated

### Educational Context
- Prominently display educational disclaimers
- Make it clear this is for learning only
- Provide links to production wallet recommendations
- Include security education resources

## Cost Considerations

### Free Tiers
- **Netlify**: 100GB bandwidth/month, unlimited sites
- **Vercel**: 100GB bandwidth/month, unlimited deployments
- **GitHub Pages**: Unlimited public repositories
- **Firebase**: 1GB storage, 10GB bandwidth/month

### Paid Options
- **Netlify Pro**: $19/month for teams features
- **Vercel Pro**: $20/month for teams features
- **AWS**: Pay-as-you-go pricing
- **Heroku**: $7/month for hobby dynos

Choose based on your traffic expectations and feature requirements.

## Support and Community

- GitHub Issues for bug reports
- Discussions for feature requests
- Discord/Slack for community support
- Documentation website for guides

Happy deploying! 🚀