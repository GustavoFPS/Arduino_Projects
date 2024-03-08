const int stepPin = 9;
const int dirPin = 8;
const int halfPin = 10;
int step = 0;

void rotation(int delayTime) {
  digitalWrite(stepPin, HIGH);
  delayMicroseconds(delayTime); 
  digitalWrite(stepPin, LOW);
  delayMicroseconds(delayTime);
}

void setup() {
  pinMode(stepPin, OUTPUT);
  pinMode(dirPin, OUTPUT);
  pinMode(halfPin, OUTPUT);
  
  digitalWrite(dirPin, HIGH);
  digitalWrite(halfPin, HIGH);

  // Realiza uma rotação inicial do motor de passo
  rotation(500);

  // Inicializa a comunicação serial com uma taxa de 9600 bps
  Serial.begin(9600);
}

void loop() {
  // Verifica se há dados disponíveis na porta serial
  if (Serial.available() > 0) {
    char receivedChar = Serial.read(); // Lê o caractere recebido
    
    if (receivedChar == 'r') {
      // Realiza uma rotação quando o caractere 'r' é recebido
      rotation(500);
      // Envia um sinal de confirmação de rotação concluída para o Python
      Serial.println("rotation_complete");
    }
  }
}
