import React, { useState } from 'react';
import styled from 'styled-components';
import Footer from '../components/Footer_New';

const FAQContainer = styled.div`
  min-height: 100vh;
  background: #0a0a0a;
  padding: 80px 20px 40px;
  color: #e0e0e0;
`;

const FAQCard = styled.div`
  max-width: 800px;
  margin: 0 auto;
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 20px;
  padding: 40px;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
`;

const Header = styled.div`
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 60px 40px;
  text-align: center;
`;

const Title = styled.h1`
  font-size: 2.5rem;
  margin-bottom: 30px;
  text-align: center;
  background: linear-gradient(135deg, #4ade80, #06b6d4);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  font-weight: 700;
  letter-spacing: -0.5px;
`;

const Subtitle = styled.p`
  font-size: 1.2rem;
  opacity: 0.9;
  font-weight: 400;
  line-height: 1.6;
`;

const FAQBody = styled.div`
  padding: 60px 40px;

  @media (max-width: 768px) {
    padding: 40px 20px;
  }
`;

const SearchBox = styled.div`
  margin-bottom: 40px;
`;

const SearchBar = styled.input`
  width: 100%;
  padding: 12px 20px;
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 25px;
  font-size: 1rem;
  margin-bottom: 30px;
  background: rgba(255, 255, 255, 0.05);
  color: #e0e0e0;
  transition: all 0.3s ease;

  &:focus {
    border-color: #4ade80;
    outline: none;
    box-shadow: 0 0 0 3px rgba(74, 222, 128, 0.1);
  }

  &::placeholder {
    color: #888;
  }
`;

const CategoryFilter = styled.div`
  margin-bottom: 30px;
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
`;

const FilterButton = styled.button`
  padding: 8px 16px;
  border: 2px solid ${props => props.active ? '#4ade80' : 'rgba(255, 255, 255, 0.2)'};
  background: ${props => props.active ? '#4ade80' : 'rgba(255, 255, 255, 0.05)'};
  color: ${props => props.active ? '#0a0a0a' : '#e0e0e0'};
  border-radius: 20px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-size: 0.9rem;
  font-weight: 500;

  &:hover {
    border-color: #4ade80;
    background: ${props => props.active ? '#4ade80' : 'rgba(74, 222, 128, 0.1)'};
    color: ${props => props.active ? '#0a0a0a' : '#4ade80'};
  }
`;

const FAQSection = styled.div`
  margin-bottom: 40px;
`;

const SectionTitle = styled.h2`
  font-size: 1.8rem;
  color: #2c3e50;
  margin-bottom: 20px;
  border-bottom: 2px solid #667eea;
  padding-bottom: 10px;
`;

const FAQItem = styled.div`
  margin-bottom: 25px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 12px;
  overflow: hidden;
  background: rgba(255, 255, 255, 0.02);
  transition: all 0.3s ease;

  &:hover {
    border-color: rgba(74, 222, 128, 0.3);
    box-shadow: 0 4px 20px rgba(74, 222, 128, 0.1);
  }
`;

const FAQQuestion = styled.div`
  padding: 20px;
  background: rgba(255, 255, 255, 0.05);
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-weight: 600;
  color: #e0e0e0;
  font-size: 1.1rem;
  transition: all 0.3s ease;

  &:hover {
    background: rgba(255, 255, 255, 0.08);
    color: #4ade80;
  }

  .icon {
    transition: transform 0.3s ease;
    color: #4ade80;
    font-size: 1.2rem;
    transform: ${props => props.isOpen ? 'rotate(180deg)' : 'rotate(0deg)'};
  }
`;

const QuestionText = styled.span`
  font-size: 1.1rem;
`;

const ExpandIcon = styled.span`
  font-size: 1.2rem;
  color: #667eea;
  transform: ${props => props.isOpen ? 'rotate(180deg)' : 'rotate(0deg)'};
  transition: transform 0.3s ease;
`;

const Answer = styled.div`
  padding: ${props => props.isOpen ? '0 20px 20px 20px' : '0'};
  max-height: ${props => props.isOpen ? '500px' : '0'};
  overflow: hidden;
  transition: all 0.3s ease;
  background: rgba(255, 255, 255, 0.02);
  border-top: ${props => props.isOpen ? '1px solid rgba(255, 255, 255, 0.1)' : 'none'};
  
  p {
    color: #b0b0b0;
    line-height: 1.6;
    margin-bottom: 15px;
  }

  ul {
    margin: 15px 0;
    padding-left: 20px;
  }

  li {
    margin-bottom: 8px;
    color: #b0b0b0;
  }

  strong {
    color: #e0e0e0;
    font-weight: 600;
  }

  code {
    background: rgba(255, 255, 255, 0.1);
    padding: 2px 6px;
    border-radius: 4px;
    font-family: 'Share Tech Mono', monospace;
    color: #4ade80;
  }
`;

const NoResults = styled.div`
  text-align: center;
  padding: 40px;
  color: #666;
  font-style: italic;
`;

const FAQ = () => {
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('all');
  const [openItems, setOpenItems] = useState({});

  const categories = [
    { id: 'all', label: 'All' },
    { id: 'general', label: 'General' },
    { id: 'security', label: 'Security' },
    { id: 'technical', label: 'Technical' },
    { id: 'wallet', label: 'Wallet' },
    { id: 'defi', label: 'DeFi' }
  ];

  const faqData = [
    {
      category: 'general',
      question: 'What is CyFoCube and what does it offer?',
      answer: `
        <p>CyFoCube is an educational platform focused on blockchain technology and cryptocurrency education. Our mission is to provide safe, accessible learning environments for people at all experience levels.</p>
        <p>We offer:</p>
        <ul>
          <li>Educational wallet applications for learning about cryptocurrency storage</li>
          <li>Interactive tutorials on blockchain fundamentals</li>
          <li>Safe testing environments that don't require real cryptocurrency</li>
          <li>Comprehensive educational content about DeFi, security, and best practices</li>
          <li>Tools designed specifically for educational purposes</li>
        </ul>
      `
    },
    {
      category: 'general',
      question: 'Is CyFoCube suitable for beginners?',
      answer: `
        <p>Absolutely! CyFoCube is designed with beginners in mind. Our educational approach ensures that complex concepts are broken down into digestible, easy-to-understand lessons.</p>
        <p>We provide:</p>
        <ul>
          <li>Step-by-step tutorials</li>
          <li>Risk-free learning environments</li>
          <li>Clear explanations of technical concepts</li>
          <li>Progressive learning paths from basic to advanced topics</li>
        </ul>
      `
    },
    {
      category: 'security',
      question: 'How does CyFoCube ensure the security of educational tools?',
      answer: `
        <p>Security is our top priority. CyFoCube educational tools are designed with multiple security layers:</p>
        <ul>
          <li><strong>Educational Focus:</strong> Our tools are designed for learning, not for managing real cryptocurrency</li>
          <li><strong>Isolated Environments:</strong> Educational wallets operate in safe, controlled environments</li>
          <li><strong>No Real Fund Risk:</strong> Most educational features work with test networks and simulated scenarios</li>
          <li><strong>Best Practice Teaching:</strong> We emphasize security best practices throughout all educational content</li>
          <li><strong>Regular Updates:</strong> All educational tools are regularly updated with the latest security standards</li>
        </ul>
      `
    },
    {
      category: 'wallet',
      question: 'What is a cold wallet and why is it important?',
      answer: `
        <p>A cold wallet is a cryptocurrency storage method that keeps your private keys completely offline, disconnected from the internet. This makes it one of the most secure ways to store cryptocurrency.</p>
        <p><strong>Key benefits of cold storage:</strong></p>
        <ul>
          <li>Protection from online attacks and hacking attempts</li>
          <li>Immune to malware and computer viruses</li>
          <li>Long-term secure storage for large amounts</li>
          <li>Full control over your private keys</li>
        </ul>
        <p>CyFoCube's educational cold wallet helps you understand these concepts safely before working with real cryptocurrency.</p>
      `
    },
    {
      category: 'wallet',
      question: 'What\'s the difference between hot and cold wallets?',
      answer: `
        <p><strong>Hot Wallets:</strong></p>
        <ul>
          <li>Connected to the internet</li>
          <li>Convenient for frequent transactions</li>
          <li>More vulnerable to online attacks</li>
          <li>Best for small amounts of daily-use cryptocurrency</li>
        </ul>
        <p><strong>Cold Wallets:</strong></p>
        <ul>
          <li>Completely offline storage</li>
          <li>Maximum security for long-term storage</li>
          <li>Less convenient for frequent transactions</li>
          <li>Best for large amounts or long-term holding</li>
        </ul>
        <p>Our educational platform helps you understand when and how to use each type effectively.</p>
      `
    },
    {
      category: 'technical',
      question: 'What blockchain networks does CyFoCube support for education?',
      answer: `
        <p>CyFoCube educational tools support learning about multiple blockchain networks:</p>
        <ul>
          <li><strong>Ethereum:</strong> Smart contracts, DeFi, and ERC-20 tokens</li>
          <li><strong>Bitcoin:</strong> Digital payments and store of value concepts</li>
          <li><strong>Polygon:</strong> Layer 2 scaling solutions and lower gas fees</li>
          <li><strong>Binance Smart Chain:</strong> Alternative smart contract platform</li>
          <li><strong>Test Networks:</strong> Safe environments for all major networks</li>
        </ul>
        <p>All educational features prioritize test networks to ensure safe learning without financial risk.</p>
      `
    },
    {
      category: 'security',
      question: 'How should I backup my educational wallet?',
      answer: `
        <p>Even for educational purposes, understanding proper backup procedures is crucial:</p>
        <ul>
          <li><strong>Seed Phrase:</strong> Write down your 12-24 word recovery phrase</li>
          <li><strong>Multiple Copies:</strong> Store copies in different secure locations</li>
          <li><strong>Offline Storage:</strong> Never store seed phrases digitally or online</li>
          <li><strong>Verify Recovery:</strong> Test your backup by recovering the wallet</li>
          <li><strong>Secure Storage:</strong> Use fireproof and waterproof storage solutions</li>
        </ul>
        <p>Our educational tools teach these concepts thoroughly before you need them for real cryptocurrency.</p>
      `
    },
    {
      category: 'defi',
      question: 'What is DeFi and how can I learn about it safely?',
      answer: `
        <p>Decentralized Finance (DeFi) refers to financial services built on blockchain technology without traditional intermediaries like banks.</p>
        <p><strong>Common DeFi concepts include:</strong></p>
        <ul>
          <li>Decentralized exchanges (DEXs)</li>
          <li>Lending and borrowing protocols</li>
          <li>Yield farming and liquidity mining</li>
          <li>Synthetic assets and derivatives</li>
        </ul>
        <p>CyFoCube provides educational content and simulations to help you understand DeFi concepts without the risks associated with real protocols. Always learn and practice in educational environments before engaging with real DeFi applications.</p>
      `
    },
    {
      category: 'technical',
      question: 'Can I use CyFoCube tools on mobile devices?',
      answer: `
        <p>Yes! CyFoCube educational tools are designed to work across multiple platforms:</p>
        <ul>
          <li><strong>Web Browsers:</strong> Access through any modern web browser</li>
          <li><strong>Desktop Applications:</strong> Native apps for Windows, macOS, and Linux</li>
          <li><strong>Mobile Responsive:</strong> Web interface adapts to mobile screens</li>
          <li><strong>Cross-Platform:</strong> Your educational progress syncs across devices</li>
        </ul>
        <p>This flexibility ensures you can learn about blockchain technology wherever you are, on whatever device you prefer.</p>
      `
    },
    {
      category: 'general',
      question: 'Are CyFoCube educational tools free to use?',
      answer: `
        <p>Yes! CyFoCube is committed to making blockchain education accessible to everyone. Our core educational tools and content are provided free of charge.</p>
        <p><strong>What's included for free:</strong></p>
        <ul>
          <li>Educational wallet applications</li>
          <li>Comprehensive learning content</li>
          <li>Interactive tutorials and guides</li>
          <li>Safe testing environments</li>
          <li>Community support and resources</li>
        </ul>
        <p>Our mission is education and accessibility, not profit from educational tools.</p>
      `
    },
    {
      category: 'security',
      question: 'What are the common security mistakes to avoid in cryptocurrency?',
      answer: `
        <p>Understanding common security mistakes is crucial for cryptocurrency safety:</p>
        <ul>
          <li><strong>Phishing Attacks:</strong> Always verify website URLs and never enter seed phrases on suspicious sites</li>
          <li><strong>Weak Passwords:</strong> Use strong, unique passwords for all crypto-related accounts</li>
          <li><strong>Public Wi-Fi:</strong> Avoid accessing wallets on public or unsecured networks</li>
          <li><strong>Seed Phrase Exposure:</strong> Never share or store seed phrases online</li>
          <li><strong>Fake Apps:</strong> Only download wallet apps from official sources</li>
          <li><strong>Social Engineering:</strong> Be wary of unsolicited contact claiming to help with crypto issues</li>
        </ul>
        <p>CyFoCube educational tools help you recognize and avoid these common pitfalls in a safe learning environment.</p>
      `
    },
    {
      category: 'technical',
      question: 'How do transaction fees work in different blockchain networks?',
      answer: `
        <p>Transaction fees (gas fees) vary significantly between blockchain networks:</p>
        <ul>
          <li><strong>Ethereum:</strong> Higher fees during network congestion, measured in gwei</li>
          <li><strong>Bitcoin:</strong> Fees based on transaction size and network demand</li>
          <li><strong>Polygon:</strong> Significantly lower fees as a Layer 2 solution</li>
          <li><strong>Binance Smart Chain:</strong> Generally lower fees than Ethereum</li>
        </ul>
        <p>Our educational tools help you understand fee structures and learn strategies for minimizing costs when the time comes to use real cryptocurrency networks.</p>
      `
    }
  ];

  const toggleItem = (index) => {
    setOpenItems(prev => ({
      ...prev,
      [index]: !prev[index]
    }));
  };

  const filteredFAQs = faqData.filter(item => {
    const matchesSearch = item.question.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         item.answer.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesCategory = selectedCategory === 'all' || item.category === selectedCategory;
    return matchesSearch && matchesCategory;
  });

  const groupedFAQs = filteredFAQs.reduce((acc, item, index) => {
    const category = item.category;
    if (!acc[category]) {
      acc[category] = [];
    }
    acc[category].push({ ...item, originalIndex: index });
    return acc;
  }, {});

  return (
    <>
      <FAQContainer className="website-page">
        <FAQCard>
          <Header>
            <Title>Frequently Asked Questions</Title>
            <Subtitle>Find answers to common questions about blockchain education and CyFoCube</Subtitle>
          </Header>

          <FAQBody>
          <SearchBox>
            <SearchBar
              type="text"
              placeholder="Search questions..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
            />
          </SearchBox>

          <CategoryFilter>
            {categories.map(category => (
              <FilterButton
                key={category.id}
                active={selectedCategory === category.id}
                onClick={() => setSelectedCategory(category.id)}
              >
                {category.label}
              </FilterButton>
            ))}
          </CategoryFilter>

          {Object.keys(groupedFAQs).length === 0 ? (
            <NoResults>
              No questions found matching your search criteria. Try different keywords or categories.
            </NoResults>
          ) : (
            Object.entries(groupedFAQs).map(([category, items]) => (
              <FAQSection key={category}>
                <SectionTitle>
                  {categories.find(cat => cat.id === category)?.label || category}
                </SectionTitle>
                {items.map((item, index) => (
                  <FAQItem key={`${category}-${index}`}>
                    <Question
                      isOpen={openItems[`${category}-${index}`]}
                      onClick={() => toggleItem(`${category}-${index}`)}
                    >
                      <QuestionText>{item.question}</QuestionText>
                      <ExpandIcon isOpen={openItems[`${category}-${index}`]}>▼</ExpandIcon>
                    </Question>
                    <Answer
                      isOpen={openItems[`${category}-${index}`]}
                      dangerouslySetInnerHTML={{ __html: item.answer }}
                    />
                  </FAQItem>
                ))}
              </FAQSection>
            ))
          )}
        </FAQBody>
      </FAQCard>
      </FAQContainer>
      <Footer />
    </>
  );
};

export default FAQ;