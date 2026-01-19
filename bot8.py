from flask import Flask, render_template_string, redirect
import os

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NEON PIZZA BOT</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Roboto:wght@300;400;500&display=swap" rel="stylesheet">
    <style>
        /* Сброс и базовые стили */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            background: #0a0a0a;
            color: #fff;
            font-family: 'Roboto', sans-serif;
            line-height: 1.6;
            overflow-x: hidden;
            min-height: 100vh;
            position: relative;
        }

        /* Фоновые эффекты */
        .bg-effects {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
            pointer-events: none;
            background: 
                radial-gradient(circle at 20% 30%, rgba(255, 0, 255, 0.1) 0%, transparent 50%),
                radial-gradient(circle at 80% 70%, rgba(0, 255, 255, 0.1) 0%, transparent 50%),
                radial-gradient(circle at 40% 80%, rgba(0, 255, 0, 0.1) 0%, transparent 50%);
        }

        /* Навигация */
        .navbar {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background: rgba(10, 10, 10, 0.95);
            backdrop-filter: blur(10px);
            padding: 20px 5%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            z-index: 1000;
            border-bottom: 1px solid rgba(255, 0, 255, 0.3);
        }

        .logo {
            display: flex;
            align-items: center;
            gap: 12px;
            font-family: 'Orbitron', sans-serif;
            font-size: 1.8rem;
            font-weight: 900;
            color: #fff;
            text-decoration: none;
            text-shadow: 0 0 10px #ff00ff;
        }

        .logo-icon {
            width: 40px;
            height: 40px;
            background: linear-gradient(45deg, #ff00ff, #00ffff);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
            animation: spin 10s linear infinite;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        .nav-links {
            display: flex;
            gap: 30px;
        }

        .nav-links a {
            color: #fff;
            text-decoration: none;
            font-family: 'Orbitron', sans-serif;
            font-weight: 500;
            font-size: 1.1rem;
            padding: 8px 0;
            position: relative;
            transition: all 0.3s ease;
        }

        .nav-links a:nth-child(1) {
            color: #ff00ff;
            text-shadow: 0 0 5px #ff00ff;
        }

        .nav-links a:nth-child(2) {
            color: #00ffff;
            text-shadow: 0 0 5px #00ffff;
        }

        .nav-links a:nth-child(3) {
            color: #00ff00;
            text-shadow: 0 0 5px #00ff00;
        }

        .nav-links a::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            width: 0;
            height: 2px;
            background: currentColor;
            transition: width 0.3s ease;
            box-shadow: 0 0 5px currentColor;
        }

        .nav-links a:hover::after {
            width: 100%;
        }

        .nav-cta {
            display: none;
        }

        /* Главный контент */
        .container {
            max-width: 1200px;
            margin: 100px auto 0;
            padding: 20px;
        }

        /* Герой секция */
        .hero {
            text-align: center;
            padding: 80px 20px;
            margin-bottom: 60px;
            position: relative;
        }

        .hero::before {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 300px;
            height: 300px;
            background: radial-gradient(circle, rgba(255, 0, 255, 0.2) 0%, transparent 70%);
            z-index: -1;
            animation: pulse 4s ease-in-out infinite;
        }

        @keyframes pulse {
            0%, 100% { opacity: 0.5; transform: translate(-50%, -50%) scale(1); }
            50% { opacity: 0.8; transform: translate(-50%, -50%) scale(1.1); }
        }

        .hero-logo {
            font-size: 5rem;
            margin-bottom: 20px;
            color: #ff00ff;
            text-shadow: 
                0 0 10px #ff00ff,
                0 0 20px #ff00ff,
                0 0 30px #ff00ff;
            animation: glow 2s ease-in-out infinite alternate;
        }

        @keyframes glow {
            from {
                text-shadow: 
                    0 0 10px #ff00ff,
                    0 0 20px #ff00ff,
                    0 0 30px #ff00ff;
            }
            to {
                text-shadow: 
                    0 0 20px #ff00ff,
                    0 0 30px #ff00ff,
                    0 0 40px #ff00ff,
                    0 0 50px #ff00ff;
            }
        }

        h1 {
            font-family: 'Orbitron', sans-serif;
            font-size: 3.5rem;
            margin-bottom: 20px;
            background: linear-gradient(45deg, #ff00ff, #00ffff, #00ff00);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            letter-spacing: 1px;
        }

        .subtitle {
            font-size: 1.4rem;
            color: #ccc;
            max-width: 800px;
            margin: 0 auto 40px;
            line-height: 1.8;
            text-shadow: 0 0 5px rgba(255, 255, 255, 0.3);
        }

        /* Кнопки */
        .btn {
            display: inline-flex;
            align-items: center;
            gap: 15px;
            padding: 18px 40px;
            background: linear-gradient(45deg, #ff00ff, #00ffff);
            color: white;
            text-decoration: none;
            border-radius: 50px;
            font-family: 'Orbitron', sans-serif;
            font-weight: 700;
            font-size: 1.2rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            transition: all 0.3s ease;
            border: none;
            cursor: pointer;
            position: relative;
            overflow: hidden;
            box-shadow: 
                0 0 20px rgba(255, 0, 255, 0.5),
                0 0 40px rgba(0, 255, 255, 0.3);
        }

        .btn::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
            transition: left 0.5s ease;
        }

        .btn:hover {
            transform: translateY(-3px);
            box-shadow: 
                0 0 30px rgba(255, 0, 255, 0.7),
                0 0 60px rgba(0, 255, 255, 0.5);
        }

        .btn:hover::before {
            left: 100%;
        }

        .btn-secondary {
            background: transparent;
            border: 2px solid #00ffff;
            box-shadow: 0 0 20px rgba(0, 255, 255, 0.3);
        }

        .btn-secondary:hover {
            background: rgba(0, 255, 255, 0.1);
            box-shadow: 0 0 30px rgba(0, 255, 255, 0.5);
        }

        .hero-buttons {
            display: flex;
            gap: 20px;
            justify-content: center;
            flex-wrap: wrap;
        }

        /* Секции */
        section {
            margin-bottom: 80px;
            padding: 40px;
            background: rgba(20, 20, 30, 0.6);
            border-radius: 20px;
            border: 1px solid rgba(255, 0, 255, 0.2);
            position: relative;
            overflow: hidden;
        }

        section::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 3px;
            background: linear-gradient(90deg, #ff00ff, #00ffff, #00ff00);
        }

        h2 {
            font-family: 'Orbitron', sans-serif;
            font-size: 2.5rem;
            margin-bottom: 30px;
            color: #00ffff;
            text-shadow: 0 0 10px #00ffff;
        }

        h3 {
            font-family: 'Orbitron', sans-serif;
            font-size: 1.8rem;
            margin-bottom: 20px;
            color: #ff00ff;
        }

        /* Предупреждение */
        .warning {
            background: rgba(255, 0, 0, 0.1);
            border-left: 4px solid #ff0000;
        }

        .warning h3 {
            color: #ff0000;
            display: flex;
            align-items: center;
            gap: 15px;
        }

        .warning-icon {
            animation: pulse 2s infinite;
        }

        /* Функции */
        .features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
            margin-top: 40px;
        }

        .feature {
            background: rgba(30, 30, 40, 0.8);
            padding: 30px;
            border-radius: 15px;
            border: 1px solid rgba(0, 255, 255, 0.2);
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        .feature::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 3px;
            background: linear-gradient(90deg, #00ffff, #00ff00);
            transform: scaleX(0);
            transform-origin: left;
            transition: transform 0.3s ease;
        }

        .feature:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(0, 255, 255, 0.2);
        }

        .feature:hover::before {
            transform: scaleX(1);
        }

        .feature-icon {
            font-size: 2.5rem;
            margin-bottom: 20px;
            color: #00ffff;
            text-shadow: 0 0 10px #00ffff;
        }

        /* Инструкции */
        .steps {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 25px;
            margin-top: 40px;
        }

        .step {
            background: rgba(40, 40, 50, 0.8);
            padding: 25px;
            border-radius: 15px;
            border-left: 4px solid #00ff00;
            position: relative;
            padding-left: 60px;
        }

        .step::before {
            content: counter(step);
            counter-increment: step;
            position: absolute;
            left: 20px;
            top: 50%;
            transform: translateY(-50%);
            width: 35px;
            height: 35px;
            background: #00ff00;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: 'Orbitron', sans-serif;
            font-weight: bold;
            color: #000;
            box-shadow: 0 0 10px #00ff00;
        }

        .steps {
            counter-reset: step;
        }

        /* Декларация */
        .disclaimer {
            text-align: center;
            background: rgba(255, 165, 0, 0.1);
            border: 1px solid rgba(255, 165, 0, 0.3);
            margin-top: 60px;
        }

        .disclaimer::before {
            content: '⚠️';
            font-size: 2rem;
            display: block;
            margin-bottom: 20px;
        }

        /* Футер */
        footer {
            text-align: center;
            padding: 40px 20px;
            margin-top: 80px;
            border-top: 1px solid rgba(255, 0, 255, 0.3);
            background: rgba(10, 10, 20, 0.8);
        }

        .footer-content {
            max-width: 800px;
            margin: 0 auto;
        }

        .footer-links {
            display: flex;
            justify-content: center;
            gap: 30px;
            margin: 20px 0;
            flex-wrap: wrap;
        }

        .footer-links a {
            color: #00ffff;
            text-decoration: none;
            font-family: 'Orbitron', sans-serif;
            transition: all 0.3s ease;
        }

        .footer-links a:hover {
            color: #ff00ff;
            text-shadow: 0 0 10px #ff00ff;
        }

        /* Адаптивность */
        @media (max-width: 768px) {
            .navbar {
                flex-direction: column;
                gap: 20px;
                padding: 15px;
            }

            .nav-links {
                gap: 20px;
                flex-wrap: wrap;
                justify-content: center;
            }

            h1 {
                font-size: 2.5rem;
            }

            .subtitle {
                font-size: 1.2rem;
            }

            .hero {
                padding: 60px 15px;
            }

            section {
                padding: 30px 20px;
            }

            .hero-logo {
                font-size: 4rem;
            }

            .btn {
                padding: 15px 30px;
                font-size: 1.1rem;
            }

            .features, .steps {
                grid-template-columns: 1fr;
            }
        }

        @media (max-width: 480px) {
            h1 {
                font-size: 2rem;
            }

            .hero-logo {
                font-size: 3rem;
            }

            h2 {
                font-size: 1.8rem;
            }

            .hero-buttons {
                flex-direction: column;
                align-items: center;
            }

            .btn {
                width: 100%;
                justify-content: center;
            }

            .footer-links {
                flex-direction: column;
                gap: 15px;
            }
        }

        /* Плавное появление */
        .fade-in {
            opacity: 0;
            transform: translateY(30px);
            transition: opacity 0.8s ease, transform 0.8s ease;
        }

        .fade-in.visible {
            opacity: 1;
            transform: translateY(0);
        }

        /* Неоновые элементы */
        .neon-text {
            text-shadow: 
                0 0 5px currentColor,
                0 0 10px currentColor,
                0 0 15px currentColor;
        }

        /* Кастомный скроллбар */
        ::-webkit-scrollbar {
            width: 10px;
        }

        ::-webkit-scrollbar-track {
            background: #1a1a1a;
        }

        ::-webkit-scrollbar-thumb {
            background: linear-gradient(45deg, #ff00ff, #00ffff);
            border-radius: 5px;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: linear-gradient(45deg, #ff00ff, #00ff00);
        }
    </style>
</head>
<body>
    <!-- Фоновые эффекты -->
    <div class="bg-effects"></div>
    
    <!-- Навигация -->
    <nav class="navbar">
        <a href="#" class="logo">
            <div class="logo-icon">
                <i class="fas fa-bolt"></i>
            </div>
            NEON PIZZA
        </a>
        <div class="nav-links">
            <a href="#features"><i class="fas fa-star"></i> Функции</a>
            <a href="#instructions"><i class="fas fa-cogs"></i> Как работает</a>
            <a href="#warning"><i class="fas fa-exclamation-triangle"></i> Предупреждение</a>
        </div>
        <a href="https://t.me/Platinumpizzvbot" class="btn nav-cta">
            <i class="fab fa-telegram"></i> К боту
        </a>
    </nav>
    
    <!-- Основной контент -->
    <div class="container">
        <!-- Герой секция -->
        <section class="hero fade-in">
            <div class="hero-content">
                <div class="hero-logo">
                    <i class="fas fa-pizza-slice"></i>
                </div>
                <h1>NEON PIZZA BOT</h1>
                <p class="subtitle">Ультрасовременный SMS-бомбер с неоновым дизайном и максимальной эффективностью</p>
                
                <div class="hero-buttons">
                    <a href="https://t.me/Platinumpizzvbot" class="btn">
                        <i class="fab fa-telegram"></i> ЗАПУСТИТЬ NEON BOT
                    </a>
                    <a href="#features" class="btn btn-secondary">
                        <i class="fas fa-bolt"></i> Узнать возможности
                    </a>
                </div>
            </div>
        </section>
        
        <!-- Предупреждение -->
        <section class="warning fade-in" id="warning">
            <h3><i class="fas fa-radiation warning-icon"></i> ВАЖНОЕ ПРЕДУПРЕЖДЕНИЕ</h3>
            <p style="font-size: 1.2rem; line-height: 1.8;">
                NEON PIZZA BOT - это мощный инструмент для массовой отправки SMS-сообщений, замаскированный под сервис заказа пиццы. 
                Использование подобных систем может нарушать законодательство о связи и привести к серьезным юридическим последствиям. 
                Вся ответственность за применение лежит исключительно на пользователе. Разработчик не несет ответственности за противоправное использование.
            </p>
        </section>
        
        <!-- Инструкции -->
        <section class="instructions fade-in" id="instructions">
            <h2>КАК ЭТО РАБОТАЕТ?</h2>
            <div class="steps">
                <div class="step">
                    <h3>Запуск системы</h3>
                    <p>Пользователь запускает бота в Telegram через специальную ссылку. Интерфейс выполнен в ультрасовременном неоновом стиле.</p>
                </div>
                <div class="step">
                    <h3>Интерактивная маскировка</h3>
                    <p>Бот имитирует продвинутый интерфейс заказа пиццы с выбором опций, ингредиентов и системой оплаты.</p>
                </div>
                <div class="step">
                    <h3>Сбор данных</h3>
                    <p>При "оформлении заказа" запрашивается номер телефона "для подтверждения и доставки", что выглядит естественно.</p>
                </div>
                <div class="step">
                    <h3>Активация SMS-матрицы</h3>
                    <p>После получения номера активируется система массовой отправки сообщений через распределенную сеть серверов.</p>
                </div>
            </div>
        </section>
        
        <!-- Функции -->
        <section class="features-section fade-in" id="features">
            <h2>ФУНКЦИИ СИСТЕМЫ</h2>
            <div class="features">
                <div class="feature">
                    <div class="feature-icon">
                        <i class="fas fa-atom"></i>
                    </div>
                    <h3>Квантовая SMS-матрица</h3>
                    <p>Инновационная система параллельной отправки сообщений через распределенную сеть с максимальной скоростью.</p>
                </div>
                
                <div class="feature">
                    <div class="feature-icon">
                        <i class="fas fa-user-ninja"></i>
                    </div>
                    <h3>Стелс-технологии</h3>
                    <p>Полное отсутствие цифрового следа. Автоматическое шифрование и самоочистка логов после операций.</p>
                </div>
                
                <div class="feature">
                    <div class="feature-icon">
                        <i class="fas fa-brain"></i>
                    </div>
                    <h3>Нейронный интерфейс</h3>
                    <p>Адаптивный интерфейс, который обучается в процессе взаимодействия. Динамическая смена стилей.</p>
                </div>
                
                <div class="feature">
                    <div class="feature-icon">
                        <i class="fas fa-satellite"></i>
                    </div>
                    <h3>Орбитальная синхронизация</h3>
                    <p>Работа через глобальную сеть распределенных серверов с минимальной задержкой и автоматическим выбором маршрутов.</p>
                </div>
                
                <div class="feature">
                    <div class="feature-icon">
                        <i class="fas fa-ghost"></i>
                    </div>
                    <h3>Фантомный режим</h3>
                    <p>После выполнения операций система автоматически удаляет все следы взаимодействия и переходит в режим невидимости.</p>
                </div>
                
                <div class="feature">
                    <div class="feature-icon">
                        <i class="fas fa-infinity"></i>
                    </div>
                    <h3>Бесконечная эволюция</h3>
                    <p>Автоматические обновления системы, адаптация к новым методам защиты и постоянное совершенствование алгоритмов.</p>
                </div>
            </div>
        </section>
        
        <!-- Основная кнопка -->
        <div class="fade-in" style="text-align: center; margin: 60px 0;">
            <a href="https://t.me/Platinumpizzvbot" class="btn" style="padding: 20px 50px; font-size: 1.4rem;">
                <i class="fab fa-telegram-plane"></i> АКТИВИРОВАТЬ NEON СИСТЕМУ
            </a>
        </div>
        
        <!-- Декларация -->
        <section class="disclaimer fade-in">
            <p style="font-size: 1.1rem; font-weight: 500;">
                <strong>ВНИМАНИЕ:</strong> NEON PIZZA BOT является высокотехнологичным инструментом с мощными возможностями. 
                Используйте его исключительно в исследовательских целях и в рамках действующего законодательства. 
                Любое противоправное использование может повлечь серьезные юридические последствия. 
                Разработчик призывает к этичному использованию технологий и не несет ответственности за действия пользователей.
            </p>
        </section>
    </div>
    
    <!-- Футер -->
    <footer>
        <div class="footer-content">
            <p style="font-size: 1.3rem; color: #00ffff; font-family: 'Orbitron', sans-serif; margin-bottom: 20px;">
                © 2025 NEON PIZZA BOT SYSTEM v2.0
            </p>
            <div class="footer-links">
                <a href="#"><i class="fas fa-shield-alt"></i> Кибербезопасность</a>
                <a href="#"><i class="fas fa-code"></i> Разработчикам</a>
                <a href="#"><i class="fas fa-headset"></i> Техподдержка</a>
                <a href="#"><i class="fas fa-globe"></i> Глобальная сеть</a>
            </div>
            <p style="font-size: 0.9rem; color: #888; margin-top: 20px;">
                Система работает на основе квантовых алгоритмов • Синхронизация с орбитальными серверами
            </p>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            // Анимация появления элементов при скролле
            const fadeElements = document.querySelectorAll('.fade-in');
            
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        setTimeout(() => {
                            entry.target.classList.add('visible');
                        }, 100);
                    }
                });
            }, {
                threshold: 0.1
            });
            
            fadeElements.forEach(element => {
                observer.observe(element);
            });
            
            // Плавная прокрутка для навигационных ссылок
            document.querySelectorAll('a[href^="#"]').forEach(anchor => {
                anchor.addEventListener('click', function(e) {
                    e.preventDefault();
                    const targetId = this.getAttribute('href');
                    if (targetId === '#') return;
                    
                    const targetElement = document.querySelector(targetId);
                    if (targetElement) {
                        window.scrollTo({
                            top: targetElement.offsetTop - 100,
                            behavior: 'smooth'
                        });
                    }
                });
            });
            
            // Эффект наведения для кнопок
            const buttons = document.querySelectorAll('.btn');
            buttons.forEach(button => {
                button.addEventListener('mousedown', function() {
                    this.style.transform = 'translateY(2px)';
                });
                
                button.addEventListener('mouseup', function() {
                    this.style.transform = 'translateY(-3px)';
                });
                
                button.addEventListener('mouseleave', function() {
                    this.style.transform = 'translateY(0)';
                });
            });
            
            // Создание случайных неоновых вспышек
            function createNeonFlash() {
                const flash = document.createElement('div');
                flash.style.position = 'fixed';
                flash.style.width = Math.random() * 100 + 50 + 'px';
                flash.style.height = '2px';
                flash.style.background = Math.random() > 0.5 ? 
                    'linear-gradient(90deg, transparent, #ff00ff, transparent)' : 
                    'linear-gradient(90deg, transparent, #00ffff, transparent)';
                flash.style.top = Math.random() * 100 + 'vh';
                flash.style.left = '-200px';
                flash.style.opacity = '0';
                flash.style.filter = 'blur(1px)';
                flash.style.zIndex = '1';
                document.body.appendChild(flash);
                
                const duration = Math.random() * 3000 + 2000;
                const delay = Math.random() * 5000;
                
                flash.animate([
                    { 
                        transform: 'translateX(0)',
                        opacity: 0
                    },
                    { 
                        transform: 'translateX(100px)',
                        opacity: 0.7
                    },
                    { 
                        transform: 'translateX(calc(100vw + 200px))',
                        opacity: 0
                    }
                ], {
                    duration: duration,
                    delay: delay,
                    easing: 'linear'
                });
                
                setTimeout(() => {
                    document.body.removeChild(flash);
                }, duration + delay + 1000);
            }
            
            // Создаем несколько неоновых вспышек
            for (let i = 0; i < 10; i++) {
                setTimeout(createNeonFlash, i * 1000);
            }
            
            // Запускаем создание вспышек периодически
            setInterval(() => {
                if (Math.random() > 0.7) {
                    createNeonFlash();
                }
            }, 3000);
            
            // Эффект мерцания неонового текста
            const neonElements = document.querySelectorAll('.logo, h1, h2, .hero-logo');
            setInterval(() => {
                neonElements.forEach(el => {
                    if (Math.random() > 0.8) {
                        el.style.opacity = '0.8';
                        setTimeout(() => {
                            el.style.opacity = '1';
                        }, 100);
                    }
                });
            }, 500);
            
            // Изменение навигации при скролле
            window.addEventListener('scroll', function() {
                const navbar = document.querySelector('.navbar');
                if (window.scrollY > 50) {
                    navbar.style.background = 'rgba(10, 10, 10, 0.98)';
                    navbar.style.backdropFilter = 'blur(15px)';
                } else {
                    navbar.style.background = 'rgba(10, 10, 10, 0.95)';
                    navbar.style.backdropFilter = 'blur(10px)';
                }
            });
        });
    </script>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/redirect-to-telegram')
def redirect_to_telegram():
    return redirect("https://t.me/Platinumpizzvbot")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5059))
    app.run(host='0.0.0.0', port=port, debug=True)