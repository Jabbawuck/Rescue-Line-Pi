#include <Wire.h>
#include <MPU6050.h>

MPU6050 mpu;

void setup() {
  Wire.begin();
  mpu.initialize();
  Serial.begin(9600);
  // Set gyro sensitivity (optional)
  mpu.setFullScaleGyroRange(MPU6050_GYRO_FS_250);
}

void loop() {
  // Read raw gyro data
  int16_t gyroX = mpu.getRotationX();
  int16_t gyroY = mpu.getRotationY();
  int16_t gyroZ = mpu.getRotationZ();
  
  // Print gyro data
  Serial.print("Gyro X: ");
  Serial.print(gyroX);
  Serial.print("  Gyro Y: ");
  Serial.print(gyroY);
  Serial.print("  Gyro Z: ");
  Serial.println(gyroZ);
  
  delay(100);
}
