<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Insurance Company of Africa - Management System</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        header {
            text-align: center;
            color: white;
            margin-bottom: 40px;
            padding: 40px 0;
        }

        h1 {
            font-size: 3rem;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }

        .subtitle {
            font-size: 1.2rem;
            opacity: 0.9;
        }

        .dashboard {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 25px;
            margin-bottom: 40px;
        }

        .card {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            backdrop-filter: blur(10px);
        }

        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 40px rgba(0,0,0,0.2);
        }

        .card h3 {
            color: #4a5568;
            margin-bottom: 15px;
            font-size: 1.4rem;
            display: flex;
            align-items: center;
        }

        .card-icon {
            width: 30px;
            height: 30px;
            margin-right: 10px;
            background: linear-gradient(45deg, #667eea, #764ba2);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: bold;
        }

        .api-section {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            padding: 30px;
            margin-bottom: 30px;
            backdrop-filter: blur(10px);
        }

        .api-endpoints {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 15px;
            margin-top: 20px;
        }

        .endpoint {
            background: #f8f9fa;
            padding: 15px;
            border-radius: 8px;
            border-left: 4px solid #667eea;
            transition: background-color 0.3s ease;
        }

        .endpoint:hover {
            background: #e9ecef;
        }

        .endpoint-url {
            font-family: 'Courier New', monospace;
            color: #667eea;
            font-weight: bold;
            margin-bottom: 5px;
        }

        .endpoint-desc {
            font-size: 0.9rem;
            color: #666;
        }

        .stats {
            display: flex;
            justify-content: space-around;
            text-align: center;
            margin-top: 20px;
        }

        .stat-item {
            padding: 15px;
        }

        .stat-number {
            font-size: 2rem;
            font-weight: bold;
            color: #667eea;
            display: block;
        }

        .stat-label {
            color: #666;
            font-size: 0.9rem;
        }

        .quick-actions {
            display: flex;
            gap: 15px;
            flex-wrap: wrap;
            margin-top: 20px;
        }

        .btn {
            background: linear-gradient(45deg, #667eea, #764ba2);
            color: white;
            padding: 12px 24px;
            border: none;
            border-radius: 25px;
            text-decoration: none;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            font-weight: 500;
            display: inline-block;
        }

        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        }

        .status-indicator {
            display: inline-block;
            width: 12px;
            height: 12px;
            background: #28a745;
            border-radius: 50%;
            margin-right: 8px;
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0% { opacity: 1; }
            50% { opacity: 0.5; }
            100% { opacity: 1; }
        }

        footer {
            text-align: center;
            color: white;
            opacity: 0.8;
            margin-top: 40px;
        }

        @media (max-width: 768px) {
            h1 {
                font-size: 2rem;
            }
            
            .dashboard {
                grid-template-columns: 1fr;
            }
            
            .stats {
                flex-direction: column;
                gap: 10px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🏢 Insurance Company of Africa</h1>
            <p class="subtitle">Comprehensive Management System</p>
            <p><span class="status-indicator"></span>System Online</p>
        </header>

        <div class="dashboard">
            <div class="card">
                <h3><span class="card-icon">👥</span>Client Management</h3>
                <p>Manage client information, policies, and relationships. Track customer interactions and maintain comprehensive records.</p>
                <div class="quick-actions">
                    <a href="/clients" class="btn">View Clients</a>
                    <a href="/customers" class="btn">Customers</a>
                </div>
            </div>

            <div class="card">
                <h3><span class="card-icon">📋</span>Policy Administration</h3>
                <p>Create, modify, and track insurance policies. Manage policy lifecycle from inception to claims.</p>
                <div class="quick-actions">
                    <a href="/policies" class="btn">Manage Policies</a>
                    <a href="/products" class="btn">Products</a>
                </div>
            </div>

            <div class="card">
                <h3><span class="card-icon">💰</span>Financial Operations</h3>
                <p>Handle premiums, commissions, and financial transactions. Monitor cash flow and generate reports.</p>
                <div class="quick-actions">
                    <a href="/premiums" class="btn">Premiums</a>
                    <a href="/ledger" class="btn">Ledger</a>
                </div>
            </div>

            <div class="card">
                <h3><span class="card-icon">🎯</span>Claims & Risk</h3>
                <p>Process insurance claims and manage reinsurance operations. Track claim status and settlements.</p>
                <div class="quick-actions">
                    <a href="/claims" class="btn">Claims</a>
                    <a href="/reinsurance" class="btn">Reinsurance</a>
                </div>
            </div>
        </div>

        <div class="api-section">
            <h2>🔗 API Endpoints</h2>
            <p>Access the Insurance Management System through our RESTful API endpoints:</p>
            
            <div class="api-endpoints">
                <div class="endpoint">
                    <div class="endpoint-url">/clients</div>
                    <div class="endpoint-desc">Client management operations</div>
                </div>
                <div class="endpoint">
                    <div class="endpoint-url">/policies</div>
                    <div class="endpoint-desc">Policy administration</div>
                </div>
                <div class="endpoint">
                    <div class="endpoint-url">/products</div>
                    <div class="endpoint-desc">Insurance products catalog</div>
                </div>
                <div class="endpoint">
                    <div class="endpoint-url">/premiums</div>
                    <div class="endpoint-desc">Premium calculations & payments</div>
                </div>
                <div class="endpoint">
                    <div class="endpoint-url">/commissions</div>
                    <div class="endpoint-desc">Agent commission tracking</div>
                </div>
                <div class="endpoint">
                    <div class="endpoint-url">/claims</div>
                    <div class="endpoint-desc">Claims processing & loans</div>
                </div>
                <div class="endpoint">
                    <div class="endpoint-url">/customers</div>
                    <div class="endpoint-desc">Customer relationship management</div>
                </div>
                <div class="endpoint">
                    <div class="endpoint-url">/agents</div>
                    <div class="endpoint-desc">Agent management system</div>
                </div>
                <div class="endpoint">
                    <div class="endpoint-url">/documents</div>
                    <div class="endpoint-desc">Document management</div>
                </div>
                <div class="endpoint">
                    <div class="endpoint-url">/audit</div>
                    <div class="endpoint-desc">Audit trail & compliance</div>
                </div>
                <div class="endpoint">
                    <div class="endpoint-url">/ledger</div>
                    <div class="endpoint-desc">Financial ledger operations</div>
                </div>
                <div class="endpoint">
                    <div class="endpoint-url">/reinsurance</div>
                    <div class="endpoint-desc">Reinsurance management</div>
                </div>
            </div>

            <div class="stats">
                <div class="stat-item">
                    <span class="stat-number">12</span>
                    <span class="stat-label">API Modules</span>
                </div>
                <div class="stat-item">
                    <span class="stat-number">50+</span>
                    <span class="stat-label">Endpoints</span>
                </div>
                <div class="stat-item">
                    <span class="stat-number">24/7</span>
                    <span class="stat-label">Availability</span>
                </div>
            </div>

            <div class="quick-actions">
                <a href="/docs" class="btn">📚 API Documentation</a>
                <a href="/redoc" class="btn">📖 ReDoc</a>
            </div>
        </div>

        <footer>
            <p>&copy; 2024 Insurance Company of Africa. All rights reserved.</p>
            <p>Powered by FastAPI & Modern Web Technologies</p>
        </footer>
    </div>

    <script>
        // Simple script to enhance user experience
        document.addEventListener('DOMContentLoaded', function() {
            // Add loading effect for buttons
            const buttons = document.querySelectorAll('.btn');
            buttons.forEach(button => {
                button.addEventListener('click', function(e) {
                    // Add a subtle loading effect
                    this.style.opacity = '0.8';
                    setTimeout(() => {
                        this.style.opacity = '1';
                    }, 200);
                });
            });

            // Update system status
            const statusIndicator = document.querySelector('.status-indicator');
            setInterval(() => {
                fetch('/')
                    .then(response => {
                        if (response.ok) {
                            statusIndicator.style.background = '#28a745';
                        }
                    })
                    .catch(() => {
                        statusIndicator.style.background = '#dc3545';
                    });
            }, 30000); // Check every 30 seconds
        });
    </script>
</body>
</html>
