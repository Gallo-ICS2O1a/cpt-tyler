enemy_size = 30
bul_size = 5
time = 0
score = 0
check = 0
menu = 0
hiscore = 0

nohit = 0
life = 3
stars = []
bulletspeed = []
enemyspeed = []
enetime = []
enemies = []
bullets = []
ebullets = []
player = 0

while len(stars) <= 75:
    stars.append(PVector(random(1, 699), random(1, 699)))


def setup():
    size(700, 700)
    background(255)
    frameRate(60)


# setup and draw
def draw():
    global nohit
    global hiscore
    global life
    global menu
    global stars
    global player
    global check
    global enemyspeed
    global bulletspeed
    global score
    global time
    global bullets
    global enemy_size
    global enemies
    global ebullets
    global bul_size
    global enetime

    # main menu
    if menu == 0:
        background(0)
        stroke(255)
        for star in stars:
            point(star.x, star.y)
        cursor()
        textSize(38)
        fill(255)
        text("HYPER REALISTIC SPACE SHOOTER", 35, 200)
        textSize(32)
        rect(250, 350, 200, 40)
        rect(250, 400, 200, 40)
        rect(250, 450, 200, 40)
        fill(0)
        text("START", 300, 380)
        textSize(27)
        text("INSTRUCTIONS", 255, 430)
        text("OTHER MODES", 255, 480)
        textSize(32)

        # menu hitbox
        if mouseX >= 250 and mouseX <= 450 and mouseY <= 450 and mouseY >= 400:
            if mousePressed == True:
                menu = 2

        if mouseX >= 250 and mouseX <= 450 and mouseY <= 390 and mouseY >= 350:
            if mousePressed == True:
                menu = 1
                nohit = 0
                life = 3

        if mouseX >= 250 and mouseX <= 450 and mouseY <= 490 and mouseY >= 450:
            if mousePressed == True:
                menu = 5

    # START OF GAME
    if menu == 1:
        background(5)

    # stars
        stroke(255)
        for star in stars:
            point(star.x, star.y)

        # sprites
        noStroke()
        player = PVector(mouseX, mouseY)
        fill(240, 0, 0)
        ellipse(mouseX, mouseY, 15, 15)
        noCursor()
        fill(0, 0, 240)

    # enemy spawn
        enemyspawn = random(0, 1000)
        if enemyspawn >= 990 and score <= 49 or enemyspawn >= 985 and score >= 50 or enemyspawn >= 980 and score >= 125 or enemyspawn >= 975 and score >= 200 or enemyspawn >= 970 and score >= 300:
            enemies.append(PVector(random(15, 685), -15))
            enetime.append(millis())
            enemyspeed.append(PVector(random(-1, 1), random(2, 3)))

    # enemies
        if len(enemies) >= 1 and len(enemyspeed) >= 1:
            for index, ene in enumerate(enemies):
                ellipse(ene.x, ene.y, 30, 30)
                if len(enemies) >= 1 and len(enemyspeed) >= 1:
                    ene.x += enemyspeed[index].x
                    ene.y += enemyspeed[index].y

                # shoot speed
                if len(enetime) >= 1:
                    if millis() >= enetime[index] + random(300, 700):
                        ebullets.append(PVector(ene.x, ene.y))
                        enetime[index] = millis()
                        bulletspeed.append(PVector(random(-1, 1), random(3, 5)))

        # if enemy hits bottom screen
                if ene.y >= 720:
                    enetime.pop(index)
                    enemyspeed.pop(index)
                    enemies.pop(index)
                    if nohit == 1:
                        score += 3
                    else:
                        score += 1

        # if enemy hits player
                if PVector.sub(ene, player).mag() <= 21:
                    life -= 1
                    enemyspeed.pop(index)
                    enetime.pop(index)
                    enemies.pop(index)

    # enemy bullets
        if len(ebullets) >= 1:
            if ebullets[0] != 0:
                for index, ebul in enumerate(ebullets):
                    ellipse(ebul.x, ebul.y, 10, 10)
                    ebul.x += bulletspeed[index].x
                    ebul.y += bulletspeed[index].y
                    if ebul.y >= 710:
                        ebullets.pop(index)
                        bulletspeed.pop(index)

                    # if bullets hit player
                    if PVector.sub(ebul, player).mag() <= 9:
                        bulletspeed.pop(index)
                        ebullets.remove(ebul)
                        life -= 1

    # if key pressed
        if nohit == 0:
            if keyPressed == True:
                if key == " " and millis() >= time + 300:
                    bullets.append(PVector(mouseX, mouseY - 9))
                    time = millis()
                    check += 1

        fill(255)

    # player bullets
        for index, bul in enumerate(bullets):
            ellipse(bul.x, bul.y, bul_size, bul_size)
            bul.y -= 10
            if bul.y <= -5:
                bullets.remove(bul)

        # player bullet and enemy hit detection
            for index, ene in enumerate(enemies):
                if PVector.sub(ene, bul).mag() <= 15:
                    score += 3
                    enemyspeed.pop(index)
                    enetime.pop(index)
                    enemies.remove(ene)
                    bullets.remove(bul)

        # hi-score
        if score > hiscore:
            hiscore = score

        # score
        fill(255)
        textSize(25)
        text("Score:", 10, 25)
        text(score, 85, 25)
        text("Hi-Score:", 10, 55)
        text(hiscore, 125, 55)
        # lives
        text("Lives:", 615, 25)
        text(life, 680, 25)

    # pause function
    if keyPressed == True:
            if key == "p":
                menu = 4

    # run out of lives
    if life <= 0:
        bulletspeed = []
        enemyspeed = []
        enetime = []
        enemies = []
        bullets = []
        ebullets = []
        menu = 3

    # help
    if menu == 2:
        textSize(20)
        stroke(32)
        fill(255)
        rect(30, 30, 630, 630)
        fill(0)

        text("""Hit space to shoot.
Use your mouse to move.
Press P to pause the game.

If an enemy hits the bottom screen you gain 1 point.
If you shoot a enemy you gain 3 points.

On Pacifist mode you cannot shoot.
Also on Pacifist mode, enemies that hit the bottom of the
screen gives you three points.
On 1 Life mode you only have one life.

You have 3 lives, when you lose all 3 you die.""", 50, 70)

        stroke(0)
        fill(0)
        rect(250, 500, 200, 40)
        textSize(32)
        fill(255)
        text("BACK", 305, 530)

        # MENU HITBOX
        if mouseX >= 250 and mouseX <= 450 and mouseY <= 540 and mouseY >= 500:
            if mousePressed == True:
                menu = 0

    # Death menu
    if menu == 3:
        background(0)
        cursor()
        stroke(255)
        for star in stars:
            point(star.x, star.y)
        noStroke()
        fill(255)
        rect(200, 150, 300, 400)

        # death menu "menu"
        fill(200, 0, 0)
        textSize(32)
        text("You Died", 280, 210)
        fill(0)
        text("Score:", 230, 265)
        text(score, 325, 265)
        text("High Score:", 230, 300)
        text(hiscore, 410, 300)
        rect(260, 350, 170, 40)
        rect(260, 500, 170, 40)
        fill(255)
        text("RETRY", 295, 380)
        text("MENU", 295, 530)

        # death menu hitbox
        if mouseX >= 260 and mouseX <= 430 and mouseY >= 350 and mouseY <= 390:
            if mousePressed == True:
                life = 3
                menu = 1
                score = 0

        if mouseX >= 260 and mouseX <= 430 and mouseY >= 500 and mouseY <= 540:
            if mousePressed == True:
                life = 3
                menu = 0
                score = 0

    # pause menu
    if menu == 4:
        background(0)
        cursor()
        stroke(255)
        for star in stars:
            point(star.x, star.y)
        noStroke()
        fill(255)
        textSize(32)
        text("Paused", 300, 300)
        text("Press space to return to the game", 100, 350)

        # return to game
        if keyPressed == True:
            if key == " ":
                menu = 1

    # Other menu
    if menu == 5:
        background(0)
        stroke(255)
        for star in stars:
            point(star.x, star.y)
        textSize(38)
        fill(255)
        text("HYPER REALISTIC SPACE SHOOTER", 35, 200)
        textSize(32)
        cursor()
        noStroke()
        fill(255)
        rect(250, 350, 200, 40)
        rect(250, 400, 200, 40)
        rect(250, 300, 200, 40)
        fill(0)
        text("BACK", 305, 330)
        text("PACIFIST", 285, 380)
        text("1 LIFE", 300, 430)

        # Other menu Hitbox
        if mouseX >= 250 and mouseX <= 450 and mouseY <= 340 and mouseY >= 300:
            if mousePressed == True:
                menu = 0

        if mouseX >= 250 and mouseX <= 450 and mouseY <= 390 and mouseY >= 350:
            if mousePressed == True:
                menu = 1
                nohit = 1
                life = 3

        if mouseX >= 250 and mouseX <= 450 and mouseY <= 440 and mouseY >= 400:
                if mousePressed == True:
                    menu = 1
                    nohit = 0
                    life = 1
